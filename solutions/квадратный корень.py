n, dst = int(input()), {}
for _ in range(n):
    a, b = input().split()
    dst[a], dst[b] = b, a
print(dst[input()])