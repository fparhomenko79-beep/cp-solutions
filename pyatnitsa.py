import heapq
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    friday = bool(input())

    dist = [[float("inf")] * 13 for _ in range(n + 1)]
    dist[1][0] = 0

    heap = [(0, 1, 0)]

    while heap:
        cur_d, v, rem = heapq.heappop(heap)

        if cur_d != dist[v][rem]:
            continue

        for to, w in graph[v]:
            if friday and (rem + w) % 13 == 0:
                continue
            if cur_d + w < dist[to][(rem + w) % 13]:
                dist[to][(rem + w) % 13] = cur_d + w
                heapq.heappush(heap, (cur_d + w, to, (rem + w) % 13))

    if friday:
        print(min(dist[n][1:]))
    else:
        print(min(dist[n]))