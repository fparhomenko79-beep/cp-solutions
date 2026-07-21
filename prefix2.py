n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = matrix[i - 1][j - 1] + prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1]

q = int(input())
lst = []
for _ in range(q):
    lx, ly, rx, ry = map(int, input().split())
    lst.append(prefix[rx][ry] - prefix[lx - 1][ry] - prefix[rx][ly - 1] + prefix[lx - 1][ly - 1])

for i in range(len(lst)):
    print(lst[i], end=" ")