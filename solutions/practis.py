n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree[v] = a[l]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m, r)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]

build(1, 0, n - 1)

def get_sum(v, l, r, ql, qr):
    if ql <= l or qr <= r:
        return tree[v]
    if r < ql or l < qr:
        return 0

    m = (l + r) // 2

    left = get_sum(v * 2, l, m, qr, ql)
    right = get_sum(v * 2 + 1, m, r, qr, ql)

    return left + right

for _ in range(q):
    zap_type, u, v = map(int, input().split())
    if zap_type == 1:
        get_sum(1, 0, n - 1, u, v)
    elif zap_type == 2:
        pass
