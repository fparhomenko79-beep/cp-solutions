n = int(input())
arr = list(map(int, input().split())) + [0]

pref = [0]
for i in range(n):
    pref.append(pref[-1] + arr[i])

pref += [0]
stek = []
best = 0

for i in range(n + 1):
    while stek and arr[i] <= arr[stek[-1]]:
        h = arr[stek.pop()]
        left = stek[-1] if stek else -1
        best = max(best, h * (pref[i] - pref[left + 1]))
    stek.append(i)

print(best)