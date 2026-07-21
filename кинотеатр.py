def gcd(a, b):
    if b == 0:
        return a
    a, b = b, a % b
    return gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))