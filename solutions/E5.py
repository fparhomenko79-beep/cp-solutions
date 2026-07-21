n = int(input())
a = list(map(int, input().split()))
k = int(input())
tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        if a[l] == 0:
            tree[v] = 1
        else:
            tree[v] = 0
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
        if x == 0:
            tree[v] = 1
        else:
            tree[v] = 0
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos, x)
        else:
            update(2 * v + 1, m + 1, r, pos, x)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]

def find(v, l, r, k):
    if l == r:
        return l

    m = (l + r) // 2
    if tree[v * 2] >= k:
        return find(v * 2, l, m, k)
    else:
        return find(v * 2 + 1, m + 1, r, k - tree[v * 2])

for i in range(k):
    inp = input().split()

    if inp[0] == "s":
        print(find(1, int(inp[1]) - 1, int(inp[2]) - 1, int(inp[3])) + 1, end=" ")
    else:
        update(1, 0, n - 1, int(inp[1]) - 1, int(inp[2]))