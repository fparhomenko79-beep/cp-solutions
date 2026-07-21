#C1
for _ in range(int(input())):
    n, x, s = map(int, input().split())
    u = input()

    dp = [-1] * (x + 1)
    dp[0] = 0

    maxim = 0

    for i in u:
        if i == "I":
            for j in range(maxim, -1, -1):
                k = dp[j]
                if k != -1 and j < x and k + 1 > dp[j + 1]:
                    dp[j + 1] = k + 1
            if maxim < x:
                maxim += 1
        elif i == "E":
            for j in range(maxim + 1):
                k = dp[j]
                if k != -1 and k < j * s:
                    dp[j] += 1
        else:
            for j in range(maxim, -1, -1):
                k = dp[j]
                if k != -1:
                    if k < j * s:
                        if k + 1 > dp[j]:
                            dp[j] = k + 1
                    if j < x:
                        if k + 1 > dp[j + 1]:
                            dp[j + 1] = k + 1
            if maxim < x:
                maxim += 1
    print(max(dp))
