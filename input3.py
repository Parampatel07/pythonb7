# Write a programe to findout my_my_bmi of user 
# weight in kg / height in meter  * height in meter
weight = float(input("Enter your weight "))
foot = int(input("Enter your height in foot "))
inch = int(input("Enter your height in inch "))
foot_meter = foot / 3.281
inch_meter  = inch / 39.37
print(f"the value of foot_meter is {foot_meter} and value of inch_meter is {inch_meter}")
total_meter = foot_meter + inch_meter
print(f"the value of total_meter is {total_meter}")
my_my_bmi = weight / (total_meter * total_meter)
print(f"the value of my_bmi is {my_bmi} ")

my_bmi = weight / (total_meter * total_meter)
print(f"the value of my_bmi is {my_bmi} ")

my_bmi = weight / (total_meter * total_meter)

print(f"the value of my_bmi is {my_bmi}")
