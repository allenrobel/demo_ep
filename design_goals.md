# Endpoint Library Design Goals

This document summarizes the design goals and architectural decisions reflected in the endpoint library codebase.

---

## 1. Type Safety as a First-Class Concern

**Goal**: Catch errors at development time, not runtime.

- Pydantic models validate parameters on assignment (`validate_assignment=True`)
- Field constraints (`min_length`, `max_length`, `ge`, `le`) enforce valid ranges
- Enums (`VerbEnum`, `BooleanStringEnum`) restrict values to API-valid options
- Type hints enable static analysis with mypy/Pyright

**Example**: Setting `fabric_name` to an empty string fails immediately, not when the API returns a 400.

---

## 2. Single Source of Truth

**Goal**: API knowledge lives in one place.

| Concern | Location |
|---------|----------|
| Base URL paths | `BasePath` class |
| HTTP verbs | Each endpoint's `verb` property |
| Required parameters | Mixin fields + `path` property validation |
| Query parameter formats | `to_query_string()` methods |
| Parameter naming conventions | `_to_camel_case()` in `EndpointQueryParams` |

When the API changes, updates are localized rather than scattered across the codebase.

---

## 3. Composition Over Inheritance

**Goal**: Build complex behavior from simple, reusable parts.

### Mixins for Shared Fields
```python
class FabricNameMixin(BaseModel):
    fabric_name: Optional[str] = Field(default=None, min_length=1, max_length=64)

class EpOneManageFabricDelete(FabricNameMixin, BaseModel):
    # Inherits fabric_name with all its validation
    ...
```

### Composable Query Parameters
```python
composite = CompositeQueryParams()
composite.add(endpoint_params)   # Endpoint-specific
composite.add(lucene_params)     # Generic filtering
query_string = composite.to_query_string()
```

This allows mixing and matching capabilities without deep inheritance hierarchies.

---

## 4. Separation of Concerns

**Goal**: Each module has a single responsibility.

| Module | Responsibility |
|--------|----------------|
| `base_paths.py` | URL path construction |
| `query_params.py` | Query string building and validation |
| `enums.py` | Type-safe enumerated values |
| `endpoints.py` | Endpoint definitions combining all pieces |

This separation enables independent testing and modification of each layer.

---

## 5. Consistent Developer Interface

**Goal**: Every endpoint works the same way.

```python
# All endpoints follow this pattern:
request = EpSomeEndpoint()
request.fabric_name = "MyFabric"        # Set path parameters
request.query_params.some_option = True  # Set query parameters
path = request.path                      # Get complete URL path
verb = request.verb                      # Get HTTP method
```

Developers learn one pattern and apply it everywhere.

---

## 6. Fail Fast with Clear Errors

**Goal**: Surface problems immediately with actionable messages.

```python
@property
def path(self) -> str:
    if self.fabric_name is None:
        raise ValueError("fabric_name must be set before accessing path")
    ...
```

Rather than constructing invalid URLs silently, the library raises descriptive errors at the point of misuse.

---

## 7. Graceful Degradation

**Goal**: Work in constrained environments.

The Pydantic fallback pattern allows the library to function without Pydantic installed:

```python
try:
    from pydantic import BaseModel, Field
except ImportError:
    class BaseModel:
        """Fallback BaseModel when pydantic is not available."""
        ...
```

This supports diverse deployment scenarios while preserving full functionality when Pydantic is available.

---

## 8. Self-Documenting Code

**Goal**: The code explains itself.

- Each endpoint class includes docstrings with:
  - Summary and description
  - Full URL path template
  - HTTP verb
  - Usage example with working code
  - Request body documentation where applicable
- Field descriptions explain each parameter's purpose
- Class names match API concepts (`EpOneManageFabricConfigDeploy`)

---

## 9. Extensibility

**Goal**: Adding new endpoints requires minimal boilerplate.

To add a new endpoint:

1. Choose appropriate mixins for path parameters
2. Choose or create a query params class
3. Implement `path` property and `verb` property
4. The framework handles validation, query string building, and path construction

```python
class EpNewEndpoint(FabricNameMixin, BaseModel):
    query_params: SomeQueryParams = Field(default_factory=SomeQueryParams)

    @property
    def path(self) -> str:
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")
        return BasePath.some_base(self.fabric_name)

    @property
    def verb(self) -> VerbEnum:
        return VerbEnum.POST
```

---

## 10. API Contract Encoding

**Goal**: The type system enforces API contracts.

- Path parameters are validated before URL construction
- Query parameters use correct types (string booleans, not Python booleans)
- Snake_case to camelCase conversion happens automatically
- URL encoding is handled transparently

The library acts as a contract layer between application code and the external API.

---

## Summary

This design prioritizes **correctness**, **maintainability**, and **developer experience** over raw simplicity. The additional structure pays dividends as the codebase scales and as multiple developers work with the API surface.
