---
title: Collect, Clear, and ClearCollect functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Collect, Clear, and ClearCollect functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/01/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Collect, Clear, and ClearCollect functions in PowerApps
Creates and clears [collections](../working-with-data-sources.md#collections) and adds [records](../working-with-tables.md#records) to any [data source](../working-with-data-sources.md).

## Description
### Collect
The **Collect** function adds records to a data source. The items to be added can be:

* A single value: The value is placed in the **[Value](function-value.md)** field of a new record.  All other properties are left [blank](function-isblank-isempty.md).
* A record: Each named property is placed in the corresponding property of a new record.  All other properties are left blank.
* A [table](../working-with-tables.md): Each record of the table is added as a separate record of the data source as described above. The table is not added as a nested table to a record. To accomplish this, wrap the table in a record first.

When used with a collection, additional [columns](../working-with-tables.md#columns) will be created as needed. The columns for other data sources are fixed by the data source and new columns cannot be added.  

If the data source doesn't already exist, a collection is created.

Collections are sometimes used to hold global variables or make a temporary copy of a data source. PowerApps are based on formulas that automatically recalculate as the user interacts with an app. Collections do not enjoy this benefit and their use can make your app harder to create and understand. Before using a collection in this manner, review [working with variables](../working-with-variables.md).

You can also use the **[Patch](function-patch.md)** function to create records in a data source.

**Collect** returns the modified data source as a table.  **Collect** can only be used in a [behavior formula](../working-with-formulas-in-depth.md).

### Clear
The **Clear** function deletes all the records of a collection.  The columns of the collection will remain.

Note that **Clear** only operates on collections and not other data sources.  You can use **[RemoveIf](function-remove-removeif.md)( *DataSource*, true )** for this purpose.  Use caution as this will remove all records from the data source's storage and can affect other users.

You can use the **[Remove](function-remove-removeif.md)** function to selectively remove records.

**Clear** has no return value.  It can only be used in a behavior formula.

### ClearCollect
The **ClearCollect** function deletes all the records from a collection and then adds a different set of records to the same collection.  With a single function, **ClearCollect** offers the combination of **Clear** and then **Collect**.

**ClearCollect** returns the modified collection as a table.  **ClearCollect** can only be used in a behavior formula.

## Syntax
**Collect**( *DataSource*, *Item*, ... )

* *DataSource* – Required. The data source that you want to add data to.  If it does not already exist, a new collection is created.
* *Item(s)* - Required.  One or more records or tables to add to the data source.  

**Clear**( *Collection* )

* *Collection* – Required. The collection that you want to clear.

**ClearCollect**( *Collection*, *Item*, ... )

* *Collection* – Required. The collection that you want to clear and then add data to.
* *Item(s)* - Required.  One or more records or tables to add to the data source.  

## Examples
### Clearing and adding records to a data source
In these examples, you'll erase and add to a collection that's named **IceCream**.  The data source begins with these contents:

![](media/function-clear-collect-clearcollect/icecream.png)

| Formula | Description | Result |
| --- | --- | --- |
| **ClearCollect( IceCream, {&nbsp;Flavor:&nbsp;"Strawberry",&nbsp;Quantity:&nbsp;300&nbsp;} )** |Clears all data from the **IceCream** collection and then adds a record that includes a quantity of strawberry ice cream. |<style> img { max-width: none } </style> ![](media/function-clear-collect-clearcollect/icecream-clearcollect.png)<br><br>The **IceCream** data source has also been modified. |
| **Collect( IceCream, {&nbsp;Flavor:&nbsp;"Pistachio",&nbsp;Quantity:&nbsp;40&nbsp;}, {&nbsp;Flavor:&nbsp;"Orange",&nbsp;Quantity:&nbsp;200&nbsp;}  )** |Adds two records to the **IceCream** collection that includes a quantity of pistachio and Orange ice cream. |![](media/function-clear-collect-clearcollect/icecream-collect.png)<br><br>The **IceCream** data source has also been modified. |
| **Clear( IceCream )** |Removes all records from the **IceCream** collection. |![](media/function-clear-collect-clearcollect/icecream-clear.png)<br><br>The **IceCream** data source has also been modified. |

### Collect a static list

1. Add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this function:<br>**Collect(Products, &quot;Europa&quot;, &quot;Ganymede&quot;, &quot;Callisto&quot;)**
   
    This function creates a collection that's named **Products** and that contains a row for each of three product names.
    
1. While holding down the Alt key, select the button.

1. (optional) To preview the collection that you created, select **Collections** on the **File menu**.

### Put a SharePoint list into a collection

1. [Create a connection to a SharePoint list](../connect-to-sharepoint.md). 

1. Add a button, and set its **[OnSelect](../controls/properties-core.md)** property to this function, replacing *ListName* with the name of your SharePoint list:<br>
**Collect**(**MySPCollection**, *ListName*)

    This function creates a collection that's named **MySPCollection** and that contains the same data as your SharePoint list.
    
1. While holding down the Alt key, select the button.

1. (optional) To preview the collection that you created, select **Collections** on the **File menu**.

For information about how to show data from a SharePoint list (such as dates, choices, and people) in a gallery, see [Show data in a gallery](../connections/connection-sharepoint-online.md#show-data-in-a-gallery). For information about how to show data in a form (with drop-down lists, date pickers, and people pickers), see [Edit form and 
Display form controls](../controls/control-form-detail.md).
