import heapq

n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [float("inf")] * (n + 1)
dist[s] = 0

heap = []
heapq.heappush(heap, (0, s))

while heap:
    cur_dist, v = heapq.heappop(heap)

    if cur_dist > dist[v]:
        continue

    for to, w in graph[v]:
        if dist[v] + w < dist[to]:
            dist[to] = dist[v] + w
            heapq.heappush(heap, (dist[to], to))

print(*list(map(lambda x: x if x != float("inf") else -1, dist[1::])))
