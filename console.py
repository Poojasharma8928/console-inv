from audioop import add
import os,time
os.system('cls')
import pandas as pd
import pyodbc
# # # Connecting With Database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ZIL1185\MSSQLDEV2019;'
                      'Database=Inventory;'
                      'Trusted_Connection=Yes;')
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
    return products
inventory()    
def calculate(productid,quantity,products):
    for i in products:
        if i[0]==productid:
            return i[1],i[4]


cart=[]
def sales(cart):
    productid = int(input("Please enter Product Id: "))
    quantity = int(input("Please enter Quantity: "))
    name_price=calculate(productid,quantity,inventory())
    cart_item=(productid,name_price[0],quantity,name_price[1],name_price[1]*quantity)
    cart.append(list(cart_item))
    temp_cart=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
    print(temp_cart)
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
        if i[2]==mobileno:
         return i[0],i[1]
    return False
if check_customer():
    sales(cart)
else:
    print("Customer Not Found")
    add_customer = input("Do You want add customer??? Y/N?")
    if add_customer=='y' or add_customer=='Y':
        New_customer_name = input("Enter customer Name")
        cursor.execute('Insert into Customer(customer_name) values (?)',New_customer_name)
    else:
        print("Thanks")
def display():
    print("1. Sales")
    print("3. Out of Stock")# if Quantity <=Reorder :
    print("4. Orders")
    print("5. Customers")
display()

