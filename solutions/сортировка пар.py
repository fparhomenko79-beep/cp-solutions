def f(n, sour, to, help):
    if n == 0:
        return

    f(n - 1, sour, help, to)
    print(f"{n} {sour} {to}")
    f(n - 1, help, to, sour)

f(int(input()), 1, 3, 2)











