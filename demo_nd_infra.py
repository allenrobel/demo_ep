"""Simple example"""

from ep_api_v1_infra_aaa import EpApiV1InfraAaaLocalUsersGet, \
    EpApiV1InfraAaaLocalUsersPost, \
    EpApiV1InfraAaaLocalUsersPut, \
    EpApiV1InfraAaaLocalUsersDelete

# Uncomment the following lines for query params example
# from query_params import LuceneQueryParams, CompositeQueryParams

# GET Example
ep = EpApiV1InfraAaaLocalUsersGet()
print(f"Endpoint path: {ep.path}")
print(f"HTTP Method: {ep.verb.value}")

# With optional login_id
ep.login_id = "admin"
print(f"Endpoint path: {ep.path}")
print(f"HTTP Method: {ep.verb.value}")

# POST Example
ep_post = EpApiV1InfraAaaLocalUsersPost()
print(f"Endpoint path: {ep_post.path}")
print(f"HTTP Method: {ep_post.verb.value}")

# PUT Example
ep_put = EpApiV1InfraAaaLocalUsersPut()
ep_put.login_id = "admin"
print(f"Endpoint path: {ep_put.path}")
print(f"HTTP Method: {ep_put.verb.value}")

# DELETE Example
ep_delete = EpApiV1InfraAaaLocalUsersDelete()
ep_delete.login_id = "admin"
print(f"Endpoint path: {ep_delete.path}")
print(f"HTTP Method: {ep_delete.verb.value}")

# Omitted: Query Params Example
# lucene_params = LuceneQueryParams()
# lucene_params.filter = "name:admin AND role:network-admin"
# lucene_params.max = 2
# lucene_params.sort = "name:asc"

# composite = CompositeQueryParams()
# composite.add(lucene_params)
# print(f"Composite Query String: {composite.to_query_string()}")
# print(f"Composite Endpoint Path: {ep.path}?{composite.to_query_string()}")
