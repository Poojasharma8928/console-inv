ALTER PROCEDURE InsertOrder
@CustomerID int,@InvoiceAmount int
as
begin
INSERT INTO Invoice(Customer_id,Invoice_Date,Invoice_amount) values(@CustomerID,GETDATE(),@InvoiceAmount)
end
begin
select SCOPE_IDENTITY() as ID ;
end
exec InsertOrder 2,2000
exec InsertOrder 2,5000


select * from Customer
exec InsertOrderDetail 2,5,6,64000

SELECT * FROM Invoice
SELECT * FROM Invoice_details

DELETE Invoice
DELETE Invoice_details

ALTER PROCEDURE InsertOrderDetail
@InvoiceID int,@ProductId int,@Quantity int,@totalAmount int
AS
BEGIN
INSERT INTO Invoice_details(Invoice_id , Product_id ,Quantity,total_amount) 
VALUES (@InvoiceID,@ProductId,@Quantity,@totalAmount)
END

insert into Invoice_details(Invoice_id,Product_id,Quantity,total_amount) values (1,5,6,64000)

CREATE PROCEDURE AddCustomer @Customer_name varchar(100),@Mobile int
AS
BEGIN
INSERT INTO Customer(customer_name,Customer_MobileNo) VALUES (@Customer_name,@Mobile)
END

exec AddCustomer 'Test',1234567890

select * from Product

CREATE PROCEDURE CustomerOrder 
@CustomerID int
AS
BEGIN
SELECT 
END

SELECT Invoice.Invoice_id,customer_name,Product_name,Invoice_Date From Invoice
LEFT JOIN Customer C ON  Invoice.Customer_id=C.Customer_id
LEFT JOIN Invoice_details ON Invoice_details.Invoice_id=Invoice.Invoice_id
LEFT JOIN Product ON Product.Product_id=Invoice_details.Product_id


--Invoice For All
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


ALTER PROCEDURE DisplayCustomerOrder @Mobile numeric
AS
BEGIN
SELECT Invoice_id,Invoice_Date,Invoice_amount FROM Invoice
LEFT JOIN Customer C ON Invoice.Customer_id=C.Customer_id
WHERE C.Customer_MobileNo=@Mobile
END



EXEC DisplayCustomerOrder 7219624662



select * from Invoice
select * from Product