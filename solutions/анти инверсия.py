n = int(input())
arr = list(map(int, input().split()))

def f(arr):
    if len(arr) <= 1:
        return arr, 0

    l, lcnt = f(arr[:len(arr) // 2])
    r, rcnt = f(arr[len(arr) // 2:])

    merg = []
    i, j = 0, 0

    ant = lcnt + rcnt

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            ant += len(r) - j
            merg.append(l[i])
            i += 1
        else:
            merg.append(r[j])
            j += 1

    merg.extend(l[i:])
    merg.extend(r[j:])

    return merg, ant

print(f(arr)[1])