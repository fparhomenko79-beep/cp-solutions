n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if i <= 1 and j <= 1:
            continue

        elif i >= 2 and j >= 2:
            dp[i][j] = dp[i - 1][j - 2] + dp[i - 2][j - 1]
        elif j >= 2 and i < 2:
            dp[i][j] = dp[i - 1][j - 2]
        elif j < 2 and i >= 2:
            dp[i][j] = dp[i - 2][j - 1]

print(dp[n - 1][m - 1])