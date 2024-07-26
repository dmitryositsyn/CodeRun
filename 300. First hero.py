#  300. Первый герой

import fractions

N = int(input())
polynomial_coefficients = [0]
multiplied = 0
mimimum = 0
if N == 1:
    a = int(input())
    if a%2 == 0:
        print(str(a//2) + '/' + str(1))
    else:
        print(str(a) + '/' + str(2))
elif N == 2:
    a, b = map(int, input().split())
    multiplied = a*b
    polynomial_coefficients.append(a+b)
    polynomial_coefficients.append(-1)
    mimimum = min(a, b)
elif N == 3:
    a, b, c = map(int, input().split())
    multiplied = a*b*c
    polynomial_coefficients.append(a*b + b*c + a*c)
    polynomial_coefficients.append(-(a + b + c))
    polynomial_coefficients.append(1)
    mimimum = min(a, b, c)
elif N == 4:
    a, b, c, d = map(int, input().split())
    multiplied = a*b*c*d
    polynomial_coefficients.append(a*b*c + a*b*d + a*c*d + b*c*d)
    polynomial_coefficients.append(-(a*b + a*c + a*d + b*c + b*d + c*d))
    polynomial_coefficients.append(a + b + c + d)
    polynomial_coefficients.append(-1)
    mimimum = min(a, b, c, d)
elif N == 5:
    a, b, c, d, e = map(int, input().split())
    multiplied = a*b*c*d*e
    polynomial_coefficients.append(a*b*c*d + a*b*c*e + a*b*d*e + a*c*d*e + b*c*d*e)
    polynomial_coefficients.append(-(a*b*c + a*b*d + a*b*e + a*c*d + a*c*e + a*d*e + b*c*d + b*c*e + b*d*e + c*d*e))
    polynomial_coefficients.append(a*b + a*c + a*d + a*e + b*c + b*d+ b*e + c*d + c*e + d*e)
    polynomial_coefficients.append(-(a + b + c + d + e))
    polynomial_coefficients.append(1)
    mimimum = min(a, b, c, d, e)

if N > 1:
    differentiated_polynomial_coefficients = []

    for i in range(1, len(polynomial_coefficients)):
        differentiated_polynomial_coefficients.append(polynomial_coefficients[i]*i)

    differentiated_polynomial_coefficients.insert(0, 0)
    integrated = [fractions.Fraction(0, 1)]
    for i in range(len(differentiated_polynomial_coefficients)):
        integrated.append(fractions.Fraction(differentiated_polynomial_coefficients[i], (i+1)*multiplied))

    ans = fractions.Fraction(0, 1)
    for i in range(1, len(integrated)):
        ans += (mimimum**i)*integrated[i]
    print(str(ans.numerator)+'/'+ str(ans.denominator))
