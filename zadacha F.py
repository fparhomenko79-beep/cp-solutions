n = int(input())

prime = [True] * 1000
prime[0] = prime[1] = False

for p in range(2, 1000):
    if prime[p]:
        for i in range(p * p, 1000, p):
            prime[i] = False

dp = [0] * 100

for i in range(100, 1000):
    num = str(i)
    num_last_2 = int(num[-2] + num[-1])
    if prime[i]:
        dp[num_last_2] += 1

for i in range(4, n + 1):
    new = [0] * 100
    for num in range(100, 1000):
            if prime[num]:
                new[num % 100] += dp[int(str(num)[:2])]
                new[num % 100] %= (10**9 + 9)
    dp = new

print(sum(dp) % (10 ** 9 + 9))