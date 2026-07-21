n = int(input())
arr = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        if n // i == i:
            continue
        f = False
        for j in range(2, int(i**0.5)):

            continue
        arr.append(i)

arr.sort()
print(arr)
s = ""
p = 0
for i in arr:
    cof = 0
    while n % i == 0:
        n //= i
        cof += 1
    if cof > 1:
        if p == 0:
            s += f"{i}^{cof}"
        else:
            s += f"*{i}^{cof}"
    else:
        if p == 0:
            s += f"{i}"
        else:
            s += f"*{i}"

print(s)