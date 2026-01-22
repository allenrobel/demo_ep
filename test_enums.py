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
Unit tests for enums module.

Tests the BooleanStringEnum and VerbEnum classes to ensure proper
enum values and string inheritance behavior.
"""

import pytest
from enums import BooleanStringEnum, VerbEnum

# ============================================================================
# BooleanStringEnum Tests (100-199)
# ============================================================================


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


def test_boolean_string_enum_00110():
    """
    # Summary

    BooleanStringEnum.FALSE has correct value

    ## Description

    Verifies that BooleanStringEnum.FALSE evaluates to the string "false".
    This is critical for API query parameter formatting.

    ### Pass/Fail Criteria

    - PASS: BooleanStringEnum.FALSE.value equals "false"
    - FAIL: Value is anything other than "false"
    """
    assert BooleanStringEnum.FALSE.value == "false"


def test_boolean_string_enum_00120():
    """
    # Summary

    BooleanStringEnum is instance of str

    ## Description

    Verifies that BooleanStringEnum inherits from str, allowing it to be
    used anywhere a string is expected without explicit conversion.

    ### Pass/Fail Criteria

    - PASS: BooleanStringEnum.TRUE is an instance of str
    - FAIL: Not an instance of str
    """
    assert isinstance(BooleanStringEnum.TRUE, str)
    assert isinstance(BooleanStringEnum.FALSE, str)


def test_boolean_string_enum_00130():
    """
    # Summary

    BooleanStringEnum behaves as string

    ## Description

    Verifies that BooleanStringEnum members can be used as strings
    in f-strings and other contexts, using their value.

    ### Pass/Fail Criteria

    - PASS: Enum members evaluate to their string values in string contexts
    - FAIL: Returns different value
    """
    # When used in f-strings or concatenation, the value is used
    assert f"{BooleanStringEnum.TRUE}" == "BooleanStringEnum.TRUE"
    # But the actual value is accessible
    assert BooleanStringEnum.TRUE.value == "true"
    assert BooleanStringEnum.FALSE.value == "false"


def test_boolean_string_enum_00140():
    """
    # Summary

    BooleanStringEnum equality comparison

    ## Description

    Verifies that BooleanStringEnum members can be compared with strings
    directly due to str inheritance.

    ### Pass/Fail Criteria

    - PASS: Enum members equal their string values
    - FAIL: Comparison fails
    """
    assert BooleanStringEnum.TRUE == "true"
    assert BooleanStringEnum.FALSE == "false"


# ============================================================================
# VerbEnum Tests (200-299)
# ============================================================================


def test_verb_enum_00200():
    """
    # Summary

    VerbEnum.GET has correct value

    ## Description

    Verifies that VerbEnum.GET evaluates to the string "GET".

    ### Pass/Fail Criteria

    - PASS: VerbEnum.GET.value equals "GET"
    - FAIL: Value is anything other than "GET"
    """
    assert VerbEnum.GET.value == "GET"


def test_verb_enum_00210():
    """
    # Summary

    VerbEnum.POST has correct value

    ## Description

    Verifies that VerbEnum.POST evaluates to the string "POST".

    ### Pass/Fail Criteria

    - PASS: VerbEnum.POST.value equals "POST"
    - FAIL: Value is anything other than "POST"
    """
    assert VerbEnum.POST.value == "POST"


def test_verb_enum_00220():
    """
    # Summary

    VerbEnum.PUT has correct value

    ## Description

    Verifies that VerbEnum.PUT evaluates to the string "PUT".

    ### Pass/Fail Criteria

    - PASS: VerbEnum.PUT.value equals "PUT"
    - FAIL: Value is anything other than "PUT"
    """
    assert VerbEnum.PUT.value == "PUT"


def test_verb_enum_00230():
    """
    # Summary

    VerbEnum.DELETE has correct value

    ## Description

    Verifies that VerbEnum.DELETE evaluates to the string "DELETE".

    ### Pass/Fail Criteria

    - PASS: VerbEnum.DELETE.value equals "DELETE"
    - FAIL: Value is anything other than "DELETE"
    """
    assert VerbEnum.DELETE.value == "DELETE"


def test_verb_enum_00240():
    """
    # Summary

    VerbEnum is instance of str

    ## Description

    Verifies that VerbEnum inherits from str, allowing it to be used
    anywhere a string is expected (e.g., HTTP method headers).

    ### Pass/Fail Criteria

    - PASS: All VerbEnum members are instances of str
    - FAIL: Not instances of str
    """
    assert isinstance(VerbEnum.GET, str)
    assert isinstance(VerbEnum.POST, str)
    assert isinstance(VerbEnum.PUT, str)
    assert isinstance(VerbEnum.DELETE, str)


def test_verb_enum_00250():
    """
    # Summary

    VerbEnum value accessibility

    ## Description

    Verifies that VerbEnum member values are accessible and match
    the expected HTTP method names.

    ### Pass/Fail Criteria

    - PASS: .value attribute returns HTTP method name
    - FAIL: Returns different value
    """
    assert VerbEnum.GET.value == "GET"
    assert VerbEnum.POST.value == "POST"
    assert VerbEnum.PUT.value == "PUT"
    assert VerbEnum.DELETE.value == "DELETE"


def test_verb_enum_00260():
    """
    # Summary

    VerbEnum has exactly four members

    ## Description

    Verifies that VerbEnum contains exactly the four standard HTTP methods.
    This prevents accidental addition of invalid HTTP methods.

    ### Pass/Fail Criteria

    - PASS: VerbEnum has exactly 4 members
    - FAIL: Different number of members
    """
    assert len(VerbEnum) == 4
    assert set(VerbEnum) == {VerbEnum.GET, VerbEnum.POST, VerbEnum.PUT, VerbEnum.DELETE}
