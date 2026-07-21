n = 8 #int(input())
a = [1, -2, 4, 5, -6, 8, 9, -3] #list(map(int, input().split()))

#всего 3 функции для струкутуры, это:

#построение дерева
tree = [0] * (4 * n)

def build(v, l, r):
    if l == r:
        tree[v] = a[l]
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


#получение суммы на отрезке
def get_sum(v, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[v]

    if r < ql or qr < l:
        return 0

    m = (l + r) // 2
    left = get_sum(v * 2, l, m, ql, qr)
    right = get_sum(v * 2 + 1, m + 1, r, ql, qr)

    return left + right

#обновление значения в дереве
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