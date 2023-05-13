# Write a programe to findout factoiral of given number take number from user 
# 5 
# 5 * 4 * 3 * 2 * 1 = 120
number = int(input("Enter any number "))
temp = 1
answer = number
while temp < number: 
     answer = answer * (number - temp)
     temp += 1 
# answer = answer * (number - temp)
# temp += 1
# answer = answer * (number - temp)
# temp += 1 
# answer = answer * (number - temp)
print("your answer is ",answer)

# num = int(input("Enter any number: ")) 
# count = 0
# factorial =1

# while  num > count:
#     factorial = factorial *  num
#     num -= 1
# print("The factorial is:",factorial)

