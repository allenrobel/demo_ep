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
Reusable mixin classes for endpoint models.

This module provides mixin classes that can be composed to add common
fields to endpoint models without duplication.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__author__ = "Allen Robel"

from typing import TYPE_CHECKING, Optional
from enums import BooleanStringEnum

if TYPE_CHECKING:
    from pydantic import BaseModel, Field
else:
    from pydantic_compat import BaseModel, Field


class ForceShowRunMixin(BaseModel):
    """Mixin for endpoints that require force_show_run parameter."""

    force_show_run: BooleanStringEnum = Field(default=BooleanStringEnum.FALSE, description="Force show running config")


class InclAllMsdSwitchesMixin(BaseModel):
    """Mixin for endpoints that require incl_all_msd_switches parameter."""

    incl_all_msd_switches: BooleanStringEnum = Field(default=BooleanStringEnum.FALSE, description="Include all MSD switches")


class FabricNameMixin(BaseModel):
    """Mixin for endpoints that require fabric_name parameter."""

    fabric_name: Optional[str] = Field(default=None, min_length=1, max_length=64, description="Fabric name")


class SwitchSerialNumberMixin(BaseModel):
    """Mixin for endpoints that require switch_sn parameter."""

    switch_sn: Optional[str] = Field(default=None, min_length=1, description="Switch serial number")


class NetworkNameMixin(BaseModel):
    """Mixin for endpoints that require network_name parameter."""

    network_name: Optional[str] = Field(default=None, min_length=1, max_length=64, description="Network name")


class VrfNameMixin(BaseModel):
    """Mixin for endpoints that require vrf_name parameter."""

    vrf_name: Optional[str] = Field(default=None, min_length=1, max_length=64, description="VRF name")


class LinkUuidMixin(BaseModel):
    """Mixin for endpoints that require link_uuid parameter."""

    link_uuid: Optional[str] = Field(default=None, min_length=1, description="Link UUID")


class LoginIdMixin(BaseModel):
    """Mixin for endpoints that require login_id parameter."""

    login_id: Optional[str] = Field(default=None, min_length=1, description="Login ID")
