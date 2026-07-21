n = int(input())
stek = []

for _ in range(n):
    s = list(map(int, input().split()))

    if s[0] == 0:
        stek.append(0)

    else:
        a = stek.pop()
        b = stek.pop()
        stek.append(max(a, b) + 1)

print(*stek)