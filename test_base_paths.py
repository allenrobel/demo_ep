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
Unit tests for base_paths module.

Tests the BasePath class to ensure correct API path construction
for all NDFC API endpoints.
"""

import pytest
from base_paths import BasePath

# ============================================================================
# Constants Tests (100-199)
# ============================================================================


def test_base_path_constants_00100() -> None:
    """
    # Summary

    BasePath.NDFC_API constant has correct value

    ## Description

    Verifies that the root NDFC API path constant is set correctly.
    This is the foundation for all API path construction.

    ### Pass/Fail Criteria

    - PASS: NDFC_API equals "/appcenter/cisco/ndfc/api"
    - FAIL: Value is different
    """
    assert BasePath.NDFC_API == "/appcenter/cisco/ndfc/api"


def test_base_path_constants_00110() -> None:
    """
    # Summary

    BasePath.ONEMANAGE constant has correct value

    ## Description

    Verifies that the OneManage path segment constant is correct.

    ### Pass/Fail Criteria

    - PASS: ONEMANAGE equals "/onemanage"
    - FAIL: Value is different
    """
    assert BasePath.ONEMANAGE == "/onemanage"


def test_base_path_constants_00120() -> None:
    """
    # Summary

    BasePath.LOGIN constant has correct value

    ## Description

    Verifies that the login path segment constant is correct.

    ### Pass/Fail Criteria

    - PASS: LOGIN equals "/login"
    - FAIL: Value is different
    """
    assert BasePath.LOGIN == "/login"


# ============================================================================
# api() Method Tests (200-299)
# ============================================================================


def test_base_path_api_00200() -> None:
    """
    # Summary

    BasePath.api() with no segments returns root

    ## Description

    When called without arguments, api() should return just the NDFC_API root.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api"
    - FAIL: Returns different value or raises error
    """
    assert BasePath.api() == "/appcenter/cisco/ndfc/api"


def test_base_path_api_00210() -> None:
    """
    # Summary

    BasePath.api() with single segment

    ## Description

    When called with one segment, api() should append it to the root.

    ### Pass/Fail Criteria

    - PASS: Returns root + "/" + segment
    - FAIL: Incorrect path construction
    """
    assert BasePath.api("custom") == "/appcenter/cisco/ndfc/api/custom"


def test_base_path_api_00220() -> None:
    """
    # Summary

    BasePath.api() with multiple segments

    ## Description

    When called with multiple segments, api() should join them with slashes.

    ### Pass/Fail Criteria

    - PASS: Returns root + "/" + all segments joined
    - FAIL: Incorrect path construction
    """
    result = BasePath.api("custom", "endpoint", "path")
    assert result == "/appcenter/cisco/ndfc/api/custom/endpoint/path"


# ============================================================================
# v1() Method Tests (300-399)
# ============================================================================


def test_base_path_v1_00300() -> None:
    """
    # Summary

    BasePath.v1() with no segments

    ## Description

    When called without arguments, v1() should return the v1 API root.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1"
    - FAIL: Incorrect path
    """
    assert BasePath.v1() == "/appcenter/cisco/ndfc/api/v1"


def test_base_path_v1_00310() -> None:
    """
    # Summary

    BasePath.v1() with segments

    ## Description

    When called with segments, v1() should append them after v1.

    ### Pass/Fail Criteria

    - PASS: Returns v1 root + segments
    - FAIL: Incorrect path construction
    """
    result = BasePath.v1("lan-fabric", "rest")
    assert result == "/appcenter/cisco/ndfc/api/v1/lan-fabric/rest"


# ============================================================================
# lan_fabric() Method Tests (400-499)
# ============================================================================


def test_base_path_lan_fabric_00400() -> None:
    """
    # Summary

    BasePath.lan_fabric() with no segments

    ## Description

    Returns the lan-fabric API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/lan-fabric"
    - FAIL: Incorrect path
    """
    assert BasePath.lan_fabric() == "/appcenter/cisco/ndfc/api/v1/lan-fabric"


def test_base_path_lan_fabric_00410() -> None:
    """
    # Summary

    BasePath.lan_fabric() with segments

    ## Description

    Appends segments to lan-fabric path.

    ### Pass/Fail Criteria

    - PASS: Returns lan-fabric path + segments
    - FAIL: Incorrect path construction
    """
    result = BasePath.lan_fabric("rest", "control")
    assert result == "/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control"


# ============================================================================
# control_fabrics() Method Tests (500-599)
# ============================================================================


def test_base_path_control_fabrics_00500() -> None:
    """
    # Summary

    BasePath.control_fabrics() with no segments

    ## Description

    Returns the control/fabrics API root path.

    ### Pass/Fail Criteria

    - PASS: Returns correct control/fabrics path
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control/fabrics"
    assert BasePath.control_fabrics() == expected


def test_base_path_control_fabrics_00510() -> None:
    """
    # Summary

    BasePath.control_fabrics() with fabric name

    ## Description

    Constructs path with fabric name segment.

    ### Pass/Fail Criteria

    - PASS: Returns control/fabrics/{fabricName} path
    - FAIL: Incorrect path construction
    """
    result = BasePath.control_fabrics("MyFabric")
    expected = "/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control/fabrics/MyFabric"
    assert result == expected


