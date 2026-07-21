n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        if j > 0 and i > 0:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10**6 + 7)
        elif j > 0 and i == 0:
            dp[i][j] = dp[i][j - 1]
        elif j == 0 and i > 0:
            dp[i][j] = dp[i - 1][j]

print(dp[n - 1][m - 1])