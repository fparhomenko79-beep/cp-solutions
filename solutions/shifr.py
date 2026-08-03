n, A, k = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10**9 + 7

ak = ""
while A:
    ak += str(A % k)
    A //= k
ak = ak[::-1]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n):
    if dp[i] == 0:
        continue
    x = 1
    for j in range(i, min(i + len(ak) - 1, n)):
        if j - i == 0 and a[j] == 0:
            x = 0
        elif j - i == 0 and a[j] == -1:
            x = (x * (k - 1)) % MOD
        else:
            if a[j] == -1:
                x = (x * k) % MOD
        dp[j + 1] = (dp[j + 1] + dp[i] * x) % MOD

    if i + len(ak) <= n:
        d = 0
        for q in range(k):
            d += 1

        dp[i + 1] = (dp[i + 1] + d) % MOD

print(dp)