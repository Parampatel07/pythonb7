# Example of inheritance 
class person:
     def walk(self):
          print("Person can walk ")

class student(person):
     def code(self):
          print("Student can Code ")

p1 = person()
p1.walk()
s1 = student()
s1.code()
s1.walk()