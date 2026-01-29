"""Simple example"""

from onemanage_vrf_endpoints import EpOneManageVrfUpdate
from query_params import LuceneQueryParams, CompositeQueryParams

ep = EpOneManageVrfUpdate()
ep.fabric_name = "MyFabric"
ep.vrf_name = "MyVrf"
print(f"Endpoint path: {ep.path}")
print(f"HTTP Method: {ep.verb.value}")

ep = EpOneManageVrfUpdate(fabric_name="AnotherFabric", vrf_name="AnotherVrf")
print(f"Endpoint path: {ep.path}")
print(f"HTTP Method: {ep.verb.value}")

lucene_params = LuceneQueryParams()
lucene_params.filter = "name:Spine* AND role:spine"
lucene_params.max = 50
lucene_params.sort = "name:asc"

composite = CompositeQueryParams()
composite.add(lucene_params)
print(f"Composite Query String: {composite.to_query_string()}")
print(f"Composite Endpoint Path: {ep.path}?{composite.to_query_string()}")
