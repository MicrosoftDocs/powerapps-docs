<properties
	pageTitle="Sort and SortByColumns functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Sort and SortByColumns functions in PowerApps"
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
   ms.date="04/26/2016"
   ms.author="gregli"/>

# Sort and SortByColumns functions in PowerApps #

Sorts a [table](../working-with-tables.md).

## Description ##

The **Sort** function sorts a table based on a formula.  

The formula is evaluated for each [record](../working-with-tables.md#records) of the table, and the results are used to sort the table.  You can use [columns](../working-with-tables.md#columns) of the table in the formula. The formula must result in a number, a string, or a Boolean value; it can't result in a table or a record.

To sort first by one column and then by another, you embed a **Sort** formula within another. For example, you can use this formula to sort a **Contacts** table first by a **LastName** column and then by a **FirstName** column:  **Sort( Sort( Contacts, LastName ), FirstName )**

The **SortByColumns** function can also be used to sort a table based on one or more columns.

The parameter list for **SortByColumns** provides the names of the columns to sort by and the sort direction per column.  Sorting is performed in the order of the parameters (sorted first by the first column, then the second, and so on).  Column names are specified as strings, requiring double quotes if directly included in the parameter list.  For example, **SortByColumns( CustomerTable, "LastName" )**.

You can combine **SortByColumns** with a **[Drop down](../controls/control-drop-down.md)** or **[List box](../controls/control-list-box.md)** control to enable users to select which column to sort by.

In addition to sorting ascending or descending, **SortByColumns** can sort based on a single column table of values.  For example, you can sort record based on the name of a day of the week by supplying **[ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]** as the sort order.  All records which have **Monday"** will come first, followed by **Tuesday**, and so on.  Records found that do not appear in the sort table are put at the end of the list.

[Tables](../working-with-tables.md) are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **Sort** and **SortByColumn** don't modify a table; instead they take a table as an argument and return a new table that has been sorted.  See [working with tables](../working-with-tables.md) for more details.

## Delegation ##

When possible, PowerApps will delegate filter and sort operations to the data source and page through the results on demand.  For example, when starting an app that shows a **[Gallery](../controls/control-gallery.md)** control filled with data, only the first set of records will be initially brought to the device.  As the user scrolls, additional data will be brought down from the data source.  The result is a faster start time for the app and access to very large data sets.

However, delegation may not always be possible.  Data sources vary on what functions and operators they support while the PowerApps formula language is relatively rich.  If complete delegation of a formula is not possible, the authoring environment will flag the **Filter** or **Sort** formula as a warning.  When possible, consider changing the formula to avoid functions and operators that cannot be delegated.   

PowerApps will delegate what it can, but will only pull down a small set of records to complete the work locally, at most 500 records.  **Filter** and **Sort** will continue to operate, but with a reduced set of records.  What is available in the **[Gallery](../controls/control-gallery.md)** may not be the complete story which could be confusing to users.  Aggregate operations, such as **Sum** and **Average**, will operate on only a portion of the data source and therefore may not give the result that is expected.

Additional limitations on delegation (which we are working to remove):

- At this time, only **Filter**, **Sort**, and **SortByColumns** functions support delegation.  **LookUp** function support will be coming soon.
- For the **Sort** function, the formula can only be the name of a single column and cannot include other operators or functions.
- For the **Filter** function, the formula can include =, <>, <, >, >=, <=, &&, and || operators.  Only names of columns and values that do not depend on the data source can be used.

## Syntax ##

**Sort**( *Table*, *Formula* [, *SortOrder* ] )

- *Table* - Required. Table to sort.
- *Formula* - Required. This formula is evaluated for each record of the table, and the results are used to sort the table.  You can reference columns within the table.
- *SortOrder* - Optional. Specify **SortOrder.Descending** to sort the table in descending order. **SortOrder.Ascending** is the default value.

**SortByColumns**( *Table*, *ColumnName1* [, *SortOrder1*, *ColumnName2*, *SortOrder2*, ... ] )

- *Table* - Required. Table to sort.
- *ColumnName(s)* - Required. The column names to sort on, as strings.
- *SortOrder(s)* - Optional.  **SortOrder!Ascending** or **SortOrder!Descending**.  **SortOrder!Ascending** is the default.  If multiple *ColumnNames* are supplied, all but the last column must include a *SortOrder*.

**SortByColumns**( *Table*, *ColumnName*, *SortOrderTable* )

- *Table* - Required. Table to sort.
- *ColumnName* - Required. The column name to sort on, as strings.
- *SortOrderTable* - Required.  Single column table of values to sort by.

## Examples ##

For the following examples, we'll use the **IceCream** [data source](../working-with-data-sources.md), which contains the data in this table:

![](media/function-sort/icecream.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Sort( IceCream, Flavor )**<br><br>**SortByColumns( IceCream, "Flavor" )** | Sorts **IceCream** by its **Flavor** column. The **Flavor** column contains strings, so the table is sorted alphabetically. By default, the sort order is ascending.  | <style> img { max-width: none; } </style> ![](media/function-sort/icecream-flavor.png) |
| **Sort( IceCream, Quantity )**<br><br>**SortByColumns( IceCream, "Quantity" )** | Sorts **IceCream** by its **Quantity** column.  The **Quantity** column contains numbers, so the table is sorted numerically.  By default, the sort order is ascending.  | ![](media/function-sort/icecream-quantity-asc.png) |
| **Sort( IceCream, Quantity, SortOrder.Descending )**<br><br>**SortByColumns( IceCream, "Quantity", SortOrder.Descending )** | Sorts **IceCream** by its **Quantity** column.  The **Quantity** column contains numbers, so the sort is done numerically.  The sort order has been specified as descending.  | ![](media/function-sort/icecream-quantity-desc.png) |
| **Sort( IceCream, Quantity + OnOrder )** | Sorts **IceCream** by the sum of its **Quantity** and **OnOrder** columns for each record individually. The sum is a number, so the table is sorted numerically.  By default, the sort order is ascending.  Since we are sorting by a formula and not by raw column values, there is no equivalent using **SortByColumns**.  | ![](media/function-sort/icecream-total.png) |
| **Sort( Sort( IceCream, OnOrder ), Quantity )**<br><br>**SortByColumns( IceCream, "OnOrder", Ascending, "Quantity", Ascending )** | Sorts **IceCream** first by its **OnOrder** column, and then by its **Quantity** column.  Note that "Pistachio" rose above "Vanilla" in the first sort based on **OnOrder**, and then together they moved to their appropriate place based on **Quantity**.  | ![](media/function-sort/icecream-onorder-quantity.png) |
| **SortByColumns( IceCream, "Flavor", [&nbsp;"Pistachio",&nbsp;"Strawberry"&nbsp;] )** | Sorts **IceCream** by it's **Flavor** column based on the single column table containing "Pistachio" and "Strawberry".  Records which have a **Flavor** of "Pistachio" will appear first in the result, followed by records that contain "Strawberry".  For values in the **Flavor** column that are not matched, such as "Vanilla", they will appear after the items that were matched.  | ![](media/function-sort/icecream-onflavor-sorttable.png) |

### Step by step ###

To run these examples yourself, create the **IceCream** data source as a [collection](../working-with-data-sources.md#collections):

1. Add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:<br>**ClearCollect( IceCream, { Flavor: "Chocolate", Quantity: 100, OnOrder: 150 }, { Flavor:  "Vanilla", Quantity: 200, OnOrder: 20 }, { Flavor: "Strawberry", Quantity: 300, OnOrder: 0 }, { Flavor: "Mint Chocolate", Quantity: 60, OnOrder: 100 }, { Flavor: "Pistachio", Quantity: 200, OnOrder: 10 } )**

1. Preview the app, select the button, and then press Esc to return to the default workspace.

1. Select **Collections** on the **File** menu to display the collection that you just created, and then press Esc to return to the default workspace.

#### Sort ####

1. Add another button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:<br>
**ClearCollect( SortByFlavor, Sort( IceCream, Flavor ) )**

 	The previous formula creates a second collection, named **SortByFlavor**, that contains the same data as **Ice Cream**. However, the new collection contains the data sorted alphabetically by the **Flavor** column in ascending order.

1. Press F5, select the new button, and then press Esc.

1. Select **Collections** on the **File** menu to display both collections, and then press Esc to return to the default workspace.

1. Repeat the last three steps, but change the name of the collection that you want to create, and replace the **Sort** formula with a different formula from the table of examples earlier in this section that uses **Sort**.

#### SortByColumns ####

1. Add another button, and set its **[OnSelect](../controls/properties-core.md)** property to this formula:<br>
**ClearCollect( SortByQuantity, SortByColumns( IceCream, "Quantity", Ascending, "Flavor", Descending ) )**

 	The previous formula creates a third collection, named **SortByQuantity**, that contains the same data as **Ice Cream**. However, the new collection contains the data sorted numerically by the **Quanity** column in ascending order, and then by the **Flavor** column in descending order.

1. Press F5, select the new button, and then press Esc.

1. Select **Collections** on the **File** menu to display all three collections, and then press Esc to return to the default workspace.

1. Repeat the last three steps, but change the name of the collection that you want to create, and replace the **SortByColumns** formula with a different formula from the table of examples earlier in this section that uses **SortByColumns**.
