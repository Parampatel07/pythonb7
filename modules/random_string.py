import string
import random

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)

def randomString():
     letter = string.ascii_lowercase
     single_letter = random.choice(letter)
     answer ="".join(single_letter)
     # print(answer)
     return answer

random_string=''
for i in range(0,10):
     random_string += randomString()
print(random_string)