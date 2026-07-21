from collections import deque

n, m = map(int, input().split())
r, c = map(int, input().split())
x, y = map(int, input().split())

matrix = [list(input()) for _ in range(n)]

que = deque()
que.append((r - 1, c - 1, x, y))

count = 1

while que:
    i, j, l, r = que.popleft()

    pos = [(i + 1, j, l, r), (i - 1, j, l, r)]
    if l > 0:
        pos.append((i, j - 1, l - 1, r))
    if r > 0:
        pos.append((i, j + 1, l, r - 1))

    for tx, ty, left, right in pos:
        if 0 <= tx < n and 0 <= ty < m and matrix[tx][ty] != "*":
            que.append((tx, ty, left, right))
            count += 1

print(count)