n = int(input())
knight_num = {1: [8, 6],
              2: [7, 9],
              3: [4, 8],
              4: [3, 9, 0],
              5: [],
              6: [1, 7, 0],
              7: [2, 6],
              8: [1, 3],
              9: [4, 2],
              0: [4, 6]}

dp = [[0 for _ in range(n + 1)] for _ in range(10)]

for i in range(10):
    dp[i][1] = 1
dp[0][1] = dp[8][1] = 0

for j in range(2, n + 1):
    for i in range(10):
        if i == 5:
            continue
        for k in knight_num[i]:
            dp[i][j] += dp[k][j - 1]

ans = 0
for i in range(10):
    ans += dp[i][-1]
print(ans)