a = input(); n = len(a)
b = input(); m = len(b)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        x = 0 if a[i - 1] == b[j - 1] else 1
        dp[i][j] = min(dp[i - 1][j] + 1,
                       dp[i][j - 1] + 1,
                       dp[i - 1][j - 1] + x)

print(dp[n][m])