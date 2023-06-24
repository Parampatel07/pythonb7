class person(object):
     def __init__(self,name,age):
          self.name = name
          self.age = age 

     def getInfo(self):
          print(f"My name is {self.name} and my age is {self.age}")

class student(person):
     def __init__(self, name, age,roll_no,marks):
          self.roll_no = roll_no
          self.marks = marks
          person.__init__(self,name,age)

     def getInfo(self):
          print(f"My name is {self.name} and my age is {self.age}")
          print(f"My roll_no is {self.roll_no} and my marks are {self.marks}")
          
s1 = student("Param",19,99,33)
s1.getInfo()
p1 = person("Jonh Doe",24)
p1.getInfo()