#  336. Иван и opensource

import re


n = int(input())
black_list = set()
for _ in range(n):
    name = input()
    black_list.add(name)

m = int(input())
paths = []
for _ in range(m):
    path = input()
    for name in black_list:
        if path.startswith(name):
            paths.append(path)
            break

q = int(input())
for _ in range(q):
    query = input()
    ans = 0
    d = {}
    for path in paths:
        if path.startswith(query):
            p, dot, ext = re.split(r'([.])', path)
            dot_ext = dot + ext
            if dot_ext not in d:
                d[dot_ext] = 0
                ans += 1
            d[dot_ext] += 1
    print(ans)
    for dot_ext in d:
        print(dot_ext + ': ' + str(d[dot_ext]))
