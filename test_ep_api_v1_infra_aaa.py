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
Unit tests for ND Infra AAA endpoint module.

Tests endpoint classes to ensure correct path construction and HTTP verb
assignment for ND Infra AAA endpoints.
"""

import pytest
from enums import VerbEnum
from ep_api_v1_infra_aaa import (
    EpApiV1InfraAaaLocalUsersGet,
    EpApiV1InfraAaaLocalUsersPost,
    EpApiV1InfraAaaLocalUsersPut,
    EpApiV1InfraAaaLocalUsersDelete,
)

# ============================================================================
# EpApiV1InfraAaaLocalUsersGet Tests (1000-1099)
# ============================================================================


def test_ep_api_v1_infra_aaa_local_users_get_01000():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet instantiation

    ## Description

    Verifies that the endpoint can be instantiated and has the correct
    default class_name.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails or incorrect class_name
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    assert ep.class_name == "EpApiV1InfraAaaLocalUsersGet"


def test_ep_api_v1_infra_aaa_local_users_get_01010():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet verb is GET

    ## Description

    Verifies that the HTTP verb for this endpoint is GET.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.GET
    - FAIL: Different verb returned
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    assert ep.verb == VerbEnum.GET


def test_ep_api_v1_infra_aaa_local_users_get_01020():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet path without login_id

    ## Description

    Verifies that the path is correctly constructed without login_id,
    returning the base endpoint path.

    ### Pass/Fail Criteria

    - PASS: Path matches /api/v1/infra/aaa/localUsers
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers"


def test_ep_api_v1_infra_aaa_local_users_get_01030():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet path with login_id

    ## Description

    Verifies that the path is correctly constructed with login_id,
    appending it as a path parameter.

    ### Pass/Fail Criteria

    - PASS: Path matches /api/v1/infra/aaa/localUsers/{login_id}
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    ep.login_id = "admin"
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers/admin"


def test_ep_api_v1_infra_aaa_local_users_get_01040():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet login_id field validation

    ## Description

    Verifies that login_id field can be set and retrieved correctly.

    ### Pass/Fail Criteria

    - PASS: login_id can be set and matches on retrieval
    - FAIL: Value not stored correctly
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    test_id = "testuser"
    ep.login_id = test_id
    assert ep.login_id == test_id


def test_ep_api_v1_infra_aaa_local_users_get_01050():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersGet login_id defaults to None

    ## Description

    Verifies that login_id defaults to None upon instantiation.

    ### Pass/Fail Criteria

    - PASS: login_id is None by default
    - FAIL: Different default value
    """
    ep = EpApiV1InfraAaaLocalUsersGet()
    assert ep.login_id is None


# ============================================================================
# EpApiV1InfraAaaLocalUsersPost Tests (1100-1199)
# ============================================================================


def test_ep_api_v1_infra_aaa_local_users_post_01100():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPost instantiation

    ## Description

    Verifies that the endpoint can be instantiated and has the correct
    default class_name.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails or incorrect class_name
    """
    ep = EpApiV1InfraAaaLocalUsersPost()
    assert ep.class_name == "EpApiV1InfraAaaLocalUsersPost"


def test_ep_api_v1_infra_aaa_local_users_post_01110():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPost verb is POST

    ## Description

    Verifies that the HTTP verb for this endpoint is POST.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.POST
    - FAIL: Different verb returned
    """
    ep = EpApiV1InfraAaaLocalUsersPost()
    assert ep.verb == VerbEnum.POST


def test_ep_api_v1_infra_aaa_local_users_post_01120():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPost path without login_id

    ## Description

    Verifies that the path for POST operations is the base endpoint
    without login_id.

    ### Pass/Fail Criteria

    - PASS: Path matches /api/v1/infra/aaa/localUsers
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersPost()
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers"


def test_ep_api_v1_infra_aaa_local_users_post_01130():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPost path with login_id

    ## Description

    Verifies that login_id can be set, though it's not typically used
    for POST operations.

    ### Pass/Fail Criteria

    - PASS: Path includes login_id when set
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersPost()
    ep.login_id = "newuser"
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers/newuser"


# ============================================================================
# EpApiV1InfraAaaLocalUsersPut Tests (1200-1299)
# ============================================================================


def test_ep_api_v1_infra_aaa_local_users_put_01200():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPut instantiation

    ## Description

    Verifies that the endpoint can be instantiated and has the correct
    default class_name.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails or incorrect class_name
    """
    ep = EpApiV1InfraAaaLocalUsersPut()
    assert ep.class_name == "EpApiV1InfraAaaLocalUsersPut"


def test_ep_api_v1_infra_aaa_local_users_put_01210():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPut verb is PUT

    ## Description

    Verifies that the HTTP verb for this endpoint is PUT.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.PUT
    - FAIL: Different verb returned
    """
    ep = EpApiV1InfraAaaLocalUsersPut()
    assert ep.verb == VerbEnum.PUT


def test_ep_api_v1_infra_aaa_local_users_put_01220():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPut path requires login_id

    ## Description

    Verifies that for PUT operations, login_id is typically required
    (though not enforced by the class).

    ### Pass/Fail Criteria

    - PASS: Path includes login_id when set
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersPut()
    ep.login_id = "admin"
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers/admin"


