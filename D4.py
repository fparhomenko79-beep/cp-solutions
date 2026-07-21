n = int(input())
a = list(map(int, input().split()))

LIM = 3 * 10 ** 5

tree = [0] * (LIM * 4 + 1)

def get_sum(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    if r < ql or qr < l:
        return 0

    m = (l + r) // 2
    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return left + right

def update(v, l, r, pos):
    if l == r:
        tree[v] += 1
    else:
        m = (l + r) // 2

        if pos <= m:
            update(2 * v, l, m, pos)
        else:
            update(2 * v + 1, m + 1, r, pos)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]

ans = [0] * n
for i in range(n):
    update(1, 0, LIM, a[i])

    if i > 0:
        ans[i] += ans[i - 1]
        ans[i] += get_sum(1, 0, LIM, a[i] + 1, LIM)

print(*ans)