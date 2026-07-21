n = int(input())
arr = list(map(int, input().split()))
cur, ans = arr[0], arr[0]

for i in range(1, n):
    if arr[i] > cur + arr[i]:
        cur = arr[i]
    else: 
        cur += arr[i]
    ans = max(ans, cur)
    
print(ans)