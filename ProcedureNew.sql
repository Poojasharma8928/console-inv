ALTER PROCEDURE InsertOrder
@CustomerID int,@InvoiceAmount int
as
begin
INSERT INTO Invoice(Customer_id,Invoice_Date,Invoice_amount) values(@CustomerID,GETDATE(),@InvoiceAmount)
end
begin
select SCOPE_IDENTITY() ;
end

SELECT * FROM Invoice_details
SELECT * FROM Customer;

select * from Invoice

Create PROCEDURE InsertOrderDetail
@Invoice_details_id int , @InvoiceID int,@ProductId int,@Quantity int,@totalAmount int
AS
BEGIN
INSERT INTO Invoice_details(Invoice_details_id , Invoice_id , Product_id ,Quantity,total_amount) 
VALUES (@Invoice_details_id, @ProductId,@InvoiceID,@Quantity,@totalAmount)
END
