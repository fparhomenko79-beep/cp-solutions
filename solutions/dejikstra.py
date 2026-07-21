from collections import deque

num = input()
target = input()

que = deque()
que.append((num, 1))

parent = {num: -1}
visited = set()
visited.add(num)

while que:
    v, cnt = que.popleft()

    if v == target:
        print(cnt)

        path = []
        while target != num:
            path.append(target)
            target = parent[target]
        path.append(num)
        for i in range(len(path) -1, -1, -1):
            print(path[i])
        break

    pos_chan = [f"{v[1:4]}{v[0]}", f"{v[3]}{v[0:3]}"]
    if int(v[0]) != 9:
        pos_chan.append(f"{int(v[0]) + 1}{v[1:4]}")
    if int(v[3]) != 1:
        print(v)
        pos_chan.append(f"{v[0:3]}{int(v[3]) - 1}")

    for to in pos_chan:
        if to not in visited:
            visited.add(to)
            parent[to] = v
            que.append((to, cnt + 1))