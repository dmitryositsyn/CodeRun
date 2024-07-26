#  204. Ошибка

n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

total = 0
ans = []
for i in range(n):
    tmp = a[i]*b[i]
    ans.append(tmp)
    total += tmp

for i in range(n):
    print(ans[i]/total)