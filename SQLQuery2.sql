/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Product_id]
      ,[Product_name]
      ,[Product_category]
      ,[Available_quantity]
      ,[price]
      ,[Reorder_Level]
  FROM [Project_Inventory].[dbo].[Product]