n, k = map(int, input().split())
a = list(map(int, input().split()))

pref = [0]
for i in range(n):
    pref.append(pref[-1] + a[i])

sumi = []
for i in range(n - k + 1):
    sumi.append(pref[i + k] - pref[i])

left = []
for i in range(len(sumi)):
    if i == 0:
        left.append(sumi[0])
    else:
        left.append(max(sumi[i], left[-1]))

right = []
for i in range(len(sumi) - 1, -1, -1):
    if i == len(sumi) - 1:
        right.append(sumi[-1])
    else:
        right.append(max(sumi[i], right[-1]))
right.reverse()

best = float("inf")
for i in range(len(sumi)):
    bob = 0
    if i - k > 0:
        bob = max(bob, left[i - k])
    if i + k < len(sumi):
        bob = max(bob, right[i + k])
    best = min(best, bob)
    
print(best)