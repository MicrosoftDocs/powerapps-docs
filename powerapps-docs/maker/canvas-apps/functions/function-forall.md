---
title: ForAll function in Power Apps
description: Reference information including syntax and examples for the ForAll function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 07/17/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# ForAll function in Power Apps

Calculates values and performs actions for all the [records](../working-with-tables.md#records) in a [table](../working-with-tables.md).

## Description

The **ForAll** function evaluates a formula for all the records in a table.  The formula can calculate a value and/or perform actions, such as modifying data or working with a connection. Use the [**With** function](function-with.md) to evaluate the formula for a single record.  

Use the [**Sequence** function](function-sequence.md) with the **ForAll** function to iterate based on a count.

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

### Return value

The result of each formula evaluation is returned in a table, in the same order as the input table.

If the result of the formula is a single value, the resulting table will be a single-column table.  If the result of the formula is a record, the resulting table contains records with the same columns as the result record.  

If the result of the formula is a *blank* value, then there is no record in the result table for that input record.  In this case, there will be fewer records in the result table than the source table.

### Taking action

The formula can include functions that take action, such as modifying the records of a data source with the **[Patch](function-patch.md)** and **[Collect](function-clear-collect-clearcollect.md)** functions.  The formula can also call methods on connections.  Multiple actions can be performed per record by using the [**;** operator](operators.md). You can't modify the table that is the subject of the **ForAll** function.

When writing your formula, keep in mind that records can be processed in any order and, when possible, in parallel.  The first record of the table may be processed after the last record.  

Take care to avoid ordering dependencies.  For this reason, you can't use the **[UpdateContext](function-updatecontext.md)**, **[Clear](function-clear-collect-clearcollect.md)**, and **[ClearCollect](function-clear-collect-clearcollect.md)** functions within a **ForAll** function because they could easily be used to hold variables that would be susceptible to this effect.  You can use **[Collect](function-clear-collect-clearcollect.md)**, but the order in which records are added is undefined.

Several functions that modify data sources, including **Collect**, **Remove**, and **Update**, return the changed data source as their return value.  These return values can be large and consume significant resources if returned for every record of the **ForAll** table.  You may also find that these return values are not what you expect because **ForAll** can operate in parallel and may separate the side effects of these functions from obtaining their result.  If the return value from **ForAll** is not used, which is often the case with data modification functions, then the return value will not be created and there are no resource or order concerns.  But if you are using the result of a **ForAll** and one of the functions that returns a data source, think carefully about how you structure the result and try it out first on small data sets.  

### Alternatives
Many functions in Power Apps can process more than one value at a time through the use of a single-column table.  For example, the **Len** function can process a table of text values, returning a table of lengths, in the same manner, that **ForAll** could.  This can eliminate the need to use **ForAll** in many cases, can be more efficient, and is easier to read.

Another consideration is that **ForAll** is not delegable while other functions may be, such as **Filter**.  

### Delegation
[!INCLUDE [delegation-no-one](../../../includes/delegation-no-one.md)]

## Syntax
**ForAll**(*Table*, *Formula*)

* *Table* - Required. Table to be acted upon.
* *Formula* - Required.  The formula to evaluate for all records of the *Table*.

## Examples
### Calculations
The following examples use the **Squares** [data source](../working-with-data-sources.md):

![Example of squares.](media/function-forall/squares.png)

To create this data source as a collection, set the **OnSelect** property of a **Button** control to this formula, open Preview mode, and then select the button:

`ClearCollect( Squares, [ "1", "4", "9" ] )`

| Formula | Description | Result |
| --- | --- | --- |
| **ForAll(&nbsp;Squares, Sqrt(&nbsp;Value&nbsp;)&nbsp;)**<br><br>**Sqrt(&nbsp;Squares&nbsp;)** |For all the records of the input table, calculates the square root of the **Value** column.  The **Sqrt** function can also be used with a single-column table, making it possible perform this example without using **ForAll**. | ![Example of Sqrt.](media/function-forall/sqrt.png) |
| **ForAll(&nbsp;Squares, Power(&nbsp;Value,&nbsp;3&nbsp;)&nbsp;)** |For all the records of the input table, raises the **Value** column to the third power.  The **Power** function does not support single-column tables. Therefore, **ForAll** must be used in this case. | ![Example of Power.](media/function-forall/power3.png) |

### Using a connection
The following examples use the **Expressions** [data source](../working-with-data-sources.md):

![Example of expressions.](media/function-forall/translate.png)

To create this data source as a collection, set the **OnSelect** property of a **Button** control to this formula, open Preview mode, and then select the button:

`ClearCollect( Expressions, [ "Hello", "Good morning", "Thank you", "Goodbye" ] )`

This example also uses a [Microsoft Translator](../connections/connection-microsoft-translator.md) connection.  To add this connection to your app, see the article about how to [manage connections](../add-manage-connections.md).

| Formula | Description | Result |
| --- | --- | --- |
| **ForAll(Expressions, MicrosoftTranslator.Translate( Value, "es"))** |For all the records in the Expressions table, translate the contents of the **Value** column into Spanish (abbreviated "es"). | ![Example with value "es."](media/function-forall/translate-es.png) |
| **ForAll(Expressions, MicrosoftTranslator.Translate( Value, "fr"))** |For all the records in the Expressions table, translate the contents of the **Value** column into French (abbreviated "fr"). | ![Example with value "fr."](media/function-forall/translate-fr.png) |

### Copying a table
Sometimes you need to filter, shape, sort, and manipulate data.  Power Apps provides many functions for doing this, such as **Filter**, **AddColumns**, and **Sort**.  Power Apps treat each table as a value, allowing it to flow through formulas and be consumed easily.      

And sometimes you want to make a copy of this result for later use, or you want to move information from one data source to another.  Power Apps provides the **Collect** function to copy data.

But before you make that copy, think carefully if it is needed.  Many situations can be addressed by filtering and shaping the underlying data source on-demand with a formula. Some of the downsides to making a copy include:

* Two copies of the same information mean that one of them can fall out of sync.  
* Making a copy can consume much of the computer memory, network bandwidth, and/or time.  
* For most data sources, copying cannot be delegated, limiting how much data can be moved.      

The following examples use the **Products** [data source](../working-with-data-sources.md):

![Example of products data source.](media/function-forall/prod.png)

To create this data source as a collection, set the **OnSelect** property of a **Button** control to this formula, open Preview mode, and then select the button:

```powerapps-dot
ClearCollect( Products, 
    Table( 
        { Product: "Widget",    'Quantity Requested': 6,  'Quantity Available': 3 }, 
        { Product: "Gadget",    'Quantity Requested': 10, 'Quantity Available': 20 },
        { Product: "Gizmo",     'Quantity Requested': 4,  'Quantity Available': 11 },
        { Product: "Apparatus", 'Quantity Requested': 7,  'Quantity Available': 6 } 
    )
)
```

Our goal is to work with a derivative table that includes only the items where more has been requested than is available, and for which we need to place an order:

![Example of derivative table.](media/function-forall/prod-order.png)  

We can perform this task in a couple of different ways, all of which produce the same result, with various pros and cons.

#### Table shaping on demand
Don't make that copy!  We can use the following formula anywhere we need:

```powerapps-dot
// Table shaping on demand, no need for a copy of the result
ShowColumns( 
    AddColumns( 
        Filter( Products, 'Quantity Requested' > 'Quantity Available' ), 
        "Quantity To Order", 'Quantity Requested' - 'Quantity Available' 
    ), 
    "Product", 
    "Quantity To Order"
)
```

A [record scope](../working-with-tables.md#record-scope) is created by the **Filter** and **AddColumns** functions to perform the comparison and subtraction operations, respectively, with the **'Quantity Requested'** and **'Quantity Available'** fields of each record.

In this example, the **Filter** function can be delegated.  This is important, as it can find all the products that meet the criteria, even if that is only a few records out of a table of millions.  At this time, **ShowColumns** and **AddColumns** cannot be delegated, so the actual number of products that need to be ordered will be limited.  If you know the size of this result will always be relatively small, this approach is fine.

And because we didn't make a copy, there is no additional copy of the information to manage or fall out of date.  

#### ForAll on demand
Another approach is to use the **ForAll** function to replace the table-shaping functions:

```powerapps-dot
ForAll( Products, 
    If( 'Quantity Requested' > 'Quantity Available', 
        { 
            Product: Product, 
            'Quantity To Order': 'Quantity Requested' - 'Quantity Available' 
        } 
    ) 
)
```

This formula may be simpler for some people to read and write.

No part of the **ForAll** is delegable.  Only the first portion of the **Products** table will be evaluated, which could be a problem if this table is large.  Because **Filter** could be delegated in the previous example, it could work better with large data sets.

#### Collect the result
In some situations, a copy of data may be required.  You may need to move information from one data source to another.  In this example, orders are placed through a **NewOrder** table on a vendor's system.  For high-speed user interactions, you may want to cache a local copy of a table so that there is no server latency.

We use the same table shaping as the previous two examples, but we capture the result into a collection:

```powerapps-dot
ClearCollect( NewOrder, 
    ShowColumns( 
        AddColumns( 
            Filter( Products, 'Quantity Requested' > 'Quantity Available' ), 
            "Quantity To Order", 'Quantity Requested' - 'Quantity Available' 
        ), 
        "Product", 
        "Quantity To Order"
    )
)
```

```powerapps-dot
ClearCollect( NewOrder, 
    ForAll( Products, 
        If( 'Quantity Requested' > 'Quantity Available', 
            { 
                Product: Product, 
                'Quantity To Order': 'Quantity Requested' - 'Quantity Available' 
            } 
        } 
    )
)
```

**ClearCollect** and **Collect** can't be delegated.  As a result, the amount of data that can be moved in this manner is limited.

#### Collect within ForAll
Finally, we can perform the **Collect** directly within the **ForAll**:

```powerapps-dot
Clear( ProductsToOrder ); 
ForAll( Products, 
    If( 'Quantity Requested' > 'Quantity Available', 
        Collect( NewOrder,  
            { 
                Product: Product, 
                'Quantity To Order': 'Quantity Requested' - 'Quantity Available' 
            } 
        )
    )
)
```

Again, the **ForAll** function can't be delegated at this time.  If our **Products** table is large, **ForAll** will look at the first set of records only and we may miss some products that need to be ordered.  But for tables that we know will remain small, this approach is fine.

Note that we are not capturing the result of the **ForAll**.  The **Collect** function calls made from within it will return the **NewOrder** data source for all the records, which could add up to numerous data if we were capturing it.  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]