# Write a program in Python to reverse a sentence .
# param = marap
sentence = input("Enter any sentence/phase ")
print(sentence)
string_size = len(sentence) #param
print(string_size) # 5
for i in range(string_size,0,-1): # 5 to 0 
     # print(i)
     print(sentence[i-1:i],end="")
