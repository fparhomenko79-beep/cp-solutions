h, w = map(int, input().split())
matrix = [list(input()) for _ in range(h)]

visited = [[False for _ in range(h + 1)] for _ in range(w + 1)]
i: int = 0
j: int = 0
x, y = i, j
while 0 <= i < h and 0 <= j < w:
    x = i
    y = j

    if visited[i][j]:
        print(-1)
        exit()
    visited[i][j] = True
    if matrix[i][j] == "U":
        i -= 1
    elif matrix[i][j] == "D":
        i += 1
    elif matrix[i][j] == "L":
        j -= 1
    else:
        j += 1

print(x + 1, y + 1)