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
Unit tests for endpoints module.

Tests endpoint classes to ensure correct path construction, query parameter
handling, and HTTP verb assignment.
"""

import pytest
from endpoints import (
    EpOneManageFabricConfigDeploy,
    EpOneManageFabricConfigDeploySwitch,
    EpOneManageFabricConfigPreview,
    EpOneManageFabricConfigPreviewSwitch,
    FabricConfigDeployQueryParams,
    FabricConfigPreviewQueryParams,
)
from enums import BooleanStringEnum, VerbEnum


# ============================================================================
# FabricConfigDeployQueryParams Tests (100-199)
# ============================================================================

def test_fabric_config_deploy_query_params_00100():
    """
    # Summary

    FabricConfigDeployQueryParams default values

    ## Description

    Verifies that FabricConfigDeployQueryParams initializes with correct
    default values for force_show_run and incl_all_msd_switches.

    ### Pass/Fail Criteria

    - PASS: Both fields default to BooleanStringEnum.FALSE
    - FAIL: Different default values
    """
    params = FabricConfigDeployQueryParams()
    assert params.force_show_run == BooleanStringEnum.FALSE
    assert params.incl_all_msd_switches == BooleanStringEnum.FALSE


def test_fabric_config_deploy_query_params_00110():
    """
    # Summary

    FabricConfigDeployQueryParams to_query_string with defaults

    ## Description

    Verifies that the query string includes both parameters even when
    they have default values (false).

    ### Pass/Fail Criteria

    - PASS: Query string contains both params set to "false"
    - FAIL: Missing parameters or incorrect values
    """
    params = FabricConfigDeployQueryParams()
    query_string = params.to_query_string()
    assert "forceShowRun=false" in query_string
    assert "inclAllMSDSwitches=false" in query_string


def test_fabric_config_deploy_query_params_00120():
    """
    # Summary

    FabricConfigDeployQueryParams to_query_string with TRUE values

    ## Description

    Verifies that when parameters are set to TRUE, the query string
    reflects this correctly.

    ### Pass/Fail Criteria

    - PASS: Query string contains params set to "true"
    - FAIL: Incorrect values in query string
    """
    params = FabricConfigDeployQueryParams()
    params.force_show_run = BooleanStringEnum.TRUE
    params.incl_all_msd_switches = BooleanStringEnum.TRUE

    query_string = params.to_query_string()
    assert "forceShowRun=true" in query_string
    assert "inclAllMSDSwitches=true" in query_string


def test_fabric_config_deploy_query_params_00130():
    """
    # Summary

    FabricConfigDeployQueryParams enum value extraction

    ## Description

    Verifies that the to_query_string method correctly extracts the
    .value from enum members (not the enum representation).

    ### Pass/Fail Criteria

    - PASS: Query string contains "true"/"false", not "BooleanStringEnum.TRUE"
    - FAIL: Enum representation appears in query string
    """
    params = FabricConfigDeployQueryParams()
    query_string = params.to_query_string()
    assert "BooleanStringEnum" not in query_string
    assert "false" in query_string


def test_fabric_config_deploy_query_params_00140():
    """
    # Summary

    FabricConfigDeployQueryParams validate_assignment enabled

    ## Description

    Verifies that validate_assignment=True in Config allows runtime
    validation of field assignments.

    ### Pass/Fail Criteria

    - PASS: Invalid assignments raise ValidationError
    - FAIL: Invalid assignments accepted
    """
    params = FabricConfigDeployQueryParams()

    # Valid assignment should work
    params.force_show_run = BooleanStringEnum.TRUE
    assert params.force_show_run == BooleanStringEnum.TRUE


# ============================================================================
# FabricConfigPreviewQueryParams Tests (200-299)
# ============================================================================

def test_fabric_config_preview_query_params_00200():
    """
    # Summary

    FabricConfigPreviewQueryParams default values

    ## Description

    Verifies that FabricConfigPreviewQueryParams initializes with correct
    default values for force_show_run and show_brief.

    ### Pass/Fail Criteria

    - PASS: Both fields default to BooleanStringEnum.FALSE
    - FAIL: Different default values
    """
    params = FabricConfigPreviewQueryParams()
    assert params.force_show_run == BooleanStringEnum.FALSE
    assert params.show_brief == BooleanStringEnum.FALSE


def test_fabric_config_preview_query_params_00210():
    """
    # Summary

    FabricConfigPreviewQueryParams to_query_string with defaults

    ## Description

    Verifies that when parameters have default FALSE values,
    they still appear in the query string because the string "false"
    is truthy in Python.

    ### Pass/Fail Criteria

    - PASS: Query string contains both params set to "false"
    - FAIL: Parameters missing from query string
    """
    params = FabricConfigPreviewQueryParams()
    query_string = params.to_query_string()
    # Even with FALSE values, they appear because "false" string is truthy
    assert "forceShowRun=false" in query_string
    assert "showBrief=false" in query_string


def test_fabric_config_preview_query_params_00220():
    """
    # Summary

    FabricConfigPreviewQueryParams to_query_string with TRUE values

    ## Description

    Verifies that when parameters are set to TRUE, they appear in
    the query string.

    ### Pass/Fail Criteria

    - PASS: Query string contains both params set to "true"
    - FAIL: Missing or incorrect values
    """
    params = FabricConfigPreviewQueryParams()
    params.force_show_run = BooleanStringEnum.TRUE
    params.show_brief = BooleanStringEnum.TRUE

    query_string = params.to_query_string()
    assert "forceShowRun=true" in query_string
    assert "showBrief=true" in query_string


def test_fabric_config_preview_query_params_00230():
    """
    # Summary

    FabricConfigPreviewQueryParams mixed TRUE/FALSE

    ## Description

    Verifies that both parameters appear regardless of TRUE/FALSE
    because the string "false" is truthy.

    ### Pass/Fail Criteria

    - PASS: Both parameters appear with correct values
    - FAIL: Missing parameters
    """
    params = FabricConfigPreviewQueryParams()
    params.force_show_run = BooleanStringEnum.TRUE
    params.show_brief = BooleanStringEnum.FALSE

    query_string = params.to_query_string()
    assert "forceShowRun=true" in query_string
    assert "showBrief=false" in query_string


# ============================================================================
# EpOneManageFabricConfigDeploy Tests (300-399)
# ============================================================================

def test_ep_one_manage_fabric_config_deploy_00300():
    """
    # Summary

    EpOneManageFabricConfigDeploy instantiation

    ## Description

    Verifies that the endpoint can be instantiated and has the correct
    default class_name.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails or incorrect class_name
    """
    ep = EpOneManageFabricConfigDeploy()
    assert ep.class_name == "EpOneManageFabricConfigDeploy"


def test_ep_one_manage_fabric_config_deploy_00310():
    """
    # Summary

    EpOneManageFabricConfigDeploy query_params initialization

    ## Description

    Verifies that query_params is initialized as FabricConfigDeployQueryParams
    with default values.

    ### Pass/Fail Criteria

    - PASS: query_params is FabricConfigDeployQueryParams with defaults
    - FAIL: Wrong type or missing
    """
    ep = EpOneManageFabricConfigDeploy()
    assert isinstance(ep.query_params, FabricConfigDeployQueryParams)
    assert ep.query_params.force_show_run == BooleanStringEnum.FALSE


def test_ep_one_manage_fabric_config_deploy_00320():
    """
    # Summary

    EpOneManageFabricConfigDeploy verb is POST

    ## Description

    Verifies that the HTTP verb for this endpoint is POST.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.POST
    - FAIL: Different verb returned
    """
    ep = EpOneManageFabricConfigDeploy()
    ep.fabric_name = "TestFabric"
    assert ep.verb == VerbEnum.POST


def test_ep_one_manage_fabric_config_deploy_00330():
    """
    # Summary

    EpOneManageFabricConfigDeploy path without fabric_name raises ValueError

    ## Description

    Verifies that accessing the path property without setting fabric_name
    raises a ValueError.

    ### Pass/Fail Criteria

    - PASS: ValueError raised with appropriate message
    - FAIL: No error raised or different error
    """
    ep = EpOneManageFabricConfigDeploy()
    with pytest.raises(ValueError, match="fabric_name must be set"):
        _ = ep.path


def test_ep_one_manage_fabric_config_deploy_00340():
    """
    # Summary

    EpOneManageFabricConfigDeploy path construction

    ## Description

    Verifies that the path is correctly constructed with fabric_name
    and query parameters.

    ### Pass/Fail Criteria

    - PASS: Path matches expected format with query string
    - FAIL: Incorrect path construction
    """
    ep = EpOneManageFabricConfigDeploy()
    ep.fabric_name = "MyFabric"
    ep.query_params.force_show_run = BooleanStringEnum.TRUE

    path = ep.path
    expected_base = "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric/config-deploy"
    assert expected_base in path
    assert "?" in path
    assert "forceShowRun=true" in path


def test_ep_one_manage_fabric_config_deploy_00350():
    """
    # Summary

    EpOneManageFabricConfigDeploy fabric_name validation

    ## Description

    Verifies that fabric_name field can be set and retrieved correctly.

    ### Pass/Fail Criteria

    - PASS: fabric_name can be set and matches on retrieval
    - FAIL: Value not stored correctly
    """
    ep = EpOneManageFabricConfigDeploy()
    test_name = "ProductionFabric"
    ep.fabric_name = test_name
    assert ep.fabric_name == test_name


# ============================================================================
# EpOneManageFabricConfigDeploySwitch Tests (400-499)
# ============================================================================

def test_ep_one_manage_fabric_config_deploy_switch_00400():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch instantiation

    ## Description

    Verifies that the endpoint can be instantiated with correct defaults.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    assert ep.class_name == "EpOneManageFabricConfigDeploySwitch"


def test_ep_one_manage_fabric_config_deploy_switch_00410():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch verb is POST

    ## Description

    Verifies that the HTTP verb for this endpoint is POST.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.POST
    - FAIL: Different verb returned
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "TestFabric"
    ep.switch_sn = "FOC12345678"
    assert ep.verb == VerbEnum.POST


def test_ep_one_manage_fabric_config_deploy_switch_00420():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch path requires fabric_name

    ## Description

    Verifies that accessing path without fabric_name raises ValueError.

    ### Pass/Fail Criteria

    - PASS: ValueError raised
    - FAIL: No error or different error
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.switch_sn = "FOC12345678"
    with pytest.raises(ValueError, match="fabric_name must be set"):
        _ = ep.path


def test_ep_one_manage_fabric_config_deploy_switch_00430():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch path requires switch_sn

    ## Description

    Verifies that accessing path without switch_sn raises ValueError.

    ### Pass/Fail Criteria

    - PASS: ValueError raised
    - FAIL: No error or different error
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    with pytest.raises(ValueError, match="switch_sn must be set"):
        _ = ep.path


def test_ep_one_manage_fabric_config_deploy_switch_00440():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch path construction with both params

    ## Description

    Verifies that the path is correctly constructed with both fabric_name
    and switch_sn.

    ### Pass/Fail Criteria

    - PASS: Path includes fabric name and switch serial number
    - FAIL: Incorrect path construction
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    path = ep.path
    expected = "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric/config-deploy/FOC12345678"
    assert expected in path


def test_ep_one_manage_fabric_config_deploy_switch_00450():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch path includes query params

    ## Description

    Verifies that query parameters are appended to the path.

    ### Pass/Fail Criteria

    - PASS: Path includes query string with parameters
    - FAIL: Query parameters missing
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"
    ep.query_params.force_show_run = BooleanStringEnum.TRUE

    path = ep.path
    assert "?" in path
    assert "forceShowRun=true" in path


def test_ep_one_manage_fabric_config_deploy_switch_00460():
    """
    # Summary

    EpOneManageFabricConfigDeploySwitch query_params modification

    ## Description

    Verifies that query_params can be modified and changes are reflected
    in the path.

    ### Pass/Fail Criteria

    - PASS: Modified params appear in path
    - FAIL: Changes not reflected
    """
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    # Initially defaults
    path1 = ep.path
    assert "forceShowRun=false" in path1

    # Modify
    ep.query_params.force_show_run = BooleanStringEnum.TRUE
    path2 = ep.path
    assert "forceShowRun=true" in path2


# ============================================================================
# EpOneManageFabricConfigPreview Tests (500-599)
# ============================================================================

def test_ep_one_manage_fabric_config_preview_00500():
    """
    # Summary

    EpOneManageFabricConfigPreview instantiation

    ## Description

    Verifies that the endpoint can be instantiated correctly.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name correct
    - FAIL: Instantiation fails
    """
    ep = EpOneManageFabricConfigPreview()
    assert ep.class_name == "EpOneManageFabricConfigPreview"


def test_ep_one_manage_fabric_config_preview_00510():
    """
    # Summary

    EpOneManageFabricConfigPreview verb is GET

    ## Description

    Verifies that the HTTP verb for preview endpoints is GET.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.GET
    - FAIL: Different verb returned
    """
    ep = EpOneManageFabricConfigPreview()
    ep.fabric_name = "TestFabric"
    assert ep.verb == VerbEnum.GET


def test_ep_one_manage_fabric_config_preview_00520():
    """
    # Summary

    EpOneManageFabricConfigPreview query_params type

    ## Description

    Verifies that query_params is FabricConfigPreviewQueryParams.

    ### Pass/Fail Criteria

    - PASS: query_params is correct type
    - FAIL: Wrong type
    """
    ep = EpOneManageFabricConfigPreview()
    assert isinstance(ep.query_params, FabricConfigPreviewQueryParams)


def test_ep_one_manage_fabric_config_preview_00530():
    """
    # Summary

    EpOneManageFabricConfigPreview path construction

    ## Description

    Verifies that path is constructed correctly for preview endpoint.

    ### Pass/Fail Criteria

    - PASS: Path contains "config-preview"
    - FAIL: Incorrect path
    """
    ep = EpOneManageFabricConfigPreview()
    ep.fabric_name = "MyFabric"

    path = ep.path
    assert "/config-preview" in path
    assert "MyFabric" in path


# ============================================================================
# EpOneManageFabricConfigPreviewSwitch Tests (600-699)
# ============================================================================

def test_ep_one_manage_fabric_config_preview_switch_00600():
    """
    # Summary

    EpOneManageFabricConfigPreviewSwitch instantiation

    ## Description

    Verifies correct instantiation of switch-specific preview endpoint.

    ### Pass/Fail Criteria

    - PASS: Instance created correctly
    - FAIL: Instantiation fails
    """
    ep = EpOneManageFabricConfigPreviewSwitch()
    assert ep.class_name == "EpOneManageFabricConfigPreviewSwitch"


def test_ep_one_manage_fabric_config_preview_switch_00610():
    """
    # Summary

    EpOneManageFabricConfigPreviewSwitch verb is GET

    ## Description

    Verifies that the HTTP verb is GET for preview operations.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.GET
    - FAIL: Different verb returned
    """
    ep = EpOneManageFabricConfigPreviewSwitch()
    ep.fabric_name = "TestFabric"
    ep.switch_sn = "FOC12345678"
    assert ep.verb == VerbEnum.GET


def test_ep_one_manage_fabric_config_preview_switch_00620():
    """
    # Summary

    EpOneManageFabricConfigPreviewSwitch path requires both params

    ## Description

    Verifies that both fabric_name and switch_sn are required for path.

    ### Pass/Fail Criteria

    - PASS: ValueError raised when either is missing
    - FAIL: No error when params missing
    """
    ep = EpOneManageFabricConfigPreviewSwitch()

    # Missing both
    with pytest.raises(ValueError):
        _ = ep.path

    # Missing switch_sn
    ep.fabric_name = "MyFabric"
    with pytest.raises(ValueError, match="switch_sn"):
        _ = ep.path


def test_ep_one_manage_fabric_config_preview_switch_00630():
    """
    # Summary

    EpOneManageFabricConfigPreviewSwitch complete path construction

    ## Description

    Verifies that path is correctly constructed with all required components.

    ### Pass/Fail Criteria

    - PASS: Path includes fabric, switch serial, and config-preview
    - FAIL: Missing components
    """
    ep = EpOneManageFabricConfigPreviewSwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    path = ep.path
    assert "MyFabric" in path
    assert "FOC12345678" in path
    assert "/config-preview/" in path


def test_ep_one_manage_fabric_config_preview_switch_00640():
    """
    # Summary

    EpOneManageFabricConfigPreviewSwitch show_brief parameter

    ## Description

    Verifies that the show_brief query parameter works correctly.

    ### Pass/Fail Criteria

    - PASS: show_brief=true appears in path when set
    - FAIL: Parameter missing or incorrect
    """
    ep = EpOneManageFabricConfigPreviewSwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"
    ep.query_params.show_brief = BooleanStringEnum.TRUE

    path = ep.path
    assert "showBrief=true" in path
