n = int(input())

def f(o, l, path):
    if o == 0:
        print(*path)

    for i in range(min(o, l), 0, -1):
        path.append(i)
        f(o - i, i, path)
        path.pop()

f(n, n, [])