n = int(input())
prime_mn = []
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime_mn.append([i, 0])
        while n % i == 0:
            n //= i
            prime_mn[-1][1] += 1

if n != 1:
    prime_mn.append([n, 1])

for i in prime_mn:
    print(f"{i[0]}^{i[1]}", end=" ")

print()
print(f"количество = {sum(i[1] for i in prime_mn)}")