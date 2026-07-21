import heapq

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w, f = map(int, input().split())
    graph[a].append((b, w, f))
    graph[b].append((a, w, f))

timings = []
for _ in range(k):
    timings.append(tuple(map(int, input().split())))

u, q, t0 = map(int, input().split())

dist = [float("inf")] * (n + 1)
dist[u] = t0

heap = []
heapq.heappush(heap, (t0, u))

while heap:
    cur, v = heapq.heappop(heap)

    if dist[v] < cur:
        continue

    for to, w, f in graph[v]:
        if f == 0:
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                heapq.heappush(heap, (dist[to], to))
        elif f == 1:
            start = -1

            if cur > timings[-1][1]:
                continue

            l, r = 0, len(timings)
            while l < r:
                mid = (l + r) // 2
                if timings[mid][0] <= cur <= timings[mid][1]:
                    start = cur
                    break
                if cur < timings[mid][0]:
                    start = timings[mid][0]
                    r = mid - 1
                else:
                    l = mid + 1
            if start == -1:
                continue
            if dist[to] > start + w:
                dist[to] = start + w
                heapq.heappush(heap, (dist[to], to))

print(dist[q] - t0 if dist[q] != float("inf") else "-1")