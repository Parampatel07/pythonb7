# 3) Write a programe to print following pattern
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 3000

first = 2 
second = 1
print(first,end=' ')
print(second,end=' ')
answer = first + second # 3
first = answer # first =3 
print(answer,end=' ')
while answer < 2207:
     answer = answer + second # 4
     second = answer # second = 4
     print(answer,end=' ')
     answer = first + answer # 7
     first = answer # first = 7
     print(answer,end=' ')
# answer = second + answer # 11
# second = answer # second = 11
# print(answer,end=' ')
# answer = first + answer # 18
# first = answer
# print(answer,end=' ')
# answer = second + answer
# print(answer,end=' ')
# answer = first + answer
# print(answer,end=' ')