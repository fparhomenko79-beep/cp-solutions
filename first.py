t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    z = input()

    c10 = c01 = c11 = 0
    for sb, zb in zip(s, z):
        if sb == '1' and zb == '0':
            c10 += 1
        elif sb == '0' and zb == '1':
            c01 += 1
        elif sb == '1' and zb == '1':
            c11 += 1

    if k % 2 == 1:
        X0 = c10 + c11
        X1 = c10 + c01
        X2 = c01 + c11
    else:
        X0 = c10 + c11
        X1 = c01 + c11
        X2 = c10 + c01

    L = 1 << k
    cnt0 = (L - 0) // 3 + 1
    cnt1 = (L - 1) // 3 + 1
    cnt2 = (L - 2) // 3 + 1

    ans = (cnt0 * X0 * (n - X0) +
           cnt1 * X1 * (n - X1) +
           cnt2 * X2 * (n - X2))
    print(ans)


