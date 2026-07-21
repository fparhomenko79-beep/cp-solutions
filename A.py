#A
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    ctom = n
    for i in set(a):
        l = sum(1 for j in a if j < i)
        r = sum(1 for j in a if j > i)
        count = max(l, r)

        ctom = min(ctom, count)

    print(ctom)
