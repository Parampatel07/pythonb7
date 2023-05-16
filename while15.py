# Write a programe to print hollow inverted half pyramid 
# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png

count = 0
space = 0
flash = 5
while count < 8:
     print("*",end="")
     count += 1 
print("")
print("*",end='')
while flash > 0:
     while space < flash:
          print(" ",end='')
          space+=1
     print("*",end='')
     print("")
     print("*",end='')
     space = 0
     flash -= 1

# while space < 3:
#      print("_",end='')
#      space +=1
# print("*",end='')
# print("")
# print("*",end='')
# space = 0
# while space < 2:
#      print("_",end='')
#      space +=1
# print("*",end='')