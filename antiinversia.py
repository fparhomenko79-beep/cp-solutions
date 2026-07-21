n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        ans += n - i

print(ans)