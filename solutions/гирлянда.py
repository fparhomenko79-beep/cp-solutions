n, k, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

colors = [0] * (n + 1)

def f(v):
    if v > n:
        return 1

    w = 0
    for i in range(1, k + 1):
        flag = True

        for to in graph[v]:
            if colors[to] == i:
                flag = False
                break

        if flag:
            colors[v] = i
            w += f(v + 1)
            colors[v] = 0
    return w

print(f(1))