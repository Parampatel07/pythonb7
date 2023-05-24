# Write a programe to peform subtraction 

def getSub(num1,num2=100):
     print("the value of num1 is ",num1)
     print("the value of num2 is ",num2)
     answer = num1 - num2
     print("the value of answer is ",answer) 
     return answer
num1 = int(input("Enter value of num1 "))
num2 = int(input("Enter value of num2 "))
getSub(num1)