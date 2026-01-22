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
OneManage Link endpoint models.

This module contains endpoint definitions for link-related operations
in OneManage multi-cluster environments.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Literal
from base_paths import BasePath
from endpoint_mixins import FabricNameMixin, LinkUuidMixin
from endpoint_query_params import LinkByUuidQueryParams
from enums import VerbEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, ConfigDict, Field
else:
    from pydantic_compat import BaseModel, ConfigDict, Field

# Common config for basic validation
COMMON_CONFIG = ConfigDict(validate_assignment=True)


class EpOneManageLinkCreate(BaseModel):
    """
    # Summary

    Link Create Endpoint (OneManage)

    ## Description

    Endpoint to create a link between fabrics in multi-cluster setup.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/links

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageLinkCreate()

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain link creation parameters:
    - sourceClusterName: str - Source cluster name
    - destinationClusterName: str - Destination cluster name
    - sourceFabric: str - Source fabric name
    - destinationFabric: str - Destination fabric name
    - sourceDevice: str - Source switch serial number
    - destinationDevice: str - Destination switch serial number
    - sourceSwitchName: str - Source switch name
    - destinationSwitchName: str - Destination switch name
    - sourceInterface: str - Source switch interface
    - destinationInterface: str - Destination switch interface
    - templateName: str - Link template name
    - nvPairs: dict - Key/value pairs of configuration items

    nvPairs dictionary keys (all string values unless noted):
    - IP_MASK
    - NEIGHBOR_IP
    - IPV6_MASK
    - IPV6_NEIGHBOR
    - MAX_PATHS
    - ROUTING_TAG
    - MTU
    - SPEED
    - DEPLOY_DCI_TRACKING (boolean)
    - BGP_PASSWORD_ENABLE
    - BGP_PASSWORD
    - ENABLE_BGP_LOG_NEIGHBOR_CHANGE
    - ENABLE_BGP_SEND_COMM
    - BGP_PASSWORD_INHERIT_FROM_MSD
    - BGP_AUTH_KEY_TYPE
    - asn
    - NEIGHBOR_ASNL
    - ENABLE_BGP_BFD
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageLinkCreate"] = Field(default="EpOneManageLinkCreate", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """Build the endpoint path."""
        return BasePath.onemanage_links()

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageLinkGetByUuid(LinkUuidMixin, BaseModel):
    """
    # Summary

    Link Get By UUID Endpoint (OneManage)

    ## Description

    Endpoint to retrieve a specific link by its UUID.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/links/{linkUUID}

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageLinkGetByUuid()
    request.link_uuid = "63505f61-ce7b-40a6-a38c-ae9a355b2116"
    request.query_params.source_cluster_name = "nd-cluster-1"
    request.query_params.destination_cluster_name = "nd-cluster-2"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageLinkGetByUuid"] = Field(default="EpOneManageLinkGetByUuid", description="Class name for backward compatibility")
    query_params: LinkByUuidQueryParams = Field(default_factory=LinkByUuidQueryParams)

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path with query parameters.

        ## Raises
        - ValueError: If link_uuid is not set

        ## Returns
        - Complete endpoint path string with query parameters
        """
        if self.link_uuid is None:
            raise ValueError("link_uuid must be set before accessing path")

        base_path = BasePath.onemanage_links(self.link_uuid)

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpOneManageLinkUpdate(LinkUuidMixin, BaseModel):
    """
    # Summary

    Link Update Endpoint (OneManage)

    ## Description

    Endpoint to update a specific link by its UUID.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/links/{linkUUID}

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageLinkUpdate()
    request.link_uuid = "63505f61-ce7b-40a6-a38c-ae9a355b2116"
    request.query_params.source_cluster_name = "nd-cluster-2"
    request.query_params.destination_cluster_name = "nd-cluster-1"

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain link update parameters:
    - sourceClusterName: str - Source cluster name
    - destinationClusterName: str - Destination cluster name
    - sourceFabric: str - Source fabric name
    - destinationFabric: str - Destination fabric name
    - sourceDevice: str - Source switch serial number
    - destinationDevice: str - Destination switch serial number
    - sourceSwitchName: str - Source switch name
    - destinationSwitchName: str - Destination switch name
    - sourceInterface: str - Source switch interface
    - destinationInterface: str - Destination switch interface
    - templateName: str - Link template name
    - nvPairs: dict - Key/value pairs of configuration items

    nvPairs dictionary keys (all string values unless noted):
    - IP_MASK
    - NEIGHBOR_IP
    - IPV6_MASK
    - IPV6_NEIGHBOR
    - MAX_PATHS
    - ROUTING_TAG
    - MTU
    - SPEED
    - DEPLOY_DCI_TRACKING (boolean)
    - BGP_PASSWORD_ENABLE
    - BGP_PASSWORD
    - ENABLE_BGP_LOG_NEIGHBOR_CHANGE
    - ENABLE_BGP_SEND_COMM
    - BGP_PASSWORD_INHERIT_FROM_MSD
    - BGP_AUTH_KEY_TYPE
    - asn
    - NEIGHBOR_ASNL
    - ENABLE_BGP_BFD
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageLinkUpdate"] = Field(default="EpOneManageLinkUpdate", description="Class name for backward compatibility")
    query_params: LinkByUuidQueryParams = Field(default_factory=LinkByUuidQueryParams)

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path with query parameters.

        ## Raises
        - ValueError: If link_uuid is not set

        ## Returns

        - Complete endpoint path string with query parameters
        """
        if self.link_uuid is None:
            raise ValueError("link_uuid must be set before accessing path")

        base_path = BasePath.onemanage_links(self.link_uuid)

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageLinksDelete(BaseModel):
    """
    # Summary

    Links Delete Endpoint (OneManage)

    ## Description

    Endpoint to delete links in multi-cluster setup.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/links

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageLinksDelete()

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain link deletion parameters.

    - linkUUID: str - Link UUID (e.g., "63505f61-ce7b-40a6-a38c-ae9a355b2116")
    - destinationClusterName: str - Destination cluster name (e.g., "nd-cluster-1")
    - sourceClusterName: str - Source cluster name (e.g., "nd-cluster-2")
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageLinksDelete"] = Field(default="EpOneManageLinksDelete", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """Build the endpoint path."""
        return BasePath.onemanage_links()

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageLinksGetByFabric(FabricNameMixin, BaseModel):
    """
    # Summary

    Links Get By Fabric Endpoint (OneManage)

    ## Description

    Endpoint to retrieve links for a specific multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/links/fabrics/{fabricName}

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageLinksGetByFabric()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageLinksGetByFabric"] = Field(default="EpOneManageLinksGetByFabric", description="Class name for backward compatibility")

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

        return BasePath.onemanage_links_fabrics(self.fabric_name)

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET
