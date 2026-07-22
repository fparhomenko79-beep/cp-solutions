n = int(input())
a = list(map(int, input().split()))

ans = []
stek = []
for i in range(n - 1, -1, -1):
    while stek and a[i] <= a[stek[-1]]:
        stek.pop()
    if stek and a[i] > a[stek[-1]]:
        ans.append(stek[-1])
    else:
        ans.append(-1)
    stek.append(i)

print(*ans[::-1])