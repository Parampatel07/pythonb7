# Example of multiplie return value function 
def calc(num1,num2):
     addittion = num1 + num2 
     subtraction = num1 - num2 
     return addittion,subtraction

num1 = int(input("Enter value of num1 "))
num2 = int(input("Enter value of num2 "))
answer = calc(num1, num2)
print(answer)