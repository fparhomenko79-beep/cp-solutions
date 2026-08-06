n, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

order = []
parent = [-1] * (n + 1)
visited = [False] * (n + 1)
visited[x] = True
que = deque()
que.append(x)

while que:
    v = que.popleft()
    order.append(v)
    for to, weight in graph[v]:
        if not visited[to]:
            que.append(to)
            visited[to] = True
            parent[to] = (v, weight)
order.reverse()

dp0 = [[float("inf") for _ in range(k + 1)] for _ in range(n + 1)]
dp1 = [[float("inf") for _ in range(k + 1)] for _ in range(n + 1)]

for v in order:
    dp0[v][1] = 0
    dp1[v][1] = 0

    cnt = 1

    for to, w in graph[v]:
        if parent[to] != v:
            continue

        new1 = [float("inf")] * (k + 1)
        new2 = [float("inf")] * (k + 1)

        for i in range(1, min(cnt, k) + 1):
            for j in range(1, k - i + 1):
                if dp0[to][j] == float("inf"):
                    continue

                new1[i + j] = min(new1[i + j], dp0[v][i] + dp0[to][j] + 2 * w)
                new2[i + j] = min(new2[i + j], dp1[v][i] + dp0[to][j] + 2 * w)
                new2[i + j] = min(new2[i + j], dp0[v][i] + dp1[to][j] + w)

        dp0[v] = new1
        dp1[v] = new2
        cnt = k
        
print(dp1[x][k])
