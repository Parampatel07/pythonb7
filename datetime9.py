# Write a programe to findout difference between your birthdate till now in seconds 
import datetime
# from datetime import time
date1 = datetime.datetime(2004,2,10,5,31,00).timestamp()
print("first date is ",date1)
date2 = datetime.datetime.now().timestamp()
print("second date is ",date2)
my_time = date2 - date1 
print(my_time)
my_minutes = my_time / 60
print(my_minutes)
my_days = my_time / 86400
print(my_days)
my_month = my_time / 2592000
print(my_month)
my_year = my_month / 12 
print(my_year)