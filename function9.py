# Write a program to findout factoiral to given number using function 
# nCr = n! / r! * (n – r)! 
# n = 5
# r = 2
#  5 factoiral / (2 factoiral * 3 factoiral)
def getFactorial(number):
     answer = 0
     count = 2
     answer = number * (number - 1) # 20
     while count < number:
          answer = answer * (number - count) # 60
          count += 1
     # print("answer is ",answer)
     return answer

n = int(input("Enter value of n "))# number of trys 
r = int(input("Enter value of r "))#number of items 

n_factorial = getFactorial(n)
r_factorial = getFactorial(r)
n_minur_r = n - r
n_minur_r_factorial = getFactorial(n_minur_r)
ncr = n_factorial / (r_factorial * n_minur_r_factorial)
print("the value of ncr is ",ncr)