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
Endpoint-specific query parameter classes.

This module provides query parameter classes tailored for specific API
endpoints, handling their unique parameter requirements.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Optional

from query_params import EndpointQueryParams
from endpoint_mixins import ForceShowRunMixin, InclAllMsdSwitchesMixin
from enums import BooleanStringEnum

if TYPE_CHECKING:
    from pydantic import ConfigDict, Field
else:
    from pydantic_compat import ConfigDict, Field

# Config for classes that use enums and need automatic value extraction
ENUM_CONFIG = ConfigDict(validate_assignment=True, use_enum_values=True)


class FabricConfigDeployQueryParams(EndpointQueryParams, ForceShowRunMixin, InclAllMsdSwitchesMixin):
    """
    # Summary

    Query parameters for fabric config deploy endpoints.

    ## Parameters

    - force_show_run: If true, fetch latest running config from device; if false, use cached version (default: "false")
    - incl_all_msd_switches: If true and MSD fabric, deploy all child fabric changes; if false, skip child fabrics (default: "false")

    ## Raises

    None
    """

    model_config = ENUM_CONFIG

    def to_query_string(self) -> str:
        """Build query string with forceShowRun and inclAllMSDSwitches parameters."""
        params = []
        # Always include these params - they have default values
        # Use .value to get the string value from the enum
        params.append(f"forceShowRun={self.force_show_run.value if hasattr(self.force_show_run, 'value') else self.force_show_run}")
        params.append(f"inclAllMSDSwitches={self.incl_all_msd_switches.value if hasattr(self.incl_all_msd_switches, 'value') else self.incl_all_msd_switches}")
        return "&".join(params)


class FabricConfigPreviewQueryParams(EndpointQueryParams, ForceShowRunMixin):
    """
    # Summary

    Query parameters for fabric config preview endpoints.

    ## Parameters

    - force_show_run: Force show running config (default: "false")
    - show_brief: Show brief output (default: "false")
    """

    show_brief: BooleanStringEnum = Field(default=BooleanStringEnum.FALSE, description="Show brief output")

    def to_query_string(self) -> str:
        """Build query string with forceShowRun and showBrief parameters."""
        params = []
        if self.force_show_run:
            params.append(f"forceShowRun={self.force_show_run.value if hasattr(self.force_show_run, 'value') else self.force_show_run}")
        if self.show_brief:
            params.append(f"showBrief={self.show_brief.value if hasattr(self.show_brief, 'value') else self.show_brief}")
        return "&".join(params)


class LinkByUuidQueryParams(EndpointQueryParams):
    """
    # Summary

    Query parameters for link by UUID endpoints.

    ## Parameters

    - source_cluster_name: Source cluster name (e.g., "nd-cluster-1")
    - destination_cluster_name: Destination cluster name (e.g., "nd-cluster-2")
    """

    source_cluster_name: Optional[str] = Field(default=None, min_length=1, description="Source cluster name")
    destination_cluster_name: Optional[str] = Field(default=None, min_length=1, description="Destination cluster name")

    def to_query_string(self) -> str:
        """Build query string with sourceClusterName and destinationClusterName parameters."""
        params = []
        if self.source_cluster_name:
            params.append(f"sourceClusterName={self.source_cluster_name}")
        if self.destination_cluster_name:
            params.append(f"destinationClusterName={self.destination_cluster_name}")
        return "&".join(params)


class NetworkNamesQueryParams(EndpointQueryParams):
    """
    # Summary

    Query parameters for network deletion endpoints.

    ## Parameters

    - network_names: Comma-separated list of network names to delete e.g. "Net1,Net2,Net3"
    """

    network_names: Optional[str] = Field(default=None, min_length=1, description="Comma-separated network names")

    def to_query_string(self) -> str:
        """Build query string with network-names parameter."""
        params = []
        if self.network_names:
            params.append(f"network-names={self.network_names}")
        return "&".join(params)


class VrfNamesQueryParams(EndpointQueryParams):
    """
    # Summary

    Query parameters for VRF deletion endpoints.

    ## Parameters

    - vrf_names: Comma-separated list of VRF names to delete e.g. "VRF1,VRF2,VRF3"
    """

    vrf_names: Optional[str] = Field(default=None, min_length=1, description="Comma-separated VRF names")

    def to_query_string(self) -> str:
        """Build query string with vrf-names parameter."""
        params = []
        if self.vrf_names:
            params.append(f"vrf-names={self.vrf_names}")
        return "&".join(params)
