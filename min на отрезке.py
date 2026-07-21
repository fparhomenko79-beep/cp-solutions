from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([0])

for i in range(1, k):
    while que and arr[i] <= arr[que[-1]]:
        que.pop()
    que.append(i)

print(arr[que[0]], end=" ")

for i in range(k, n):
    if que and que[0] < i - k + 1:
        que.popleft()

    while que and arr[i] <= arr[que[-1]]:
        que.pop()
    que.append(i)

    print(arr[que[0]], end=" ")




