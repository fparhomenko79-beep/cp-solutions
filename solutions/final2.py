n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())