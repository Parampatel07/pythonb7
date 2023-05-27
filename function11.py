# Write a programe to calc marks using keyword argument function 

def calcMarks(science=0,math=0,english=0):
     total = science + math + english
     print("the value of science is ",science)
     print("the value of math is ",math)
     print("the value of english is ",english)
     print("total of your marks is ",total)

english = int(input("Enter marks for english "))
math = int(input("Enter marks for math "))
science = int(input("Enter marks for science "))
calcMarks(english=english,science=science,math=math)