# Typed Endpoint Classes vs. Hardcoded Strings: Key Benefits

## 1. Compile-Time/Static Analysis Safety

- Pydantic validation catches errors *before* runtime—missing required parameters like `fabric_name` raise `ValueError` immediately when accessing `.path`, not as a cryptic 404 from the API
- Type checkers (mypy, Pyright) can verify correct usage across the codebase
- A generic query-string builder gives you a string; this gives you *guarantees*

## 2. Self-Documenting Code

- Each endpoint class has its path template, HTTP verb, required parameters, and usage examples in one place
- Compare `EpOneManageFabricConfigDeploy()` vs. `f"/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabric_name}/config-deploy?forceShowRun={...}&inclAllMSDSwitches={...}"`
- New team members can understand the API surface by reading the class definitions

## 3. IDE Support & Discoverability

- Autocomplete shows all available endpoints, their parameters, and query options
- Hover for docstrings with usage examples
- Refactoring tools can rename parameters safely across the codebase

## 4. Consistency Through Mixins

- `FabricNameMixin`, `SwitchSerialNumberMixin`, etc. ensure the same validation rules (e.g., `min_length=1, max_length=64`) apply everywhere
- Change a constraint once, it propagates everywhere

## 5. Testability

- Each endpoint class is independently instantiable and testable
- You can unit test path generation, parameter validation, and query string building without making HTTP calls
- Mocking is straightforward—pass endpoint objects rather than raw strings

## 6. Centralized API Knowledge

- When the API changes (parameter renamed from `forceShowRun` to `force_show_run`), you update one `to_query_string()` method
- With hardcoded strings scattered throughout, you're searching the entire codebase

## 7. Query Parameter Type Safety

- `BooleanStringEnum` ensures you pass `"true"/"false"`, not `True/False` or `"yes"/"no"`
- The API expects specific string values; enums enforce this at assignment time

## 8. Graceful Degradation

- The Pydantic fallback allows the code to work even without Pydantic installed, maintaining compatibility across environments

---

## Addressing the Counterargument

> "A generic query builder is simpler."

Yes, but simpler isn't always better. A generic builder:

- Shifts all validation to runtime (or never)
- Provides no discoverability
- Requires developers to remember exact parameter names and valid values

This approach *encodes the API contract in the type system*, catching errors earlier and making the codebase more maintainable as it scales.
