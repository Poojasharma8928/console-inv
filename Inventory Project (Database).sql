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


SELECT * FROM Invoice

CREATE TABLE [Purchase] (
  [Purchase_id] int PRIMARY KEY,
  [Product_id] int,
  [Quantity] int,
  [purchase_date] date,
  [expiry_date] date
)
GO

CREATE TABLE [Customer] (
  [Customer_id] int PRIMARY KEY,
  [customer_name] varchar(55)
)
GO

Alter table Customer
Add Customer_MobileNo Char(10);

Insert into Customer([Customer_id]  , [customer_name])
values( 201 , 'Pooja'),
(202 , 'Sayli'),
(203 , 'Uzaif'),
(204 , 'Mayur'),
(205 , 'Rishabh');
 
 Select * from Customer;

CREATE TABLE [Invoice_details] (
  [Invoice_details_id] int,
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

ALTER TABLE Purchase
ADD Constraint FK_PurchaseProduct
Foreign key (Product_id) REFERENCES Product(Product_id)


ALTER TABLE Invoice ADD Customer_id INT





