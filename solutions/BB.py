n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n

for i in range(1, n):
    if a[i - 1] < a[i]:
        b[i] = 1

cnt = 0
for i in range(n):
    if i < k - 1:
        cnt += b[i]
        continue
    elif i == k - 1:
        cnt += b[i]
    else:
        cnt -= b[i - k + 1]
        cnt += b[i]
    print(cnt, end=" ")