from collections import deque

n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
visited[s] = True

dist = [-1] * (n + 1)
dist[s] = 0

que = deque()
que.append(s)

while que:
    v = que.popleft()

    for to in graph[v]:
        if dist[to] == -1:
            dist[to] = dist[v] + 1
        dist[to] = min(dist[to], dist[v] + 1)

        if not visited[to]:
            visited[to] = True
            que.append(to)

print(*dist[1::])