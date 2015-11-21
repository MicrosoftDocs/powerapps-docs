<properties
	pageTitle="PowerApps: Working with Tables"
	description="Reference information for working with tables, columns, and records"
	services=""
	suite="powerapps"
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

Tables and Records help organize related information:
-  Records hold information about a single person, place, or thing.  For example, a **Customer** record which has **Name**, **Email**, and **Phone** properties.  
-  Tables hold multiple records, each with a consistent set of properties.  For example, a **Customers** table may hold 10 **Customer** records.  In a table, the consistent properties of the records are known as columns.

In PowerApps, tables and records can be calculated just as numbers are.  Functions can take tables and records as arguments and also return them.  

Tables of information appear in a wide variety of systems, including Excel, SharePoint Lists, and SQL Server, to name but a few.  PowerApps use a [data source](working-with-data-sources.md), an extended table, to read and write information to an external source.  [Collections](working-with-data-sources.md) can also be used within a PowerApp to hold a temporary table.
 
## Elements of a Table ##

![](media/working-with-tables/elements-of-a-table.png)

### Records ###

Records contain detailed information for a person, place, or thing.  In the above example, there are three records shown horizontally, one each for the products Chocolate, Bread, and Water.  For each product, price and quantity properties are available.

Records can be used by themselves in formulas, outside of a table's context.  For example, **First(Proudcts)** returns the first record of the above table.  Records can be expressed in formulas using curly braces, for example **{ Name: "Chcocolate" }** or using a formula for the value **{ Price: Cost * 2 }**.

You may have referred to records as "rows" or "items" in other tools.

### Properties ###

Properties refer to each individual piece of information for a record.

Just as with controls, properties of a record are accessed the **!** operator on the record.  For example **First(Products)!Name** would return the **Name** property for the first record of this table: "Chocolate".

A property can contain another record or table.  Records and tables can be nested arbitrarily deep.

### Columns ###

Columns refer to the same properties for each record of a table.  In the above example, each product has a price property, and that price is in the same column for all products.  The above table has four columns shown vertically: **Product**, **Price**, **Quanity on Hand**, and **Quantity on Order**. 

The column's name is the same as the properties in that column.

All values within a column share a common data type.  In the above example, the "Quantity on Hand" column always contains a number and cannot contain a string such as "12 units" for one record.  The value of any property may also be *blank*.  

You may have referred to columns as "fields" in other tools.

### Table ###

A table is made up of multiple records, each with multiple properties that have consistent names across the records.

If a table is stored, in a service or a collection, then it will have a name.  You use this name to refer to the table and pass it to functions that take tables as arguments.  Tables can also be the result of a function or formula.

As an example, you can express a tables in a formulas using the **Table** function with a set of records expressed with curly brace records.  For example: **Table( { Name: "Strawberry" }, { Name: "Vanilla" } )**.

## Table Formulas ##

In PowerApps, formulas calculate with strings and numbers just as they do in Excel.  A label's may display the value of the formula **TextBox!Text * 2** which will display the **4** if the user has entered **2** in the text box.  If the user changes the text box to **4**, then **8** will be displayed in the label as the formulas recalculates.

The same is true for tables and records.  Tables and records are stand alone values and can be the result of a function or formula.  They can also be passed as arguments.  Just as with numbers, formulas involving tables and records are automatically recalculated as the underlying table or record changes.

Let's walk through some simple examples.

1. if you place a textual gallery control on a screen, it brings with it a sample data source named **TextualGallerySample**, which as a table can be used in the **Items** property of the gallery.  Some controls have been rearranged and enlarged for illustration purposes.

	![](media/working-with-tables/gallery-items.png)

2. The **Items** property can not only be the name of a data source, but a formula that returns a table.  To sort this gallery based on the number at the end of the **Heading** column, use the **Sort** function.  **Sort** takes a table as its first argument and returns a table.

	![](media/working-with-tables/gallery-items-sort.png)

3. Going one step further, to show only the first two records in the gallery, use the **FistN** function.  This function also takes a table as its first argument and returns a table.  In our example, the base data source is first passed through **Sort**, and then through **FirstN**, and then it is displayed in the gallery.  Note that we are seeing the first two records of the sorted table.

	![](media/working-with-tables/gallery-items-sort-firstn.png)

### Table Functions and Control Properties ### 

If a table is provided as an argument, many of PowerApps functions return a table.  Note that these functions transform the original table to create a new table as a result, they do not modify the original table even if it is a data source.

