# 1) Write a python programe count number of letter in the given string accept string from user  .
sentence = input("Enter any sentence/phase ")

# sentence = "this is python batch7"
count = 0
for letter in sentence:
     print(letter,end=' ')
     if letter != ' ':
          count += 1 

print("\ntotal number of letter are ",count)