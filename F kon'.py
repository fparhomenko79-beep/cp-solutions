n = int(input())
a = list(map(int, input().split()))

tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree[v] = 0 if a[l] != 0 else 1
    else:
        m = (l + r) // 2

        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]
build(1, 0, n - 1)

def update(v, l, r, pos, val):
    if l == r:
        tree[v] = 0 if val != 0 else 1
    else:
        m = (l + r) // 2
        if pos <= m:
            update(v * 2, l, m, pos, val)
        else:
            update(v * 2 + 1, m + 1, r, pos, val)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]

def get_sum(v, l, r, ql, qr):
    if l > qr or r < ql:
        return 0

    if l >= ql and r <= qr:
        return tree[v]

    m = (l + r) // 2

    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return left + right

def find(v, l, r, ql, qr, k):
    if l == r:
        return l

    m = (l + r) // 2

    left = get_sum(v * 2, l, m, ql, qr)

    if left >= k:
        return find(v * 2, l, m, ql, qr, k)
    else:
        return find(v * 2 + 1, m + 1, r, ql, qr, k - left)


m = int(input())
for _ in range(m):
    inp = input().split()

    if inp[0] == "u":
        update(1, 0, n - 1, int(inp[1]) - 1, int(inp[2]))
    elif inp[0] == "s":
        print(find(1, 0, n - 1, int(inp[1]), int(inp[2]), int(inp[3])), end=" ")

