CREATE DATABASE Project_Inventory;

CREATE TABLE [Product] (
  [Product_id] int PRIMARY KEY,
  [Product_name] varchar(255),
  [Product_category] varchar(64),
  [Available_quantity] int,
  [price] int
)
GO

ALTER TABLE Product 
ADD Reorder_Level INT ;

--Insert into Product([Reorder_Level])
--Values (10 ), (10) ,(10) , (10), (10) ,(10) , (10) , (10), (10 ), (10) ,(10) , (10), (10) ,(10) , (10) , (10), (10) , (10) , (10) , (10);

SELECT * FROM Product;

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
  [Invoice_id] int PRIMARY KEY,
  [Customer_id] int,
  [Product_id] int,
  [Quantity] int,
  [Invoice_amount] int
)
GO

Insert into Invoice([Invoice_id] , [Customer_id] , [Product_id] , [Quantity] , [Invoice_amount])
Values (101 , 501 , 10 , 5 , 100),
(102 , 502 , 3  , 1 , 80000),
(103 , 503 , 4 , 1 , 30000),
(104 , 504 , 8 , 5 , 4000),
(105 , 505 , 5 , 10 , 5000);

SELECT * FROM Invoice;

CREATE TABLE [Purchase] (
  [Purchase_id] int PRIMARY KEY,
  [Product_id] int,
  [Quantity] int,
  [purchase_date] date,
  [expiry_date] date
)
GO

SELECT * FROM Purchase;



CREATE TABLE [Customer] (
  [Customer_id] int PRIMARY KEY,
  [customer_name] varchar(55)
)
GO

Select * from Customer;

Insert into Customer([Customer_id]  , [customer_name])
values( 201 , 'Pooja'),
(202 , 'Sayli'),
(203 , 'Uzaif'),
(204 , 'Mayur'),
(205 , 'Rishabh');

Select * from Customer;

CREATE TABLE [Invoice_details] (
  [Customer_id] int,
  [Invoice_id] int,
  [total_amount] int
)
GO

ALTER TABLE [Purchase] ADD FOREIGN KEY ([Purchase_id]) REFERENCES [Product] ([Product_id])
GO

ALTER TABLE [Customer] ADD FOREIGN KEY ([Customer_id]) REFERENCES [Invoice_details] ([Customer_id])
GO

ALTER TABLE [Customer] ADD FOREIGN KEY ([Customer_id]) REFERENCES [Invoice] ([Customer_id])
GO

ALTER TABLE [Purchase] ADD FOREIGN KEY ([Product_id]) REFERENCES [Invoice] ([Product_id])
GO

ALTER TABLE [Invoice_details] ADD FOREIGN KEY ([Invoice_id]) REFERENCES [Invoice] ([Invoice_id])
GO
