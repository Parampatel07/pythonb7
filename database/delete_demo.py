import mysql.connector as con 

db = con.connect(host="localhost",user='root',passwd='',database='py7',port=3306)
print("connection established ")

id = int(input("enter id to be deleted "))

mycursor = db.cursor()

sql = "delete from student where id = %s "

data = [id]

mycursor.execute(sql,data)

db.commit()

print("row deleted successfully ")