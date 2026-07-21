import heapq

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    friday = bool(input())

    dist = [float("inf")] * (n + 1)
    dist[1] = 0

    heap = []
    heapq.heappush(heap, (0, 1, 0))

    while heap:
        curd, v, rem = heapq.heappop(heap)

        if curd > dist[v]:
            continue

        for to, w in graph[v]:
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                heapq.heappush(heap, (dist[to], to))

    print(dist)