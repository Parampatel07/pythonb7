# Write a programe to findout how many days user given month has take month in number 
month = int(input("Enter your month number "))

if month >= 1 and month <= 12:
     if month == 1 or month==3 or month==5 or month == 7 or month ==8 or month == 10 or month == 12:
          print("it has 31 days ")
     elif month == 2:
          print("it has 28 - 29 days ")
     elif month==4 or month==6 or month==9 or month==11 :
          print("it has 30 days ")
else:
     print("invalid input ")

print("Goodbyee..")