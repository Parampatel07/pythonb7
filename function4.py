# Example of function with input and with output 
#Write a programe to peform addition 

def getAdd(a,b):
     answer  = a + b 
     return answer
     answer  = a - b 

num1 = int(input("Enter value of num1 "))
num2 = int(input("Enter value of num2 "))
ans = getAdd(num1, num2)
print("the value of answer is ",ans)