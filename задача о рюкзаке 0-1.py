n, w = map(int, input().split())
weight = list(map(int, input().split()))

dp = [False] * (w + 1)
dp[0] = True

for i in weight:
    for j in range(w, i - 1, -1):
        if dp[j - i]:
            dp[j] = True

for i in range(w, -1, -1):
    if dp[i]:
        print(i)
        break