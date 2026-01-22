# Unit Test Suite

This directory contains a comprehensive pytest-based unit test suite for the NDFC API endpoint library.

## Test Files

- **test_enums.py** - Tests for BooleanStringEnum and VerbEnum (12 tests)
- **test_base_paths.py** - Tests for BasePath class methods (26 tests)
- **test_query_params.py** - Tests for query parameter classes (41 tests)
- **test_endpoints.py** - Tests for endpoint classes (24 tests)

**Total: 103 tests**

## Running Tests

### Run all tests:
```bash
python3 -m pytest test_*.py -v
```

### Run specific test file:
```bash
python3 -m pytest test_enums.py -v
```

### Run with coverage:
```bash
python3 -m pytest test_*.py --cov=. --cov-report=html
```

### Run specific test:
```bash
python3 -m pytest test_enums.py::test_boolean_string_enum_00100 -v
```

## Test Naming Convention

Tests follow a structured naming pattern:
- `test_<module>_<test_range>`
- Example: `test_boolean_string_enum_00100`

### Range Allocation:
- **Enums Module**:
  - BooleanStringEnum: 100-199
  - VerbEnum: 200-299

- **BasePath Module**:
  - Constants: 100-199
  - api() method: 200-299
  - v1() method: 300-399
  - lan_fabric() method: 400-499
  - control_fabrics() method: 500-599
  - onemanage() method: 600-699
  - onemanage_fabrics() method: 700-799
  - onemanage_links() method: 800-899
  - onemanage_links_fabrics() method: 900-999
  - onemanage_top_down() method: 1000-1099
  - onemanage_top_down_fabrics() method: 1100-1199

- **Query Params Module**:
  - EndpointQueryParams: 100-299
  - LuceneQueryParams: 300-599
  - CompositeQueryParams: 600-899

- **Endpoints Module**:
  - FabricConfigDeployQueryParams: 100-199
  - FabricConfigPreviewQueryParams: 200-299
  - EpOneManageFabricConfigDeploy: 300-399
  - EpOneManageFabricConfigDeploySwitch: 400-499
  - EpOneManageFabricConfigPreview: 500-599
  - EpOneManageFabricConfigPreviewSwitch: 600-699

Tests increment by 10 to allow for future insertion without renumbering.

## Test Documentation Format

Each test includes a Markdown-formatted docstring with:

### Summary
One-line description of what the test validates.

### Description
Detailed explanation of the test's purpose and what it's checking.

### Pass/Fail Criteria
- PASS: Specific conditions that must be met
- FAIL: Conditions that indicate failure

Example:
```python
def test_boolean_string_enum_00100():
    """
    # Summary

    BooleanStringEnum.TRUE has correct value

    ## Description

    Verifies that BooleanStringEnum.TRUE evaluates to the string "true".
    This is critical for API query parameter formatting.

    ### Pass/Fail Criteria

    - PASS: BooleanStringEnum.TRUE.value equals "true"
    - FAIL: Value is anything other than "true"
    """
    assert BooleanStringEnum.TRUE.value == "true"
```

## Test Coverage

### Enums Module
- ✅ Enum value correctness
- ✅ String inheritance behavior
- ✅ String representation
- ✅ Equality comparisons
- ✅ Member count validation

### BasePath Module
- ✅ Constant values
- ✅ Path composition with no segments
- ✅ Path composition with single segment
- ✅ Path composition with multiple segments
- ✅ All helper methods (api, v1, onemanage, etc.)
- ✅ Complex path construction

### Query Params Module
- ✅ EndpointQueryParams instantiation
- ✅ CamelCase conversion
- ✅ None value exclusion
- ✅ Empty detection
- ✅ LuceneQueryParams all parameters
- ✅ URL encoding (enabled/disabled)
- ✅ Complex Lucene filters (AND, OR, NOT, wildcards, ranges, nested)
- ✅ Field validation (sort, max, offset)
- ✅ CompositeQueryParams composition
- ✅ Method chaining
- ✅ Empty parameter group handling
- ✅ Parameter ordering

### Endpoints Module
- ✅ Query parameter initialization
- ✅ Default values
- ✅ Enum value extraction
- ✅ Path construction
- ✅ Required field validation
- ✅ HTTP verb assignment
- ✅ Query string generation
- ✅ Query parameter modification

## Requirements

```bash
pip install pytest pydantic
```

## CI/CD Integration

These tests are designed to integrate with CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install pytest pydantic
    pytest test_*.py -v --junitxml=test-results.xml
```

## Adding New Tests

When adding new tests:

1. Follow the naming convention: `test_<module>_<next_available_number>`
2. Increment by 10 from the previous test
3. Include complete Markdown docstring with Summary, Description, and Pass/Fail Criteria
4. Place in the appropriate range for the module/class being tested

Example:
```python
def test_new_feature_00150():  # Next available in 100-199 range
    """
    # Summary

    Brief one-line description

    ## Description

    Detailed explanation of what this test does and why it matters.

    ### Pass/Fail Criteria

    - PASS: Specific success conditions
    - FAIL: Specific failure conditions
    """
    # Test implementation
    assert actual == expected
```

## Troubleshooting

### Pydantic Warnings
The test suite may show deprecation warnings about class-based Config. These are informational and don't affect test results.

### Import Errors
Ensure you're running tests from the project root directory where all modules are accessible.

### Test Failures
Check the detailed output with `-v` flag and review the Pass/Fail criteria in the test docstring to understand expected behavior.
