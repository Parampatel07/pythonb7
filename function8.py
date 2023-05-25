# Write a program to findout factoiral to given number using function 
number = int(input("Enter value of number "))

# 5 * 4 * 3 * 2 * 1  
def getFactorial(number):
     answer = 0
     count = 2
     answer = number * (number - 1) # 20
     while count < number:
          answer = answer * (number - count) # 60
          count += 1
     # answer = answer * (number - 3) # 120
     # answer = answer * (number - 4) # 120
     print("answer is ",answer)


if number == 1 :
     print("answer is 1 ")
else :
     getFactorial(number)