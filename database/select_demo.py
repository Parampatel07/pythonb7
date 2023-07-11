import mysql.connector as con 

db = con.connect(host="localhost",user='root',passwd='',database='py7',port=3306)
print("connection established ")

sql = "Select * from student"

mycursor = db.cursor(dictionary=True)

mycursor.execute(sql)

# data = mycursor.fetchone()
# print(data)
data = mycursor.fetchall()
# print(data)
print(f"{'id':5} {'name':24}  {'age':5}  {'email':60}  {'mobile':15}")
for i in data:
     my_data = f" {i['id']:5} {i['name']:20}  {i['age']:5}  {i['email']:60}  {i['mobile']:15}"
     print(my_data)