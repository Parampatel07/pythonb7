# Write a programe to print 2 digit number in words 
# number = 73
# seven three 
number = int(input("Enter number only digit values "))

first = int(number / 10)
second = int(number % 10)

print(f"the value of first is {first} and second is {second}")

if first == 1 :
     print("One ",end='')
elif first == 2 :
     print("Two ",end='')
elif first == 3 :
     print("Three ",end='')
elif first == 4:
     print("Four ",end='')
elif first == 5:
     print("Five ",end='')
elif first == 6:
     print("Six ",end='')
elif first == 7:
     print("Seven ",end='')
elif first == 8:
     print("Eight " ,end='')
elif first == 9:
     print("Nine ",end='')
elif first == 0:
     print("Zero ",end='')
  

if second == 1 :
     print("One ")
elif second == 2 :
     print("Two ")
elif second == 3 :
     print("Three ")
elif second == 4:
     print("Four ")
elif second == 5:
     print("Five ")
elif second == 6:
     print("Six ")
elif second == 7:
     print("Seven ")
elif second == 8:
     print("Eight " )
elif second == 9:
     print("Nine ")
elif second == 0:
     print("Zero ")
  