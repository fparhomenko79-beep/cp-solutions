n, q = map(int, input().split())
a = list(map(int, input().split()))

tree_max = [0] * (4 * n)
tree_min = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree_max[v] = a[l]
        tree_min[v] = a[l]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        tree_max[v] = max(tree_max[v * 2], tree_max[v * 2 + 1])
        tree_min[v] = min(tree_min[v * 2], tree_min[v * 2 + 1])
build(1, 0, n - 1)

def get_sum(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree_max[v], tree_min[v]

    if r < ql or qr < l:
        return -float("inf"), float("inf")

    m = (l + r) // 2
    max_l, min_l = get_sum(v * 2, l, m, ql, qr)
    max_r, min_r = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return max(max_l, max_r), min(min_l, min_r)

def update(v, l, r, pos, x):
    if l == r:
        tree_max[v] = x
        tree_min[v] = x
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        tree_max[v] = max(tree_max[v * 2], tree_max[v * 2 + 1])
        tree_min[v] = min(tree_min[v * 2], tree_min[v * 2 + 1])

for _ in range(q):
    t, r, c = map(int, input().split())

    if t == 1:
        mx, mn = get_sum(1, 0, n - 1, r - 1, c - 1)
        print(mx - mn)
    elif t == 2:
        update(1, 0, n - 1, r - 1, c)