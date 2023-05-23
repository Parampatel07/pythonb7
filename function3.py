#Example of function without input and with return value 
#Write a programe to findout area of cylinder 
# area = 2 * pi * r * h + 2 * pi * (r * r)
def getPi():
     pi = 3.14159
     return pi

radius = int(input("Enter value of radius "))
height = int(input("Enter value of height "))
pi = getPi()
area = (2 * pi * radius * height) + (2 * pi * (radius*radius))
print("the area of cylinder is ",area)