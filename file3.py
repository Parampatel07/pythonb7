# Write a programe to read a file and findout how many vowel does it contains (file should contain minimum 100 character)
file = open("demo1.html")
content = file.read()
print(content)
file.close()
vowels = ['a','e','i','o','u']
count=0
content = content.lower()
content_list = [*content]
print(content_list)
for i in content_list:
     print(i)
     if i in vowels:
          count = count + 1

print("total number of vowel are ",count)

# def myvowels():
#     file = open("demo1.html")
#     myread = file.read()
#     vowels = list("aeiouAEIOU")
#     count=0
    
    
#     for vowel in myread:
#         if vowel in vowels:
#             count+=1
#     return count
# print("Total Vowels is",myvowels())