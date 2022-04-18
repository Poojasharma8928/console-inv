import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ZIL1180\MSSQLDEV2019;'
                      'Database=inventory;'
                      'Trusted_Connection=yes;')

cursor=conn.cursor()

cursor.execute("SELECT * FROM products")
products=[list(i) for i in cursor.fetchall()]
df=pd.DataFrame(products,columns=["Product_Id","Product_Name","Category","Available Quantity","Price"])
print(df)


prod_id = input("Please Enter Product Id")
cursor.execute('SELECT * FROM products where pid=?',prod_id)
stock=[list(i) for i in cursor.fetchall()]
stock_df=pd.DataFrame(stock,columns=["Product_Id","Product_Name","Category","Available Quantity","Price"])
print(stock_df)
quantity = input("Please Enter Quantity: ")
cursor.execute('UPDATE products SET avl_quant=avl_quant+? where pid=?',(quantity,prod_id))
cursor.commit()
cursor.execute('SELECT * FROM products where pid=?',prod_id)
stock=[list(i) for i in cursor.fetchall()]
stock_df=pd.DataFrame(stock,columns=["Product_Id","Product_Name","Category","Available Quantity","Price"])
print(stock_df)

product_id = input("Please Enter Product Id:")
cursor.execute('SELECT * FROM products where pid=?',product_id)
sale=[list(i) for i in cursor.fetchall()]
sale=pd.DataFrame(sale,columns=["Product_Id","Product_Name","Category","Available Quantity","Price"])
print(sale)
quantity = input("Please Enter Quantity: ")
cursor.execute('UPDATE products SET avl_quant=avl_quant-? where pid=?',(quantity,product_id))
cursor.commit()
cursor.execute('SELECT * FROM products where pid=?',product_id)
sale=[list(i) for i in cursor.fetchall()]
sale=pd.DataFrame(sale[0])
print(sale)
