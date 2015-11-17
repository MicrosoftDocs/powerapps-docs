<properties
	pageTitle="PowerApps: Working with Tables"
	description="Reference information for working with tables, columns, and records"
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

# Working with Tables and Records in PowerApps #

Tables make working with a group of related information easier.  They can be found in Excel, SharePoint, SQL Server, and a wide variety of other sources.  They can also be the result of a calculation.  

## Elements of a Table ##

![Elements of a Table](media/working-with-tables/elements-of-a-table.png)

### Records ###

Records contain detailed information for a person, place, or thing.  In the above example, there are three records shown horizontally, one each for the products Chocolate, Bread, and Water.  For each product, price and quantity information is available.

Records can be used by themselves in formulas, outside of a table's context.  For example, **First(Proudcts)** returns the first record of the above table.  Records can be expressed in formulas using curly braces, for example **{ Name: "Chcocolate" }**.

You may have seen records referred to as "rows" or "items" in other tools.

### Columns ###

Columns contain the same kind of information for each record of a table.  In the above example, each product has a price, and that price is in the same column for all products.  The above table has four columns shown vertically: Product, Price, Quanity on Hand, and Quantity on Order. 

Each column is named.  You use this name in formulas to read the value of that column for a record.  In the above example, if this table were held in the Products collection, **First(Products)!Name** would result in "Chocolate", the value of the "Name" column for the first record of the collection.     

All values within a column share a common data type.  In the above example, the "Quantity on Hand" column always contains a number and cannot contain a string such as "12 units".  A value in a column may also be blank.  

You may have referred to columns as "fields" in other tools.

### Properties ###

Properties refer to each individual piece of information for a record.

Just as with controls, properties of a record can be obtained by using the **!** operator in formulas.  

## Formulas ##

In PowerApps, you can write formulas for numbers just as you do in Excel.  A label's **Text** property may use the formula **TextBox!Text * 2** and will display the number **4** if the user has entered 2 in the textbox.  If the user enters 4 in the textbox, then 8 will be displayed in the label as formulas are recalculated.

The same is true for tables and records.  Tables and records can be stand alone values and the result of a function or formula.  They need not be stored anywhere.  Just as with numbers, formulas involving tables and records are automatically recalculated if the underlying table or record changes.  

For example, a gallery's **Items** property may use the formula **Order(Products, Price, Descending)**.  This will sort the Products collection based on Price, and show this sorted list of items in the gallery.  If the price for a product changes, the sort will automatically recalculate and the gallery will show the new result.  

Functions that return Tables include Order, Filter, Collect, and Table.  

Records are similar.  If the price of Chocolate goes up, then **First(Products)!Price** will result in a different value that will propagate throughout any formulas that use it.

Functions that return Records include First, Last, Patch, and Update.

Functions that return a Property include Lookup.

## Syntax ##

Records and tables can be written in a formula as a literal value, just as the number 4 or the string "Hello, World" is written.  

Records can be expressed using curly braces that contain named property values.  For example, the first record in the table above could be written:

**{ Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quanityt on Order': 10 }**

Column names that contain special characters, such as a space or a colon, can be enclosed in single quotes.  TODO: Escaping single quote.

Note that the dollar sign does not appear in the Price.  This is formatting for a number that is applied when it is displayed.  

Tables can be created with the **[Table](funciton-table.md)** function and a set of records.  The above table could be expressed as:

**Table( { Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Bread", Price: 4.95, 'Quantity on Hand': 34, 'Quantity on Order': 0 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Water", Price: 4.95, 'Quantity on Hand': 10, 'Quantity on Order': 0 } )**

The property of a record, or the value of a column, is available with the **!** operator.  For example:

**{ Name: "Chocolate", Price: 3.95 }!Name**

returns the string "Chocolate".

## Displaying a Table ##

Browse Screen, Gallery, bound to Table

Detail screen passed a record from Gallery

Editing -> Working with Data Sources

## Nesting ##

## Shaping a Table ##

AddColumns
DropColumns
RenameColumns
ShowColumns




  
  

    
