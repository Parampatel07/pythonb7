# Write a programe to findout how many odd and even number does the given list has 
numbers = [10,22,36,41,50,65,44,59,59,45,10,35,20,65,84,23,1,2,77]
even = 0
odd = 0
count= 0
even_number = []
odd_number = []
# if count <= len(numbers):
while count < len(numbers):
     if numbers[count] % 2 == 0:
          even += 1
          # print(count)
          even_number.append(numbers[count])
     else:
          odd += 1
          # print(count)
          odd_number.append(numbers[count])
     count+=1
print("total even numbers are ",even)
print("total odd numbers are ",odd)
print("list of even number is ",even_number)
print("list of odd number is ",odd_number)
# if numbers[1] % 2 == 0:
#      even+=1
# else:
#      odd +=1 
# if numbers[2] % 2 == 0:
#      even +=1
# else:
#      odd+=1