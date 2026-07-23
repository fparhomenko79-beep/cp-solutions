n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("1")
    exit()

l, r = 0, 1
cnt = {}
res = 1

while r < n:
    if a[r] not in cnt:
        cnt[a[r]] = 0
    else:
        while cnt[a[r]] >= 1 and l < r:
            cnt[a[l]] -= 1
            l += 1

    cnt[a[r]] += 1
    res = max(res, r - l + 1)
    r += 1

print(res)