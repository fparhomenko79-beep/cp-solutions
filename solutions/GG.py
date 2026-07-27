n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []
cur = 0
for i in range(n):
    if i <= k - 1:
        cur += a[i]
    if i == k - 1:
        b.append(cur)
    if i >= k:
        cur += a[i]
        
