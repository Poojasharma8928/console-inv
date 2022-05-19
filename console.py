import os,time
import QRConnection
os.system('cls')
import pandas as pd
import connection
os.system('cls')
import re
# # # Connecting With Database

# # #Opening A Cursor
cursor=connection.conn.cursor()

#Fetching All Products from inventory
cursor.execute("SELECT * FROM Product")
products=[list(i) for i in cursor.fetchall()]


def inventory():
    cursor.execute("SELECT * FROM Product")
    products=[list(i) for i in cursor.fetchall()]
    global df_inventory
    df_inventory=pd.DataFrame(products,columns=["Product_Id","Product_Name","Category","Available Quantity","Price","Reorder Level"])
    # print(df)
    return products
inventory()    
def calculate(productid,quantity,products):
    for i in products:
        if i[0]==productid:
            return i[1],i[4],i[4]*quantity

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
        if int(input("Press 1 for Specific Invoice Details: "))==1:
            InvoiceDetail()


def InvoiceDetail():
    cursor.execute('EXEC DisplayInvoiceOrder ?',int(input("Please Enter Invoice ID:")))   
    orders=pd.DataFrame([list(i) for i in cursor.fetchall()],columns=['Invoice Date','Product Name','Quantity','Total Amount'])
    print(orders)
    

def Customer_Invoice():
    cursor.execute('EXEC DisplayCustomerOrder ?',int(input("For Invoice Please Enter Customer Mobile No:")))   
    orders=pd.DataFrame([list(i) for i in cursor.fetchall()],columns=['Invoice ID','Invoice Date','Invoice Amount'])
    print(orders)

def removecart(cart):
    productid=int(input("Please Enter Product Id: "))
    for i in cart:
        if (i[0]==productid):
            cart.remove(i)
            cart_df=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
            print(cart_df)
            choice=int(input("1.\tADD\n2.\tREMOVE\n3.\tCheckout \t"))
            if choice==1:
                sales(cart,id)
            if choice==2:
                removecart(cart)
    
def init_cart():
    global cart
    cart=[]
