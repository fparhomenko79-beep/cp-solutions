n, m = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * (n - 1)
for i in range(n - 1):
    b[i] = a[i + 1] - a[i]

tree_max = [0] * (4 * n)
tree_min = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree_max[v] = b[l]
        tree_min[v] = b[l]
    else:
        m = (l + r) // 2

        build(v * 2, l, m)
        build(v * 2, m + 1, r)

        tree_max[v] = max(tree_max[v * 2], tree_max[v * 2 + 1])
        tree_min[v] = min(tree_min[v * 2], tree_min[v * 2 + 1])
build(1, 0, n - 2)

def update(v, l, r, pos, val):
    if l == r:
        tree_max[v] += val
        tree_min[v] += val
    else:
        m = (l + r) // 2
        if m >= pos:
            update(v * 2, l, m, pos, val)
        else:
            update(v * 2 + 1, m + 1, r, pos, val)

        tree_max[v] = max(tree_max[v * 2], tree_max[v * 2 + 1])
        tree_min[v] = min(tree_min[v * 2], tree_min[v * 2 + 1])

def get_max(v, l, r, ql, qr):
    if ql > r or qr < l:
        return float("-inf")

    if qr <= r and l >= ql:
        return tree_max[v]

    m = (l + r) // 2

    left = get_max(v * 2, l, m, ql, qr)
    right = get_max(v * 2 + 1, m + 1, r, ql, qr)

    return max(left, right)


def get_min(v, l, r, ql, qr):
    if ql > r or qr < l:
        return float("inf")

    if qr <= r and l >= ql:
        return tree_min[v]

    m = (l + r) // 2

    left = get_min(v * 2, l, m, ql, qr)
    right = get_min(v * 2 + 1, m + 1, r, ql, qr)

    return min(left, right)


for _ in range(m):
    inp = input().split()
    type = inp[0]

    if type == "1":
        x, y = int(inp[1]), int(inp[2])

        if x > y and get_min(1, 0, n - 2, y - 1, x - 2) >= -1:
            print("YES")
        else:
            if x < y and get_max(1, 0, n - 2, x - 1, y - 2) <= 1:
                print("YES")
            else:
                print("NO")

    else:
        l, r, k = int(inp[1]), int(inp[2]), int(inp[3])
        update(1, 0, n - 2, l - 2, k)
        update(1, 0, n - 2, r - 1, -k)