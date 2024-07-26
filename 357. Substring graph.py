#  357. Граф подстрок

N = int(input())
ans = {}
for i in range(N):
    string = input()
    for i in range(0, len(string)-3):
        tmp_string = string[i:i+3]
        if tmp_string not in ans:
            ans[tmp_string] = {}
        if string[i+1:i+4] not in ans[tmp_string]:
            ans[tmp_string][string[i+1:i+4]] = 0
        ans[tmp_string][string[i+1:i+4]] += 1

set_of_node = set(ans.keys())
for key in ans.keys():
    set_of_node.update(set(ans[key].keys()))

print(len(set_of_node))

count_of_edge = 0
for key in ans.keys():
    count_of_edge += len(ans[key].keys())

print(count_of_edge)

for key1 in ans.keys():
    for key2 in ans[key1].keys():
        print(key1, key2, ans[key1][key2])