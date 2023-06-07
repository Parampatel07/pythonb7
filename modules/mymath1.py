import math

print(math.ceil(10.1)) #largest integer

num1 = 10
num2 = -20
num1 = math.copysign(num1,num2)
print(num1)

num2 = math.fabs(num2)
print(num2)

answer = math.factorial(5)
print(answer)

answer = math.floor(10.2)
print(answer)

answer = math.fmod(7,3)
print(answer)

answer = math.isfinite(7/3)
print(answer)

number = float('inf')
print(number)
answer = math.isinf(number)
print(answer)

answer = float('nan')
print(answer)
print(math.isnan(answer))

a = 10
b = 5
print(math.ldexp(a, b))
# answer = 10 * (2 ** 5)

print(math.modf(10.3))

print(math.trunc(10.6))

print(math.exp(2))
#e = 2.718 ** 2
print(math.expm1(2))