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
OneManage Network endpoint models.

This module contains endpoint definitions for network-related operations
in OneManage multi-cluster environments.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Literal
from base_paths import BasePath
from endpoint_mixins import FabricNameMixin, NetworkNameMixin
from endpoint_query_params import NetworkNamesQueryParams
from enums import VerbEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, ConfigDict, Field
else:
    from pydantic_compat import BaseModel, ConfigDict, Field

# Common config for basic validation
COMMON_CONFIG = ConfigDict(validate_assignment=True)


class EpOneManageNetworkCreate(FabricNameMixin, BaseModel):
    """
    # Summary

    Network Create Endpoint (OneManage)

    ## Description

    Endpoint to create a network in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabricName}/networks

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageNetworkCreate()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```

    ### Request Body

    The request body should contain network creation parameters:
    - id: int - Link ID
    - vrfId: int - VRF ID
    - networkId: int - Network ID
    - vrf: str - Name of the VRF
    - fabric: str - Name of the Fabric
    - networkTemplate: str - Network template name
    - networkTemplateConfig: str - Network extension template config
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageNetworkCreate"] = Field(default="EpOneManageNetworkCreate", description="Class name for backward compatibility")

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

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "networks")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageNetworkUpdate(FabricNameMixin, NetworkNameMixin, BaseModel):
    """
    # Summary

    Network Update Endpoint (OneManage)

    ## Description

    Endpoint to update single Network in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabric_name}/networks/{network_name}

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageNetworkUpdate()
    request.fabric_name = "MyFabric"
    request.network_name = "MyNetwork1"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageNetworkUpdate"] = Field(default="EpOneManageNetworkUpdate", description="Class name for backward compatibility")

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
        if self.network_name is None:
            raise ValueError("network_name must be set before accessing path")

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "networks", self.network_name)

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageNetworksDelete(FabricNameMixin, BaseModel):
    """
    # Summary

    Networks Delete Endpoint (OneManage)

    ## Description

    Endpoint to bulk-delete networks from a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabric_name}/bulk-delete/networks

    ## Verb

    - DELETE

    ## Usage

    ```python
    request = EpOneManageNetworksDelete()
    request.fabric_name = "MyFabric"
    request.query_params.network_names = "MyNetwork1,MyNetwork2,MyNetwork3"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageNetworksDelete"] = Field(default="EpOneManageNetworksDelete", description="Class name for backward compatibility")
    query_params: NetworkNamesQueryParams = Field(default_factory=NetworkNamesQueryParams)

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

        base_path = BasePath.onemanage_top_down_fabrics(self.fabric_name, "bulk-delete", "networks")

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.DELETE


class EpOneManageNetworksGet(FabricNameMixin, BaseModel):
    """
    # Summary

    Networks Get Endpoint (OneManage)

    ## Description

    Endpoint to retrieve all networks from a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/top-down/fabrics/{fabricName}/networks

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageNetworksGet()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageNetworksGet"] = Field(default="EpOneManageNetworksGet", description="Class name for backward compatibility")

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

        return BasePath.onemanage_top_down_fabrics(self.fabric_name, "networks")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET
