# Example of strptime function 
from datetime import datetime 

date = datetime.now()
print(date)

string_date = date.strftime("%d-%m-%Y")
print(string_date)
date_object = datetime.strptime(string_date,"%d-%m-%Y")
print(date_object)