- **Sort**, **Filter** - Sorts and filters records. 
- **FirstN**, **LastN** - Returns the first N or last N records of the table.
- **Abs**, **Sqrt**, **Round**, **RoundUp**, **RoundDown** - Arithmetic operations on each record of a single column table, resulting in a single column table of results.
- **Left**, **Mid**, **Right**, **Replace**, **Substitute**, **Replace**, **Trim**, **Lower**, **Upper**, **Proper** - String manipulations on each record of a single column table, resulting in a single column table of strings.
- **Len** - For a column of strings, returns a single column table with the length of each string.
- **Concatenate** - Concatenates multiple columns of strings, resulting in a single column table of strings. 
- **AddColumns**, **DropColumns**, **RenameColumns**, **ShowColumns** - Column manipulation of the table, resulting in a new table with different columns.
- **Distinct** - Removes duplicates records.
- **Shuffle** - Randomly shuffles records.
- **HashTags** - Searches for hash tags in a string. 
- **Errros** - Error information when working with data sources.

For tables that use a single column as an argument, a column can be extracted from a larger table by using the **ShowColumns** function.  For example, a lower case list of products can be calculated with **Lower( ShowColumns( Products, "Name" ) )**.  When combined with **AddColumns**, **RenameCOlumns**, and **DropColumns**, a table can be completely reshaped as needed.

The data source functions do modify one of their arguments: the records of the data source. In general, they also return the data source's new value as a table.

- **Collect**, **Clear**, **ClearCollect** - Clear, create, and add to a collection.
- **Update**, **UpdateIf** - Updates records.
- **Remove**, **RemoveIf** - Deletes records.

The following controls have table valued properties:

- **Items** - Applies to Gallery and Listbox.  Table to display in the gallery.
- **SelectedItems** - Applies to Listbox.  Table of the items the user has selected. 

## Record Formulas ##

Just like tables, individual records can be calculated, passed to functions, and returned from functions.

Returning to our gallery example above, let's add a label to display information for the currently selected item.

To accomplish this, use the **Gallery1!Selected** property.  This property returns a record which includes the currently selected record's properties from the **Items** table, as well as the controls that are in the gallery's item.  In this case, the record returned is:

![](media/working-with-tables/selected-collection.png)

As an author, you can visualize a record or table by creating a **Collection** with the  **Collect** function using the collection viewer in the PowerApps client.  In this case, **Collect( SelectedRecord, Gallery1!Selected )** was performed through a temporary button's **OnSelect** formula. 

**Body1** and **Subtitle1** are controls in the gallery and included in **Selected** as nested records, which you can drill into by clicking on the table icons.  **Body** and **Subtitle** are the values taken directly from the incoming **Items** table.

Now that we have the selected record, we can extra individual properties from it with the **!** operator.  Let's display the **Heading** property in a new label control:  

![](media/working-with-tables/gallery-selected.png)

This new control uses the formula **Gallery!Selected!Heading**.  We have taken the **Selected** property, which is a record, and extracted a single property, the **Heading** property.  

Records are also useful as a general purpose container for related named values.  The **UpdateContext** and **Navigate** functions use a record to gather the context variables that are to be updated. The **Updates** property on a gallery gathers the changes to be made to a data source. The **Patch** function is used to update data sources, but can also be used to merge records together.  In these cases, the record was never a part of a table.

### Record Functions and Control Properties ###

Functions that return records:

- **FirstN**, **LastN** - First or last record of the table.
- **Lookup** - First record from a table that matches a criteria.
- **Patch** - Used to update a data source or merge records.
- **Defaults** - Default values for a data source.

Properties that return records:

- **Selected** - Applies to Gallery and Listbox.  Currently selected record.
- **Updates** - Applies to Gallery.  You use this to pull together all the changes that a user makes to a data entry form.
- **Update** Applies to input controls (Input Text, Slider, etc).  Use this to setup  individual properties for the Gallery to pull together. 

## Inline Syntax ##

### Records ###

Records are expressed using curly braces that contain named property values.  For example, the first record in the table above could be written:

**{ Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 }**

This formula can also have embedded formulas within it, for example:

**{ Name: First(Products)!Name, Price: First(Products)!Price * 1.095 }**

A record can contain nested records by nesting curly braces, for example:

**{ 'Quantity': { 'OnHand': ThisItem!QuantOnHand, 'OnOrder': ThisItem!QuantOnOrder } }**

Column names that contain special characters, such as a space or a colon, can be enclosed in single quotes.  

<!-- TODO: Escaping single quote. -->

Note that the dollar sign does not appear in the Price.  This is formatting that is applied to a number when displayed.  

### Tables ###

Tables can be created with the **[Table](funciton-table.md)** function and a set of records.  The above table could be expressed as:

**Table( { Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Bread", Price: 4.95, 'Quantity on Hand': 34, 'Quantity on Order': 0 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Water", Price: 4.95, 'Quantity on Hand': 10, 'Quantity on Order': 0 } )**

Tables can also be nested:

**Table( { Name: "Chocolate",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Quantity History': Table( { Quarter: "Q1", OnHand: 10, OnOrder: 10 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Quarter: "Q2", OnHand: 18, OnOrder: 0 } ) } )** 







  
  

    
