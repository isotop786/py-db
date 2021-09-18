import mysql.connector

def db_connect():
    conn = mysql.connector.connect(
        user="root",
        password ="",
        host="localhost",
        database="test"
    )
    
