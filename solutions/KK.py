from collections import deque

n, m = map(int, input().split())

s_i, s_j = -1, -1
f_i, f_j = -1, -1

graph = []
for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j] == "S":
            s_i, s_j = i, j
        elif row[j] == "F":
            f_i, f_j = i, j
    graph.append(row)

dist = [[float("inf")] * m for _ in range(n)]
dist[s_i][s_j] = 0
que = deque()
que.append((s_i, s_j))

while que:
    vi, vj = que.popleft()

    steps = [[vi + 1, vj], [vi - 1, vj], [vi, vj + 1], [vi, vj - 1]]

    for to_i, to_j in steps:
        if (0 <= to_i < n) and (0 <= to_j < m) and graph[to_i][to_j] != "#" and dist[vi][vj] + 1 < dist[to_i][to_j]:
            que.append((to_i, to_j))
            dist[to_i][to_j] = dist[vi][vj] + 1

print(dist[f_i][f_j])