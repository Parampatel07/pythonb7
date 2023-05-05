# Write a programe to peform swap without using 3rd variable 
a = 10
b = 20
print(f"the value of before swap a is {a} and b is {b} ")
a = a + b 
b = a - b 
a = a - b 
print(f"the value of after swap a is {a} and b is {b} ")