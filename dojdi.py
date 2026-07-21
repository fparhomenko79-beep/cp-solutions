n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [[0, 0, 0, 0] for _ in range(4 * n)]

def build(v, l, r):
    if l == r:
        tree[v] = [a[l], a[l], a[l], 1]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)

        left = tree[v * 2]
        right = tree[v * 2 + 1]

        if left[1] == left[3]:
            pref = left[3] + right[1]
        else:
            pref = left[1]

        if right[2] == right[3]:
            suff = right[3] + left[2]
        else:
            suff = right[2]

        tree[v] = [max(left[0], right[0], left[2] + right[1]), pref, suff, left[3] + right[3]]
build(1, 0, n - 1)

def update(v, l, r, pos, x):
    if l == r:
        tree[v] = [x, x, x, 1]
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        left = tree[v * 2]
        right = tree[v * 2 + 1]

        if left[1] == left[3]:
            pref = left[3] + right[1]
        else:
            pref = left[1]

        if right[2] == right[3]:
            suff = right[3] + left[2]
        else:
            suff = right[2]

        tree[v] = [max(left[0], right[0], left[2] + right[1]), pref, suff, left[3] + right[3]]

def get_max(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    m = (l + r) // 2

    if qr <= m:
        return get_max(v * 2, l, m, ql, qr)
    if ql > m:
        return get_max(v * 2 + 1, m + 1, r, ql, qr)

    left = get_max(v * 2, l, m, ql, qr)
    right = get_max(v * 2 + 1, m + 1, r, ql, qr)

    if left[1] == left[3]:
        res_pref = left[3] + right[1]
    else:
        res_pref = left[1]

    if right[2] == right[3]:
        res_suff = right[3] + left[2]
    else:
        res_suff = right[2]

    return [max(left[0], right[0], left[2] + right[1]), res_pref, res_suff, left[3] + right[3]]

for _ in range(q):
    inp = input().split()
    t, x, y = map(int, inp)

    if t == 1:
        print(get_max(1, 0, n - 1, x - 1, y - 1)[0])
    else:
        update(1, 0, n - 1, x - 1, y)