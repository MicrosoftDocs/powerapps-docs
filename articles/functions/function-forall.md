<properties
	pageTitle="ForAll function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the ForEach function in PowerApps"
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

# ForAll function in PowerApps #

Calculated values and performs actions for all [records](../working-with-tables.md#records) of a [table](../working-with-tables.md).

## Description ##

The **ForAll** function evaluates a formula for all records of a table.  The formula can calculate a value and/or perform actions, such as modifying data or working with a connection.

[AZURE.INCLUDE [record-scope](../../includes/record-scope.md)] 

### Return value ###

The result of each formula evaluation is returned in a table, in the same order as the input table. 

If the result of the formula is a single value, the resulting table will be a single column table.  If the result of the formula is a record, the resulting table will contain records with the same columns as the result record.  

If the result of the formula is a *blank* value, then there will be no record in the result table for that input record.  In this case, there will be fewer records in the result table than the source table.

### Taking action ###

The formula can include functions that take action, such as modifying the records of a data source with the **[Patch](function-patch.md)** and **[Collect](function-clear-collect-clearcollect.md)** functions.  The formula can also call methods on connections.  Multiple actions can be performed per record by using the [**;** operator](operators.md).  Modifying the table that is the subject of the **ForAll** is not allowed.

When writing your formula, keep in mind that records can be processed in any order and, when possible, in parallel.  The first record of the table may be processed after the last record.  Take care to avoid ordering dependencies.  For this reason, as they could easily be used to hold variables that would be susceptible to this effect, the **[UpdateContext](function-updatecontext.md)**, **[Clear](function-clear-collect-clearcollect.md)**, and **[ClearCollect](function-clear-collect-clearcollect.md)** functions cannot be used within a **ForAll**.  **[Collect](function-clear-collect-clearcollect.md)** can be used, but the order in which records are added is undefined.

Several of the functions that modify data sources return the changed data source as their return value, including **Collect**, **Remove**, and **Update**.  These return values can be large and consume significant resources if returned for every record of the **ForAll** table.  You may also find that these return values are not what you expect, since **ForAll** can operate in parallel and may separate the side effects of these functions from obtaining their result.  Fortunately, if the return value from **ForAll** is not actually used, which is often the case with data modification functions, then the return value will not be created and there are no resource or ordering concerns.  But if you are using the result of a **ForAll** and one of the functions that returns a data source, think carefully about how you structure the result and try it out first on small data sets.  

### Alternatives ###

Many functions in PowerApps can process more than one value at a time through use of a single column table.  For example, the **Len** function can process a table of text values, returning a table of lengths, in the same manner that **ForAll** could.  This can eliminate the need to use **ForAll** in many cases, can be more efficient, and is easier to read.

Another consideration is that **ForAll** is not delegatable while other functions may be, such as **Filter**.  

## Syntax ##

**ForAll**( *Table*, *Formula* )

- *Table* - Required. Table to be acted upon.
- *Formula* - Required.  The formula to evaluate for all records of the *Table*.

## Examples ##

### Calculations ###

The following examples use the **Squares** [data source](../working-with-data-sources.md):

![](media/function-forall/squares.png)

To create this data source as a collection, use this formula as the OnSelect property of a Button control: 

- **ClearCollect( Squares, [ "1", "4", "9" ] )**

| Formula | Description | Result |
|---------|-------------|--------|
| **ForAll(&nbsp;Squares,&nbsp;Sqrt(&nbsp;Value&nbsp;)&nbsp;)**<br><br>**Sqrt(&nbsp;Squares&nbsp;)** | For all the records of the input table, calculates the square root of the **Value** column.  The **Sqrt** function can also be used with a single column table, making it possible perform this example without using **ForAll**. | <style> img { max-width: none } </style> ![](media/function-forall/sqrt.png) | 
| **ForAll(&nbsp;Squares,&nbsp;Power(&nbsp;Value,&nbsp;3&nbsp;)&nbsp;)** | For all the records of the input table, raises the **Value** column to the third power.  The **Power** function does not support single column tables and therefore **ForAll** must be used in this case. | <style> img { max-width: none } </style> ![](media/function-forall/power3.png) |
### Using a Connection ###

The following examples use the **Expressions** [data source](../working-with-data-sources.md):

![](media/function-forall/translate.png)

To create this data source as a collection, use this formula as the OnSelect property of a Button control: 

- **ClearCollect( Expressions, [ "Hello", "Good morning", "Thank you", "Goodbye" ] )**

This example also uses a [Microsoft Translator](../connections/connection-microsoft-translator.md) connection.  To add this to your app, see the article on [managing connections](../add-manage-connections.md).

| Formula | Description | Result |
|---------|-------------|--------|
| **ForAll( Expressions, MicrosoftTranslator.Translate( Value, "es" ) )** | For all the records in the Expressions table, translate the contents of the **Value** column into Spanish (abbreviated "es") | <style> img { max-width: none } </style> ![](media/function-forall/translate-es.png) |
| **ForAll( Expressions, MicrosoftTranslator.Translate( Value, "fr" ) )** | For all the records in the Expressions table, translate the contents of the **Value** column into French (abbreviated "fr") | <style> img { max-width: none } </style> ![](media/function-forall/translate-fr.png) |

### Copying a Table ###

Sometimes you need to filter, shape, sort and manipulate data.  PowerApps provides a number of functions for doing this, such as **Filter**, **AddColumns**, and **Sort**.  PowerApps treats tables as a value, allowing them to flow through formulas and be consumed easily.      

And sometime you will want to make a copy of this result for later use.  Or you will want to move information from one data source to another.  PowerApps provides the **Collect** function to copy data.

But before you make that copy, think carefully if it is really needed.  Many situations can be addressed by filtering and shaping the underlying data source on demand with a formula. Some of the downsides to making a copy include:
* Two copies of the same information means that one of them can fall out of sync.  
* Making a copy can consume a lot of computer memory, network bandwidth, and/or time.  
* For most data sources, copying cannot be delegated, limiting how much data can be moved.      

The following examples use the **Products** [data source](../working-with-data-sources.md):

![](media/function-forall/prod.png)

The create this data source as a collection, use this formula as the **OnSelect** property of a **Button** control:

- **ClearCollect( Products, Table( { Product: "Widget", 'Quantity Requested': 6, 'Quantity Available': 3 }, { Product: "Gadget", 'Quantity Requested': 10, 'Quantity Available': 20 }, { Product: "Gizmo", 'Quantity Requested': 4, 'Quantity Available': 11 }, { Product: "Apparatus", 'Quantity Requested': 7, 'Quantity Available': 6 } ) )**

Our goal is to work with a derivative table that includes only the items where more has been requested than is available, and for which we need to place an order:

![](media/function-forall/prod-order.png)  

We can perform this task in a couple of different ways, all of which produce the same result, with various pros and cons.

#### Table shaping on demand ####

Don't make that copy!  We can use the following formula anywhere we need:

- **ShowColumns( AddColumns( Filter( Products, 'Quantity Requested' > 'Quantity Available' ), "Quantity To Order", 'Quantity Requested' - 'Quantity Available' ), "Product", "Quantity To Order" )**

A [record scope](../working-with-tables#record-scope) is created by the **Filter** and **AddColumns** functions to perform the comparison and subtraction operations, respectively, with the **'Quantity Requested'** and **'Quantity Available'** fields of each record. 

In this example, the **Filter** function can be delegated.  This is important, as it can find all the products that meet the criteria, even if that is only a few records out of a table of millions.  At this time, **ShowColumns** and **AddColumns** cannot be delegated, so the actual number of products that needs to be ordered will be limited.  If you know the size of this result will always be relatively small, then this is fine.

Ans since we didn't make a copy, there is no additional copy of the information to manage or fall out of date.  

#### ForAll on demand ####

Another approach is to use the **ForAll** function to replace the table shaping functions:

- **ForAll( Products, If( 'Quantity Requested' > 'Quantity Available', { Product: Product, 'Quantity To Order': 'Quantity Requested' - 'Quantity Available' } ) )**

This may be simpler for some people to read and write.

No part of the **ForAll** is delegatable.  Only the first portion of the **Products** table will be evaluated which could be a problem if this table is very large.  Since the **Filter** could be delegated in the previous example, it could work better with large data sets.

#### Collect the result ####

In some situations, a copy of data may be required.  You may need to move information from one data source to another.  In this example perhaps there is a **NewOrder** table on a vendor's system and this is how orders are placed.  For high speed user interactions, you may want to cache a local copy of a table so that there is no server latency.

We use the same table shaping as the previous two examples, but capture the result into a collection:

- **ClearCollect( NewOrder, ShowColumns( AddColumns( Filter( Products, 'Quantity Requested' > 'Quantity Available' ), "Quantity To Order", 'Quantity Requested' - 'Quantity Available' ), "Product", "Quantity To Order" ) )**

- **ClearCollect( NewOrder, ForAll( Products, If( 'Quantity Requested' > 'Quantity Available', { Product: Product, 'Quantity To Order': 'Quantity Requested' - 'Quantity Available' } ) ) )**

**ClearCollect** and **Collect** can not be delegated.  As a result the amount of data that can be moved in this manner is limited. 

#### Collect within ForAll ####

Finally, we can perform the **Collect** directly within the **ForAll**:

- **Clear( ProductsToOrder ); ForAll( Products, If( 'Quantity Requested' > 'Quantity Available', Collect( NewOrder, { Product: Product, 'Quantity To Order': 'Quantity Requested' - 'Quantity Available' } ) )**
 
Again, the **ForAll** function cannot be delegated at this time.  If our **Products** table is large, **ForAll** will only look at the first set of records and we may miss some products that need to be ordered.  But for tables that we know will remain small, this is a fine approach.

Note that we are not capturing the result of the **ForAll**.  The **Collect** function calls made from within it will be returning the **NewOrder** data source for all the records, which could add up to a lot of data if we were capturing it.  


