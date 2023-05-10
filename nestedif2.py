# Write a programe to findout number of days a month has without using elif 

month = int(input("Enter month number "))
if month <= 12 and month >= 1:
     if month != 2 :
          if month == 1 or month == 3 or month ==5 or month ==7 or month == 8 or month ==10 or month ==12:
               print("it has 31 days")
          else:
               print("it has 30 days ")
     else:
          print("it has 28 - 29 days ")
else:
     print("Invalid input ")
print("Goodbyee..")