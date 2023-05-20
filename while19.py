count=0
temp=5
space=0
size=5
num=5
while size>=1:
    while count < temp-num:
        print("_",end='')
        num+=1
        
    while count < size-space:
          print("*",end=" ")
          count+=1
          
    print("")       
    
    size-=1
    num-=1
    count=0