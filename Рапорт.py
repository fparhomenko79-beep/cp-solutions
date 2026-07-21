w, n, m = map(int, input().split())
left_part = list(map(int, input().split()))
right_part = list(map(int, input().split()))

def check_weight(weight, h):
    heigtleft = 0
    i = 0
    while i < len(left_part):
        cur = 0
        while cur < weight - 1 and left_part[i] <= weight - cur:
            cur += left_part[i] + 1
            i += 1
        heigtleft += 1

    heigtright = 0
    j = 0
    while j < len(right_part):
        cur = 0
        while cur < w - weight and right_part[j] < (w - weight) - cur and j < (w - weight) - 1:
            if right_part[j + 1] < (w - weight) - cur - right_part[j]:
                cur += right_part[j]
            else:
                cur += right_part[j] + 1
            j += 1
        if j == len(right_part) - 1 and cur == 0:
            heigtright += 1
            j += 1
        heigtright += 1

    return max(heigtleft, heigtright) <= h

maxlenword = max(max(left_part), max(right_part))

def check_height(h):
    left, right = maxlenword, w

    while left < right:
        mid = (left + right) // 2

        if check_weight(mid, h):
            right = mid
        else:
            left = mid + 1

    return right <= h

L, R = 1, max(n, m)
while L <= R:
    mid = (L + R) // 2

    if check_height(mid):
        R = mid
    else:
        L = mid + 1

print(R)
