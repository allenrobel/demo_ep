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
OneManage VRF endpoint models.

This module contains endpoint definitions for VRF-related operations
in OneManage multi-cluster environments.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Literal
from base_paths import BasePath
from endpoint_mixins import FabricNameMixin, VrfNameMixin
from endpoint_query_params import VrfNamesQueryParams
from enums import VerbEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, ConfigDict, Field
else:
    from pydantic_compat import BaseModel, ConfigDict, Field

# Common config for basic validation
COMMON_CONFIG = ConfigDict(validate_assignment=True)


class EpOneManageVrfCreate(FabricNameMixin, BaseModel):
    """
    # Summary

    VRF Create Endpoint (OneManage)

    ## Description

    Endpoint to create a VRF in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabricName}/vrfs

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageVrfCreate()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain VRF creation parameters:
    - id: int - Link ID
    - vrfId: int - VRF ID
    - vrfName: str - Name of the VRF
    - fabric: str - Name of the fabric
    - vrfTemplate: str - VRF template name
    - vrfExtensionTemplate: str - VRF extension template name
    - vrfTemplateConfig: str - JSON string representing the VRF configuration
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageVrfCreate"] = Field(default="EpOneManageVrfCreate", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path.

        ## Raises

        - ValueError: If fabric_name is not set

        ## Returns

        - Complete endpoint path string
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "vrfs")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageVrfUpdate(FabricNameMixin, VrfNameMixin, BaseModel):
    """
    # Summary

    VRF Update Endpoint (OneManage)

    ## Description

    Endpoint to update single VRF in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabric_name}/vrfs/{vrf_name}

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageVrfUpdate()
    request.fabric_name = "MyFabric"
    request.vrf_name = "MyVRF1"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageVrfUpdate"] = Field(default="EpOneManageVrfUpdate", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path.

        ## Raises

        - ValueError: If fabric_name or vrf_name is not set

        ## Returns

        - Complete endpoint path string
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")
        if self.vrf_name is None:
            raise ValueError("vrf_name must be set before accessing path")

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "vrfs", self.vrf_name)

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageVrfsDelete(FabricNameMixin, BaseModel):
    """
    # Summary

    VRFs Delete Endpoint (OneManage)

    ## Description

    Endpoint to bulk-delete VRFs from a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabric_name}/bulk-delete/vrfs

    ## Verb

    - DELETE

    ## Usage

    ```python
    request = EpOneManageVrfsDelete()
    request.fabric_name = "MyFabric"
    request.query_params.vrf_names = "MyVRF1,MyVRF2,MyVRF3"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageVrfsDelete"] = Field(default="EpOneManageVrfsDelete", description="Class name for backward compatibility")
    query_params: VrfNamesQueryParams = Field(default_factory=VrfNamesQueryParams)

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path with query parameters.

        ## Raises

        - ValueError: If fabric_name is not set

        ## Returns

        - Complete endpoint path string with query parameters
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")

        base_path = BasePath.onemanage_top_down_fabrics(self.fabric_name, "bulk-delete", "vrfs")

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.DELETE


class EpOneManageVrfsGet(FabricNameMixin, BaseModel):
    """
    # Summary

    VRFs Get Endpoint (OneManage)

    ## Description

    Endpoint to retrieve all VRFs from a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabricName}/vrfs

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageVrfsGet()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageVrfsGet"] = Field(default="EpOneManageVrfsGet", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path.

        ## Raises

        - ValueError: If fabric_name is not set

        ## Returns

        - Complete endpoint path string
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "vrfs")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET
