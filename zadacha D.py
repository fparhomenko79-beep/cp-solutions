from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

order = []
parent = [-1] * (n + 1)

visited = [False] * (n + 1)
que = deque()
que.append(1)

while que:
    v = que.popleft()
    visited[v] = True
    order.append(v)
    for to, w in graph[v]:
        if not visited[to]:
            que.append(to)
            parent[to] = v

order.reverse()

dp0 = [0] * (n + 1)
dp1 = [0] * (n + 1)

for v in order:
    basa = 0
    best = 0
    for to, w in graph[v]:
        if parent[to] == v:
            basa += dp0[to]
            x = w + dp1[to] - dp0[to]
            best = max(best, x)
    dp1[v] = basa
    dp0[v] = basa + best

print(dp0[1])