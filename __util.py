from mysql.connector import connect

mydb = connect(
    user = "root",
    password= "",
    host = "localhost",
    database="test"
)

cursor = mydb.cursor()