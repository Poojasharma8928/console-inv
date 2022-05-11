-- Insertorder procedure gor invoice


ALTER PROCEDURE InsertOrder
@CustomerID int,@InvoiceAmount int , @Mode_of_transaction char(15)
as
begin
INSERT INTO Invoice(Customer_id,Invoice_Date,Invoice_amount , Mode_of_transaction) values(@CustomerID,GETDATE(),@InvoiceAmount , @Mode_of_transaction)
end
begin
select SCOPE_IDENTITY() ;
end

exec InsertOrder 2,5000 , "Cash"

exec InsertOrderDetail 2,5,6,64000

SELECT * FROM Invoice
SELECT * FROM Invoice_details
DELETE Invoice
DELETE Invoice_details

-- Insertorderdetails procedure for Invoicedetails
ALTER PROCEDURE InsertOrderDetail
@InvoiceID int,@ProductId int,@Quantity int,@totalAmount int
AS
BEGIN
INSERT INTO Invoice_details(Invoice_id , Product_id ,Quantity,total_amount) 
VALUES (@InvoiceID,@ProductId,@Quantity,@totalAmount)
END


--insert into Invoice_details(Invoice_id,Product_id,Quantity,total_amount) values (1,5,6,64000) (Manually insertion)
-- Add customer Procedure for Customer table
ALTER PROCEDURE AddCustomer @Customer_name varchar(100),@Mobile Numeric
AS
BEGIN
INSERT INTO Customer(customer_name,Customer_MobileNo) VALUES (@Customer_name,@Mobile)
END

select * from Purchase

CREATE PROCEDURE DisplayOrders
AS
BEGIN
SELECT Invoice_id, customer_name,Invoice_amount,Invoice_Date FROM Invoice
LEFT JOIN Customer C ON Invoice.Customer_id=C.Customer_id
END

EXEC DisplayOrders

CREATE PROCEDURE DisplayInvoiceOrder @InvoiceID int
AS
BEGIN
SELECT Invoice_Date,Product_name,Quantity, total_amount FROM Invoice_details
LEFT JOIN Invoice ON Invoice_details.Invoice_id=Invoice.Invoice_id
LEFT JOIN Customer C ON Invoice.Customer_id=C.Customer_id
LEFT JOIN Product P ON Invoice_details.Product_id=P.Product_id
WHERE Invoice.Invoice_id=@InvoiceID
END

EXEC DisplayInvoiceOrder 13


CREATE PROCEDURE DisplayCustomerOrder @Mobile numeric
AS
BEGIN
SELECT Invoice_id,Invoice_Date,Invoice_amount FROM Invoice
LEFT JOIN Customer C ON Invoice.Customer_id=C.Customer_id
WHERE C.Customer_MobileNo=@Mobile
END



EXEC DisplayCustomerOrder 7219624662








-- Outofstock procedure
create procedure out_of_stock
as
BEGIN
select * from Product
where Available_quantity < Reorder_Level
END
exec out_of_stock 



-- Procedure for PurchaseOrder

Alter PROCEDURE PurchaseOrder
@Purchase_Amount int
as
begin
INSERT INTO Purchase(purchase_date,Purchase_Amount) values(GETDATE(),@Purchase_Amount)
end
begin
select SCOPE_IDENTITY() ;
end

exec PurchaseOrder 2 , 100

select * from Invoice_details

select * from Purchase_Details
select * from Purchase


--Procedure for PurchaseOrderdetais
CREATE PROCEDURE PurchaseOrderDetails
@Purchase_id int,@ProductId int,@Quantity int,@Price int 
AS
BEGIN
INSERT INTO Purchase_Details(Purchase_id , Product_id ,Quantity,price ) 
VALUES (@Purchase_id,@ProductId,@Quantity,@Price )
END

exec PurchaseOrderDetails 1 ,2 , 5 , 500




select * from dbo.Supplier


CREATE PROCEDURE CalculatePurchase 
@Product_Id int, @Purchase_Quantity int
AS
BEGIN

select P.Product_id,Product_name,S.Price,@Purchase_Quantity*S.Price as Total from Product P
INNER JOIN Supplier S ON P.Product_id=S.Product_id
WHERE P.Product_id=@Product_Id

END

EXEC CalculatePurchase 5,6