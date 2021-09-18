import mysql.connector
from mysql import *

con = mysql.connector.connect(
    user='ardit700_student',
    password='ardit700_student',
    host = '108.167.140.127',
    database= 'ardit700_pm1database'
)

cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary")
result = cursor.fetchall()

if len(result) <1:
    print('Loading data from database...')

print(result)

