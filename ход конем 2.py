n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1

for s in range(m + n):
    for i in range(n):
        j = s - i

        if 0 <= j < m and not (i == 0 and j == 0):
            poss_mov = [[i - 2, j + 1], [i - 2, j - 1], [i - 1, j - 2], [i + 1, j - 2]]

            for ni, nj in poss_mov:
                if (0 <= ni < n) and (0 <= nj < m):
                     dp[i][j] += dp[ni][nj]

print(dp[n - 1][m - 1])