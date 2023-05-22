# Write a program in Python to reverse a sentence .

sentence = input("enter any sentence/phase ")
my_list = [*sentence]
print(my_list)
for i in reversed(my_list):
     print(i,end="")