def gcde(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcde(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

a, b, c = map(int, input().split())

g, x0, y0 = gcde(a, b)

if c % g != 0:
    print("impossible")
else:
    f = c // g
    x = x0 * f
    y = y0 * f
    print(g, x, y)


