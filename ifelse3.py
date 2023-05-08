# Write a programe to findout which office greater out of given 2 office user will given lenght and width of both office 
lenght1 = float(input("Enter lenght of office 1 "))
width1 = float(input("Enter width of office 1 "))
lenght2 = float(input("Enter lenght of office 2 "))
width2 = float(input("Enter width of office 2 "))

office1 = float(lenght1 * width1)
office2 = float(lenght2 * width2)

print(f"the value of office 1 is {office1} and office 2 is {office2} ")

if office1 > office2:
     print("Office 1 is greater than office 2 ")
else:
     print("office 2 is greater than office 1 ")

print("Goodbyee...")