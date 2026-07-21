n, k = map(int, input().split())
a = list(map(int, input().split()))

p = [0] * (n - 1)
for i in range(n - 1):
    if a[i] < a[i + 1]:
        p[i] = 1
print(*p)
ctom = 0
for i in range(k - 1):
    ctom += p[i]

best = ctom

for i in range(k - 1, n - 1):
    ctom -= p[i - k - 1]
    ctom += p[i]
    best = min(best, ctom)

print(best)




rgbwebreui
