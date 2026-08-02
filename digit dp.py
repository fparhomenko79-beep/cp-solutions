q = int(input())

for _ in range(q):
    a, b = input().split()
    a = a.zfill(len(b))
    a = list(map(int, a))
    b = list(map(int, b))

    dp = {(1, 1): 0}

    for i in range(len(a)):
        new = {}

        for (low, high), current_sum in dp.items():
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

                new_sum = current_sum + j

                sost = (new_low, new_high)

                if sost not in new:
                    new[sost] = new_sum
                else:
                    new[sost] = max(new[sost], new_sum)

        dp = new

    ans = 0
    for current_sum in dp.values():
        ans = max(ans, current_sum)

    print(ans)