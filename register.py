#!C:\Python\python.exe
import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

print("<h1>registration successfull"
"</h1>")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fmobilenumber=form.getvalue("mobilenumber")
femail=form.getvalue("email")

print("<h2>,fname,fmobilenumber,femail</h2>")

mydb=mysql.connector.connect(
    host="Fitness world",
    user="root",
    password="",
    database="members"
 )
mycursor=mydb.cursor()

sql="INSERT INTO user(name,mobilenumber,email)VALUES(%s,%s)";
value=(fname,fmobilenumber,femail)

mycursor.execute(sql,value)
mydb.commit()

print("</body>")
print("</html>")