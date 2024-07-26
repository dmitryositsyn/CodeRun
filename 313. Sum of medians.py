#  313. Сумма медиан

import heapq

N = int(input())
mas = list(map(int, input().split()))

if N == 1:
    print(mas[0])
else:
    ans = 0
    heap_min = []
    heap_max = []
    heapq.heappush(heap_max, -mas[0])
    ans += mas[0]
    for i in range(1, len(mas)):
        if mas[i] > -heap_max[0]:
            heapq.heappush(heap_min, mas[i])
            if len(heap_min) > len(heap_max):
                tmp = heapq.heappop(heap_min)
                heapq.heappush(heap_max, -tmp)
        else:
            heapq.heappush(heap_max, -mas[i])
            if len(heap_max)-1 > len(heap_min):
                tmp = -heapq.heappop(heap_max)
                heapq.heappush(heap_min, tmp)
        ans -= heap_max[0]
    print(ans)
