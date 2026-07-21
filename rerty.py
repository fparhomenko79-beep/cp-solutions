n, q = map(int, input().split())
arr = [0] * (n + 2)

for _ in range(q):
    l, r, d = map(int, input().split())
    arr[l] += d
    arr[r + 1] += -d

prefix = [0]
for i in range(1, n + 2):
    prefix.append(prefix[-1] + arr[i])

print(*prefix[1:-1])