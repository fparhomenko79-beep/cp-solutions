from sys import stdin, stdout; input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    if n <= 1000:
        found = False
        for a in range(n, -1, -1):
            if (n - a) % 12 == 0 and str(a) == str(a)[::-1]:
                print(f"{a} {n - a}")
                found = True
                break
        if not found:
            print("-1")
        continue

    s = str(n)
    d = len(s)
    ans = "-1"

    for m in [d, d - 1]:
        if ans != "-1" or m <= 0:
            break
        L = (m + 1) // 2
        X = int(s[:L]) if m == d else int("9" * L)

        for i in range(15):
            for j in range(12):
                Y = X - i - j * (10 ** (L - 1))
                if Y < 10 ** (L - 1) and Y != 0:
                    continue

                sY = str(Y)
                if m % 2 == 0:
                    pal = int(sY + sY[::-1])
                else:
                    pal = int(sY + sY[:-1][::-1])

                if pal <= n and (n - pal) % 12 == 0:
                    ans = f"{pal} {n - pal}"
                    break
            if ans != "-1":
                break

    if ans == "-1" and n % 12 == 0:
        ans = f"0 {n}"

    print(ans)