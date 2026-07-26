n, s = map(int, input().split())
a = list(map(int, input().split()))

cur = 0
count = 0
l = 0

for r in range(n):
    cur += a[r]
    while cur > s:
        cur -= a[l]
        l += 1
    count += r - l + 1

print(count)