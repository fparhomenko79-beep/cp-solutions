n = int(input())

def f(m, s):
    if m == 0:
        print(s)
        return

    if not s:
        for i in "([":
            f(m - 1, i)
        return

    opened = []
    for i in s:
        if i == "(" or i == "[":
            opened.append(i)
        elif i == ")" and opened[-1] == "(":
            opened.pop()
        elif i == "]" and opened[-1] == "[":
            opened.pop()

    if not opened:
        f(m - 1, s + "(")
        f(m - 1, s + "[")
        return
    if len(opened) < m:
        f(m - 1, s + "(")
        f(m - 1, s + "[")
    if opened[-1] == "(":
        f(m - 1, s + ")")
    if opened[-1] == "[":
        f(m - 1, s + "]")
f(n, "")

