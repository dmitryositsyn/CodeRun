#  309. Модель молекулы

N, M = map(int, input().split())
dc = {}
di = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if (a, b) not in dc:
        dc[(a, b)] = 0
    dc[(a, b)] += 1
    di.append((a, b))

Q = int(input())
ld = list(map(int, input().split()))
for i in ld:
    dc[di[i-1]] -= 1
    if dc[di[i-1]] == 0:
        dc.pop(di[i-1])

components = [i for i in range(N)]

def parent(a, components):
    if a == components[a]:
        return a
    else:
        indices = [a]
        temp_par = parent(components[indices[-1]], components)
        while indices[-1] != temp_par:
            indices.append(temp_par)
            temp_par = parent(indices[-1], components)
        for i in indices:
            components[i] = indices[-1]
        return components[a]

def draw_an_edge(a, b, components):
        parent_a = parent(a, components)
        parent_b = parent(b, components)
        if parent_a != parent_b:
            components[parent_b] = parent_a
            return False
        else:
            return True

counter = N
for a, b in dc:
    if not draw_an_edge(a, b, components):
        counter -= 1
ans = [counter]
for i in reversed(ld):
    if i != ld[0]:
        if not draw_an_edge(*di[i-1], components):
            counter -= 1
        ans.append(counter)

for i in reversed(ans):
    print(i, end=' ')
