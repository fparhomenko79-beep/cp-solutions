A, B = map(int, input().split())

primes = [True] * (B + 1)
primes[0] = primes[1] = False

for p in range(2, int(B ** 0.5) + 1):
    if primes[p]:
        for i in range(p * p, B + 1, p):
            primes[i] = False

arr = [i for i, is_prime in enumerate(primes) if is_prime and i >= A]

print(*arr)