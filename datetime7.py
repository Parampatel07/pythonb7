# Example of getting time object from user given input 
from datetime import time

hours = int(input("Enter number of hours "))
minutes = int(input("Enter number of minutes "))
second = int(input("Enter number of seconds "))

my_time = time(hour=hours,minute=minutes,second=second,microsecond=450)
print(my_time)

print("the value of hours is ",my_time.hour)
print("the value of minute is ",my_time.minute)
print("the value of second is ",my_time.second)