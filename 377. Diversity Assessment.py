#  377. Оценка разнообразия

n = int(input())
d = {}
for _ in range(n):
    product_i, category_i = map(int, input().split())
    d[product_i] = category_i
order = list(map(int, input().split()))

cat_to_last_idx = {}
flag = False
ans = 100001
for i, product_id in enumerate(order):
    if d[product_id] in cat_to_last_idx:
        flag = True
        if i - cat_to_last_idx[d[product_id]] < ans:
            ans = i - cat_to_last_idx[d[product_id]]
    cat_to_last_idx[d[product_id]] = i

if not flag:
    print(n)
else:
    print(ans)
