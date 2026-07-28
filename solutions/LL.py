n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def dfs(vi: int, vj: int):
    visited[vi][vj] = True
    steps = [[vi + 1, vj], [vi, vj + 1], [vi, vj - 1], [vi - 1, vj]]
    for toi, toj in steps:
        if (0 <= toi < n) and (0 <= toj < m) and graph[toi][toj] == "#" and not visited[toi][toj]:
            dfs(toi, toj)

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "#" and not visited[i][j]:
            res += 1
            dfs(i, j)

print(res)