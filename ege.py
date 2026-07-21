with open("ege/26.txt", "r") as file:
    n = int(file.readline())
    arr = [int(line.strip()) for line in file.readlines()]

maxi = 0
count = 0
for i in range(n - 1):
    x, y = arr[i], arr[i + 1]

    mean = (x + y) / 2

    if x % 2 == 0 and y % 2 == 0:
        mean = int(mean)
    else:
        continue

    print(mean in arr)

    maxi = max(maxi, mean)
    count += 1

print(count, maxi)