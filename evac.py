from collections import deque
from sys import stdin, stdout; input = stdin.readline

n = int(input())
k = int(input())
exits = sorted(list(map(int, input().split())))
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

time = [-1] * (n + 1)
closest = [-1] * (n + 1)

que = deque()

for ex in exits:
    time[ex] = 0
    closest[ex] = ex
    que.append(ex)

while que:
    v = que.popleft()

    for to in graph[v]:
        if time[to] == -1:
            time[to] = time[v] + 1
            closest[to] = closest[v]
            que.append(to)

stdout.write(" ".join(map(str, time[1:])) + "\n")
stdout.write(" ".join(map(str, closest[1:])) + "\n")