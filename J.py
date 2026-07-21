t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    nech, chet = 0, 0
    for i in range(n):
        if arr[i] % 2 == 0:
            chet += 1
        else:
            nech += 1

    if not nech:
        print("No")
        continue

    if nech % 2 == 0:
        nech -= 1

    if x % 2 != 0:
        print("Yes" if x - (nech + chet) <= 0 else "No")
    else:
        if chet == 0:
            print("No")
            continue
        else:
            print("yes" if chet - (x - nech) >= 0 else "No")
