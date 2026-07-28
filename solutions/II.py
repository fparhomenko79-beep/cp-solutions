n, m = map(int, input().split())
a = list(map(int, input().split()))

def check(length: int) -> bool:
    cnt = 0
    for i in range(n):
        if length > a[i]:
            return False
        cnt += a[i] // length
    return cnt >= m

left = 0
right: int = max(a)
res = -1

while left < right:
    mid: int = (left + right) // 2
    if check(mid):
        left = mid + 1
        res = max(res, mid)
    else:
        right = mid - 1

print(res)
