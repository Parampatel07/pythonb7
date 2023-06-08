import random

def getNumber():
    my_list=[]
    for otp in range(10):
          otp= str(random.randrange(90,99))+ str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))
          my_list.append(otp)
    return my_list

getNumber()    
print("your number is +91",getNumber())