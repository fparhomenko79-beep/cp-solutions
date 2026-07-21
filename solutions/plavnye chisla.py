n = int(input())
dp = [1] * 10
dp[0] = 0

for i in range(2, n + 1):
    new = [0] * 10
    for j in range(10):
        var = []
        if j > 0:
            var.append(dp[j - 1])
        var.append(dp[j])
        if j < 9:
            var.append(dp[j + 1])
        new[j] = sum(var)
    dp = new

print(sum(dp))