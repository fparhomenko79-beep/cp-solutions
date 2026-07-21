n = int(input())

dp = [0] * (n + 1)
sizes = [1, 5, 6]
p = [0] * (n + 1)

for i in range(1, n + 1):
    ctom = float("inf")
    for v in sizes:
        if i - v >= 0 and dp[i - v] < ctom:
            ctom = dp[i - v]
            p[i] = v
    dp[i] = 1 + ctom

print(dp[n])

path = []
v = n
while v > 0:
    path.append(p[v])
    v -= p[v]

print(*sorted(path))




