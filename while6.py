# Write a program to print a multiplication table of 5 
# 5 x 1 = 5 
# 5 x 2 = 10 

table = int(input("Enter value of table "))
multiplier = 1 
answer = 0

while multiplier <= 10:
     answer = table * multiplier
     print(f"{table} x {multiplier} = {answer}")
     multiplier += 1
# print(f"{table} x {multiplier} = {answer}")
# multiplier += 1
# answer = table * multiplier
# print(f"{table} x {multiplier} = {answer}")
# multiplier += 1
# answer = table * multiplier
# print(f"{table} x {multiplier} = {answer}")
# multiplier += 1
# answer = table * multiplier
# print(f"{table} x {multiplier} = {answer}")