#  324. Много стульев

N, M = map(int, input().split())
purchase_prices = list(map(int, input().split()))
selling_prices = list(map(int, input().split()))
ans = 0
for pp, sp in zip(sorted(purchase_prices), reversed(sorted(selling_prices))):
    if sp-pp > 0:
        ans += (sp-pp)
    else:
        break
print(ans)