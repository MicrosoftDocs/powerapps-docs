<properties
	pageTitle="Sort function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Sort function in PowerApps"
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
   ms.date="10/21/2015"
   ms.author="gregli"/>

# Sort function in PowerApps #

Sorts a [table](working-with-tables.md).

## Description ##

The **Sort** function sorts a table based on a formula.  

The formula is evaluated for each [record](working-with-tables.md#records) of the table, and the results are used to sort the table.  You can use [columns](working-with-tables.md#columns) of the table in the formula. The formula must result in a number, a string, or a Boolean value; it can't result in a table or a record.

To sort first by one column and then by another, you embed a **Sort** formula within another. For example, you can use this formula to sort a **Contacts** table first by a **LastName** column and then by a **FirstName** column:<br>
**Sort( Sort( Contacts, LastName ), FirstName )**

A tables is a value in PowerApps, just as a string or a number is. You can specify a table as an argument for a function, and a function can return a table as a result. **Sort** doesn't modify a table; instead it takes a table as an argument and returns a new table that has been sorted. See [working with tables](working-with-tables.md) for more details.

## Syntax ##

**Sort**( *Table*, *Formula* [, *SortOrder* ] )

- *Table* - Required. Table to sort.
- *Formula* - Required. This formula is evaluated for each record of the table, and the results are used to sort the table.  You can reference columns within the table.
- *SortOrder* - Optional. Specify **SortOrder!Descending** to sort the table in descending order. **SortOrder!Ascending** is the default value.

## Examples ##

For the following examples, we'll use the **IceCream** [data source](working-with-data-sources.md), which contains the data in this table:

![](media/function-sort/icecream.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Sort( IceCream, Flavor )** | Sorts **IceCream** by its **Flavor** column. The **Flavor** column contains strings, so the table is sorted alphabetically. By default, the sort order is ascending.  | <style> img { max-width: none; } </style> ![](media/function-sort/icecream-flavor.png) |
| **Sort( IceCream, Quantity )** | Sorts **IceCream** by its **Quantity** column.  The **Quantity** column contains numbers, so the table is sorted numerically.  By default, the sort order is ascending.  | ![](media/function-sort/icecream-quantity-asc.png) |
| **Sort( IceCream, Quantity, SortOrder!Descending )** | Sorts **IceCream** by its **Quantity** column.  The **Quantity** column contains numbers, so the sort is done numerically.  The sort order has been specified as descending.  | ![](media/function-sort/icecream-quantity-desc.png) |
| **Sort( IceCream, Quantity + OnOrder )** | Sorts **IceCream** by the sum of its **Quantity** and **OnOrder** columns for each record individually. The sum is a number, so the table is sorted numerically.  By default, the sort order is ascending.  | ![](media/function-sort/icecream-total.png) |
| **Sort( Sort( IceCream, OnOrder ), Quantity )** | Sorts **IceCream** first by its **OnOrder** column, and then by its **Quantity** column.  Note that "Pistachio" rose above "Vanilla" in the first sort based on **OnOrder**, and then together they moved to their appropriate place based on **Quantity**.  | ![](media/function-sort/icecream-onorder-quantity.png) |

To run these examples yourself, create the **IceCream** data source as a [collection](working-with-data-sources.md#collections):

1. Add a button, and set its **OnSelect** property to this formula:<br>**ClearCollect( IceCream, { Flavor: "Chocolate", Quantity: 100, OnOrder: 150 }, { Flavor:  "Vanilla", Quantity: 200, OnOrder: 20 }, { Flavor: "Strawberry", Quantity: 300, OnOrder: 0 }, { Flavor: "Mint Chocolate", Quantity: 60, OnOrder: 100 }, { Flavor: "Pistachio", Quantity: 200, OnOrder: 10 } )**

1. Preview the app, select the button, and then press Esc to return to the default workspace.

1. Select **Collections** on the **File** menu to display the collection that you just created, and then press Esc to return to the default workspace.

1. Add another button, and set its **OnSelect** property to this formula:<br>
**ClearCollect(SortByFlavor, Sort( IceCream, Flavor ))**

 	The previous formula creates a second collection, named **SortByFlavor**, that contains the same data as **Ice Cream**. However, the new collection contains the data sorted alphabetically by the **Flavor** column in ascending order.

1. Press F5, select the new button, and then press Esc.

1. Select **Collections** on the **File** menu to display both collections, and then press Esc to return to the default workspace.

1. Repeat the last three steps, but change the name of the collection that you want to create, and replace the **Sort** formula with a different formula from the table of examples earlier in this section.
