# Write a programe to peform split of any 2 digit number 
# number = 57 
# first = 5 , second = 7 
number = 61 
first = number % 10 
second = number - first
third = second / 10
print(f"the value of first is {third}")
print(f"the value of second is {first}")