n = int(input())

count = 0
y = set()
diag1 = set()
diag2 = set()

def f(x):
    global count

    if x == n:
        count += 1
        return

    for i in range(n):
        if i in y or (x - i) in diag1 or (x + i) in diag2:
            continue

        y.add(i)
        diag1.add(x - i)
        diag2.add(x + i)

        f(x + 1)

        y.remove(i)
        diag1.remove(x - i)
        diag2.remove(x + i)

f(0)
print(count)