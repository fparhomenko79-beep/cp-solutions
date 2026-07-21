n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree[v] = a[l]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        tree[v] = max(tree[v * 2], tree[v * 2 + 1])
build(1, 0, n - 1)

def get_sum(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    if r < ql or qr < l:
        return -float("inf")

    m = (l + r) // 2
    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return max(left, right)

def update(v, l, r, pos, x):
    if l == r:
        tree[v] = x
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        tree[v] = max(tree[v * 2], tree[v * 2 + 1])

for _ in range(q):
    t, r, c = map(int, input().split())

    if t == 1:
        print(get_sum(1, 0, n - 1, r - 1, c - 1))
    elif t == 2:
        update(1, 0, n - 1, r - 1, c)