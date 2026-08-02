q = int(input())

for _ in range(q):
    a, b = input().split()
    a = a.zfill(len(b))
    a = list(map(int, a))
    b = list(map(int, b))

    dp = {(1, 1, 0, 0): 0}

    for i in range(len(a)):
        new = {}

        for (low, high, started, is_even_pos), score in dp.items():
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

                if started:
                    new_started = 1
                    if is_even_pos and (j % 2 == 0):
                        new_score = score + 1
                    else:
                        new_score = score

                    new_is_even_pos = 1 - is_even_pos
                else:
                    if j == 0:
                        new_started = 0
                        new_is_even_pos = 0
                        new_score = score
                    else:
                        new_started = 1
                        new_is_even_pos = 1
                        new_score = score

                sost = (new_low, new_high, new_started, new_is_even_pos)

                if sost not in new:
                    new[sost] = new_score
                else:
                    new[sost] = max(new[sost], new_score)

        dp = new

    ans = 0

    for (low, high, started, is_even_pos), score in dp.items():
        if started:
            ans = max(ans, score)
    print(ans)