# Write a programe to print hollow full pyramid 
count= 1
flash = 1
size = int(input("Enter value of size "))
while flash <= size:
     while count<=(size-flash):
          print("_",end='')
          count+=1
     count=1
     while count <= flash:
          if count == 1 or flash==size or count == flash:
               print("* ",end='')
          else:
               print(" ",end=" ")
          count+=1
     print(" ")
     count=1
     flash+=1
print(f"the value of size is {size} and value of flash is {flash}")
# count= 0
# while count<6:
#      print("_",end='')
#      count+=1
# count=0
# while count < 5:
#      print("*",end='')
#      count+=1
