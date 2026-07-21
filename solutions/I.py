n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    v = int(input())
    graph[i].append(v)
    graph[v].append(i)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True

    for to in graph[v]:
        if not visited[to]:
            dfs(to)

res = 0
for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)
        res += 1

print(res)


