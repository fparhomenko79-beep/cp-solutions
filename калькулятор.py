n = int(input())

dp = [float("inf")] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

path = []
while n > 1:
    if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
        path.append(3)
        n //= 3
    elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
        path.append(2)
        n //= 2
    else:
        path.append(1)
        n -= 1

print("".join(map(str, path[::-1])))
