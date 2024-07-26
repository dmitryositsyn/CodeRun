#  360. Частый элемент

N = int(input())
numbers = list(map(int, input().split()))
d = {}

for number in numbers:
    if number not in d:
        d[number] = 0
    d[number] += 1

max_count = max([d[key] for key in d.keys()])
max_number = -1
for key in d.keys():
    if d[key] == max_count and key >= max_number:
        max_number = key
print(max_number)