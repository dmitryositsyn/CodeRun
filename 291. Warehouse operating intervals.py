#  291. Интервалы работы складов

import sys
import re


mas = []
types = ['KGT', 'COLD', 'OTHER']
for line in sys.stdin:
    if line == '':
        break
    i, date, t = map(str, line.strip().split(','))
    date1, date2 = map(str, date.split())
    if t == 'NULL':
        for tmp in types:
            mas.append((i, date1, date2, tmp))
    else:
        mas.append((i, date1, date2, t))
    
    
mas = sorted(mas)
ans = []
ignored_indices = set()
for i in range(len(mas)):
    if i not in ignored_indices:
        a = mas[i][1]
        b = mas[i][2]
        for j in range(i+1, len(mas)):
            if j not in ignored_indices:
                if mas[i][0] == mas[j][0] and mas[i][3] == mas[j][3]:
                    if a <= mas[j][1] <= b:
                        b = max(mas[j][2], b)
                        ignored_indices.add(j)
        ans.append((mas[i][0], a, b, mas[i][3]))
ans = sorted(ans, key=lambda x: (x[0], (x[3] != 'KGT', x[3] != 'COLD', x[3]!='OTHER'), x[1], x[2]))
for current in ans:
    print(current[0], end=',')
    print(current[1], end=' ')
    print(current[2], end=',')
    print(current[3])