init_cart()
def sales(cart,id):
    productid = int(input("Please enter Product Id: "))
    for i in inventory():
        if i[0]==productid:
            while True:
                quantity = int(input("Please enter Quantity: "))
                if quantity<int(i[3]):
                    break
                else:
                    print("Not Enough Stock")
        
    name_price=calculate(productid,quantity,inventory())
    cart_item=(productid,name_price[0],quantity,name_price[1],name_price[2])
    cart.append(list(cart_item))
    temp_cart=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
    print(temp_cart)
    total=[i[4] for i in cart ]
    total=sum(total)
    print("\t\t\t\t\tTotal :{}".format(total))
    choice=int(input("1.\tADD\n2.\tREMOVE\n3.\tCheckout \t"))
    if choice==1:
        sales(cart,id)
    if choice==2:
        removecart(cart)
        total=[i[4] for i in cart]

    else:
        cart_df=pd.DataFrame(cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
        print(cart_df)
        print("1. Cash \n2.UPI")
        mode = int(input("Please Select Mode of Transaction: "))
        if mode==1:
            mode='Cash'
        elif mode==2:
            mode='UPI'
            QRConnection.QR(total)

        cursor.execute('EXEC InsertOrder ?,?,?',id,total,mode)
        cursor.commit()
        cursor.execute('SELECT max(invoice_id) from Invoice')
        invoiceid=cursor.fetchval()
        for i in cart:
            cursor.execute('UPDATE Product set Available_quantity=Available_quantity-? WHERE Product_id=?',i[2],i[0])
            cursor.commit()
            cursor.execute('EXEC InsertOrderDetail ?,?,?,?',invoiceid,i[0],i[2],i[4])
            cursor.commit()
        print("\t\t\t\t\ttotal :{}".format(total))
        init_cart()
        display()

def addcustomer(Name,Mobile):
    cursor.execute('EXEC AddCustomer ?,?',Name,Mobile)
    cursor.commit()
    print("Customer Added Successfully.")
    display()

def customer():
    global customer_list
    cursor.execute('SELECT * FROM customer')
    customer_list=[list(i) for i in cursor.fetchall()]
    customer_df=pd.DataFrame(customer_list,columns=['Customer_id','Customer Name','Mobile No'])
    return customer_df
customer()



def check_customer():
    while True:
        Mobile=input("Customer Mobile NO.:")
        if valid_mobile(Mobile):
            break
        else:
            print("Invalid")
    for i in customer_list:
        if i[2]==Mobile:
         return i[0]
    return False

def calculate_purchase(productid,quantity):
    cursor.execute('EXEC CalculatePurchase ?,?',productid,quantity)
    return cursor.fetchone()



def purchase(purchase_cart):
        productid = int(input("Please enter Product Id you want to purchase: "))
        quantity = int(input("Please enter No. of Quantity you want to purchase: "))
        name_price=calculate_purchase(productid,quantity)
        purchase_item=(productid,name_price[1],quantity,name_price[2],name_price[3])
        purchase_cart.append(list(purchase_item))
        temp_purchase_cart=pd.DataFrame(purchase_cart,columns=['Product Id','Product Name','Quantity','Price','Total'])
        print(temp_purchase_cart)
        total=[i[4] for i in purchase_cart ]
        total=sum(total)
        print("\t\t\t\t\ttotal :{}".format(total))
        choice=input("Do You want add more??? Y/N?")
        if choice=='y' or choice=='Y':
            purchase(purchase_cart)
        else:
            cursor.execute('exec PurchaseOrder ?',total)
            cursor.commit()
            cursor.execute('SELECT MAX(Purchase_Id) From Purchase')
            purchaseid=cursor.fetchval()
            for i in purchase_cart:
                cursor.execute('exec PurchaseOrderDetails  ?,?,?,?',purchaseid,i[0],i[2],i[4])
                cursor.commit()
            print("\t\t\t\t\ttotal :{}".format(total))
            display()

def valid_name(name):
    pat = re.compile(r"[A-Za-z' ']+")
    # Prompts the user for input string
    # Checks whether the whole string matches the re.pattern or not
    if re.fullmatch(pat,name):
        return True

#Contact Number Validation
def valid_mobile(mobile):
    result=re.fullmatch(r'\d{10}',mobile)
    if result:
        return True      



def display():
    # os.system('color 2')
    cursor.execute('EXEC out_of_stock')
    out= [list(i)for i in cursor.fetchall()]
    print("1. Sales\n")
    if out:
        print("2. Out of Stock [*]\n")# if Quantity <=Reorder :
    else:
        print("2. Out of Stock\n")# if Quantity >=Reorder :
    print("3. Orders\n")
    print("4. Customers\n")
    print("5. Purchase\n")
    print("6. Inventory\n")
    choice = int(input("Please Enter Choice :"))
    if choice==1:
        id=check_customer()
        if id:
            sales(cart,id)
        else:
            print("Customer Not Found !\n")
            addcustomer(input("Enter Customer Name:"),int(input("Enter Mobile No.:")))

    if choice == 2:
        if out:
            os.system('cls')
            print("\t\t\t\tOut of Stock Products")
            out=pd.DataFrame(out, columns=['product id','Product name','Product category','Available quantity','Price','Reorder level'])
            print(out)
            print("\n")
            display()
        else:
            os.system('cls')
            print("\nNo Product Out Of Stock\n")
            display()
    
    if choice==3:
        orders()
        display()
    
    if choice==6:
        os.system('cls')
        inventory()
        print(df_inventory)
        display()

    if choice == 4:
        os.system('cls')
        print(customer())
        Customer_Invoice()
        display()       
    if choice==5:
        os.system('cls')
        purchase_cart=[]
        purchase(purchase_cart)
        display()
display()