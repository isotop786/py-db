import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="test"
)

cursor = mydb.cursor()

sql = "SELECT * FROM customers right join items on customers.id = items.seller_id"

cursor.execute(sql)

result = cursor.fetchall()

for r in result:
    print(r)

