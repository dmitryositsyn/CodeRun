#  251. Набор символов

string = input()
s = set(input())
d = {}
l = r = 0
min_len = 101
while l < len(string):
    if not set(d.keys()).issuperset(s) and r < len(string):
        if string[r] not in d:
            d[string[r]] = 0
        d[string[r]] += 1
        r += 1
    elif set(d.keys()).issuperset(s):
        if set(d.keys()) == s:
            if r - l < min_len:
                min_len = r - l
        d[string[l]] -= 1
        if d[string[l]] == 0:
            d.pop(string[l])
        l += 1
    elif not set(d.keys()).issuperset(s) and r == len(string):
        break

if min_len < 101:
    print(min_len)
else:
    print(0)