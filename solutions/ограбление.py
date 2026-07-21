n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(26)] for _ in range(n)]

dp[0][arr[0]] = 1

for i in range(1, n):
    for j in range(26):
        if dp[i - 1][j] == 0:
            continue
        if arr[i] == 0:
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % (10 ** 9 + 7)
        else:
            if j + arr[i] < 26:
                dp[i][j + arr[i]] = (dp[i][j + arr[i]] + dp[i - 1][j]) % (10 ** 9 + 7)
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] = (dp[i][j - arr[i]] + dp[i - 1][j]) % (10 ** 9 + 7)

print(sum(dp[n - 1]) % (10**9 + 7))