n, A, k = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10 ** 9 + 7

ak = []
while A:
    ak.append(A % k)
    A //= k
ak = ak[::-1]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n):
    if dp[i] == 0 or a[i] == 0:
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
        dp0 = 1
        dp1 = 0

        for j in range(len(ak)):
            lim = ak[j]
            minimal_num = 1 if j == 0 else 0
            num_dp0 = num_dp1 = 0

            if a[i + j] == -1:
                num_dp1 = (dp1 * (k - minimal_num)) % MOD
                
                if lim > minimal_num:
                    num_dp1 = (num_dp1 + dp0 * (lim - minimal_num)) % MOD
                if lim >= minimal_num:
                    num_dp0 = dp0
            else:
                d = a[i + j]
                if d >= minimal_num:
                    num_dp1 = dp1
                    if d < lim:
                        num_dp1 = (num_dp1 + dp0) % MOD
                    elif d == lim:
                        num_dp0 = dp0
            dp0 = num_dp0
            dp1 = num_dp1

        dp[i + len(ak)] = (dp[i + len(ak)] + dp[i] * (dp0 + dp1)) % MOD

print(dp[n])