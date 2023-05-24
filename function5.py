# Write a programe to create a bmi calc 
# https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.cdc.gov%2Fhealthyweight%2Fimages%2Fassessing%2Fbmi-adult-fb-600x315.jpg%3F_%3D07167&tbnid=OBVtIozsohR6zM&vet=12ahUKEwiD0oqQ04v_AhWbk9gFHVHsB2kQMygAegUIARDjAQ..i&imgrefurl=https%3A%2F%2Fwww.cdc.gov%2Fhealthyweight%2Fassessing%2Fbmi%2Fadult_bmi%2Findex.html&docid=f4E-W45ma3qlxM&w=600&h=315&q=bmi&client=firefox-b-d&ved=2ahUKEwiD0oqQ04v_AhWbk9gFHVHsB2kQMygAegUIARDjAQ

# bmi = weight / (meter * meter )

def footToMeter(foot):
     answer = foot / 3.281
     return answer

def inchToMeter(inch):
     answer = inch / 39.37
     return answer

def getAdd(a,b):
     answer = a + b
     return answer

def getBmi(a,b):
     answer = a / ( b * b)
     return answer

def getCategory(bmi):
     if bmi <= 18.5:
          print("you are underweight ")
     elif bmi >=18.6 and bmi < 24.9:
          print("you are normal weight")
     elif bmi >=24.9 and bmi <29.9:
          print("you are over weight ")
     elif bmi >= 29.9 and bmi < 34.9:
          print("you are obese ")
     else:
          print("you are extremly obese ")

weight = float(input("Enter your weight "))
foot = int(input("Enter your height in foot ")) 
inch = int(input("Enter your height in inch "))
foot_meter  = footToMeter(foot)
# print("the value of converted meter from foot is ",foot_meter)
inch_meter = inchToMeter(inch)
# print("the value of converted meter from inch is ",inch_meter)
height = getAdd(foot_meter,inch_meter)
# print("the value of users height is ",height)
bmi=getBmi(weight,height)
print("the value bmi is ",bmi)
getCategory(bmi)