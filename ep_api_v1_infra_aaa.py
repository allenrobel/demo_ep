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
ND Infra AAA endpoint models.

This module contains endpoint definitions for AAA-related operations
in the ND Infra API.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Literal
from base_paths import BasePath
from endpoint_mixins import LoginIdMixin
from enums import VerbEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, ConfigDict, Field
else:
    from pydantic_compat import BaseModel, ConfigDict, Field

# Common config for basic validation
COMMON_CONFIG = ConfigDict(validate_assignment=True)


class _EpApiV1InfraAaaLocalUsersBase(LoginIdMixin, BaseModel):
    """
    Base class for ND Infra AAA Local Users endpoints.

    Provides common functionality for all HTTP methods on the
    /api/v1/infra/aaa/localUsers endpoint.
    """

    model_config = COMMON_CONFIG

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path.

        ## Returns

        - Complete endpoint path string, optionally including login_id
        """
        if self.login_id is not None:
            return BasePath.nd_infra_aaa("localUsers", self.login_id)
        return BasePath.nd_infra_aaa("localUsers")


class EpApiV1InfraAaaLocalUsersGet(_EpApiV1InfraAaaLocalUsersBase):
    """
    # Summary

    ND Infra AAA Local Users GET Endpoint

    ## Description

    Endpoint to retrieve local users from the ND Infra AAA service.
    Optionally retrieve a specific local user by login_id.

    ## Path

    - /api/v1/infra/aaa/localUsers
    - /api/v1/infra/aaa/localUsers/{login_id}

    ## Verb

    - GET

    ## Usage

    ```python
    # Get all local users
    request = EpApiV1InfraAaaLocalUsersGet()
    path = request.path
    verb = request.verb

    # Get specific local user
    request = EpApiV1InfraAaaLocalUsersGet()
    request.login_id = "admin"
    path = request.path
    verb = request.verb
    ```
    """

    class_name: Literal["EpApiV1InfraAaaLocalUsersGet"] = Field(
        default="EpApiV1InfraAaaLocalUsersGet", description="Class name for backward compatibility"
    )

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpApiV1InfraAaaLocalUsersPost(_EpApiV1InfraAaaLocalUsersBase):
    """
    # Summary

    ND Infra AAA Local Users POST Endpoint

    ## Description

    Endpoint to create a local user in the ND Infra AAA service.

    ## Path

    - /api/v1/infra/aaa/localUsers

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpApiV1InfraAaaLocalUsersPost()
    path = request.path
    verb = request.verb
    ```
    """

    class_name: Literal["EpApiV1InfraAaaLocalUsersPost"] = Field(
        default="EpApiV1InfraAaaLocalUsersPost", description="Class name for backward compatibility"
    )

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpApiV1InfraAaaLocalUsersPut(_EpApiV1InfraAaaLocalUsersBase):
    """
    # Summary

    ND Infra AAA Local Users PUT Endpoint

    ## Description

    Endpoint to update a local user in the ND Infra AAA service.

    ## Path

    - /api/v1/infra/aaa/localUsers/{login_id}

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpApiV1InfraAaaLocalUsersPut()
    request.login_id = "admin"
    path = request.path
    verb = request.verb
    ```
    """

    class_name: Literal["EpApiV1InfraAaaLocalUsersPut"] = Field(
        default="EpApiV1InfraAaaLocalUsersPut", description="Class name for backward compatibility"
    )

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpApiV1InfraAaaLocalUsersDelete(_EpApiV1InfraAaaLocalUsersBase):
    """
    # Summary

    ND Infra AAA Local Users DELETE Endpoint

    ## Description

    Endpoint to delete a local user from the ND Infra AAA service.

    ## Path

    - /api/v1/infra/aaa/localUsers/{login_id}

    ## Verb

    - DELETE

    ## Usage

    ```python
    request = EpApiV1InfraAaaLocalUsersDelete()
    request.login_id = "admin"
    path = request.path
    verb = request.verb
    ```
    """

    class_name: Literal["EpApiV1InfraAaaLocalUsersDelete"] = Field(
        default="EpApiV1InfraAaaLocalUsersDelete", description="Class name for backward compatibility"
    )

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.DELETE

