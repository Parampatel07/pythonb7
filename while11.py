# Write a program to print following pattern
# 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231 .. 1000

number = 1
temp = 5
answer = 0
print(number,end=' ')
answer = number + temp

while answer < 1000:
     print(answer,end=' ')
     temp += 4
     answer = answer + temp
# print(answer,end=' ')
# temp += 4
# answer = answer + temp
# print(answer,end=' ')
# temp += 4
# answer = answer + temp
# print(answer,end=' ')
