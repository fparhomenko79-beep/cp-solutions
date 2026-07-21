s = input(); n = len(s)

dp = [["" for _ in range(n)] for _ in range(n)]

for length in range(1, n + 1):
    for l in range(0, n - length + 1):
        r = l + length - 1

        dp[l][r] = s[l:r + 1]

        for k in range(l, r):
            cand = dp[l][k] + dp[k + 1][r]

            if len(cand) < len(dp[l][r]):
                dp[l][r] = cand

        sub = s[l:r + 1]

        for p in range(1, length):
            if length % p == 0:
                block = sub[:p]
                count = length // p

                if block * count == sub:
                    cand = str(count) + "(" + dp[l][l + p - 1] + ")"

                    if len(cand) < len(dp[l][r]):
                        dp[l][r] = cand

print(dp[0][n - 1])
