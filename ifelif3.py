# Write a programe to pepare a calc using elif 
# Give following option 
# -> addition
# -> subtraction
# -> multiplication
# -> division
# -> modlus
# -> maximum
# -> minimum
# -> equaltiy
num1 = float(input("Enter value of number 1 "))
num2 = float(input("Enter value of number 2 "))
option = int(input('''
Enter 1 for addition 
Enter 2 for subtraction 
Enter 3 for multiplication
Enter 4 for division 
Enter 5 for modlus 
Enter 6 for maximum
Enter 7 for minimum
Enter 8 for equality 
'''))

if option == 1 :
     answer = num1 + num2
     print("the value of answer is ",answer)
elif option == 2:
     print("the value of answer is ",num1 - num2)
elif option == 3 :
     print("the value of answer is ",num1 * num2)
elif option == 4:
     print("the value of asnwer is ",num1 / num2)
elif option == 5:
     print("the value of answer is ",num1 % num2)
elif option == 6:
     if num1 > num2 :
          print("num1 is maximum ")
     elif num2 > num1 :
          print("num2 is maximum ")
     else:
          print("both number are same ")
elif option == 7 :
     if num1 < num2 :
          print("num1 is minimum ")
     elif num2 < num1 :
          print("num2 is minimum ")
     else:
          print("both number are same ")
elif option == 8:
     if num1 == num2:
          print("both are equal ")
     else:
          print("both are not equal ")
else :
     print("invalid input ")

print("Goodbyee...")