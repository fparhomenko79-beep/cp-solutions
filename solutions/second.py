from sys import stdin, stdout; input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    stdout.write(f"{res}\n")