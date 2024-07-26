#  222. Тимбилдинг

import queue

n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [False] * (n+1)
components_count = 0
components = [[] for _ in range(n)]
q = queue.Queue()

for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        components_count += 1
        q.put(i)
        while not q.empty():
            v = q.get()
            components[components_count-1].append(v)
            for neig in graph[v]:
                if visited[neig] == False:
                    visited[neig] = True
                    q.put(neig)

q.queue.clear()
visited.clear()
if components_count >= 3:
    print(-1)
elif components_count == 2:
    flag = False
    edges1 = len(graph[components[0][0]])
    for v in components[0]:
        if len(graph[v]) != edges1:
            flag = True
    
    edges2 = len(graph[components[1][0]])
    for v in components[1]:
        if len(graph[v]) != edges2:
            flag = True
    
    if flag:
        print(-1)
    else:
        print(len(components[0]))
        for v in components[0]:
            print(v, end=' ')
        print()
        for v in components[1]:
            print(v, end=' ')
	
elif components_count == 1:
    components.clear()
    for i in range(1, n+1):
        graph[i].add(i)
    #agraph = [set() for _ in range(n+1)]
    #for i in range(1, n+1):
    #    for node in range(1, n+1):
    #        if node not in graph[i]:
    #            agraph[i].add(node)
    #    graph[i].clear()
    #graph.clear()
    flag = False
    mas = [-1 for _ in range(n+1)]
    q1 = queue.Queue()
    for i in range(1, n+1):
        if mas[i] == -1:
            q1.put(i)
            mas[i] = 1
            while not q1.empty():
                current = q1.get()
                for neig in range(1, n+1):
                    if neig not in graph[current]:
                        if mas[neig] == -1:
                            q1.put(neig)
                            if mas[current] == 1:
                                mas[neig] = 2
                            else:
                                mas[neig] = 1
                        elif mas[current] == mas[neig]:
                            flag = True
                            break
    q1.queue.clear()
    if flag:
        print(-1)
    else:
        ans1 = []
        ans2 = []
        for i in range(1, n+1):
            if mas[i] == 1:
                ans1.append(i)
            else:
                ans2.append(i)
        if len(ans1) == n:
            print(n-1)
            for i in range(1, n):
                print(i, end=' ')
            print()
            print(n)
        else:
            print(len(ans1))
            for i in ans1:
                print(i, end=' ')
            print()
            for i in ans2:
                print(i, end=' ')