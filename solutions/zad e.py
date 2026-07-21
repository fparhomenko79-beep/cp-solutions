S = int(input())

dp = [0] * 82
dp[0] = 1

for i in range(9):
    new = [0] * 82
    for j in range(82):
        for d in range(10):
            if j + d <= 81:
                new[j + d] += dp[j]
    dp = new

res = dp[S]
if S == 1:
    res += 1
print(res)