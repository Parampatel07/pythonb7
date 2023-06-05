import calc_module
option=''
while option != 0:
     a=int(input("Enter First Number:"))
     b=int(input("Enter Second Number:"))
     option = int(input('''Enter 1 is Addition
Enter 2 is subtraction
Enter 3 is multiplication
Enter 4 for division
Enter 5 for modlus
Enter 0 for Exit'''))
     if option==1:
          res=calc_module.add(a,b)
          print("Addition",res)
     elif option==2:
          res=calc_module.sub(a,b)
          print("Subtraction",res)
     elif option==3:
          res=calc_module.mul(a,b)
          print("Multiplication",res)
     elif option==4:
          res=calc_module.div(a,b)
          print("Division",res)
     elif option==5:
          res=calc_module.mod(a,b)
          print("MOdules",res)
# print(calc.add(number1=number2))
# print(calc.sub)
# print(calc.mul)
# print(calc.div)
# print(calc.mod)
