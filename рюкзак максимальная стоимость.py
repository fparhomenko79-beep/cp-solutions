n, w = map(int, input().split())
weight = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if weight[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + cost[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

ctom, curw = [], w
for i in range(n, 0, -1):
    if dp[i][curw] != dp[i - 1][curw]:
        ctom.append(i)
        curw -= weight[i - 1]

print(len(ctom))
print(*ctom)