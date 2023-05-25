# Write a programe to print 2 digit number in words using function 
# number = 56
# five six
def number_to_word(number):#single digit number only 
     if number == 1:
          print("One ")
     elif number == 2:
          print("Two ")
     elif number == 3:
          print("Three")
     elif number == 4:
          print("Four ")
     elif number == 5:
          print("Five ")
     elif number == 6:
          print("Six ")
     elif number == 7:
          print("Seven ")
     elif number == 8:
          print("Eight ")
     elif number == 9:
          print("Nine ")
     elif number == 0:
          print("Zero ")

number = int(input("Enter value of number only 2 digit "))
if number <=9 and number >=100:
     print("invalid number ")
else:
     first = int(number / 10 ) # 5
     second = int(number % 10) # 6
     number_to_word(first)
     number_to_word(second)