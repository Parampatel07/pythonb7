# write a programe to print following pattern
# 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 1000

second = 1
temp = 2 
print(" 0 ",end=' ')
print(second,end=' ')
while second < 990:
     second = second + temp
     print(second,end=' ')
     temp += 1
# second = second + temp
# print(second,end=' ')
# temp += 1
# second = second + temp
# print(second,end=' ')
# temp += 1
# second = second + temp
# print(second,end=' ')
# second = second + 6 
# print(second,end=' ')
