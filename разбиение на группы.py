n = int(input())# O(n^2)
arr = sorted(list(map(int, input().split())))

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(2, n + 1):
    for j in range(0, i - 1):
        dp[i] = min(dp[j] + arr[i - 1] - arr[j], dp[i])

print(dp[n])