#Example of instance variable 
class person:
     def __init__(self,name,age,gender):
          print("constructor called....")
          self.name = name
          self.age = age
          self.gender = gender

     def walk(self):
          print("I can Walk ")

     def myInfo(self):
          print(f"my name is {self.name} age is {self.age} gender is {self.gender}")     

name = input("Enter your name ")
age = input("Enter your age ")
gender = input("Enter your gender ")

p1 = person(name,age,gender)
p1.walk()
p1.myInfo()

