from __util import mydb,cursor

#cursor = mydb.cursor()

# taking user input 
option = input("What you want to search\n1=>Customers\t2=>Items\n")

if option == "1":
    keyword = input("Enter the name of customer: ")
elif option == "2":
    keyword = input("Enter Item name: ")
else:
    print("Invalid Option. Try again.")        


def sql_gen(option,keyword):
    if option =="1":
        sql = f"SELECT * FROM customers WHERE name LIKE '%{keyword.lower()}%' "
    else:
        sql = f"SELECT * FROM items WHERE name LIKE '%{keyword.lower()}%' "

    return sql

def output(option,result):
    
    if option =="1":
        print("Name\t\t\t\tCity")
        print("_____________________________________________________")
        for r in result:
            print(f"{r[1][:6]} \t\t|\t\t {r[3]}")
            print("-------------------------------------------")
    
    else:
        print("Name\t\t\t\t\t\tPrice\t\t\t\tBids")
        print("__________________________________________________________________________________________")
        for r in result:
            print(f"{r[1]} \t\t\t|\t\t ${r[3]} \t\t|\t\t {r[4]}")
            print("---------------------------------------------------------------------------------------")
            
    
# sql query for searching customer in customers table
sql = sql_gen(option,keyword)

cursor.execute(sql)

result = cursor.fetchall()


output(option,result)




# print("---------------------------------")
# print("Name\t\t\t\tCity")
# print("_____________________________________________________")
# for r in result:
#     print(f"{r[1][:6]} \t\t|\t\t {r[3]}")
#     print("-------------------------------------------")
