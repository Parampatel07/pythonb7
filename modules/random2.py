# Create a function that can generate random otp
import random
def getOtp():
     otp = str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
     # print(otp)
     return otp

my_otp = getOtp()
print(my_otp)