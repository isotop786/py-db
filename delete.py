from __util import mydb, cursor




try:
    id =input("Enter id: ")
    sql = f"DELETE FROM customers WHERE id = {id}"
    
    
    cursor.execute(sql)
except Exception as e:
    print("Error is : ",e)
else:
    mydb.commit()
    
    print(cursor.rowcount," record deleted.")         