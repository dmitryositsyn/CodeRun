#  381. Форматирование календаря

nDays, weekday = map(str, input().split())
nDays = int(nDays)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_to_idx = {}
for i, day in enumerate(days):
    day_to_idx[day] = i

last_idx = day_to_idx[weekday]
for i in range(last_idx):
    print('..', end=' ')
last_num = 1
for i in range(last_idx, 7):
    print(str('.') + str(last_num), end=' ')
    last_num += 1
print()
is_enter = 0
while last_num != nDays+1:
    if last_num // 10 == 0:
        print(str('.') + str(last_num), end=' ')
    else:
        print(last_num, end=' ')
    last_num += 1
    is_enter += 1
    if is_enter == 7:
        is_enter = 0
        print()
