n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
dct = {}

for i in range(len(b)):
    dct[b[i]] = i

tree = [[0, 0]] * (4 * n)

def merge(a, b):
    if a[0] > b[0]:
        return a
    if a[0] < b[0]:
        return b
    return [a[0], (a[1] + b[1]) % (10 ** 9 + 7)]

def update(v, l, r, pos, x):
    if l == r:
        tree[v] = merge(tree[v], x)

    else:
        m = (l + r) // 2
        if pos <= m:
            update(v * 2, l, m, pos, x)
        else:
            update(v * 2 + 1, m + 1, r, pos, x)

        tree[v] = merge(tree[v * 2], tree[v * 2 + 1])

def get_sum(v, l, r, ql, qr):
    if l > qr or r < ql:
        return [0, 0]

    if l >= ql and qr >= r:
        return tree[v]

    m = (l + r) // 2

    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return merge(left, right)

for i in range(n):
    x = a[i]
    best = get_sum(1, 0, len(b) - 1, 0, dct[x] - 1)

    if best[0] == 0:
        cur = [1, 1]
    else:
        cur = [best[0] + 1, best[1]]

    update(1, 0, len(b) - 1, dct[x], cur)

print(tree[1][1] % (10 ** 9 + 7))