k, n = map(int, input().split())  #O(N)

dp = [0] * (n + 1)
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    dp[i] += (dp[i - 1] * 2) % (10 ** 7 + 7)
    if i - k > 0:
        dp[i] -= dp[i - k - 1]

print(dp[n])