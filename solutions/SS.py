n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (s + 1)
dp[0] = 1

for c in a:
    for i in range(c, s + 1):
        dp[i] = (dp[i] + dp[i - c]) % (10**9 + 7)

print(dp[s])