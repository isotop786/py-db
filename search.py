from __util import mydb,cursor

#cursor = mydb.cursor()

# taking user input 
customer = input("Enter the name of customer: ")

# sql query for searching customer in customers table
sql = f"SELECT * FROM customers WHERE name LIKE '%{customer}%' "

cursor.execute(sql)

result = cursor.fetchall()

print("---------------------------------")
print("Name\t\t\t\tCity")
print("_____________________________________________________")
for r in result:
    print(f"{r[1][:6]} \t\t|\t\t {r[3]}")
    print("-------------------------------------------")
