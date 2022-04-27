import os,time
from datetime import datetime
import pandas as pd
import connection
os.system('cls')
# # # Connecting With Database

# # #Opening A Cursor
cursor=connection.conn.cursor()

#Fetching All Products from inventory
cursor.execute("SELECT * FROM Product")
products=[list(i) for i in cursor.fetchall()]
def inventory():
    cursor.execute("SELECT * FROM Product")
    products=[list(i) for i in cursor.fetchall()]
    df=pd.DataFrame(products,columns=["Product_Id","Product_Name","Category","Available Quantity","Price","Reorder Level"])
    # print(df)
    return products
inventory()    
#sdfgh
def calculate(productid,quantity,products):
    for i in products:
        if i[0]==productid:
            return i[1],i[4]

def orders():
    cursor.execute('EXEC DisplayOrders')
    orders=[list(i) for i in cursor.fetchall()]
    orders=pd.DataFrame(orders,columns=['Invoice ID','Customer Name','Invoice Amount','Invoice Date'])
    print(orders)
    print("1. Order Details using Invoice ID")   
    print("2. Order of Specific Customer")
    choice = int(input("Please enter: "))
    if choice==1:
        InvoiceDetail()
    if choice==2:
        Customer_Invoice()
        if int(input("Press 1 for Specific Invoice Details"))==1:
            InvoiceDetail()


def InvoiceDetail():
    cursor.execute('EXEC DisplayInvoiceOrder ?',int(input("Please Enter Invoice ID:")))   
    orders=pd.DataFrame([list(i) for i in cursor.fetchall()],columns=['Invoice Date','Product Name','Quantity','Total Amount'])
    print(orders)

def Customer_Invoice():
    cursor.execute('EXEC DisplayCustomerOrder ?',int(input("Please Enter Customer Mobile No:")))   
    orders=pd.DataFrame([list(i) for i in cursor.fetchall()],columns=['Invoice ID','Invoice Date','Invoice Amount'])
    print(orders)



cart=[]
def sales(cart,id):
    productid = int(input("Please enter Product Id: "))
    quantity = int(input("Please enter Quantity: "))
    name_price=calculate(productid,quantity,inventory())
    cart_item=(productid,name_price[0],quantity,name_price[1],name_price[1]*quantity)
    cart.append(list(cart_item))
    temp_cart=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
    print(temp_cart)
    total=[i[4] for i in cart ]
    total=sum(total)
    print("Total = {}".format(total))
    choice=input("Do You want add more??? Y/N?")
    if choice=='y' or choice=='Y':
        sales(cart,id)
    else:
        cart_df=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
        print(cart_df)
        cursor.execute('EXEC InsertOrder ?,?',id,total)
        cursor.commit()
        cursor.execute('SELECT max(invoice_id) from Invoice')
        invoiceid=cursor.fetchval()
        for i in cart:
            cursor.execute('UPDATE Product set Available_quantity=Available_quantity-? WHERE Product_id=?',i[2],i[0])
            cursor.commit()
            cursor.execute('EXEC InsertOrderDetail ?,?,?,?',invoiceid,i[0],i[2],i[4])
            cursor.commit()
        print("\t\t\t\t\ttotal :{}".format(total))
        cursor.close()


def customer():
    global customer_list
    cursor.execute('SELECT * FROM customer')
    customer_list=[list(i) for i in cursor.fetchall()]
    customer_df=pd.DataFrame(customer_list,columns=['Customer_id','Customer Name','Mobile No'])
    return customer_df
customer()



def check_customer():
    mobileno = input("Please enter customer mobile no: ")
    for i in customer_list:
        if i[2]==mobileno:
         return i[0]
    return False


def display():
    print("1. Sales")
    print("2. Out of Stock")# if Quantity <=Reorder :
    print("3. Orders")
    print("4. Customers")
    choice = int(input("Please Enter Choice :"))
    if choice==1:
        id=check_customer()
        if id:
            sales(cart,id)
        else:
            print("Customer Not Found")
            add_customer = input("Do You want add customer??? Y/N?")
            if add_customer=='y' or add_customer=='Y':
                Name = input("Enter customer Name :")
                Mobile = input("Enter customer Mobile:")
                cursor.execute('EXEC AddCustomer ?,?',Name,Mobile)
                cursor.commit()
            else:
                display()   
    if choice == 2:
        cursor.execute('EXEC out_of_stock')
        out= [list(i)for i in cursor.fetchall()]
        out=pd.DataFrame(out, columns=['product id','Product name','Product category','Available quantity','Price','Reorder level'])
        print(out)
    
    if choice==3:
        orders()

    if choice == 4:
        print(customer())


display()