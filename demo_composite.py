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
Demonstration of CompositeQueryParams usage.

This example shows how to build complex queries that combine:
- Endpoint-specific query parameters (e.g., force_show_run, ticket_id)
- Lucene-style filtering (e.g., filter, max, sort)
- Multiple parameter types in a single request
"""

from urllib.parse import urlencode, quote

from base_paths import BasePath
from endpoints import BooleanStringEnum, EpOneManageFabricConfigDeploySwitch
from query_params import CompositeQueryParams, LuceneQueryParams


def example_1_basic_composite() -> None:
    """
    Example 1: Basic Composite - Endpoint params + Lucene filtering

    This demonstrates the most common use case: combining endpoint-specific
    parameters with Lucene-style filtering to search for specific switches
    while configuring how the endpoint behaves.
    """
    print("=" * 80)
    print("Example 1: Basic Composite Query with URL Encoding")
    print("=" * 80)

    # Create the endpoint
    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    # Set endpoint-specific query parameters
    ep.query_params.force_show_run = BooleanStringEnum.TRUE
    ep.query_params.incl_all_msd_switches = BooleanStringEnum.FALSE

    # Create Lucene filtering parameters to find specific switches
    lucene_params = LuceneQueryParams(
        filter="name:Spine* AND role:spine",
        max=50,
        sort="name:asc"
    )

    # Compose them together
    composite = CompositeQueryParams()
    composite.add(ep.query_params)  # Add endpoint-specific params
    composite.add(lucene_params)     # Add Lucene filtering

    # Build the complete URL - use BasePath to get path without query params
    base_path = BasePath.onemanage_fabrics(ep.fabric_name, "config-deploy", ep.switch_sn)
    query_string = composite.to_query_string(url_encode=True)
    full_url = f"{base_path}?{query_string}" if query_string else base_path

    print(f"\nEndpoint: {ep.__class__.__name__}")
    print(f"Base Path: {base_path}")
    print(f"\nEndpoint Parameters:")
    print(f"  - force_show_run: {ep.query_params.force_show_run}")
    print(f"  - incl_all_msd_switches: {ep.query_params.incl_all_msd_switches}")
    print(f"\nLucene Filters:")
    print(f"  - filter: {lucene_params.filter}")
    print(f"  - max: {lucene_params.max}")
    print(f"  - sort: {lucene_params.sort}")
    print(f"\nComposite Query String (URL-encoded):")
    print(f"  {query_string}")
    print(f"\nComposite Query String (not encoded):")
    print(f"  {composite.to_query_string(url_encode=False)}")
    print(f"\nFull URL:")
    print(f"  {full_url}")
    print()


def example_2_lucene_only() -> None:
    """
    Example 2: Lucene-Only Filtering

    Sometimes you only need Lucene filtering without endpoint-specific params.
    This is useful for list/search endpoints that don't have custom parameters.
    """
    print("=" * 80)
    print("Example 2: Lucene-Only Query (no endpoint params)")
    print("=" * 80)

    fabric_name = "MyFabric"
    switch_sn = "FOC12345678"

    # Only use Lucene filtering - no endpoint-specific params
    lucene_params = LuceneQueryParams(
        filter="ipAddress:10.1.* OR ipAddress:10.2.*",
        max=100,
        offset=0,
        sort="ipAddress:asc",
        fields="serialNumber,ipAddress,hostname,role"
    )

    composite = CompositeQueryParams()
    composite.add(lucene_params)

    base_path = BasePath.onemanage_fabrics(fabric_name, "config-deploy", switch_sn)
    query_string = composite.to_query_string()
    full_url = f"{base_path}?{query_string}" if query_string else base_path

    print(f"\nBase Path: {base_path}")
    print(f"\nLucene Filters:")
    print(f"  - filter: {lucene_params.filter}")
    print(f"  - max: {lucene_params.max}")
    print(f"  - offset: {lucene_params.offset}")
    print(f"  - sort: {lucene_params.sort}")
    print(f"  - fields: {lucene_params.fields}")
    print(f"\nComposite Query String (URL-encoded):")
    print(f"  {query_string}")
    print(f"\nFull URL:")
    print(f"  {full_url}")
    print()


def example_3_complex_lucene_filters() -> None:
    """
    Example 3: Complex Lucene Filter Expressions

    Demonstrates advanced Lucene filter syntax including:
    - AND/OR/NOT operators
    - Wildcards
    - Range queries
    - Nested conditions
    """
    print("=" * 80)
    print("Example 3: Complex Lucene Filter Expressions")
    print("=" * 80)

    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "ProductionFabric"
    ep.switch_sn = "FOC99999999"

    # Example 3a: AND with wildcards
    print("\n--- 3a: Find all spine switches in MyFabric ---")
    lucene_3a = LuceneQueryParams(
        filter="fabricName:MyFabric AND role:spine AND name:Spine-*",
        max=20,
        sort="name:asc"
    )
    composite_3a = CompositeQueryParams().add(ep.query_params).add(lucene_3a)
    print(f"Filter: {lucene_3a.filter}")
    print(f"Query: {composite_3a.to_query_string()}\n")

    # Example 3b: OR conditions
    print("--- 3b: Find switches that are either spine or leaf ---")
    lucene_3b = LuceneQueryParams(
        filter="role:spine OR role:leaf",
        max=50
    )
    composite_3b = CompositeQueryParams().add(ep.query_params).add(lucene_3b)
    print(f"Filter: {lucene_3b.filter}")
    print(f"Query: {composite_3b.to_query_string()}\n")

    # Example 3c: NOT conditions
    print("--- 3c: Find all switches except those in maintenance mode ---")
    lucene_3c = LuceneQueryParams(
        filter="NOT mode:maintenance AND status:active",
        max=100
    )
    composite_3c = CompositeQueryParams().add(ep.query_params).add(lucene_3c)
    print(f"Filter: {lucene_3c.filter}")
    print(f"Query: {composite_3c.to_query_string()}\n")

    # Example 3d: Range query (for date/time or numeric values)
    print("--- 3d: Find switches deployed in 2024 ---")
    lucene_3d = LuceneQueryParams(
        filter="deployedDate:[2024-01-01 TO 2024-12-31]",
        sort="deployedDate:desc"
    )
    composite_3d = CompositeQueryParams().add(ep.query_params).add(lucene_3d)
    print(f"Filter: {lucene_3d.filter}")
    print(f"Query: {composite_3d.to_query_string()}\n")

    # Example 3e: Complex nested conditions
    print("--- 3e: Complex nested query ---")
    lucene_3e = LuceneQueryParams(
        filter="(role:spine OR role:leaf) AND status:active AND NOT ipAddress:192.168.*",
        max=75,
        sort="role:asc,name:asc",
        fields="serialNumber,hostname,role,ipAddress,status"
    )
    composite_3e = CompositeQueryParams().add(ep.query_params).add(lucene_3e)
    print(f"Filter: {lucene_3e.filter}")
    print(f"Query: {composite_3e.to_query_string()}\n")


def example_4_pagination() -> None:
    """
    Example 4: Pagination with Lucene

    Shows how to use max/offset for paginating through large result sets.
    """
    print("=" * 80)
    print("Example 4: Pagination Pattern")
    print("=" * 80)

    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"
    ep.query_params.force_show_run = BooleanStringEnum.TRUE

    base_path = BasePath.onemanage_fabrics(ep.fabric_name, "config-deploy", ep.switch_sn)

    # Pagination settings
    page_size = 25
    total_pages = 3

    print(f"\nFetching {total_pages} pages with {page_size} items each:\n")

    for page in range(total_pages):
        offset = page * page_size

        lucene_params = LuceneQueryParams(
            filter="status:active",
            max=page_size,
            offset=offset,
            sort="name:asc"
        )

        composite = CompositeQueryParams()
        composite.add(ep.query_params)
        composite.add(lucene_params)

        query_string = composite.to_query_string()
        full_url = f"{base_path}?{query_string}"

        print(f"Page {page + 1}:")
        print(f"  Offset: {offset}, Max: {page_size}")
        print(f"  URL: {full_url}")
    print()


def example_5_dynamic_composition() -> None:
    """
    Example 5: Dynamic Composition Based on Conditions

    Shows how to conditionally add different parameter groups based on
    runtime conditions or user input.
    """
    print("=" * 80)
    print("Example 5: Dynamic Composition")
    print("=" * 80)

    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    base_path = BasePath.onemanage_fabrics(ep.fabric_name, "config-deploy", ep.switch_sn)

    # Scenario: User can optionally enable filtering
    enable_filtering = True
    filter_by_role = "spine"
    show_only_active = True
    limit_results = True

    # Always add endpoint params
    composite = CompositeQueryParams()
    composite.add(ep.query_params)

    # Conditionally add Lucene filtering
    if enable_filtering:
        filter_parts = []

        if filter_by_role:
            filter_parts.append(f"role:{filter_by_role}")

        if show_only_active:
            filter_parts.append("status:active")

        lucene_filter = " AND ".join(filter_parts) if filter_parts else None

        lucene_params = LuceneQueryParams(
            filter=lucene_filter,
            max=50 if limit_results else None,
            sort="name:asc"
        )
        composite.add(lucene_params)

    query_string = composite.to_query_string()
    full_url = f"{base_path}?{query_string}" if query_string else base_path

    print(f"\nConfiguration:")
    print(f"  - Enable Filtering: {enable_filtering}")
    print(f"  - Filter by Role: {filter_by_role}")
    print(f"  - Show Only Active: {show_only_active}")
    print(f"  - Limit Results: {limit_results}")
    print(f"\nGenerated URL:")
    print(f"  {full_url}")
    print()


def example_6_method_chaining():
    """
    Example 6: Method Chaining

    CompositeQueryParams.add() returns self, enabling fluent interface pattern.
    """
    print("=" * 80)
    print("Example 6: Method Chaining (Fluent Interface)")
    print("=" * 80)

    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"
    ep.query_params.force_show_run = BooleanStringEnum.TRUE

    lucene_params = LuceneQueryParams(
        filter="role:spine",
        max=25,
        sort="name:asc"
    )

    # Chain multiple add() calls
    query_string = (
        CompositeQueryParams()
        .add(ep.query_params)
        .add(lucene_params)
        .to_query_string()
    )

    print(f"\nUsing method chaining:")
    print(f"  query = CompositeQueryParams()")
    print(f"          .add(endpoint_params)")
    print(f"          .add(lucene_params)")
    print(f"          .to_query_string()")
    print(f"\nResult:")
    print(f"  {query_string}")
    print()


def example_7_empty_handling() -> None:
    """
    Example 7: Handling Empty Parameters

    Shows how CompositeQueryParams handles cases where no parameters are set,
    or only some parameter groups are populated.
    """
    print("=" * 80)
    print("Example 7: Empty Parameter Handling")
    print("=" * 80)

    ep = EpOneManageFabricConfigDeploySwitch()
    ep.fabric_name = "MyFabric"
    ep.switch_sn = "FOC12345678"

    base_path = BasePath.onemanage_fabrics(ep.fabric_name, "config-deploy", ep.switch_sn)

    # Case 1: No Lucene params set (all None)
    print("\n--- Case 1: Endpoint params only (no Lucene filters) ---")
    ep.query_params.force_show_run = BooleanStringEnum.TRUE
    empty_lucene = LuceneQueryParams()  # All fields are None

    composite_1 = CompositeQueryParams()
    composite_1.add(ep.query_params)
    composite_1.add(empty_lucene)

    print(f"Endpoint params empty: {ep.query_params.is_empty()}")
    print(f"Lucene params empty: {empty_lucene.is_empty()}")
    print(f"Composite empty: {composite_1.is_empty()}")
    print(f"Query string: {composite_1.to_query_string()}")

    # Case 2: Only Lucene params set
    print("\n--- Case 2: Lucene filters only (no endpoint params) ---")
    ep2 = EpOneManageFabricConfigDeploySwitch()
    ep2.fabric_name = "MyFabric"
    ep2.switch_sn = "FOC12345678"

    lucene_only = LuceneQueryParams(filter="role:spine", max=10)

    composite_2 = CompositeQueryParams()
    composite_2.add(ep2.query_params)  # Default values
    composite_2.add(lucene_only)

    print(f"Endpoint params empty: {ep2.query_params.is_empty()}")
    print(f"Lucene params empty: {lucene_only.is_empty()}")
    print(f"Composite empty: {composite_2.is_empty()}")
    print(f"Query string: {composite_2.to_query_string()}")

    # Case 3: No parameters at all
    print("\n--- Case 3: No parameters set ---")
    ep3 = EpOneManageFabricConfigDeploySwitch()
    ep3.fabric_name = "MyFabric"
    ep3.switch_sn = "FOC12345678"

    empty_lucene_2 = LuceneQueryParams()

    composite_3 = CompositeQueryParams()
    composite_3.add(ep3.query_params)
    composite_3.add(empty_lucene_2)

    print(f"Composite empty: {composite_3.is_empty()}")
    query_str = composite_3.to_query_string()
    print(f"Query string: '{query_str}' (empty string)")
    full_url = f"{base_path}?{query_str}" if query_str else base_path
    print(f"Full URL: {full_url}")
    print()


if __name__ == "__main__":
    # Run all examples
    example_1_basic_composite()
    example_2_lucene_only()
    example_3_complex_lucene_filters()
    example_4_pagination()
    example_5_dynamic_composition()
    example_6_method_chaining()
    example_7_empty_handling()

    print("=" * 80)
    print("All examples completed!")
    print("=" * 80)
    print("\nKey Takeaways:")
    print("  1. CompositeQueryParams combines endpoint-specific and Lucene params")
    print("  2. Each parameter type is independently testable and maintainable")
    print("  3. Lucene filters support complex expressions (AND, OR, NOT, ranges)")
    print("  4. Empty parameter groups are automatically excluded from query strings")
    print("  5. Method chaining enables fluent interface pattern")
    print("  6. Useful for pagination, filtering, and field selection")
    print()
