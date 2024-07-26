#  260. Телефонные номера

N = int(input())
digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
phone_numbers = []
for i in range(N):
    current = input()
    number = []
    for sym in current:
        if sym in digits:
            number.append(sym)
    phone_numbers.append(''.join(number))
M = int(input())
d = {}
for _ in range(M):
    template, country_and_operator = map(str, input().split('-'))
    d[template] = country_and_operator

for number in phone_numbers:
    #print()
    #print(number)
    result = ''
    for template in d.keys():
        flag = True
        idx = 0
        #print(template)
        for sym in template:
            if sym in digits:
                if sym == number[idx]:
                    idx += 1
                else:
                    #print(sym, idx)
                    flag = False
                    break
            elif sym == 'X':
                idx += 1
        #print(flag)
        if idx == len(number) and flag:
            i = 0
            for sym in template:
                if sym in digits:
                    print(sym, end='')
                    i += 1
                elif sym == 'X':
                    print(number[i], end='')
                    i += 1
                else:
                    print(sym, end='')
            print('-', end='')
            print(d[template])
            break
