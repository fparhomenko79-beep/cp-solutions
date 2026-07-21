n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [0] * m
p = [-1] * m

for i in range(n):
    ctom = 0
    p1 = -1
    for j in range(m):
        if b[j] < a[i]:
            if dp[j] > ctom:
                ctom = dp[j]
                p1 = j
        elif b[j] == a[i]:
            if ctom + 1 > dp[j]:
                dp[j] = ctom + 1
                p[j] = p1

maxim = 0
idx = -1
for i in range(len(dp)):
    if dp[i] > maxim:
        idx = i
        maxim = dp[i]

v = idx
path = []
while v != -1:
    path.append(b[v])
    v = p[v]

print(len(path))
print(*path[::-1])