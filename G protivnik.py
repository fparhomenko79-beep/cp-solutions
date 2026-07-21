n = int(input())
A = list(map(int, input().split()))

b = sorted(set(A))
ctom = {b[i]: i + 1 for i in range(len(b))}
a = [ctom[A[i]] for i in range(n)]

tree = [0] * (4 * n)

def update(v, l, r, pos):
    if l == r:
        tree[v] += 1
    else:
        m = (l + r) // 2
        if pos <= m:
            update(v * 2, l, m, pos)
        else:
            update(v * 2 + 1, m + 1, r, pos)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]

def get_sum(v, l, r, left, right):
    if right >= r and left <= l:
        return tree[v]
    if right < l or left > r:
        return 0

    m = (l + r) // 2

    return get_sum(v * 2, l, m, left, right) + get_sum(v * 2 + 1, m + 1, r, left, right)

left = [0] * n
right = [0] * n

for i in range(n):
    if a[i] == len(b):
        left[i] = 0
    else:
        left[i] = get_sum(1, 1, len(b), a[i] + 1, len(b))
    update(1, 1, len(b), a[i])

tree = [0] * (4 * n)

for i in range(n - 1, -1, -1):
    if a[i] == 0:
        right[i] = 0
    else:
        right[i] = get_sum(1, 1, len(b), 0, a[i] - 1)
    update(1, 1, len(b), a[i])

res = 0
for i in range(n):
    res += left[i] * right[i]
print(res)