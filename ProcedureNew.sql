create PROCEDURE InsertOrder
@CustomerID int,@InvoiceAmount int
as
begin
INSERT INTO Invoice(Customer_id,Invoice_Date,Invoice_amount) values(@CustomerID,GETDATE(),@InvoiceAmount)
end
begin
select SCOPE_IDENTITY() ;
end

exec InsertOrder 2,5000

exec InsertOrderDetail 2,5,6,64000

SELECT * FROM Invoice
SELECT * FROM Invoice_details

CREATE PROCEDURE InsertOrderDetail
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
