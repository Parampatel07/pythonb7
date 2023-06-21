import time
file_read = open("demo1.html","r")
file_write = open("py70.txt",'w')

for i in file_read:
     print(i)
     time.sleep(2)
     file_write.write(i)
# print()
file_read.close()
file_write.close()