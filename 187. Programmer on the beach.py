#  187. Программист на пляже

N = int(input())
for i in range(N):
    n = int(input())
    numbers = sorted(list(map(int, input().split())))
    digits = {}
    for num in numbers:
        l = len(format(num, 'b'))
        if l not in digits:
            digits[l] = []
        digits[l].append(num)
    
    s = set()
    for key in digits.keys():
        if len(digits[key]) >= 2:
            s.add(key)
    ans = -1
    
    if len(s) == 0:
        keys = list(digits.keys())
        ans = digits[keys[0]][0] ^ digits[keys[1]][0]
    else:
        min_range = int(1e+10)
        ans = int(1e+10)
        for digit in s:
            l = digits[digit]
            for i in range(1, len(l)):
                if l[i] ^ l[i-1] < ans:
                    ans = l[i] ^ l[i-1]

    print(ans)