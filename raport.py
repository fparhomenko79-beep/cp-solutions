w, n, m = map(int, input().split())
lp = list(map(int, input().split()))
rp = list(map(int, input().split()))

maxleft = max(lp)
maxright = max(rp)

def check_weight(weight):
    heightleft, heightright, rightweight = 0, 0, w - weight

    cur = 0
    for wordlen in lp:
        if wordlen <= weight - cur:
            cur += wordlen + 1
        else:
            cur = wordlen
            heightleft += 1

    cur = 0
    for wordlen in rp:
        if wordlen <= rightweight - cur:
            cur += wordlen + 1
        else:
            cur = wordlen
            heightright += 1

    return [heightright, heightleft]

def check_height(h):
    l, r = maxleft, w - maxright
    best = float('inf')

    while l < r:
        mider = (l + r) // 2
        resl, resr = check_weight(mider)
        if resl < resr:
            l = mider + 1
            best = min(best, resr)
        elif resl > resr:
            r = mider - 1
            best = min(best, resl)
        else:
            best = min(best, resl)
            break
    return best <= h

left, right = 1, max(n, m)
ans = float('inf')

while left < right:
    mid = (left + right) // 2
    if check_height(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)