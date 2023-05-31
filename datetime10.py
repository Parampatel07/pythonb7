# https://www.geeksforgeeks.org/python-datetime-strptime-function/
import datetime
date = datetime.datetime.now()
print(date)
formated_date = date.strftime("%y-%m-%d = %a")
print(formated_date)
formated_date = date.strftime("%y-%m-%d = %A")
print(formated_date)
formated_date = date.strftime("%y-%m-%d = %w")
print(formated_date)
formated_date = date.strftime("%y-%m-%d = %b")
print(formated_date)
formated_date = date.strftime("%y-%m-%d = %B")
print(formated_date)
formated_date = date.strftime("%y-%m-%d = %y")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %Y")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %H")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %I")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %p")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %M")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %S")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %f")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %z")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %j")
print(formated_date)
formated_date = date.strftime(f"%y-%m-%d - %U")
print(formated_date)
formated_date = date.strftime(f"%c")
print(formated_date)
formated_date = date.strftime(f"%x")
print(formated_date)
formated_date = date.strftime(f"%X")
print(formated_date)