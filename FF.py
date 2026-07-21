n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

operation = []
for _ in range(m):
    l, r, d = map(int, input().split())
    operation.append((l, r, d))

razmetka = [0] * (m + 2)
for _ in range(k):
    x, y = map(int, input().split())
    razmetka[x] += 1
    razmetka[y + 1] -= 1

op = [0] * (m + 1)
curcount = 0
for i in range(1, m + 1):
    curcount += razmetka[i]
    op[i] = curcount

diff = [0] * (n + 2)
for i in range(m):
    cnt = op[i + 1]
    if cnt > 0:
        l, r, d = operation[i]
        diff[l] += d * cnt
        diff[r + 1] -= d * cnt

result = []
ctom = 0
for i in range(n):
    ctom += diff[i + 1]
    result.append(arr[i] + ctom)

print(*(result))