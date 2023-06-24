# multiple inheritance 
class person(object):
     def __init__(self,name):
          print("person class constructor called ...")
          self.name = name
     def walk(self):
          print("I can Walk")

class student(object):
     def __init__(self,roll_no):
          print("student class constructor called....")
          self.roll_no = roll_no
     def write(self):
          print("I can write")

class employee(person,student):
     def __init__(self, name,roll_no):
          print("Employee class constructor called ...")
          person.__init__(self,name)
          student.__init__(self,roll_no)

e1 = employee("Param",99)
e1.walk()
e1.write()