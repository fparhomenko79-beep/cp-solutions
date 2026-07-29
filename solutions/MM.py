from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [float("inf")] * (n + 1)
dist[1] = 0
que = deque()
que.append(1)

while que:
    v = que.popleft()

    for to in graph[v]:
        if dist[to] > dist[v] + 1:
            que.append(to)
            dist[to] = dist[v] + 1

print(*dist[1::])