# Write a programe to findout user's birth timestamp accept month , day and year as input 

import datetime

day = int(input("Enter your birth day "))
month = int(input("Enter your birth month "))
year = int(input("Enter your birth year "))

my_birthdate = datetime.datetime(year,month,day)
print(my_birthdate)

my_timestamp = my_birthdate.timestamp()
print(my_timestamp)