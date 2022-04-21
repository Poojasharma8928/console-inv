import os,time
os.system('cls')
import pandas as pd
import pyodbc
# # # Connecting With Database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ZIL1161\MSSQLDEV2019;'
                      'UID=SA;'
                      'PWD=perficient@123;'
                      'Database=Inventory;'
                      'Trusted_Connection=no;')
animation = "|/-\\"
idx = 0
while True:
    print("Connecting With Database..",animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
    if idx==30:
        break
os.system('cls')
print("Connected Successfully")


# # #Opening A Cursor
cursor=conn.cursor()

#Fetching All Products from inventory
cursor.execute("SELECT * FROM Product")
products=[list(i) for i in cursor.fetchall()]
def inventory():
    cursor.execute("SELECT * FROM Product")
    products=[list(i) for i in cursor.fetchall()]
    df=pd.DataFrame(products,columns=["Product_Id","Product_Name","Category","Available Quantity","Price","Reorder Level"])
    print(df)
    
inventory()

def calculate(productid,quantity,products):
    for i in products:
        if i[0]==productid:
            return i[1],i[4]


cart=[]
def sales(cart):
    productid = int(input("Please enter Product Id: "))
    quantity = int(input("Please enter Quantity: "))
    name_price=calculate(productid,quantity,products)
    cart_item=(productid,name_price[0],quantity,name_price[1],name_price[1]*quantity)
    cart.append(list(cart_item))
    choice=input("Do You want add more??? Y/N?")
    if choice=='y' or choice=='Y':
        sales(cart)
    else:
        cart_df=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
        print(cart_df)
        for i in cart:
            cursor.execute('UPDATE Product set Available_quantity=Available_quantity-? WHERE Product_id=?',i[2],i[0])
            cursor.commit()

def customer():
    global customer_list
    cursor.execute('SELECT * FROM customer')
    customer_list=[list(i) for i in cursor.fetchall()]
    customer_df=pd.DataFrame(customer_list,columns=['Customer_id','Customer Name','Mobile No'])
    print(customer_df)
customer()
def check_customer():
    mobileno = input("Please enter customer mobile no: ")
    for i in customer_list:
        if i[3]==mobileno:
         return i[0],i[1]
        return False
if check_customer():
    sales(cart)
else:
    print("No customer Found")


def display():
    print("1. Sales")
    print("2. Inventory")
    print("3. Out of Stock")
    print("4. Orders")
    print("5. Customers")


