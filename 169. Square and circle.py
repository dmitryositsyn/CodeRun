#  169. Квадрат и окружность

#  У Васи есть квадрат, вершины которого расположены в точках с координатами 
#  (0, 0), (0, 1), (1, 0), (1, 1).
#  В этом квадрате расположены N фишек, i-я фишка имеет координаты (x_i, y_i).
#  Фишки имеют пренебрежительно малые размеры, будем считать их материальными точками. 
#  Вася играет в игру. Он выбирает случайную точку с равномерным распределением в своем квадрате.
#  Потом Вася подсчитывает количество фишек, расстояние от которых до выбранной точки не превышает 
#  R, и получает соответствующее количество очков. 
#  Помогите Васе узнать математическое ожидание количества очков, которые он наберёт в описанной выше игре.

import math
N, R = map(float, input().split())
N = int(N)
chips = []
for i in range(N):
    xi, yi = map(float, input().split())
    chips.append((xi, yi))

def intersection(xi, yi, x, y):
    dx = abs(x-xi)
    dy = abs(y-yi)
    if dx**2 + dy**2 <= R**2:
        return dx*dy
    else:
        x0, y0 = 0, 0
        A = []
        B = []
        if dx < R and dy < R:
            if x == 0 and y == 0:
                x0 = xi - math.sqrt(R**2 - yi**2)
                y0 = yi - math.sqrt(R**2 - xi**2)
                A = [x0, 0]
                B = [0, y0]
            elif x == 1 and y == 0:
                x0 = xi + math.sqrt(R**2 - yi**2)
                y0 = yi - math.sqrt(R**2 - (1-xi)**2)
                A = [x0, 0]
                B = [1, y0]
            elif x == 0 and y == 1:
                x0 = xi - math.sqrt(R**2 - (1-yi)**2)
                y0 = yi + math.sqrt(R**2 - xi**2)
                A = [x0, 1]
                B = [0, y0]
            elif x == 1 and y == 1:
                x0 = xi + math.sqrt(R**2 - (1-yi)**2)
                y0 = yi + math.sqrt(R**2 - (1-xi)**2)
                A = [x0, 1]
                B = [1, y0]

            a = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
            half_alpha = math.asin((a/2)/R)
            sector = R**2 * half_alpha
            return (0.5 * (dy*abs(xi-x0) + dx*abs(yi-y0)) + sector)
        elif dx < R and dy >= R:
            y0 = 0
            A = []
            B = []
            if x == 0 and y == 0:
                y0 = yi - math.sqrt(R**2 - xi**2)
                A = [xi, yi-R]
                B = [0, y0]
            elif x == 1 and y == 0:
                y0 = yi - math.sqrt(R**2 - (1-xi)**2)
                A = [xi, yi-R]
                B = [1, y0]
            elif x == 0 and y == 1:
                y0 = yi + math.sqrt(R**2 - xi**2)
                A = [xi, yi+R]
                B = [0, y0]

            elif x == 1 and y == 1:
                y0 = yi + math.sqrt(R**2 - (1-xi)**2)
                A = [xi, yi+R]
                B = [1, y0]
            
            a = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
            half_alpha = math.asin((a/2)/R)
            sector = R**2 * half_alpha

            return (0.5*(dx*abs(yi-y0)) + sector)
        elif dx >= R and dy < R:
            x0 = 0
            A = []
            B = []
            if x == 0 and y == 0:
                x0 = xi - math.sqrt(R**2 - yi**2)
                A = [x0, 0]
                B = [xi - R, yi]
            elif x == 1 and y == 0:
                x0 = xi + math.sqrt(R**2 - yi**2)
                A = [x0, 0]
                B = [xi + R, yi]
            elif x == 0 and y == 1:
                x0 = xi - math.sqrt(R**2 - (1-yi)**2)
                A = [x0, 1]
                B = [xi - R, yi]
            elif x == 1 and y == 1:
                x0 = xi + math.sqrt(R**2 - (1-yi)**2)
                A = [x0, 1]
                B = [xi + R, yi]
            
            a = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
            half_alpha = math.asin((a/2)/R)
            sector = R**2 * half_alpha
            return (0.5*(dy * abs(xi-x0)) + sector)
        elif dx >= R and dy >= R:
            return (math.pi*(R**2)/4)

def full_intersection(xi, yi):
    return intersection(xi, yi, 0, 0) + intersection(xi, yi, 1, 0) + \
         intersection(xi, yi, 0, 1) + intersection(xi, yi, 1, 1)

ans = 0
for chip in chips:
    ans += full_intersection(*chip)

print(ans)