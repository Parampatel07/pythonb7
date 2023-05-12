# 2) Write a programe to print following pattern
# 1 8 27 64 .... 10000
number = 1

answer = number * number * number
print(answer,end=' ')
while number < 21:
     print(number * number * number)
     number = number + 1
# number = number + 1
# answer = number * number * number
# print(answer,end=' ')