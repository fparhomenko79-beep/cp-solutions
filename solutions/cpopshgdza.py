q = int(input())

for _ in range(q):
    a, b = input().split()

    a = a.zfill(len(b))

    a = list(map(int, a))
    b = list(map(int, b))

    dp = {(1, 1, 0): 1}

    for i in range(len(a)):
        new = {}

        for (low, high, flag), proizv in dp.items():
            if low:
                left_num = a[i]
            else:
                left_num = 0

            if high:
                right_num = b[i]
            else:
                right_num = 9

            for j in range(left_num, right_num + 1):
                new_low = low and j == a[i]
                new_high = high and j == b[i]

                if flag:
                    new_flag = 1
                    new_proizv = proizv * j
                else:
                    if j == 0:
                        new_flag = 0
                        new_proizv = proizv
                    else:
                        new_flag = 1
                        new_proizv = proizv * j

                sost = (new_low, new_high, new_flag)

                if sost not in new:
                    new[sost] = new_proizv
                else:
                    new[sost] = max(new[sost], new_proizv)

        dp = new

    ans = 0

    for (low, high, flag), proizv in dp.items():
        if flag:
            ans = max(ans, proizv)

    print(ans)
