from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

color = [0] * (n + 1)
color[1] = 1
que = deque()
que.append(1)

res = True
while que:
    v = que.popleft()

    for to in graph[v]:
        if color[to] == 0:
            que.append(to)
            color[to] = 3 - color[v]
        elif color[to] == color[v]:
            res = False
        else:
            continue

print("YES" if res else "NO")