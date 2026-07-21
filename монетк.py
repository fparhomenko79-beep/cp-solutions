n, k = map(int, input().split())
coin = {i: 2 for i in map(int, input().split())}

def f(coin, s):
    if s == k:
        return True

    for nom, cnt in coin.items():
        if cnt > 0:
            coin[nom] -= 1

            if f(coin, s + nom):
                return True

            coin[nom] += 1
    return False

print("YES" if f(coin, 0) else "NO")