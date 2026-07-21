n = int(input())
a = list(map(int, input().split()))

pref = [0]
for i in range(n):
    pref.append(pref[-1] + a[i])

total = pref[n]
min_pref = pref[1]
idx_min_pref = 1# длина первого круга
idx_pl = -1
min_pref_positive = -1
idx_min_pref_positive = -1
f = False

if pref[1] > 0:
    idx_min_pref_positive = 1
    idx_pl = 1
    min_pref_positive = pref[1]

for i in range(2, n):
    if min_pref_positive != -1 and pref[i] > min_pref_positive:
        j = idx_min_pref_positive
        print(j, i - j, n - i)
        f = True
        break

    if idx_pl != -1 and total - pref[i] > 0:
        j = idx_pl
        print(j, i - j, n - i)
        f = True
        break

    if pref[i] > min_pref and total - pref[i] > 0:
        j = idx_min_pref
        print(j, i - j, n - i)
        f = True
        break

    if pref[i] < min_pref:
        min_pref = pref[i]
        idx_min_pref = i

    if pref[i] > 0:
        idx_pl = i
        if min_pref_positive == -1 or pref[i] < min_pref_positive:
            min_pref_positive = pref[i]
            idx_min_pref_positive = i

if not f:
    print(0)