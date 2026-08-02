q, m = map(int, input().split())

for _ in range(q):
    a, b = input().split()
    a = a.zfill(len(b))
    a = list(map(int, a))
    b = list(map(int, b))

    dp = {(1, 1, 0): 1}

    for i in range(len(a)):
        new = {}

        for (low, high, rem), prod in dp.items():
            if low:
                left_num = a[i]
            else:
                left_num = 0

            if high:
                right_num = b[i]
            else:
                right_num = 9

            for j in range(left_num, right_num + 1):
                new_low = 1 if (low and j == a[i]) else 0
                new_high = 1 if (high and j == b[i]) else 0

                new_rem = (rem + j) % m

                if j > 0:
                    new_prod = prod * j
                else:
                    new_prod = prod

                sost = (new_low, new_high, new_rem)

                if sost not in new:
                    new[sost] = new_prod
                else:
                    new[sost] = max(new[sost], new_prod)

        dp = new
    ans = 0

    for (low, high, rem), prod in dp.items():
        if rem == 0:
            ans = max(ans, prod)
    print(ans)