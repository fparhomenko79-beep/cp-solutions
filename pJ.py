# def find(x: int) -> int:
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
# 
# def union(x: int, y: int) -> None:
#     rx = find(x)
#     ry = find(y)
# 
#     if rx != ry:
#         if rank[rx] < rank[ry]:
#             parent[rx] = ry
#         else:
#             parent[ry] = rx
#             if rank[rx] == rank[ry]:
#                 rank[rx] += 1