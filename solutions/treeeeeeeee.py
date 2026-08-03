from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
value = [0] * (n + 1)
for i in range(n):
    a, b = map(int, input().split())
    value[i + 1] = a
    if b != -1:
        graph[b].append(i + 1)
        graph[i + 1].append(b)

order = []
parent = [-1] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
que = deque()
que.append(1)

while que:
    v = que.popleft()
    order.append(v)
    for to in graph[v]:
        if not visited[to]:
            que.append(to)
            parent[to] = v
            visited[to] = True

order.reverse()

team = value.copy()
best1 = [-float("inf")] * (n + 1)
free = [-float("inf")] * (n + 1)
best2 = [-float("inf")] * (n + 1)

for v in order:
    for u in graph[v]:
        if u != parent[v]:
            team[v] += max(0, team[u])

    best1[v] = team[v]
    for u in graph[v]:
        if u != parent[v]:
            best1[v] = max(best1[v], best1[u])

    for u in graph[v]:
        if u != parent[v]:
            if team[u] > 0:
                free[v] = max(free[v], free[u])
            else:
                free[v] = max(free[v], best1[u])

    best2[v] = team[v] + free[v]

    for u in graph[v]:
        if u != parent[v]:
            best2[v] = max(best2[v], best2[u])

    max1, max2 = -float("inf"), -float("inf")
    for u in graph[v]:
        if u != parent[v]:
            if best1[u] > max1:
                max2 = max1
                max1 = best1[u]
            elif best1[u] > max2:
                max2 = best1[u]

    if max1 != -float("inf") and max2 != -float("inf"):
        best2[v] = max(best2[v], max1 + max2)

print(best2[1])