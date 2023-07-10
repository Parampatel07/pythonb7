import mysql.connector as con 

db = con.connect(host="localhost",user="root",passwd="",database='py7',port=3306)
print("connection established ")

mycursor = db.cursor()

sql  = "INSERT into student (name,age,email,mobile) values (%s,%s,%s,%s);"

name = input("Enter your name ")
age = int(input("Enter your age "))
email = input("Enter your email ")
mobile = int(input("Enter your mobile number "))

data = [name,age,email,mobile]

mycursor.execute(sql,data)

db.commit()

print("row inserted successfully ")
print("total rows added ",mycursor.rowcount)