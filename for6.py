# Write a programe to count number of words in given sentence

sentence = input("Enter any sentence/phase ")

# sentence = "this is  python batch7"
count= 0
my_list = sentence.split()
print(my_list)
for i in my_list:
     print(i,end=" ")
     count+=1

print("\nthe value of count is ",count)