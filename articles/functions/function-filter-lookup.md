<properties
	pageTitle="PowerApps: Filter and LookUp functions"
	description="Reference information for the Filter and LookUp function in PowerApps, including syntax and examples"
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

# Filter and LookUp functions in PowerApps #

Finds one or more [records](working-with-tables.md#records) in a [table](working-with-tables.md).

## Description ##

The **Filter** function finds records in a table that satisfy a formula.  Use **Filter** to find a set of records that match a criteria and discard those that do not.

The **LookUp** function finds the first record in a table that satisfies a formula.  Use **LookUp** to find a single record that matches a criteria.

For both, the formula is evaluated for each record of the table.  Records that result in *true* are included in the result.  [Columns](working-with-tables.md#columns) of the table can be used in the formula, as well as control properties and other values from throughout your app.  

**Filter** returns all records found as a table with the same columns as the original.  **LookUp** returns only the first record found, after applying a formula to reduce the record to a single value.  If no records are found, **Filter** returns an empty table and **LookUp** returns *blank*.  

Tables are a value in PowerApps, just like a string or number.  They can be passed to and returned from functions.  **Filter** and **LookUp** do not modify a table, instead they take a table as an argument and return a table, record, or single value from it.  See [working with tables](working-with-tables.md) for more details.

## Syntax ##

**Filter**( *Table*, *Formula1* [, *Formula2*, ... ] )

- *Table* - Required. Table to search.
- *Formula(s)* - Required. This formula is evaluated for each record of the table, and those that result in **true** are included in the result.  You can reference columns within the table.  If more than one formula is supplied, the results of all formulas are combined with the **[And](function-logicals.md)** function.

**LookUp**( *Table*, *Formula*, *ReductionFormula* )

- *Table* - Required. Table to search.
- *Formula* - Required. This formula is evaluated for each record of the table, and the first record that results in **true** is returned.  You can reference columns within the table.  
- *ReductionFormula* - Required. This formula is evaluated over the record that was found, reducing the record to a single value.  You can reference columns within the table.  

## Examples ##

The following examples use the **IceCream** data source:

![](media/function-filter-lookup/icecream.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Filter( IceCream, OnOrder > 0 )** | Returns records where **OnOrder** is greater than zero. | <style> img { max-width: none; } </style> ![](media/function-filter-lookup/icecream-onorder.png) |
| **Filter( IceCream, Quantity + OnOrder > 225 )** | Returns records where the sum of **Quantity** and **OnOrder** columns is greater than 225. | ![](media/function-filter-lookup/icecream-overstock.png) |
| **Filter( IceCream, "chocolate" in Lower( Flavor ) )** | Returns records where the word "chocolate" appears in the **Flavor** name, independent of uppercase or lowercase letters. | ![](media/function-filter-lookup/icecream-chocolate.png) |
| **Filter( IceCream, Quantity < 10  && OnOrder < 20 )** | Returns records where the **Quantity** is less than 10 and **OnOrder** is less than 20.  There are no records that match this criteria, so an empty table is returned. | ![](media/function-filter-lookup/icecream-empty.png) |
| **LookUp( IceCream, Flavor = "Chocolate", Quantity )** | Searches for a record with **Flavor** equal to "Chocolate", of which there is one.  For the first record that is found, returns the **Quantity** of that record. | 100 |
| **LookUp( IceCream, Quantity > 150, Quantity + OnOrder )** | Searches for a record with **Quantity** greater than 100, of which there are multiple.  For the first record that is found, which is "Vanilla" **Flavor**, returns the sum of **Quantity** and **OnOrder** columns. | 250 |
| **LookUp( IceCream, Flavor = "Pistachio", OnOrder )** | Searches for a record with **Flavor** equal to "Pistachio", of which there are none.  Since none were found, **Lookup** returns *blank*. | *blank* | 



