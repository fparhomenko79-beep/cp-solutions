n, s = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * (n + 1)
res = 0

def dfs(v):
    global res

    res += 1
    visited[v] = True
    for j in range(n):
        if graph[v][j] == 1 and not visited[j]:
            dfs(j)

dfs(s - 1)
print(res)