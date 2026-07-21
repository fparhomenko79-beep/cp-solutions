from collections import deque

n = int(input())
a = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = []
parent = [-1] * (n + 1)

visited = [False] * (n + 1)
que = deque()
que.append(1)

while que:
    v = que.popleft()
    visited[v] = True
    order.append(v)
    for to in graph[v]:
        if not visited[to]:
            que.append(to)
            parent[to] = v

order.reverse()

dp0 = [0] * (n + 1)
dp1 = [0] + [a[i] for i in range(n)]

for v in order:
    p = parent[v]
    if p != -1:
        dp0[p] += max(dp0[v], dp1[v])
        dp1[p] += dp0[v]

print(max(dp0[1], dp1[1]))