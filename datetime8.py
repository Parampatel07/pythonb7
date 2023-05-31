# Example of creating a datetime object from user's input 
from datetime import datetime
hour = int(input("Enter value of hours "))
minutes = int(input("Enter value of minutes "))
seconds = int(input("Enter value of seconds "))
year = int(input("Enter value of year "))
month = int(input("Enter value of month "))
day = int(input("Enter value of day "))

my_datetime = datetime(year=year,hour=hour,month=month,second=seconds,minute=minutes,day=day) #keyword agrument function 
print(my_datetime)