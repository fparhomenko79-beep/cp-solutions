n, k = map(int, input().split())
ans = float("inf")

d = 2
while d <= int(k ** 0.5) + 1:
    if k % d == 0:
        count = 0
        while k % d == 0:
            k //= d
            count += 1
        x, p = n, 0
        while x:
            x //= d
            p += x
        ans = min(ans, p // count)
    d += 1

if k > 1:
    x, p = n, 0
    while x:
        x //= k
        p += x
    ans = min(ans, p)

print(ans)