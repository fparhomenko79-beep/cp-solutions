import math

n, x, y = map(int, input().split())

nt = min(x, y) + math.ceil((n - 1) / (1/x + 1/y))
print(nt)

# def check(t, x, y, n):
#
#     return nt <= t
#
# res = float("inf")
# l, r = 0, 10**18
# while l < r:
#     mid = (l + r) // 2
#     if check(mid, x, y, n):
#         r = mid - 1
#         res = min(res, mid)
#     else:
#         l = mid + 1
#
# print(res)