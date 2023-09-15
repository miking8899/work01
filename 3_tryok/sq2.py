import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jacky5257"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE runoob_db")

