# Write a programe to print numbered half pyramid 
# https://i1.faceprep.in/fp/articles/img/55984_1580817324.png
count = 1
flash = 1
size = int(input("Enter size of triangle "))
while flash <= size:
     while count<=flash:
          print(count,end='')
          count+=1
     print("")
     count=1
     flash += 1
# while count<3:
#      print("*",end='')
#      count += 1
# print("")
# count =0
# while count < 4:
#      print("*",end='')
#      count += 1
# print("")
