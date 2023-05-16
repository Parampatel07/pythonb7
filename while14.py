# Write a programe to print following triangle 
# 1
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
count = 1
flash = 1
while flash < 5 :
     while count <= flash:
          print(flash,end="")
          count += 1
     print("")
     count = 1
     flash += 1