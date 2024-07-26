#  182. Закрытый ключ

import math

def factoring(n):
    d = {}
    cur = n
    for i in range(2, math.ceil(math.sqrt(n+1)) + 1):
        while cur % i == 0:
            if i not in d:
                d[i] = 0
            d[i] += 1
            cur //= i
    if cur != 1:
        d[cur] = 1
    return d

GCD, LCM = map(int, input().split())
ans = 1
if LCM % GCD != 0: 
    ans = 0
elif LCM == GCD:
    ans = 1
else:
    dGCD = factoring(GCD)
    dLCM = factoring(LCM)
    counter = 0
    for key in dLCM.keys():
        if key not in dGCD:
            counter += 1
        else:
            if dLCM[key] > dGCD[key]:
                counter += 1
    ans = 2**(counter)
print(ans)