n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

def biniry_search(tar, a):
    l, r = 0, len(a) - 1
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > tar:
            r = mid - 1
        else:
            res = mid
            l = mid + 1
    return res

for i in range(q):
    ans = biniry_search(x[i], a)
    print(ans + 1 if ans != 0 else 0, end=" ")
