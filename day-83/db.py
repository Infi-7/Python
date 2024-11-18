import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("Create Database mydatabase")
mycursor.execute("select * from projects")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)