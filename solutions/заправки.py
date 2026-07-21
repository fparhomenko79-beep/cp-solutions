import heapq

n = int(input())
values = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph[0].append(1)

cost = [[float("inf"), float("inf")] for i in range(n + 1)]
cost[1][0] = 0

heap = []
heapq.heappush(heap, (0, 1, 0))

while heap:
    c, v, k = heapq.heappop(heap)

    if c != cost[v][k]:
        continue

    for to in graph[v]:
       if k == 0:
           if c + values[v - 1] < cost[to][0]:
               cost[to][0] = c + values[v - 1]
               heapq.heappush(heap, (c + values[v - 1], to, 0))
           if c + values[v - 1] * 2 < cost[to][1]:
               cost[to][1] = c + values[v - 1] * 2
               heapq.heappush(heap, (c + values[v - 1] * 2, to, 1))

       else:
           if c < cost[to][0]:
               cost[to][0] = c
               heapq.heappush(heap, (c, to, 0))
           if c + values[v - 1] < cost[to][1]:
               cost[to][1] = c + values[v - 1]
               heapq.heappush(heap, (c + values[v - 1], to, 1))

print(min(cost[n][1], cost[n][0]))