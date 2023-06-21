# Example of reading a file 
file = open('demo1.html')
print(file)
count= 0
for value in file:
     print(value)
     count+=1

print(count)
file.close()