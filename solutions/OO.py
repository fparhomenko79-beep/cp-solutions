from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inv = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    inv[v] += 1

que = deque()
order = []

for i in range(1, n + 1):
    if not inv[i]:
        que.append(i)

while que:
    v = que.popleft()
    order.append(v)

    for to in graph[v]:
        inv[to] -= 1
        if not inv[to]:
            que.append(to)

if len(order) == n:
    print(*order)
else:
    print(-1)