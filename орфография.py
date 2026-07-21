string = input()
n = len(string)

ans = ["None"] * n

def f(l, r, i):
    if l > r:
        return i
    ans[(l + r) // 2] = string[i]
    i += 1
    i = f(l, ((l + r) // 2) - 1, i)
    i = f(((l + r) // 2) + 1, r, i)
    return i

f(0, n - 1, 0)
print("".join(map(str, ans)))