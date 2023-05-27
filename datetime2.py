import datetime

year = int(input("Enter any year "))
month = int(input("Enter any month "))
day = int(input("Enter any day "))

print(f"{day} - {month} - {year}")

date = datetime.date(year,month,day)
print(date)

print("the year is ",date.year)
print("the month is ",date.month)
print("the day is ",date.day)