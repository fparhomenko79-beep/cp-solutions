n, w = map(int, input().split())
weight = []
cost = []
for _ in range(n):
    q, c = map(int, input().split())
    weight.append(q)
    cost.append(c)

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if weight[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], cost[i - 1] + dp[i - 1][j - weight[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][w])


