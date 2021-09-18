# import mysql.connector
from mysql.connector import connect

conn = connect(
    user="root",
    password = "",
    host="localhost",
    database="test"
)

cursor = conn.cursor()
query = cursor.execute("SELECT * FROM ITEMS ORDER BY name ")
#query = cursor.execute("select name, cost from items")


result = cursor.fetchall()

print("Name\t\t\t\t\t\t Price")
for r in result:
    print(f"{r[1]} \t\t\t\t {r[2]}")

print("\n-----lenght:----")    
print(len(result))    
    