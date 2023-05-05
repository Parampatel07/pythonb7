# Write a programe to findout wether the given year is millineum year 
# 1000,2000,3000,4000,5000,6000,.... 
year = int(input("Enter your year "))

answer = year % 1000

if answer == 0:
     print("it is millinuem year ")
print("goodbyee..")