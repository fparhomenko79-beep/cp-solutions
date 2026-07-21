n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)] # O(nm)

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = matrix[i][j]
            continue
        if matrix[i][j] == 0:
            continue
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

ctom = 0
cord = [0, 0]
for i in range(n):
    for j in range(m):
        if dp[i][j] >= ctom:
            ctom = dp[i][j]
            cord = [i - dp[i][j] + 2, j - dp[i][j] + 2]

print(ctom)
print(*cord)