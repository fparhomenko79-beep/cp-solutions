q = int(input())
for _ in range(q):
    a, b = input().split()
    N = len(b)
    a.zfill(N)
    a = list(map(int, a))
    b = list(map(int, b))

    dp = [[-1] * 2 for _ in range(N)]
    dp[1][1] = 0

    for i in range(N):
        A = int(a[i])
        B = int(b[i])

        new = [[-1] * 2 for _ in range(N)]

        for low in range(2):
            for high in range(2):
                if dp[low][high] == -1:
                    continue

                min_d = A if low else 0
                max_d = B if high else 9

                for d in range(min_d. max_d + 1):
                    nxt_low = 1 if (low and d == A) else 0
                    nxt_high = 1 if (high and d == B) else 0

                    if dp[low][high] + d > new[nxt_low][nxt_high]:
                        new[nxt_low][nxt_high] = dp[low][high] + d
        dp = new

    print(max(dp[0][0], dp[0][1], dp[1][0], dp[1][1]))
    