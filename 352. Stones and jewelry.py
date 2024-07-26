#  352. Камни и украшения

s = set(input())
string = input()
ans = 0
for el in string:
    if el in s:
        ans += 1
print(ans)