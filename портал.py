from collections import deque

n, m = map(int, input().split())
matrix = []
s, f = (-1, -1), (-1, -1)
for i in range(n):
    p = input()
    for j in range(m):
        if p[j] == "S":
            s = (i, j)
        if p[j] == "T":
            f = (i, j)
    matrix.append(p)

dist = [[float("inf") for _ in range(m)] for _ in range(n)]
dist[s[0]][s[1]] = 0

que = deque()
que.append(s)
dif = [(0, 1), (1, 0), (-1, 0), (0, -1)]

while que:
    vx, vy = que.popleft()

    if (vx, vy) == f:
        break

    for dx, dy in dif:
        nx, ny = vx + dx, vy + dy

        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != "#":
            if dist[nx][ny] > dist[vx][vy] + 1:
                dist[nx][ny] = dist[vx][vy] + 1
                que.append((nx, ny))

    for fx, fy in dif:
        if 0 <= vx + fx < n and 0 <= vy + fy < m and matrix[vx + fx][vy + fy] == "#":
            for dx, dy in dif:
                x, y = vx, vy

                while 0 <= x + dx < n and 0 <= y + dy < m and matrix[x + dx][y + dy] != "#":
                    x += dx
                    y += dy

                if dist[x][y] > dist[vx][vy] + 1:
                    dist[x][y] = dist[vx][vy] + 1
                    que.append((x, y))
            break

print(dist[f[0]][f[1]] if dist[f[0]][f[1]] != float("inf") else -1)

# cell_width = max(len(str(x)) for row in dist for x in row) + 1
# for row in dist:
#     # Шаблон f"{x:>{cell_width}}" выравнивает элементы по правому краю
#     print(" ".join(f"{x:>{cell_width}}" for x in row))
#10  9
#########
#......T#
#.....###
#.....###
#.....###
#....S..#
#.......#
#.......#
#.......#
#########