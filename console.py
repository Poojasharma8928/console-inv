# Importing Libraries
import os,time
os.system('cls')
import pandas as pd
import pyodbc
# # # Connecting With Database
conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=ZIL1157\MSSQLSRVDEV19;'
                    'Database=Project_inventory;'
                    'Trusted_Connection=yes;')
# animation = "|/-\\"
# idx = 0
# while True:
#     print("Connecting With Database..",animation[idx % len(animation)], end="\r")
#     idx += 1
#     time.sleep(0.1)
#     if idx==30:
#         break
# os.system('cls')
# print("Connected Successfully")

fg
# # #Opening A Cursor
cursor=conn.cursor()

#Fetching All Products from inventory
cursor.execute("SELECT * FROM products")
products=[list(i) for i in cursor.fetchall()]
def inventory():
    
    cursor.execute("SELECT * FROM Product")
    products=[list(i) for i in cursor.fetchall()]
    df=pd.DataFrame(products,columns=["Product_Id","Product_Name","Category","Available Quantity","Price"])
inventory()

def calculate(productid,quantity):
    # comment: to calculate total amount 
    for i in products:
        if i[0]==productid:
            return (i[0],i[1],i[4]*quantity)
# end def


def sales(order):
    product_id=int(input("Please Enter Product ID:"))
    quantity=int(input("Please Enter Quantity:"))
    order.append((product_id,quantity))
    choice=input("Do You want to Purchase more?? Y/N?")
    if choice=='y':
        sales(order,products)
    else:
        print(order)
        for i in order:
            cursor.execute('UPDATE Product SET available_quantity = available_quantity-? where Product_id=?',(i[1],i[0]))
            cursor.commit()
        return
order=[]
sales(order,products)


# def display():
#     print("1. Sales")
#     print("2. Inventory")
#     print("3. Out of Stock")
#     print("4. Orders")
#     print("5. Customers")

# display()