import os,time
import pyodbc
# # # Connecting With Database
conn = pyodbc.connect('Driver={SQL Server};'
                      'SERVER=ZIL1180\MSSQLDEV2019;'
                      'DATABASE=Inventory;'
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
