# Write a programe to findout smallest number out of given 3 number 
num1 = int(input("Enter value of number 1 "))
num2 = int(input("Enter value of number 2 "))
num3 = int(input("Enter value of number 3 "))

if num1 < num2 and num1 < num3:
     print("number 1 is smallest ")
elif num2 < num1 and num2 < num3:
     print("number 2 is smallest ")
else:
     print("number 3 is smallest ")

print("goodbyee..")