from os import stat
from __util import cursor,mydb


def item_inserter():
    try:
        item_name = input("Item name: ")
        cost = input("Price of the item: ")
        seller_id = input("Seller id: ")
        
        sql ="INSERT INTO items(name,cost,seller_id,bids) VALUES(%s,%s,%s,%s)"
        values = (item_name.title(),cost,seller_id,0)
        
        cursor.execute(sql,values)
        
    except Exception as e:
        print("Error is: ",e)
    else:
        mydb.commit()
        print("1 record inserted, id:",cursor.lastrowid)
          

def customer_inserter():
    
    try:
        customer_name = input("Name of customer: ")
        address = input("Address of customer: ")
        city = input("City name: ")
        state = input("State: ")
        zip = input("Zip Code: ")

        sql = "INSERT INTO customers(name, address,city,state,zip) VALUES(%s,%s,%s,%s,%s)"
        val = (customer_name,address,city,state,zip)
        cursor.execute(sql,val)
    except Exception as e:
        print(f"Error is :{e}")
    else:
        mydb.commit()

        print(cursor.rowcount," record inserted, id: ",cursor.lastrowid)



choice = input("What you want to insert?\nCustomer=1 \t Item=2 \n")
if choice =="1":
    customer_inserter()
elif choice =="2":
    item_inserter()
else:
    print("Invalid Choice.")
    
    