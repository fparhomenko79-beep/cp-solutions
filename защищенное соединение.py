import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

dist = [float("inf")] * n
parent = [-1] * n

heap = []
for v in range(n):
    if a[v] == 1:
        dist[v] = 0
        parent[v] = v
        heapq.heappush(heap, (0, v))

while heap:
    cur, v = heapq.heappop(heap)

    if cur > dist[v]:
        continue

    for to, w in graph[v]:
        if dist[to] > dist[v] + w:
            dist[to] = dist[v] + w
            parent[to] = parent[v]
            heapq.heappush(heap, (dist[to], to))

best = float("inf")
city = None
for i in range(n):
    if a[i] == 2 and dist[i] < best:
        best = dist[i]
        city = i

print(f"{parent[city] + 1} {city + 1} {best}" if city else "-1")