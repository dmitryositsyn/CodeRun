#  344. Шашки

N, M = map(int, input().split())
w = int(input())
white = set()
for i in range(w):
    x, y = map(int, input().split())
    white.add((x,y))

b = int(input())
black = set()
for i in range(b):
    x, y = map(int, input().split())
    black.add((x, y))

color = input()

def check(color1, color2):
    directionx = [1, 1, -1, -1]
    directiony = [1, -1, -1, 1]
    for x, y in color1:
        for v1, v2 in zip(directionx, directiony):
            if ((x+v1, y+v2) in color2) and ((x+2*v1, y+2*v2) not in color2) and \
            ((x+2*v1, y+2*v2) not in color1) and (1 <= x+2*v1 <= N) and (1 <= y+2*v2 <= M):
                return True
    return False

ans = False
if color == 'white':
    ans = check(white, black)
elif color == 'black':
    ans = check(black, white)

if ans:
    print('Yes')
else:
    print('No')