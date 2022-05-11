CREATE DATABASE Inventory;

CREATE TABLE [Product] (
  [Product_id] int PRIMARY KEY,
  [Product_name] varchar(255),
  [Product_category] varchar(64),
  [Available_quantity] int,
  [price] int
)
GO
Alter table Product
ADD Reorder_level Int;

Insert into Product([product_id] , [product_name] , [product_category] , [available_quantity] ,[Price])
Values (1 , 'Mobile' , 'Electronic' , 35 , 20000),
(2 , 'Laptop' , 'Electronic' , 30 , 55000),
(3 , 'Tablet' , 'Electronic' , 25 , 80000),
(4 , 'TV' , 'Electronic' , 30, 45000),
(5 , 'Tshirt', 'Fashion' , 50 , 500),
(6 , 'Jeans' , 'Fashion' , 50 , 1000),
(7 , 'Sarees' , 'Fashion' , 40 , 2000),
(8 , 'Kurti' , 'Fashion' , 35 , 800),
(9 , 'Buiscuits' , 'Grocery' , 30 , 35),
(10 , 'Chips' , 'Grocery' , 30 , 20),
(11 , 'Dry Fruits' , 'Grocery' , 45 , 500),
(12 , 'Oil_Packet' , 'Grocery' , 20 , 150),
(13 , 'Maggie' , 'Grocery' , 45, 50),
(14 , 'Apples' , 'Fruits' , 50 , 50),
(15, 'Bananas' ,'Fruits' , 30 , 60),
(16, 'Pineapple' , 'Fruits' , 25 , 100),
(17 , 'Grapes' , 'Fuits' , 50 , 120),
(18 , 'Pencil Box' , 'Stationary', 50 , 100),
(19, 'Pen Box' ,'Stationary' , 25 , 120),
(20 , 'Books' , 'Stationary' , 20 , 120);

SELECT * FROM Product;


CREATE TABLE [Invoice] (
  [Invoice_id] int IDENTITY(1,1)  PRIMARY KEY,
  [Customer_id] int,
  [Invoice_amount] int,
  [Invoice_Date] Date
)
GO

alter table Invoice 
add  Mode_of_transaction Char(15)

SELECT * FROM Invoice

CREATE TABLE [Purchase] (
  [Purchase_id] int IDENTITY(1,1) PRIMARY KEY,
  [Supplier_id] int,
  [purchase_date] date,
  [Purchase_Amount] int
)
GO

ALTER TABLE Purchase 
Drop column Supplier_id




SELECT * FROM Purchase

CREATE TABLE Purchase_Details (
[Purchase_DetailsID] int IDENTITY(1,1) PRIMARY KEY ,
[Purchase_id] int ,
[Product_id] int ,
[Quantity] int ,
[price] int , 
[Expiry_Date] Date
)

alter table Purchase_details
add Supplier_id int 

SELECT * FROM Purchase_Details

CREATE TABLE [Customer] (
  [Customer_id] int Identity(1,1) PRIMARY KEY,
  [customer_name] varchar(55),
  [Customer_MobileNo] Char(10)
)
GO

Create table Supplier( Supplier_id int  , 
Product_id int , Price int)



Insert into Supplier([Supplier_id] , [Product_id] , [Price]) VALUES( 1 , 1 , 18000),
(1 , 2 , 53000), (1 , 3 , 78000),
(1 , 4 , 43000) , (2 , 5 , 300) , (2 ,6, 800) , (2 , 7 , 1800) , (2 , 8 , 600), 
(3 , 9 , 30) , (3 , 10 , 15) , (3 , 11 , 450) , (3 , 12 , 120) , (3 , 13 , 40) , (4 , 14 , 40) , (4, 15 , 50) , (4 , 16 , 80) , (4 , 17 , 100),
(5 , 18 , 70) , (5 , 19 , 90) , (5 , 20 , 90)

SELECT * FROM Supplier

Insert into Customer( [customer_name] , [Customer_MobileNo])
values(  'Pooja' , 9359909579),
( 'Sayli' , 9876543210),
( 'Uzaif', 7219624662 ),
( 'Mayur' , 8888305737),
( 'Rishabh' , 7743834334);
 
 Select * from Customer;

CREATE TABLE [Invoice_details] (
  [Invoice_details_id] int IDENTITY(1,1) PRIMARY KEY,
  [Product_id] int,
  [Invoice_id] int,
  [Quantity] int,
  [total_amount] int
)
GO

select * from Invoice_details

-- Added primary key for all tables
ALTER TABLE Product 
ADD Constraint PK_Product PRIMARY KEY (Product_id)

ALTER TABLE Purchase
ADD Constraint PK_Purchase PRIMARY KEY (Purchase_id)

ALTER TABLE Invoice
ADD Constraint PK_Invoice PRIMARY KEY (Invoice_id)

ALTER TABLE Invoice_details
ADD Invoice_details_id int NOT NULL

ALTER TABLE Invoice_details
ADD Constraint PK_Invoice_details PRIMARY KEY (Invoice_details_id)

ALTER TABLE Customer
ADD Constraint PK_customer PRIMARY KEY (Customer_id)

-- Added Foreign key for all tables
ALTER TABLE Invoice_details
ADD Constraint FK_ProductInvoice_details
Foreign key (Product_id) REFERENCES Product(Product_id)


ALTER TABLE dbo.Invoice
ADD Constraint FK_CustomerInvoice
Foreign key (Customer_id) REFERENCES Customer(Customer_id)

ALTER TABLE Invoice_details
ADD Constraint FK_InvoiceInvoice_details
Foreign key (Invoice_id) REFERENCES Invoice(Invoice_id)

ALTER TABLE Purchase_Details
ADD Constraint FK_Purchase_DetailsPurchase
Foreign key (Purchase_id) REFERENCES Purchase(Purchase_id)

ALTER TABLE Purchase_Details
ADD Constraint FK_Purchase_DetailsProduct
Foreign Key (Product_id) REFERENCES Product(Product_id)








