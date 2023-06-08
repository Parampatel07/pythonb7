name = "The EasyLearn"


print(name.upper())
print(name.lower())

my_string = "param"
my_string2 = "PaRAM"
print(my_string.isalnum())
print(my_string.isalpha())
print(my_string.islower())
print(my_string2.isnumeric())
print(my_string2.isspace())
print(my_string2.istitle())
print(my_string2.isupper())

country = ['India','Usa','Austrialia','Canada']
seperator = " -- "
answer = seperator.join(country)
print(answer)

my_string3 = "AEHFISLOS"
answer = my_string3.replace("I","P")
print(answer)

my_string4 = "Param"
# lists = ['I','am','Param']
answer = my_string4.split("a")
print(answer)

my_string5 = ['1','2','3','4','5','6','7','8','9','10']
seperator = "+"
answer = seperator.join(my_string5)
print(answer)

answer = my_string4 + " + " + my_string3
print(answer)