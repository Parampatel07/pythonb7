# Example of for loop in python 
fruits = ['Apple','Mango','Orange','Grapes','Pineapple'] 
person = {'name':'Param','age':19,'weight':45.45}
for item in fruits :
     print(item,end=" ")
print()
for item in person:
     # print(item)
     print(f"{item}-{person[item]}")