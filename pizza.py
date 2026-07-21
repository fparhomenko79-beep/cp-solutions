t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    time = 1
    left, right = 0, n - 1

    while right - left > k:
        while arr[left] == 0:
            left += 1
        while arr[right] == 0:
            right -= 1

        if arr[left] < arr[right]:
            const = arr[left]
            arr[left] = 0
            arr[right] -= const
            left += 1

        elif arr[left] > arr[right]:
            const = arr[right]
            arr[right] = 0
            arr[left] -= const
            right -= 1

        else:
            const = arr[left]
            arr[left] = 0
            arr[right] = 0
            left += 1
            right -= 1

        time += const
    print(time)