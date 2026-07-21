import bisect

n, a1, k, b, m = map(int, input().split())

a = [a1]
for i in range(1, n):
    a.append((k * a[-1] + b) % m)

d = []
pos = []
parent = [-1] * n

for i in range(n):
    idx = bisect.bisect_left(d, a[i])

    if idx == len(d):
        d.append(a[i])
        pos.append(i)
    else:
        d[idx] = a[i]
        pos[idx] = i

    if idx > 0:
        parent[i] = pos[idx - 1]
    else:
        parent[i] = -1

print(len(d))

path = []
v = pos[-1] if pos else -1
while v != -1:
    path.append(a[v])
    v = parent[v]

print(*path[::-1])

