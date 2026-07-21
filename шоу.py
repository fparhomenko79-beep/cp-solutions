n = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
ans = float("inf")

def f(m, i, last, cur):
    global ans
    if m == 1:
        ans = min(ans, cur)
        return
    
    if i == len(primes):
        return

    for k in range(last, 1, -1):
        if m % k == 0:
            f(m // k, i + 1, k, cur * primes[i] ** (k - 1))

f(n, 0, n, 1)

print(ans if ans <= 10 ** 9 else 0)
