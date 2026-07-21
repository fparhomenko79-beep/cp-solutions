n = int(input())
arr = sorted(list(map(int, input().split())))

dp = [0] * (n + 1)

dp[1] = float("inf")
dp[2] = arr[1] - arr[0]

for i in range(3, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + (arr[i - 1] - arr[i - 2])

print(dp[n])

