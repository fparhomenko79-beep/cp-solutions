n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(n):
    if i % 2 == 0:
        b[i] = a[i]
    else:
        b[i] = -a[i]

tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree[v] = b[l]
    else:
        m = (l + r) // 2

        build(2 * v, l, m)
        build(2 * v + 1, m + 1, r)

        tree[v] = tree[2 * v] + tree[2 * v + 1]
build(1, 0, n - 1)

def updatдe(v, l, r, pos, x):
    if l == r:
        tree[v] = x

    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        tree[v] = tree[2 * v] + tree[2 * v + 1]

def get_sum(v, l, r, ql, qr):
    if l > qr or r < ql:
        return 0

    if l >= ql and r <= qr:
        return tree[v]

    m = (l + r) // 2

    left = get_sum(2 * v, l, m, ql, qr)
    right = get_sum(2 * v + 1, m + 1, r, ql, qr)

    return left + right

m = int(input())
for _ in range(m):
    inp = list(map(int, input().split()))

    if inp[0] == 0:
        update(1, 0, n - 1, inp[1] - 1, inp[2] if (inp[1] - 1) % 2 == 0 else -inp[2])

    else:
        q = get_sum(1, 0, n - 1, inp[1] - 1, inp[2] - 1)
        print(-q if (inp[1] - 1) % 2 != 0 else q)