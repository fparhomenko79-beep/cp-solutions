n = int(input())
a = list(map(int, input().split()))
k = int(input())

tree = [[0, 0] for _ in range(4 * n)]

def build(v, l, r):
    if l == r:
        tree[v] = [a[l], l + 1]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        if tree[v * 2][0] >= tree[v * 2 + 1][0]:
            tree[v] = tree[v * 2]
        else:
            tree[v] = tree[v * 2 + 1]
build(1, 0, n - 1)

def get_max(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    if r < ql or qr < l:
        return [-float("inf"), -1]

    m = (l + r) // 2
    left = get_max(v * 2, l, m, ql, qr)
    right = get_max(v * 2 + 1, m + 1, r, ql, qr)

    if left[0] >= right[0]:
        return left
    else:
        return right

for _ in range(k):
    l, r = map(int, input().split())
    print(*get_max(1, 0, n - 1, l - 1, r - 1))