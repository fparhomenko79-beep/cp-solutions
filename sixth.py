n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [[0, 0, 0, 0] for _ in range(4 * n)]

def build(v, l, r):
    if l == r:
        tree[v] = a[l]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]
build(1, 0, n - 1)

def get_sum(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    if r < ql or qr < l:
        return 0

    m = (l + r) // 2
    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return left + right

def update(v, l, r, pos, x):
    if l == r:
        tree[v] = x
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]

def find(v, l, r, x):
    if tree[v] < x:
        return -1
    if l == r:
        return l

    m = (l + r) // 2
    if tree[v * 2] >= x:
        return find(v * 2, l, m, x)
    else:
        return find(v * 2 + 1, m + 1, r, x - tree[v * 2])

for _ in range(q):
    inp = input().split()

    if len(inp) == 2:
        t, i = map(int, inp)
        res = find(1, 0, n - 1, i)
        print(res + 1 if res != -1 else - 1)
    else:
        t, x, y = map(int, inp)
        update(1, 0, n - 1, x - 1, y)
