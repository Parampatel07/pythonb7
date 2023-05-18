# Write a programe to findout how many letterr does sentence have and also which letter how many times if the letter is not in the sentence then display it as 0 also count space 

sentence = input("Enter your sentence ")
count = 0 
alphabets = {'a' : 0,'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,'l' : 0,'m' : 0,'n' : 0,'o' : 0,'p' : 0,'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,'v' : 0,'w' : 0,'x' : 0,'y' : 0,'z' : 0,' ':0}
my_list = [*sentence]
print(my_list)
count = 0
while count < len(my_list):
     if my_list[count] in alphabets:
          alphabets[my_list[count]] += 1 
          count += 1 
print(alphabets)