t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    P = [0] * (n + 1)
    ctom = [0] * (n + 1)


    for i in range(n):
        P[i + 1] = P[i] + abs(a[i])

    for i in range(n - 1, -1, -1):
        ctom[i] = ctom[i + 1] + a[i]

    maxim = ctom[0]
    idx = None

    for i in range(n):
        if a[i] > 0:
            cur = P[i] - a[i] + ctom[i + 1]
            if cur > maxim:
                maxim = cur
                idx = i

    if idx is None:
        print(0)
        print()
        continue

    k,x = [], 0
    for i in range(idx - 1, -1, -1):
        cur = a[i]
        if x % 2 != 0:
            cur = -cur
        if cur > 0:
            k.append(i + 1)
            x += 1

    k.append(idx + 1)
    print(len(k))
    print(*k)

