#  176. День рождения Васи

import math 


n = int(input())
dishes = []
for i in range(n):
    d_i, c_i, z_i = map(str, input().split())
    c_i = int(c_i)
    z_i = int(z_i)
    ingredients_i = {}
    for j in range(z_i):
        s_ij, a_ij, u_ij = map(str, input().split())
        a_ij = int(a_ij)
        if u_ij == 'tens':
            a_ij *= 10
            u_ij = 'cnt'
        elif u_ij == 'kg':
            a_ij *= 1000
            u_ij = 'g'
        elif u_ij == 'l':
            a_ij *= 1000
            u_ij = 'ml' 
        ingredients_i[s_ij] = (a_ij, u_ij)
    dishes.append((d_i, c_i, ingredients_i))

k = int(input())
first_d = {}
for i in range(k):
    t_i, p_i, a_i, u_i = map(str, input().split())
    p_i = int(p_i)
    a_i = int(a_i)
    if u_i == 'tens':
        a_i *= 10
        u_i = 'cnt'
    elif u_i == 'kg':
        a_i *= 1000
        u_i = 'g'
    elif u_i == 'l':
        a_i *= 1000
        u_i = 'ml'

    first_d[t_i] = (p_i, a_i, u_i)

total_cost = 0
ans_1 = {}

for ingredient in first_d.keys():
    ans_1[ingredient] = 0
    count_to_cook = 0
    count_to_buy = 0 
    for dish in dishes:
        if ingredient in dish[2]:
            count_to_cook += dish[1]*dish[2][ingredient][0]
    
    count_to_buy = math.ceil(count_to_cook / first_d[ingredient][1])
    ans_1[ingredient] = count_to_buy
    total_cost += count_to_buy * first_d[ingredient][0]

m = int(input())
second_d = {}
for i in range(m):
    t_i, a_i, u_i, pr_i, f_i, ch_i, fv_i = map(str, input().split())
    a_i = int(a_i)
    if u_i == 'tens':
        a_i *= 10
        u_i = 'cnt'
    elif u_i == 'kg':
        a_i *= 1000
        u_i = 'g'
    elif u_i == 'l':
        a_i *= 1000
        u_i = 'ml'
    pr_i = float(pr_i)
    f_i = float(f_i)
    ch_i = float(ch_i)
    fv_i = float(fv_i)
    second_d[t_i] = (1, u_i, pr_i/a_i, f_i/a_i, ch_i/a_i, fv_i/a_i)

ans_2 = {}
for dish in dishes:
    d_pr_i = 0
    d_f_i = 0
    d_ch_i = 0
    d_fv_i = 0
    for ingredient in dish[2].keys():
        d_pr_i += dish[2][ingredient][0] * second_d[ingredient][2]
        d_f_i += dish[2][ingredient][0] * second_d[ingredient][3]
        d_ch_i += dish[2][ingredient][0] * second_d[ingredient][4]
        d_fv_i += dish[2][ingredient][0] * second_d[ingredient][5]
    ans_2[dish[0]] = (d_pr_i, d_f_i, d_ch_i, d_fv_i)
print(total_cost)
for key in ans_1:
    print(key, ans_1[key])
for key in ans_2:
    print(key, ans_2[key][0], ans_2[key][1], ans_2[key][2], ans_2[key][3])