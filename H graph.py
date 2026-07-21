n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n):
    s = input()
    for j in range(len(s)):
        graph[i].append((i + j + 1, s[j]))

R = [set() for _ in range(n + 1)]
B = [set() for _ in range(n + 1)]

for v in range(n - 1, 0, -1):
    for to, col in graph[v]:
        if col == "R":
            R[v].add(to)
            R[v].update(R[to])
        elif col == "B":
            B[v].add(to)
            B[v].update(B[to])

    if R[v] & B[v]:
        print("YES")
        exit()

print("NO")


