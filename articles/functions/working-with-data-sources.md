<properties
	pageTitle="PowerApps: Working with Data Sources"
	description="Reference information for working with connections and data sources"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/10/2015"
   ms.author="gregli"/>

# Working with Data Sources #

Data Sources are an extension of [Tables](working-with-tables.md) that use [Connections](file-name.md) to retrieve and store information.  You can use Data Sources to read and write data in Excel workbooks, SharePoint lists, SQL Server tables, and many other data stores.

## Extending Tables ##

As we learned in [Working with Tables](working-with-tables.md), Tables in PowerAops are values, just as a number or a string is a value. Tables are not stored anywhere. The structure and data of a table cannot be modified directly, only derivative tables created through a formula. 

However some of the most interesting tables are stored outside the PowerApp.  PowerApps provides Connections to read and write data in other locations.  Most connections will expose more than one table.  As an author, you will need to select which table to use from a connection.  Once selected, this table becomes a Data Source in the PowerApp.

A Data Source is an extension of a table and can be used in any context that a table is used.  Just like a table, it has records, columns, and properties and can be used in formulas.  In addition, Data Sources have some qualities that go beyond a table:
- It has the same column names and data types as the underlying table in the connection.
- It automatically reads and makes available the records of the underlying table in the connection.  As records change in the underlying table, the Data Source is kept up to date and the author can force a refresh with the **[Refresh](function-refresh.md)** function.
- Records in the Data Source can be created and modified with the **[Patch](function-patch.md)**, **[Collect](function-collect.md)**, and **[Update](function-update.md)** functions.  Changes made to the Data Source are pushed to the underlying table in the connection.
- Records in the Data Source can be removed with the **[Remove](funciotn-remove.md)** function.
- The **[DataSourceInfo](function-datasourceinfo.md)**, **[Defaults](funciton-defautls.md)**, and **[Validate](function-validate.md)** functions can be used to retrieve metadata about the underlying table and to validate that changes to records will be accepted. 
- The Data Source has a Primary Key made up of one or more columns.  Every record of the Data Source can be uniquely identified with this set of properties.

PowerApps cannot be sued to create a table in a connection, the table must already exist.  To create a new table in for example an Excel workbook, you must use Excel to create the table first.   

## Displaying records from a Data Source ##
![](media/working-with-data-sources/reading-from-a-datasource.png)

As we saw with a table, we can use the Items property of a Gallery to browse the items of a Data Source.

1. Create a connection to an Office 365 site.  You can use any connection that supports Data Sources.
2. Add the connection to your app.  You will be asked which table you would like to use from the connection.  In this case, we are using the Customers SharePoint List and the Data Source name will default to **Customers**.
3. Craete a screen.
4. Add a Gallery to the screen.
5. Set the Items property of the Gallery to the Data Source that was added in step 2, named **Customers**.  You can use the **[Order](function-order.md)** function to order the records in the gallery, and the **[Filter](function-filter.md)** function to select which records to show.
6. You will see the Customers SharePoint List displayed in the Gallery.

The SharePoint List could be modified outside of the PowerApp.  The PowerApp will refresh its copy of the Data Source from time to time, but this can also be forced manually by using the **[Refresh](function-refresh.md)** function.

## Creating and Modifying records in a Data Source ##

![](media/working-with-data-sources/writing-to-a-datasource.png)
What differentiates a data source from a table is the ability to write back changes.  

## Screens Working Together ##

![](media/working-with-data-sources/screens-working-together.png)

## Primary Keys ##


## Collections ##

Collections are a special kind of Data Source.  They are local to the app and not backed by a connection.

LoadData
SaveData

Import from Excel


