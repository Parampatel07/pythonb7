# Create a class that has method which can convert given inch to foot , inch to meter , inch to centimeter 
class Inchconverter:
     task = "Converts Inches "
     def __init__(self,inch):
          self.inch = inch 
     
     def inchToFoot(self):
          answer = self.inch / 12
          print(f"foot of {self.inch} is {answer}")

     def inchToMeter(self):
          answer = self.inch / 39.37
          print(f"Meter of {self.inch} is {answer}")

     def inchToCentimeter(self):
          answer = self.inch * 2.54
          print(f"Centimeter of {self.inch} is {answer}")

inch = int(input("Enter value of inch "))
i1 = Inchconverter(inch)
i1.inchToFoot()
i1.inchToMeter()
i1.inchToCentimeter()
print(i1.task)