import mysql.connector as con 

db = con.connect(host="localhost",user='root',passwd='',database='py7',port=3306)
print("connection established  ")

id = int(input("Enter student id "))
name = input("Enter your name ")
age = int(input('Enter your age '))
email = input("Enter your email ")
mobile = int(input("Enter your Mobile number"))

sql = "Update student set name = %s , age = %s , email = %s ,mobile = %s where id = %s "

values = [name,age,email,mobile,id]

mycursor = db.cursor()

mycursor.execute(sql,values)

db.commit()
print("Row updated successfully  ")