def test_base_path_control_fabrics_00520() -> None:
    """
    # Summary

    BasePath.control_fabrics() with fabric and operation

    ## Description

    Constructs path with fabric name and operation segments.

    ### Pass/Fail Criteria

    - PASS: Returns control/fabrics/{fabricName}/{operation} path
    - FAIL: Incorrect path construction
    """
    result = BasePath.control_fabrics("MyFabric", "config-deploy")
    expected = "/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control/fabrics/MyFabric/config-deploy"
    assert result == expected


# ============================================================================
# onemanage() Method Tests (600-699)
# ============================================================================


def test_base_path_onemanage_00600() -> None:
    """
    # Summary

    BasePath.onemanage() with no segments

    ## Description

    Returns the onemanage API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage"
    - FAIL: Incorrect path
    """
    assert BasePath.onemanage() == "/appcenter/cisco/ndfc/api/v1/onemanage"


def test_base_path_onemanage_00610() -> None:
    """
    # Summary

    BasePath.onemanage() with segments

    ## Description

    Constructs onemanage path with additional segments.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage path + segments
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage("fabrics", "MyFabric")
    assert result == "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric"


# ============================================================================
# onemanage_fabrics() Method Tests (700-799)
# ============================================================================


def test_base_path_onemanage_fabrics_00700() -> None:
    """
    # Summary

    BasePath.onemanage_fabrics() with no segments

    ## Description

    Returns the onemanage/fabrics API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics"
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics"
    assert BasePath.onemanage_fabrics() == expected


def test_base_path_onemanage_fabrics_00710() -> None:
    """
    # Summary

    BasePath.onemanage_fabrics() with fabric name

    ## Description

    Constructs path with fabric name segment.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage/fabrics/{fabricName} path
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage_fabrics("MyFabric")
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric"
    assert result == expected


def test_base_path_onemanage_fabrics_00720() -> None:
    """
    # Summary

    BasePath.onemanage_fabrics() with fabric, operation, and serial

    ## Description

    Constructs full path with all segments for switch-specific operations.

    ### Pass/Fail Criteria

    - PASS: Returns complete path with all segments
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage_fabrics("MyFabric", "config-deploy", "FOC12345678")
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric/config-deploy/FOC12345678"
    assert result == expected


# ============================================================================
# onemanage_links() Method Tests (800-899)
# ============================================================================


def test_base_path_onemanage_links_00800() -> None:
    """
    # Summary

    BasePath.onemanage_links() with no segments

    ## Description

    Returns the onemanage/links API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage/links"
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/links"
    assert BasePath.onemanage_links() == expected


def test_base_path_onemanage_links_00810() -> None:
    """
    # Summary

    BasePath.onemanage_links() with UUID

    ## Description

    Constructs path with link UUID segment.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage/links/{uuid} path
    - FAIL: Incorrect path construction
    """
    uuid = "63505f61-ce7b-40a6-a38c-ae9a355b2116"
    result = BasePath.onemanage_links(uuid)
    expected = f"/appcenter/cisco/ndfc/api/v1/onemanage/links/{uuid}"
    assert result == expected


# ============================================================================
# onemanage_links_fabrics() Method Tests (900-999)
# ============================================================================


def test_base_path_onemanage_links_fabrics_00900() -> None:
    """
    # Summary

    BasePath.onemanage_links_fabrics() with no segments

    ## Description

    Returns the onemanage/links/fabrics API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage/links/fabrics"
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/links/fabrics"
    assert BasePath.onemanage_links_fabrics() == expected


def test_base_path_onemanage_links_fabrics_00910() -> None:
    """
    # Summary

    BasePath.onemanage_links_fabrics() with fabric name

    ## Description

    Constructs path with fabric name segment.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage/links/fabrics/{fabricName} path
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage_links_fabrics("MyFabric")
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/links/fabrics/MyFabric"
    assert result == expected


# ============================================================================
# onemanage_top_down() Method Tests (1000-1099)
# ============================================================================


def test_base_path_onemanage_top_down_01000() -> None:
    """
    # Summary

    BasePath.onemanage_top_down() with no segments

    ## Description

    Returns the onemanage/top-down API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage/top-down"
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/top-down"
    assert BasePath.onemanage_top_down() == expected


def test_base_path_onemanage_top_down_01010() -> None:
    """
    # Summary

    BasePath.onemanage_top_down() with segments

    ## Description

    Constructs top-down path with additional segments.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage/top-down path + segments
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage_top_down("fabrics", "MyFabric")
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/MyFabric"
    assert result == expected


# ============================================================================
# onemanage_top_down_fabrics() Method Tests (1100-1199)
# ============================================================================


def test_base_path_onemanage_top_down_fabrics_01100() -> None:
    """
    # Summary

    BasePath.onemanage_top_down_fabrics() with no segments

    ## Description

    Returns the onemanage/top-down/fabrics API root path.

    ### Pass/Fail Criteria

    - PASS: Returns "/appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics"
    - FAIL: Incorrect path
    """
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics"
    assert BasePath.onemanage_top_down_fabrics() == expected


def test_base_path_onemanage_top_down_fabrics_01110() -> None:
    """
    # Summary

    BasePath.onemanage_top_down_fabrics() with fabric name

    ## Description

    Constructs path with fabric name segment.

    ### Pass/Fail Criteria

    - PASS: Returns onemanage/top-down/fabrics/{fabricName} path
    - FAIL: Incorrect path construction
    """
    result = BasePath.onemanage_top_down_fabrics("MyFabric")
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/MyFabric"
    assert result == expected
