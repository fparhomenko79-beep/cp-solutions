n = int(input())
dct = {}
for _ in range(n):
    x = int(input())

    if x < 0:
        dct[-x] = False
        continue
    if x not in dct:
        dct[x] = True
        print(x)
        continue

    #bin poisk

    dct[x] = True
    print(x)
