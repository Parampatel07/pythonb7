#A list can contain any datatype in it 
numbers = [10 , 20 , 30, 40, 50 , "ten" , 70 , True]
name = ["s","u","n"]
print(numbers)
print(name)
print(numbers[0])
print(numbers[5])
numbers[1] = 100
print(numbers)
print(numbers[ 1 : 6 ])
print(numbers + name)
number_name = numbers[1:6] + name
print(number_name)
my_number = [numbers[0] , numbers[2] , numbers[4] ]
print(my_number)
print(numbers * 5)
print("param " * 5)