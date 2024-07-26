#  317. Карты

import math


N = int(input())
a, b, c = map(int, input().split())
S1 = (N*(N+1))//2
S2 = (N*(N+1)*(2*N+1))//6
S3 = ((N**2)*((N+1)**2))//4

A = S1 - a
B = (A**2 + b - S2)//2
C = ((S3-c) - A*((S2-b) - B))//3

for z in range(1, N+1):
    D = (C - B*z)**2 - 4*C*(z**3)
    if D>=0:
        y = int(((B*z - C) + math.sqrt((C - B*z)**2 - 4*C*(z**3)))/(2*(z**2)))
        x = int(C/(y*z))
        if (x + y + z == A) and (x*y + y*z + x*z == B) and (x*y*z == C):
            print(x, y, z)
            break