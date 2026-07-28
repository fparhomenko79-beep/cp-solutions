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
        cur += (a[i] - a[i - k])
        b.append(cur)

left = [b[0]]
right = [b[-1]]
for i in range(1, len(b)):
    left.append(max(left[-1], b[i]))
for i in range(len(b) - 2, -1, -1):
    right.append(max(right[-1], b[i]))
right.reverse()

res = 0
for i in range(len(b) - k):
    res = max(res, left[i] + right[i + k])

print(res)
