# multilevel inheritance 
class base(object):
     def __init__(self,name):
          self.name = name
          print("base class constructor called ...")
     def write(self):
          print("i can write ")

class child(base):
     def __init__(self, name,age):
          self.age = age
          base.__init__(self, name)
     def walk(self):
          print("i can walk")

class grandChild(child):
     def __init__(self, name, age,weight):
          self.weight = weight
          child.__init__(self, name, age)
     def talk(self):
          print("i can talk")

gc1 = grandChild("Param",19,53.24)
gc1.walk()
gc1.talk()
gc1.write()