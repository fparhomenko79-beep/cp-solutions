n = int(input())

pd = []
for _ in range(n):
    pd.append([])
    for _ in range(4):
        pd[-1].append(input())

pd = sorted(pd, key=lambda x: (x[2], x[0]))

for i in range(n):
    print(pd[i][2], pd[i][0], pd[i][1], pd[i][3])

