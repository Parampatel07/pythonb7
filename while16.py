# Write a programe to findout how many letter does the given string has and also count number of vowels 

sentence = input("Enter any phase/sentence ")
vowels = ['a','e','i','o','u']
my_list = [*sentence]
print(my_list)

letter_count = len(my_list)
print("total number of letter in string are ",letter_count)

count = 0
vowel_count = 0
while count < len(my_list):
     if my_list[count] in vowels :
          vowel_count += 1
     count += 1 

print("the value of vowel count is ",vowel_count)
