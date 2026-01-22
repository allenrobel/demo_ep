#!/usr/bin/env python3
# Copyright (c) 2026 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit tests for query_params module.

Tests the EndpointQueryParams, LuceneQueryParams, and CompositeQueryParams classes
to ensure correct query string construction, URL encoding, and composition.
"""

import pytest
from query_params import EndpointQueryParams, LuceneQueryParams, CompositeQueryParams
from enums import BooleanStringEnum

# ============================================================================
# EndpointQueryParams Tests (100-299)
# ============================================================================


def test_endpoint_query_params_00100():
    """
    # Summary

    EndpointQueryParams instantiation with no parameters

    ## Description

    Verifies that EndpointQueryParams can be instantiated without any
    parameters and produces an empty query string.

    ### Pass/Fail Criteria

    - PASS: Instance created successfully, to_query_string() returns empty string
    - FAIL: Instantiation fails or returns non-empty string
    """
    params = EndpointQueryParams()
    assert params.to_query_string() == ""
    assert params.is_empty() is True


def test_endpoint_query_params_00110():
    """
    # Summary

    EndpointQueryParams camelCase conversion

    ## Description

    Verifies that snake_case field names are correctly converted to camelCase
    for API compatibility when generating query strings.

    ### Pass/Fail Criteria

    - PASS: snake_case fields are converted to camelCase
    - FAIL: Incorrect case conversion
    """

    # Create a simple subclass for testing
    class TestParams(EndpointQueryParams):
        test_field: str = "value"

    params = TestParams()
    query_string = params.to_query_string()
    assert "testField=value" in query_string


def test_endpoint_query_params_00120():
    """
    # Summary

    EndpointQueryParams excludes None values

    ## Description

    Verifies that fields with None values are excluded from the query string.

    ### Pass/Fail Criteria

    - PASS: None values are excluded from query string
    - FAIL: None values appear in query string
    """

    class TestParams(EndpointQueryParams):
        field_one: str = "present"
        field_two: str | None = None

    params = TestParams()
    query_string = params.to_query_string()
    assert "fieldOne=present" in query_string
    assert "fieldTwo" not in query_string


def test_endpoint_query_params_00130():
    """
    # Summary

    EndpointQueryParams is_empty() with defaults

    ## Description

    Verifies that is_empty() correctly identifies when only default
    values are set (excluding defaults in the check).

    ### Pass/Fail Criteria

    - PASS: is_empty() returns True when only defaults are set
    - FAIL: Returns False incorrectly
    """

    class TestParams(EndpointQueryParams):
        field_with_default: str = "default_value"

    params = TestParams()
    # Should be empty because no non-default values are set
    assert params.is_empty() is True


# ============================================================================
# LuceneQueryParams Tests (300-599)
# ============================================================================


def test_lucene_query_params_00300():
    """
    # Summary

    LuceneQueryParams instantiation with all None

    ## Description

    Verifies that LuceneQueryParams can be instantiated with all fields
    as None and produces an empty query string.

    ### Pass/Fail Criteria

    - PASS: Instance created, empty query string, is_empty() returns True
    - FAIL: Instantiation fails or incorrect empty detection
    """
    params = LuceneQueryParams()
    assert params.to_query_string() == ""
    assert params.is_empty() is True


def test_lucene_query_params_00310():
    """
    # Summary

    LuceneQueryParams filter parameter

    ## Description

    Verifies that the filter parameter is correctly included in the
    query string.

    ### Pass/Fail Criteria

    - PASS: filter parameter appears in query string
    - FAIL: Missing or incorrectly formatted
    """
    params = LuceneQueryParams(filter="name:MyFabric")
    query_string = params.to_query_string(url_encode=False)
    assert "filter=name:MyFabric" in query_string


def test_lucene_query_params_00320():
    """
    # Summary

    LuceneQueryParams max parameter

    ## Description

    Verifies that the max parameter is correctly included and formatted.

    ### Pass/Fail Criteria

    - PASS: max parameter appears as integer in query string
    - FAIL: Missing or incorrectly formatted
    """
    params = LuceneQueryParams(max=100)
    query_string = params.to_query_string()
    assert "max=100" in query_string


def test_lucene_query_params_00330():
    """
    # Summary

    LuceneQueryParams offset parameter

    ## Description

    Verifies that the offset parameter is correctly included.

    ### Pass/Fail Criteria

    - PASS: offset parameter appears in query string
    - FAIL: Missing or incorrectly formatted
    """
    params = LuceneQueryParams(offset=25)
    query_string = params.to_query_string()
    assert "offset=25" in query_string


def test_lucene_query_params_00340():
    """
    # Summary

    LuceneQueryParams sort parameter

    ## Description

    Verifies that the sort parameter is correctly included.

    ### Pass/Fail Criteria

    - PASS: sort parameter appears in query string
    - FAIL: Missing or incorrectly formatted
    """
    params = LuceneQueryParams(sort="name:asc")
    query_string = params.to_query_string(url_encode=False)
    assert "sort=name:asc" in query_string


def test_lucene_query_params_00350():
    """
    # Summary

    LuceneQueryParams fields parameter

    ## Description

    Verifies that the fields parameter is correctly included.

    ### Pass/Fail Criteria

    - PASS: fields parameter appears in query string
    - FAIL: Missing or incorrectly formatted
    """
    params = LuceneQueryParams(fields="name,id,status")
    query_string = params.to_query_string(url_encode=False)
    assert "fields=name,id,status" in query_string


def test_lucene_query_params_00360():
    """
    # Summary

    LuceneQueryParams URL encoding enabled

    ## Description

    Verifies that special characters in filter expressions are URL-encoded
    when url_encode=True (default).

    ### Pass/Fail Criteria

    - PASS: Special characters are URL-encoded (: becomes %3A, space becomes %20, etc.)
    - FAIL: Special characters not encoded
    """
    params = LuceneQueryParams(filter="name:Spine* AND role:spine")
    query_string = params.to_query_string(url_encode=True)
    # Colon should be encoded as %3A, space as %20, asterisk as %2A
    assert "%3A" in query_string  # Colon
    assert "%20" in query_string  # Space
    assert "%2A" in query_string  # Asterisk


def test_lucene_query_params_00370():
    """
    # Summary

    LuceneQueryParams URL encoding disabled

    ## Description

    Verifies that special characters are not encoded when url_encode=False.

    ### Pass/Fail Criteria

    - PASS: Special characters remain unencoded
    - FAIL: Characters are encoded
    """
    params = LuceneQueryParams(filter="name:Spine* AND role:spine")
    query_string = params.to_query_string(url_encode=False)
    assert "name:Spine* AND role:spine" in query_string
    assert "%3A" not in query_string


def test_lucene_query_params_00380():
    """
    # Summary

    LuceneQueryParams multiple parameters

    ## Description

    Verifies that multiple Lucene parameters are correctly combined
    with ampersands.

    ### Pass/Fail Criteria

    - PASS: All parameters present, separated by &
    - FAIL: Missing parameters or incorrect separator
    """
    params = LuceneQueryParams(filter="status:active", max=50, offset=10, sort="name:desc")
    query_string = params.to_query_string(url_encode=False)
    assert "filter=status:active" in query_string
    assert "max=50" in query_string
    assert "offset=10" in query_string
    assert "sort=name:desc" in query_string
    assert query_string.count("&") == 3  # 4 params = 3 ampersands


def test_lucene_query_params_00390():
    """
    # Summary

    LuceneQueryParams sort validation accepts valid format

    ## Description

    Verifies that the sort field validator accepts properly formatted
    sort directives (field:asc or field:desc).

    ### Pass/Fail Criteria

    - PASS: Valid sort formats are accepted without error
    - FAIL: Validation error raised for valid input
    """
    # Should not raise
    params1 = LuceneQueryParams(sort="name:asc")
    params2 = LuceneQueryParams(sort="created:desc")
    params3 = LuceneQueryParams(sort="role:ASC")  # Case insensitive
    assert params1.sort == "name:asc"
    assert params2.sort == "created:desc"
    assert params3.sort == "role:ASC"


def test_lucene_query_params_00400():
    """
    # Summary

    LuceneQueryParams sort validation rejects invalid direction

    ## Description

    Verifies that the sort field validator rejects invalid sort
    directions (anything other than asc/desc).

    ### Pass/Fail Criteria

    - PASS: ValueError raised for invalid direction
    - FAIL: Invalid direction accepted
    """
    with pytest.raises(ValueError, match="Sort direction must be"):
        LuceneQueryParams(sort="name:invalid")


def test_lucene_query_params_00410():
    """
    # Summary

    LuceneQueryParams max value range validation

    ## Description

    Verifies that max value must be between 1 and 10000.

    ### Pass/Fail Criteria

    - PASS: Valid range accepted, invalid range rejected
    - FAIL: Validation not working correctly
    """
    # Valid values
    params1 = LuceneQueryParams(max=1)
    params2 = LuceneQueryParams(max=10000)
    assert params1.max == 1
    assert params2.max == 10000

    # Invalid values
    with pytest.raises(Exception):  # Pydantic ValidationError
        LuceneQueryParams(max=0)

    with pytest.raises(Exception):  # Pydantic ValidationError
        LuceneQueryParams(max=10001)


def test_lucene_query_params_00420():
    """
    # Summary

    LuceneQueryParams offset non-negative validation

    ## Description

    Verifies that offset must be >= 0.

    ### Pass/Fail Criteria

    - PASS: Non-negative offsets accepted, negative rejected
    - FAIL: Validation not working correctly
    """
    # Valid
    params = LuceneQueryParams(offset=0)
    assert params.offset == 0

    # Invalid
    with pytest.raises(Exception):  # Pydantic ValidationError
        LuceneQueryParams(offset=-1)


def test_lucene_query_params_00430():
    """
    # Summary

    LuceneQueryParams complex AND filter

    ## Description

    Verifies that complex Lucene filter expressions with AND operators
    are correctly handled.

    ### Pass/Fail Criteria

    - PASS: Complex filter preserved in query string
    - FAIL: Filter corrupted or missing
    """
    filter_expr = "fabricName:MyFabric AND role:spine AND status:active"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


def test_lucene_query_params_00440():
    """
    # Summary

    LuceneQueryParams complex OR filter

    ## Description

    Verifies that Lucene filter expressions with OR operators
    are correctly handled.

    ### Pass/Fail Criteria

    - PASS: OR filter preserved in query string
    - FAIL: Filter corrupted or missing
    """
    filter_expr = "role:spine OR role:leaf"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


def test_lucene_query_params_00450():
    """
    # Summary

    LuceneQueryParams NOT filter

    ## Description

    Verifies that Lucene filter expressions with NOT operators
    are correctly handled.

    ### Pass/Fail Criteria

    - PASS: NOT filter preserved in query string
    - FAIL: Filter corrupted or missing
    """
    filter_expr = "NOT status:deleted"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


def test_lucene_query_params_00460():
    """
    # Summary

    LuceneQueryParams wildcard filter

    ## Description

    Verifies that wildcard characters in filters are preserved.

    ### Pass/Fail Criteria

    - PASS: Wildcards preserved in query string
    - FAIL: Wildcards removed or corrupted
    """
    filter_expr = "name:Spine-* OR ipAddress:10.1.*"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


def test_lucene_query_params_00470():
    """
    # Summary

    LuceneQueryParams range filter

    ## Description

    Verifies that range expressions [value TO value] are correctly handled.

    ### Pass/Fail Criteria

    - PASS: Range expression preserved in query string
    - FAIL: Range corrupted or missing
    """
    filter_expr = "deployedDate:[2024-01-01 TO 2024-12-31]"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


def test_lucene_query_params_00480():
    """
    # Summary

    LuceneQueryParams nested parentheses filter

    ## Description

    Verifies that complex nested filter expressions with parentheses
    are correctly handled.

    ### Pass/Fail Criteria

    - PASS: Nested expression preserved in query string
    - FAIL: Parentheses or expression corrupted
    """
    filter_expr = "(role:spine OR role:leaf) AND status:active AND NOT ipAddress:192.168.*"
    params = LuceneQueryParams(filter=filter_expr)
    query_string = params.to_query_string(url_encode=False)
    assert filter_expr in query_string


# ============================================================================
# CompositeQueryParams Tests (600-899)
# ============================================================================


def test_composite_query_params_00600():
    """
    # Summary

    CompositeQueryParams instantiation

    ## Description

    Verifies that CompositeQueryParams can be instantiated and starts empty.

    ### Pass/Fail Criteria

    - PASS: Instance created, is_empty() returns True
    - FAIL: Instantiation fails or not empty
    """
    composite = CompositeQueryParams()
    assert composite.is_empty() is True
    assert composite.to_query_string() == ""


def test_composite_query_params_00610():
    """
    # Summary

    CompositeQueryParams add() returns self for chaining

    ## Description

    Verifies that add() returns self to enable method chaining.

    ### Pass/Fail Criteria

    - PASS: add() returns the CompositeQueryParams instance
    - FAIL: Returns None or different object
    """
    composite = CompositeQueryParams()
    lucene = LuceneQueryParams(filter="test:value")
    result = composite.add(lucene)
    assert result is composite


def test_composite_query_params_00620():
    """
    # Summary

    CompositeQueryParams method chaining

    ## Description

    Verifies that multiple add() calls can be chained together.

    ### Pass/Fail Criteria

    - PASS: Chaining works, all params added correctly
    - FAIL: Chaining fails or params not added
    """
    lucene1 = LuceneQueryParams(filter="test1:value1")
    lucene2 = LuceneQueryParams(max=50)

    composite = CompositeQueryParams().add(lucene1).add(lucene2)
    query_string = composite.to_query_string(url_encode=False)

    assert "filter=test1:value1" in query_string
    assert "max=50" in query_string


def test_composite_query_params_00630():
    """
    # Summary

    CompositeQueryParams with single LuceneQueryParams

    ## Description

    Verifies that a CompositeQueryParams with only Lucene parameters
    produces the correct query string.

    ### Pass/Fail Criteria

    - PASS: Query string matches LuceneQueryParams output
    - FAIL: Incorrect query string
    """
    lucene = LuceneQueryParams(filter="status:active", max=100)
    composite = CompositeQueryParams()
    composite.add(lucene)

    query_string = composite.to_query_string(url_encode=False)
    assert "filter=status:active" in query_string
    assert "max=100" in query_string


def test_composite_query_params_00640():
    """
    # Summary

    CompositeQueryParams with multiple parameter groups

    ## Description

    Verifies that multiple parameter groups are correctly combined
    with ampersands.

    ### Pass/Fail Criteria

    - PASS: All parameter groups present, properly separated
    - FAIL: Missing groups or incorrect separator
    """
    lucene1 = LuceneQueryParams(filter="test:value")
    lucene2 = LuceneQueryParams(max=50)

    composite = CompositeQueryParams()
    composite.add(lucene1)
    composite.add(lucene2)

    query_string = composite.to_query_string(url_encode=False)
    assert "filter=test:value" in query_string
    assert "max=50" in query_string
    assert "&" in query_string


def test_composite_query_params_00650():
    """
    # Summary

    CompositeQueryParams skips empty parameter groups

    ## Description

    Verifies that parameter groups with no values set are excluded
    from the final query string.

    ### Pass/Fail Criteria

    - PASS: Empty groups excluded, non-empty included
    - FAIL: Empty groups appear in query string
    """
    lucene_empty = LuceneQueryParams()  # All None
    lucene_with_value = LuceneQueryParams(max=100)

    composite = CompositeQueryParams()
    composite.add(lucene_empty)
    composite.add(lucene_with_value)

    query_string = composite.to_query_string()
    assert query_string == "max=100"


def test_composite_query_params_00660():
    """
    # Summary

    CompositeQueryParams is_empty() with all empty groups

    ## Description

    Verifies that is_empty() returns True when all added parameter
    groups are empty.

    ### Pass/Fail Criteria

    - PASS: is_empty() returns True
    - FAIL: Returns False
    """
    lucene1 = LuceneQueryParams()
    lucene2 = LuceneQueryParams()

    composite = CompositeQueryParams()
    composite.add(lucene1)
    composite.add(lucene2)

    assert composite.is_empty() is True


def test_composite_query_params_00670():
    """
    # Summary

    CompositeQueryParams is_empty() with non-empty group

    ## Description

    Verifies that is_empty() returns False when at least one parameter
    group is non-empty.

    ### Pass/Fail Criteria

    - PASS: is_empty() returns False
    - FAIL: Returns True
    """
    lucene_empty = LuceneQueryParams()
    lucene_with_value = LuceneQueryParams(max=10)

    composite = CompositeQueryParams()
    composite.add(lucene_empty)
    composite.add(lucene_with_value)

    assert composite.is_empty() is False


def test_composite_query_params_00680():
    """
    # Summary

    CompositeQueryParams clear() method

    ## Description

    Verifies that clear() removes all parameter groups.

    ### Pass/Fail Criteria

    - PASS: After clear(), is_empty() returns True
    - FAIL: Groups remain after clear()
    """
    lucene = LuceneQueryParams(max=100)
    composite = CompositeQueryParams()
    composite.add(lucene)

    assert composite.is_empty() is False

    composite.clear()
    assert composite.is_empty() is True


def test_composite_query_params_00690():
    """
    # Summary

    CompositeQueryParams URL encoding propagates to Lucene params

    ## Description

    Verifies that the url_encode parameter is correctly passed to
    LuceneQueryParams during query string generation.

    ### Pass/Fail Criteria

    - PASS: URL encoding applied when url_encode=True
    - FAIL: Encoding not applied
    """
    lucene = LuceneQueryParams(filter="name:Spine* AND role:spine")
    composite = CompositeQueryParams()
    composite.add(lucene)

    # With encoding
    encoded = composite.to_query_string(url_encode=True)
    assert "%3A" in encoded  # Colon encoded

    # Without encoding
    not_encoded = composite.to_query_string(url_encode=False)
    assert "%3A" not in not_encoded  # Colon not encoded


def test_composite_query_params_00700():
    """
    # Summary

    CompositeQueryParams preserves parameter order

    ## Description

    Verifies that parameter groups are output in the order they were added.

    ### Pass/Fail Criteria

    - PASS: Parameters appear in add() order
    - FAIL: Order is different
    """
    lucene1 = LuceneQueryParams(filter="first:value")
    lucene2 = LuceneQueryParams(max=50)
    lucene3 = LuceneQueryParams(offset=10)

    composite = CompositeQueryParams()
    composite.add(lucene1)
    composite.add(lucene2)
    composite.add(lucene3)

    query_string = composite.to_query_string(url_encode=False)

    # Check order: filter should come before max, max before offset
    filter_pos = query_string.find("filter=")
    max_pos = query_string.find("max=")
    offset_pos = query_string.find("offset=")

    assert filter_pos < max_pos < offset_pos
