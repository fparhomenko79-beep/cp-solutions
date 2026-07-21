import math

n = int(input())

tree = [0] * (4 * n)
ctom = {}

def update(v, l, r, pos, val):
    if l == r:
        tree[v] = val
    else:
        m = (l + r) // 2
        if m >= pos:
            update(v * 2, l, m, pos, val)
        else:
            update(v * 2 + 1, m + 1, r, pos, val)
        tree[v] = math.gcd(tree[v * 2], tree[v * 2 + 1])

op = []
values_list = []
for i in range(n):
    type_of_operation, value = input().split()
    value = int(value)
    op.append((type_of_operation, value))
    values_list.append(value)

values_list = sorted(set(values_list))
pos = {values_list[i]: i for i in range(len(values_list))}

for i in range(n):
    to = op[i][0]
    val = pos[op[i][1]]

    if to == "+":
        if val not in ctom:
            ctom[val] = 0
            update(1, 0, n - 1, val, op[i][1])
        ctom[val] += 1
    else:
        if ctom[val] == 1:
            update(1, 0, n - 1, val, 0)
        ctom[val] -= 1

    print(tree[1])