n = int(input())
arr = list(map(int, input().split()))

stek = []
new = [-1] * n

for i in range(n):
    if not stek:
        stek.append((arr[i], i))
        continue

    while stek and stek[-1][0] > arr[i]:
        new[stek[-1][1]] = i
        stek.pop()

    stek.append((arr[i], i))

print(*new)