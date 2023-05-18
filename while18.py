# Write a programe to print full pyramid 
count = 0
temp = 0
flash = 0
minus = 5
adder = 1
while flash < 5 :
     while count < minus :
          print(" ",end="")
          count += 1
     while temp < adder :
          print("*",end="")
          print(" ",end="")
          temp += 1
     print("")
     adder += 1
     minus -= 1
     temp = 0
     count = 0
     flash += 1
# while count < 4:
#      print(" ",end="")
#      count+=1
# temp = 0
# while temp < 2:
#      print("*",end="")
#      print(" ",end="")
#      temp += 1 
# # print("*",end="")
# print("")
# count = 0
# while count < 3:
#      print(" ",end="")
#      count +=1 
# # print(" ",end="")
# # print(" ",end="")
# temp = 0
# while temp < 3:
#      print("*",end="")
#      print(" ",end="")
#      temp +=1
# # print("*",end="")
# # print(" ",end="")
# # print("*",end="")
# # print(" ",end="")
# print("")
# count = 0
# while count < 2:
#      print(" ",end="")
#      count += 1
# # print(" ",end="")
# print("*",end="")
# print(" ",end="")
# print("*",end="")
# print(" ",end="")
# print("*",end="")
# print(" ",end="")
# print("*",end="")
# # print(" ",end="")