#  12) Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
# https://in.pinterest.com/pin/81698180718875314/

month = int(input("Enter your birth month "))
day = int(input("Enter your birth day "))

if month >12 and month <1:          
     print("invalid input ")
else:

     if (month == 3 and (day >= 21 or day <=31)) or (month == 4 and (day <= 19 or day>=1 )):
          print("your zodiac sign is aries ")
          male_zodiac = "aries"

     elif (month == 4 and day >= 20) or (month==5 and day <= 20):
          print("your zodiac sign is taurus ")
          male_zodiac = "taurus"