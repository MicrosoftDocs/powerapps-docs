<properties
	pageTitle="Working with tables | Microsoft PowerApps"
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

# Working with tables and records in PowerApps #

Tables and records help organize related information:

-  Records hold information about a single person, place, or thing.  For example, a **Customer** record might have **Name**, **Email**, and **Phone** properties.  

-  Tables hold multiple records, each with a consistent set of properties.  For example, a **Customers** table may hold 10 **Customer** records.  In a table, the consistent properties of the records are known as columns.

In PowerApps, tables and records can be calculated just as numbers are.  Functions can take tables and records as arguments and also return them.  

Tables of information appear in a wide variety of systems, including Microsoft Excel, SharePoint lists, and SQL Server, to name but a few.  PowerApps use a [data source](working-with-data-sources.md), which is an extended table, to read and write information to an external source.  You can also create a [collection](working-with-data-sources.md#collections) within an app to hold a temporary table.

## Elements of a table ##

![](media/working-with-tables/elements-of-a-table.png)

### Records ###

Each record contains detailed information for a person, place, or thing.  In the above example, three records are displayed horizontally, one each for the products Chocolate, Bread, and Water.  For each product, price and quantity properties are available.

Records can be used by themselves in formulas, outside of a table's context.  You can write a record in a formula by using curly braces.  For example, **{ Name: "Strawberries", Price: 7.99 }** is a record that and has no association with a table.

You may have referred to records as "rows" or "items" in other tools.

### Properties ###

A property is an individual piece of information for a record.

Just as with controls, you access a property of a record by using the **!** [operator](operators.md) on the record.  For example, **First(Products)!Name** would return the **Name** property for the first record of the "Chocolate" table.

A property can contain another record or table.  You can nest as many levels of records and tables as you want.

### Columns ###

Columns refer to the same properties for each record of a table.  In the above example, each product has a price property, and that price is in the same column for all products.  The above table has four columns, shown vertically:

- **Product**

- **Price**

- **Quantity on Hand**

- **Quantity on Order**.

The column's name is the same as the properties in that column.

All values within a column share a common data type.  In the above example, the "Quantity on Hand" column always contains a number and can't contain a string, such as "12 units," for one record.  The value of any property may also be *blank*.  

You may have referred to columns as "fields" in other tools.

### Table ###

A table comprises multiple records, each with multiple properties that have consistent names across the records.

Any table that's stored in a service or a collection has a name, which you use to refer to the table and pass it to functions that take tables as arguments.  Tables can also be the result of a function or a formula.

As in the following example, you can express a table in a formula by using the **[Table](function-table.md)** function with a set of records, which you express in curly braces:

**Table( { Value: "Strawberry" }, { Value: "Vanilla" } )**

You can also define a single-column table with square brackets.  An equivalent way to write the above:

**[ "Strawberry", "Vanilla" ]**

## Table formulas ##

In PowerApps, formulas calculate with strings and numbers just as they do in Excel.  A label displays **4** if the user types **2** into **TextBox1** and the **Text** property of the label is set to this formula:<br>**TextBox1!Text * 2**<br>If the user changes the value in the text box to **4**, the label will display **8** as the formula recalculates.

The same is true for tables and records.  Tables and records are stand-alone values and can be the result of a function or formula.  You can also pass them as arguments.  Just as with numbers, formulas that involve tables and records are automatically recalculated as the underlying table or record changes.

Let's walk through some simple examples.

1. If you place a textual gallery on a screen, it brings with it a sample data source named **TextualGallerySample**, which as a table can be used in the **Items** property of the gallery.  Some controls have been rearranged and enlarged for illustration purposes.

	![](media/working-with-tables/gallery-items.png)

2. The **Items** property can be not only the name of a data source but also a formula that returns a table.  To sort this gallery based on the number at the end of the **Heading** column, use the **[Sort](function-sort.md)** function.  **[Sort](function-sort.md)** takes a table as its first argument and returns a table.

	![](media/working-with-tables/gallery-items-sort.png)

3. Going one step further, show only the first two records in the gallery by using the **[FirstN](function-first-last.md)** function.  This function also takes a table as its first argument and returns a table.  In our example, the base data source is passed through **[Sort](function-sort.md)**, passed through **[FirstN](function-first-last.md)**, and then displayed in the gallery.  Note that we're seeing the first two records of the sorted table.

	![](media/working-with-tables/gallery-items-sort-firstn.png)

### Table functions and control properties ###

If a table is provided as an argument, many functions in PowerApps return a table.  Note that these functions transform the original table to create a second table as a result. They don't modify the original table even if it's a data source.

- **[Sort](function-sort.md)**, **[Filter](function-filter-lookup.md)** - Sorts and filters records.
- **[FirstN](function-first-last.md)**, **[LastN](function-first-last.md)** - Returns the first N or last N records of the table.
- **[Abs](function-numericals.md)**, **[Sqrt](function-numericals.md)**, **[Round](function-round.md)**, **[RoundUp](function-round.md)**, **[RoundDown](function-round.md)** - Arithmetic operations on each record of a single-column table, resulting in a single-column table of results.
- **[Left](function-left-mid-right.md)**, **[Mid](function-left-mid-right.md)**, **[Right](function-left-mid-right.md)**, **[Replace](function-replace-substitute.md)**, **[Substitute](function-replace-substitute.md)**, **[Replace](function-replace-substitute.md)**, **[Trim](function-trim.md)**, **[Lower](function-lower-upper-proper.md)**, **[Upper](function-lower-upper-proper.md)**, **[Proper](function-lower-upper-proper.md)** - String manipulations on each record of a single-column table, resulting in a single-column table of strings.
- **[Len](function-len.md)** - For a column of strings, returns a single-column table that contains the length of each string.
- **[Concatenate](function-concatenate.md)** - Concatenates multiple columns of strings, resulting in a single-column table of strings.
- **[AddColumns](function-table-shaping.md)**, **[DropColumns](function-table-shaping.md)**, **[RenameColumns](function-table-shaping.md)**, **[ShowColumns](function-table-shaping.md)** - Column manipulation of the table, resulting in a new table with different columns.
- **[Distinct](function-distinct.md)** - Removes duplicates records.
- **[Shuffle](function-shuffle.md)** - Randomly shuffles records.
- **[HashTags](function-hashtags.md)** - Searches for hash tags in a string.
- **[Errors](function-errors.md)** - Provides error information when you work with a data source.

For tables that use a single column as an argument, you can extract a column from a larger table by using the **[ShowColumns](function-table-shaping.md)** function.  For example, you can calculate a lowercase list of products by using this function:<br>**Lower( ShowColumns( Products, "Name" ) )**<br>If you combine a table with **[AddColumns](function-table-shaping.md)**, **[RenameColumns](function-table-shaping.md)**, and **[DropColumns](function-table-shaping.md)**, you can completely reshape the table as needed.

The data-source functions do modify one of their arguments: the records of the data source. In general, these functions also return the data source's new value as a table.

- **[Collect](function-clear-collect-clearcollect.md)**, **[Clear](function-clear-collect-clearcollect.md)**, **[ClearCollect](function-clear-collect-clearcollect.md)** - Clear, create, and add to a collection.
- **[Update](function-update-updateif.md)**, **[UpdateIf](function-update-updateif.md)** - Updates records.
- **[Remove](function-remove-removeif.md)**, **[RemoveIf](function-remove-removeif.md)** - Deletes records.

The following controls have properties that are tables:

- **Items** - Applies to galleries and listboxes.  Table to display in the gallery.
- **SelectedItems** - Applies to listboxes.  Table of the items the user has selected.

## Record formulas ##

Just like tables, individual records can be calculated, passed to functions, and returned from functions.

Returning to our gallery example above, let's add a label to display information for the currently selected item.

To accomplish this, use the **Gallery1!Selected** property.  This property returns a record that includes the currently selected record's properties from the **Items** table, as well as the controls that are in the gallery's item.  In this case, this record is returned:

![](media/working-with-tables/selected-collection.png)

You can visualize a record or a table by using the **[Collect](function-clear-collect-clearcollect.md)** function to create a collection and then viewing the collection in PowerApps.  In this case, **Collect( SelectedRecord, Gallery1!Selected )** was performed through a temporary button's **OnSelect** formula.

**Body1** and **Subtitle1** are controls in the gallery and included in **Selected** as nested records, which you can drill into by clicking the table icons. **Body** and **Subtitle** are the values taken directly from the incoming **Items** table.

Now that we have the selected record, we can extract individual properties from it with the **!** operator.  Let's display the **Heading** property in a new label:  

![](media/working-with-tables/gallery-selected.png)

This new control uses the formula **Gallery!Selected!Heading**.  We've taken the **Selected** property, which is a record, and extracted the **Heading** property from it.  

Records are also useful as a general-purpose container for related named values.  The **[UpdateContext](function-updatecontext.md)** and **[Navigate](function-navigate.md)** functions use a record to gather the [context variables](working-with-variables.md#context-variables) that are to be updated. The **Updates** property on a gallery gathers the changes to be made to a data source. The **[Patch](function-patch.md)** function is used to update data sources, but can also be used to merge records together.  In these cases, the record was never a part of a table.

### Record functions and control properties ###

Functions that return records:

- **[FirstN](function-first-last.md)**, **[LastN](function-first-last.md)** - Returns the first or last record or records of the table.
- **[Lookup](function-filter-lookup.md)** - Returns the first record from a table that matches one or more criteria.
- **[Patch](function-patch.md)** - Updates a data source or merges records.
- **[Defaults](function-defaults.md)** - Returns the default values for a data source.

Properties that return records:

- **Selected** - Applies to galleries and listboxes. Returns the currently selected record.
- **Updates** - Applies to galleries.  You use this to pull together all the changes that a user makes in a data-entry form.
- **[Update](function-update-updateif.md)** Applies to input controls such as input-text controls and sliders.  Use this to set up individual properties for the gallery to pull together.

## Inline syntax ##

### Records ###

You express records by using curly braces that contain named property values.  For example, you can express the first record in the previous table by using this formula:

**{ Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 }**

This formula can also have embedded formulas within it, as in this example:

**{ Name: First(Products)!Name, Price: First(Products)!Price * 1.095 }**

You can nest records by nesting curly braces, as in this example:

**{ 'Quantity': { 'OnHand': ThisItem!QuantOnHand, 'OnOrder': ThisItem!QuantOnOrder } }**

Enclose each column name that contains a special character, such as a space or a colon, in single quotes.  To use a single quote within a column name, double it.

Note that the value in the Price column doesn't include a currency symbol, such as a dollar sign. That formatting will be applied when the value is displayed.  

### Tables ###

You can create a table by using the **[Table](function-table.md)** function and a set of records. You can express the previous table by using this formula:

**Table( { Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12, 'Quantity on Order': 10 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Bread", Price: 4.95, 'Quantity on Hand': 34, 'Quantity on Order': 0 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Name: "Water", Price: 4.95, 'Quantity on Hand': 10, 'Quantity on Order': 0 } )**

You can also nest tables:

**Table( { Name: "Chocolate",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Quantity History': Table( { Quarter: "Q1", OnHand: 10, OnOrder: 10 },<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Quarter: "Q2", OnHand: 18, OnOrder: 0 } ) } )**

Single-column tables can be created with square brackets containing values.  The resulting table has a single column, named "Value".  **[ 1, 2, 3, 4 ]** is equivalent to **Table( { Value: 1 }, { Value: 2 }, { Value: 3 }, { Value: 4 } )**.
