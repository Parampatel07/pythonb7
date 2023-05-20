# Write a programe to count number of even numbers and odd numbers in given list and also print list for both 
numbers = [10,20,65,35,12,54,95,3,0,125,3,952,65,21,5,96,32,54,89,74,56,85,41,12,98]
print(numbers)
even_count = 0
odd_count = 0
count = 0
even_numbers = []
odd_numbers = []
for value in numbers :
     if value % 2 == 0:
          even_count += 1
          even_numbers.append(value)
          # reversed(even_numbers)
          # even_numbers.reverse()
     elif value % 2 != 0:
          odd_count += 1
          odd_numbers.append(value)
     count += 1
print("the value of even count is ",even_count)
print("the value of odd count is ",odd_count)
print("the total number of value in list are ",count)
even_numbers.sort()
even_numbers.reverse()
odd_numbers.sort()
print("even numbers are ",even_numbers)
print("odd numbers are ",odd_numbers)