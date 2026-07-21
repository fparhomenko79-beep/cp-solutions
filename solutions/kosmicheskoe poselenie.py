n, a, b, w, h = map(int, input().split())

def check(x):
    A = a + 2 * x
    B = b + 2 * x

    kw = w // A
    kh = h // B
    count1 = kw * kh

    kw = w // B
    kh = h // A
    count2 = kw * kh

    return max(count1, count2) >= n

left, right = 0, max(w, h)
ans =  0

while left < right:
    mid = (left + right) // 2

    if check(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)