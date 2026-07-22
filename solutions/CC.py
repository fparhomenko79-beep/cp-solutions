from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

que = deque()

for i in range(n):
    while que and que[0] < i - k + 1:
        que.popleft()
    while que and a[i] <= a[que[-1]]:
        que.pop()
    que.append(i)
    if i >= k - 1:
        print(a[que[0]], end=" ")

