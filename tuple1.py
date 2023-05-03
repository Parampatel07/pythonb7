person = ("Param",19,45.45,True)
print(person)
#this cannot be done while using tuple 
# del person[0]
# person[0]="pratham"
print(person[0:2])
print(person + person)
print(person * 3)
temp = person.count(19)
print(temp)
temp = person.index(True)
print(temp)