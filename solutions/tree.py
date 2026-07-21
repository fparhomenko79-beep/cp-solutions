from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = []
parent: list[int] = [-1] * (n + 1)
visited = [False] * (n + 1)
dp: list[int] = [1] * (n + 1)
que = deque()

que.append(1)

while que:
    v = que.pop()

    order.append(v)
    visited[v] = True

    for to in graph[v]:
        if not visited[to]:
            parent[to] = v
            que.append(to)

order.reverse()
for i in order:
    if parent[i] != -1:
        dp[parent[i]] += dp[i]

print(*dp[1:])