def test_ep_api_v1_infra_aaa_local_users_put_01230():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersPut path without login_id

    ## Description

    Verifies that path can be constructed without login_id, though
    this may not be semantically valid for PUT operations.

    ### Pass/Fail Criteria

    - PASS: Path matches /api/v1/infra/aaa/localUsers
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersPut()
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers"


# ============================================================================
# EpApiV1InfraAaaLocalUsersDelete Tests (1300-1399)
# ============================================================================


def test_ep_api_v1_infra_aaa_local_users_delete_01300():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersDelete instantiation

    ## Description

    Verifies that the endpoint can be instantiated and has the correct
    default class_name.

    ### Pass/Fail Criteria

    - PASS: Instance created, class_name set correctly
    - FAIL: Instantiation fails or incorrect class_name
    """
    ep = EpApiV1InfraAaaLocalUsersDelete()
    assert ep.class_name == "EpApiV1InfraAaaLocalUsersDelete"


def test_ep_api_v1_infra_aaa_local_users_delete_01310():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersDelete verb is DELETE

    ## Description

    Verifies that the HTTP verb for this endpoint is DELETE.

    ### Pass/Fail Criteria

    - PASS: verb property returns VerbEnum.DELETE
    - FAIL: Different verb returned
    """
    ep = EpApiV1InfraAaaLocalUsersDelete()
    assert ep.verb == VerbEnum.DELETE


def test_ep_api_v1_infra_aaa_local_users_delete_01320():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersDelete path requires login_id

    ## Description

    Verifies that for DELETE operations, login_id is typically required
    (though not enforced by the class).

    ### Pass/Fail Criteria

    - PASS: Path includes login_id when set
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersDelete()
    ep.login_id = "olduser"
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers/olduser"


def test_ep_api_v1_infra_aaa_local_users_delete_01330():
    """
    # Summary

    EpApiV1InfraAaaLocalUsersDelete path without login_id

    ## Description

    Verifies that path can be constructed without login_id, though
    this may not be semantically valid for DELETE operations.

    ### Pass/Fail Criteria

    - PASS: Path matches /api/v1/infra/aaa/localUsers
    - FAIL: Incorrect path construction
    """
    ep = EpApiV1InfraAaaLocalUsersDelete()
    path = ep.path
    assert path == "/api/v1/infra/aaa/localUsers"


# ============================================================================
# Cross-Endpoint Behavior Tests (1400-1499)
# ============================================================================


def test_ep_api_v1_infra_aaa_multiple_instances_01400():
    """
    # Summary

    Multiple endpoint instances maintain independent state

    ## Description

    Verifies that multiple instances of different endpoint classes
    maintain independent state.

    ### Pass/Fail Criteria

    - PASS: Each instance has its own login_id
    - FAIL: Instances share state
    """
    get_ep = EpApiV1InfraAaaLocalUsersGet()
    delete_ep = EpApiV1InfraAaaLocalUsersDelete()

    get_ep.login_id = "user1"
    delete_ep.login_id = "user2"

    assert get_ep.login_id == "user1"
    assert delete_ep.login_id == "user2"


def test_ep_api_v1_infra_aaa_path_consistency_01410():
    """
    # Summary

    All endpoint classes produce consistent paths

    ## Description

    Verifies that all endpoint classes produce the same path for
    the same login_id value.

    ### Pass/Fail Criteria

    - PASS: All classes produce identical paths for same input
    - FAIL: Different classes produce different paths
    """
    login_id = "testuser"

    get_ep = EpApiV1InfraAaaLocalUsersGet()
    post_ep = EpApiV1InfraAaaLocalUsersPost()
    put_ep = EpApiV1InfraAaaLocalUsersPut()
    delete_ep = EpApiV1InfraAaaLocalUsersDelete()

    get_ep.login_id = login_id
    post_ep.login_id = login_id
    put_ep.login_id = login_id
    delete_ep.login_id = login_id

    expected_path = "/api/v1/infra/aaa/localUsers/testuser"

    assert get_ep.path == expected_path
    assert post_ep.path == expected_path
    assert put_ep.path == expected_path
    assert delete_ep.path == expected_path


def test_ep_api_v1_infra_aaa_verb_distinction_01420():
    """
    # Summary

    Each endpoint class returns correct verb

    ## Description

    Verifies that each endpoint class returns its specific HTTP verb.

    ### Pass/Fail Criteria

    - PASS: Each class returns correct verb
    - FAIL: Verbs are incorrect or identical
    """
    get_ep = EpApiV1InfraAaaLocalUsersGet()
    post_ep = EpApiV1InfraAaaLocalUsersPost()
    put_ep = EpApiV1InfraAaaLocalUsersPut()
    delete_ep = EpApiV1InfraAaaLocalUsersDelete()

    assert get_ep.verb == VerbEnum.GET
    assert post_ep.verb == VerbEnum.POST
    assert put_ep.verb == VerbEnum.PUT
    assert delete_ep.verb == VerbEnum.DELETE
