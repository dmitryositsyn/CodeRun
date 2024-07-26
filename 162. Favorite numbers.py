#  162. Любимые числа
#  У Саши есть три любимых числа: 5,6,10. Кроме них, у Саши есть число N, не содержащее нулей.
#  Он хочет сделать так, чтобы оно делилось хотя бы на одно из его любимых чисел. Для этого он 
#  K раз выполняет следующее: случайно выбирает две цифры, стоящие на разных позициях, и меняет
#  их местами. Помогите Саше найти вероятность того, что итоговое число
#  будет делиться хотя бы на одно из любимых чисел.

N = int(input())
K = int(input())

current = N
l = 0
suitable_numbers = 0
fives = 0
even_numbers = 0
sum_of_numbers = 0
while current > 0:
    tmp = current % 10
    sum_of_numbers += tmp
    l += 1
    if tmp == 5:
        fives += 1
    elif tmp % 2 == 0:
        even_numbers += 1
    current //= 10

if sum_of_numbers % 3 == 0:
    suitable_numbers = fives + even_numbers
else:
    suitable_numbers = fives

dp1 = [0 for _ in range(K+1)]  #
dp2 = [0 for _ in range(K+1)]  #
last = N % 10
if sum_of_numbers % 3 == 0:
    if last % 5 == 0 or last % 2 == 0:
        dp1[0] = 1
    else:
        dp2[0] = 1
else:
    if last % 5 == 0:
        dp1[0] = 1
    else:
        dp2[0] = 1
for k in range(1, K+1):
    dp1[k] = dp1[k-1]*(((l-1)*(l-2))//2) + dp1[k-1]*(suitable_numbers-1) + dp2[k-1]*suitable_numbers
    dp2[k] = dp1[k-1] * (l-suitable_numbers) + dp2[k-1]*(((l-1)*(l-2))//2) + dp2[k-1]*(l-suitable_numbers-1)

#print(dp1)
#print(dp2)
print(dp1[K]/(dp1[K] + dp2[K])) 