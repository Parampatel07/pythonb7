row=1
column1=1
column2=1
while row<=6:
    while column1<=(6-row):
        print(" ",end='')
        column1+=1
    while column2<=row:
     #    print(f"{column2} ",end='')
        if column2==1 or row==column2 or row==6:
            print(f" *",end='')
        else:
            print("  ",end='')    
        column2+=1
    column1=1
    column2=1
    row+=1
    print(" ")
print(" all  pyramid completed")