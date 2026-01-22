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
OneManage Fabric endpoint models.

This module contains endpoint definitions for fabric-related operations
in OneManage multi-cluster environments.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Literal
from base_paths import BasePath
from endpoint_mixins import FabricNameMixin, SwitchSerialNumberMixin
from endpoint_query_params import FabricConfigDeployQueryParams, FabricConfigPreviewQueryParams
from enums import VerbEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, ConfigDict, Field
else:
    from pydantic_compat import BaseModel, ConfigDict, Field

# Common config for basic validation
COMMON_CONFIG = ConfigDict(validate_assignment=True)

# Config for classes that use enums and need automatic value extraction
ENUM_CONFIG = ConfigDict(validate_assignment=True, use_enum_values=True)


class EpOneManageFabricConfigDeploy(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Config-Deploy Endpoint (OneManage)

    ## Description

    Endpoint to deploy the configuration for a specific multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/config-deploy

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageFabricConfigDeploy()
    request.fabric_name = "MyFabric"
    request.query_params.force_show_run = "true"
    request.query_params.incl_all_msd_switches = "false"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricConfigDeploy"] = Field(default="EpOneManageFabricConfigDeploy", description="Class name for backward compatibility")
    query_params: FabricConfigDeployQueryParams = Field(default_factory=FabricConfigDeployQueryParams)

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

        base_path = BasePath.onemanage_fabrics(self.fabric_name, "config-deploy")

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageFabricConfigDeploySwitch(FabricNameMixin, SwitchSerialNumberMixin, BaseModel):
    """
    # Summary

    Fabric Config-Deploy Switch Endpoint (OneManage)

    ## Description

    Endpoint to deploy the configuration for a specific switch in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/config-deploy/{switchSN}

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageFabricConfigDeploySwitch()
    request.fabric_name = "MyFabric"
    request.switch_sn = "92RZ2OMQCNC"
    request.query_params.force_show_run = "true"
    request.query_params.incl_all_msd_switches = "false"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = ENUM_CONFIG

    class_name: Literal["EpOneManageFabricConfigDeploySwitch"] = Field(
        default="EpOneManageFabricConfigDeploySwitch", description="Class name for backward compatibility"
    )
    query_params: FabricConfigDeployQueryParams = Field(default_factory=FabricConfigDeployQueryParams)

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path with query parameters.

        ## Raises

        - ValueError: If fabric_name or switch_sn is not set

        ## Returns

        - Complete endpoint path string with query parameters
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")
        if self.switch_sn is None:
            raise ValueError("switch_sn must be set before accessing path")

        base_path = BasePath.onemanage_fabrics(self.fabric_name, "config-deploy", self.switch_sn)

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageFabricConfigPreview(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Config-Preview Endpoint (OneManage)

    ## Description

    Endpoint to preview the configuration for a specific multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/config-preview

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageFabricConfigPreview()
    request.fabric_name = "MyFabric"
    request.query_params.force_show_run = "true"
    request.query_params.show_brief = "false"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricConfigPreview"] = Field(
        default="EpOneManageFabricConfigPreview", description="Class name for backward compatibility"
    )
    query_params: FabricConfigPreviewQueryParams = Field(default_factory=FabricConfigPreviewQueryParams)

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

        base_path = BasePath.onemanage_fabrics(self.fabric_name, "config-preview")

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpOneManageFabricConfigPreviewSwitch(FabricNameMixin, SwitchSerialNumberMixin, BaseModel):
    """
    # Summary

    Fabric Config-Preview Switch Endpoint (OneManage)

    ## Description

    Endpoint to preview the configuration for a specific switch in a multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/config-preview/{switchSN}

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageFabricConfigPreviewSwitch()
    request.fabric_name = "MyFabric"
    request.switch_sn = "92RZ2OMQCNC"
    request.query_params.force_show_run = "true"
    request.query_params.show_brief = "false"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricConfigPreviewSwitch"] = Field(
        default="EpOneManageFabricConfigPreviewSwitch", description="Class name for backward compatibility"
    )
    query_params: FabricConfigPreviewQueryParams = Field(default_factory=FabricConfigPreviewQueryParams)

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path with query parameters.

        ## Raises

        - ValueError: If fabric_name or switch_sn is not set

        ## Returns

        - Complete endpoint path string with query parameters
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")
        if self.switch_sn is None:
            raise ValueError("switch_sn must be set before accessing path")

        base_path = BasePath.onemanage_fabrics(self.fabric_name, "config-preview", self.switch_sn)

        query_string = self.query_params.to_query_string()
        if query_string:
            return f"{base_path}?{query_string}"
        return base_path

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpOneManageFabricConfigSave(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Config-Save Endpoint (OneManage)

    ## Description

    Endpoint to save the configuration for a specific multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/config-save

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageFabricConfigSave()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricConfigSave"] = Field(default="EpOneManageFabricConfigSave", description="Class name for backward compatibility")

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

        return BasePath.onemanage_fabrics(self.fabric_name, "config-save")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageFabricCreate(BaseModel):
    """
    # Summary

    Fabric Create Endpoint (OneManage)

    ## Description

    Endpoint to create a new multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics

    ## Verb

    - POST

    ## Usage

    ```python
    request = EpOneManageFabricCreate()

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricCreate"] = Field(default="EpOneManageFabricCreate", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """Build the endpoint path."""
        return "/appcenter/cisco/ndfc/api/v1/onemanage/fabrics"

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.POST


class EpOneManageFabricDelete(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Delete Endpoint (OneManage)

    ## Description

    Endpoint to delete a specific multi-cluster fabric.

    ## Path (nd322m apidocs)

    -  /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}

    ## Verb

    - DELETE

    ## Usage

    ```python
    request = EpOneManageFabricDelete()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```

    ### Note
    The delete endpoint uses the regular LAN fabric control API with /onemanage prefix,
    not the onemanage-specific API endpoint. This is required for multi-cluster fabrics.
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricDelete"] = Field(default="EpOneManageFabricDelete", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """
        # Summary

        Build the endpoint path.

        ## Raises

        - ValueError: If fabric_name is not set

        ## Returns

        - Complete endpoint path string with /onemanage prefix
        """
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")

        return f"/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{self.fabric_name}"

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.DELETE


class EpOneManageFabricDetails(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Details Endpoint as documented in nd322m apidocs (OneManage)

    ## Description

    Endpoint to query details for a specific multi-cluster fabric.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/MyFabric

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageFabricDetails()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricDetails"] = Field(default="EpOneManageFabricDetails", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """Build the endpoint path."""
        if self.fabric_name is None:
            raise ValueError("fabric_name must be set before accessing path")

        return f"/appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{self.fabric_name}"

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpOneManageFabricGroupMembersGet(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Group Members Get Endpoint (OneManage)

    ## Description

    Endpoint to retrieve members of a specific multi-cluster fabric group.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/members

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageFabricGroupMembersGet()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricGroupMembersGet"] = Field(
        default="EpOneManageFabricGroupMembersGet", description="Class name for backward compatibility"
    )

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

        return BasePath.onemanage_fabrics(self.fabric_name, "members")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET


class EpOneManageFabricGroupMembersUpdate(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Group Members Update Endpoint (OneManage)

    ## Description

    Endpoint to add or remove members to/from a multi-cluster fabric group.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}/members

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageFabricGroupMembersUpdate()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain fabric group update parameters:
    - clusterName: str - Name of the cluster
    - fabricName: str - Name of the fabric
    - operation: str - Operation type ("add" or "remove")
      - "add": Add fabricName to clusterName
      - "remove": Remove fabricName from clusterName
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricGroupMembersUpdate"] = Field(
        default="EpOneManageFabricGroupMembersUpdate", description="Class name for backward compatibility"
    )

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

        return BasePath.onemanage_fabrics(self.fabric_name, "members")

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageFabricGroupUpdate(FabricNameMixin, BaseModel):
    """
    # Summary

    Fabric Group Update Endpoint (OneManage)

    ## Description

    Endpoint to update a specific multi-cluster fabric group.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics/{fabricName}

    ## Verb

    - PUT

    ## Usage

    ```python
    request = EpOneManageFabricGroupUpdate()
    request.fabric_name = "MyFabric"

    path = request.path
    verb = request.verb
    ```

    ## Request Body

    The request body should contain fabric update parameters:
    - fabricName: str - Name of the Fabric
    - fabricType: str - Type of the fabric
    - fabricTechnology: str - Fabric technology
    - nvPairs: dict - Key value pairs describing the fabric configuration

    nvPairs dictionary keys (all string values unless noted):
    - ANYCAST_GW_MAC
    - BGP_RP_ASN
    - BGW_ROUTING_TAG
    - BGW_ROUTING_TAG_PREV
    - BORDER_GWY_CONNECTIONS
    - DCI_SUBNET_RANGE
    - DCI_SUBNET_TARGET_MASK
    - DELAY_RESTORE
    - ENABLE_BGP_BFD
    - ENABLE_BGP_LOG_NEIGHBOR_CHANGE (boolean)
    - ENABLE_BGP_SEND_COMM (boolean)
    - ENABLE_PVLAN
    - ENABLE_PVLAN_PREV
    - ENABLE_RS_REDIST_DIRECT (boolean)
    - ENABLE_TRM_TRMv6
    - ENABLE_TRM_TRMv6_PREV
    - EXT_FABRIC_TYPE
    - FABRIC_NAME
    - FABRIC_TYPE
    - FF
    - L2_SEGMENT_ID_RANGE
    - L3_PARTITION_ID_RANGE
    - LOOPBACK100_IPV6_RANGE
    - LOOPBACK100_IP_RANGE
    - MSO_CONTROLER_ID
    - MSO_SITE_GROUP_NAME
    - MS_IFC_BGP_AUTH_KEY_TYPE
    - MS_IFC_BGP_AUTH_KEY_TYPE_PREV
    - MS_IFC_BGP_PASSWORD
    - MS_IFC_BGP_PASSWORD_ENABLE
    - MS_IFC_BGP_PASSWORD_ENABLE_PREV
    - MS_IFC_BGP_PASSWORD_PREV
    - MS_LOOPBACK_ID
    - MS_UNDERLAY_AUTOCONFIG (boolean)
    - PARENT_ONEMANAGE_FABRIC
    - PREMSO_PARENT_FABRIC
    - RP_SERVER_IP
    - RS_ROUTING_TAG
    - TOR_AUTO_DEPLOY
    - V6_DCI_SUBNET_RANGE
    - V6_DCI_SUBNET_TARGET_MASK
    - VXLAN_UNDERLAY_IS_V6
    - default_network
    - default_pvlan_sec_network
    - default_vrf
    - network_extension_template
    - vrf_extension_template
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricGroupUpdate"] = Field(default="EpOneManageFabricGroupUpdate", description="Class name for backward compatibility")

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

        return BasePath.onemanage_fabrics(self.fabric_name)

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.PUT


class EpOneManageFabricsGet(BaseModel):
    """
    # Summary

    Fabrics Get Endpoint (OneManage)

    ## Description

    Endpoint to retrieve all multi-cluster fabrics.

    ## Path

    - /appcenter/cisco/ndfc/api/v1/onemanage/fabrics

    ## Verb

    - GET

    ## Usage

    ```python
    request = EpOneManageFabricsGet()

    path = request.path
    verb = request.verb
    ```
    """

    model_config = COMMON_CONFIG

    class_name: Literal["EpOneManageFabricsGet"] = Field(default="EpOneManageFabricsGet", description="Class name for backward compatibility")

    @property
    def path(self) -> str:
        """Build the endpoint path."""
        return BasePath.onemanage_fabrics()

    @property
    def verb(self) -> VerbEnum:
        """Return the HTTP verb for this endpoint."""
        return VerbEnum.GET
