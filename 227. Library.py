#  227. Библиотека

k, m, d = map(int, input().split())
days = 0

cur = 1
total = m

def every_day(cur, total, days):
    d = 1
    while total >= 0:
        if d<=5:
            total += k
        total -= cur
        
        d = (d%7) + 1
        days += 1
        cur += 1
    return days - 1


def every_week(cur, total, days):
    while total >= 0:
        total += 5*k
        total -= 7*cur + 21
        cur += 7
        days += 7
    if total < 0:
        days -= 7
        cur -= 7
        total += 7*cur + 21
        total -= 5*k
        return every_day(cur, total, days)

def every_month(cur, total, days):
    while total >= 0:
        total += 20*k
        total -= 28*cur + 378
        cur += 28
        days += 28
    if total < 0:
        days -= 28
        cur -= 28
        total += 28*cur + 378
        total -= 20*k
        return every_week(cur, total, days)

def every_year(cur, total, days):
    while total >= 0:
        total += 240*k
        total -= 336*cur + 56280
        cur += 336
        days += 336
    if total < 0:
        days -= 336
        cur -= 336
        total += 336*cur + 56280
        total -= 240*k
        return every_month(cur, total, days)

def every_10_years(cur, total, days):
    while total >= 0:
        total += 2400*k
        total -= 3360*cur + 5643120
        cur += 3360
        days += 3360
    if total < 0:
        days -= 3360
        cur -= 3360
        total += 3360*cur + 5643120
        total -= 2400*k
        return every_year(cur, total, days)
        


if d==1:
    print(every_10_years(cur, total, days))
else:
    while total >= 0:
        if d<=5:
            total += k
        total -= cur
        
        d = (d%7) + 1
        days += 1
        cur += 1
        if d == 1:
            break
    if total < 0:
        print(days-1)
    else:
        print(every_10_years(cur, total, days))