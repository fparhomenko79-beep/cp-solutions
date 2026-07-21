n, k = map(int, input().split())
s = input()

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
suma = 0

for d in range(1, n + 1):
    for i in range(n - d + 1):
        j = i + d - 1

        if i == j:
            suma += 1
            continue
        if i + 1 > n or j > n:
            continue
            
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = dp[i + 1][j - 1] + 1

        if dp[i][j] <= k:
            suma += 1

print(suma)