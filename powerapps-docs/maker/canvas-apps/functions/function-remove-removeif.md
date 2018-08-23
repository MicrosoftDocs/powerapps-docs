---
title: Remove and RemoveIf functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Remove and RemoveIf functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/21/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Remove and RemoveIf functions in PowerApps
Removes [records](../working-with-tables.md#records) from a [data source](../working-with-data-sources.md).

## Description
### Remove function
Use the **Remove** function to remove a specific record or records from a data source.  

For [collections](../working-with-data-sources.md#collections), the entire record must match. You can use the **All** argument to remove all copies of a record; otherwise, only one copy of the record is removed.

### RemoveIf function
Use the **RemoveIf** function to remove a record or records based on a condition or a set of conditions. Each condition can be any formula that results in a **true** or **false** and can reference [columns](../working-with-tables.md#columns) of the data source by name. Each condition is evaluated individually for each record, and the record is removed if all conditions evaluate to **true**.

**Remove** and **RemoveIf** return the modified data source as a [table](../working-with-tables.md). You can use both functions only in [behavior formulas](../working-with-formulas-in-depth.md).

You can also use the **[Clear](function-clear-collect-clearcollect.md)** function to remove all of the records in a data source.

### Delegation
[!INCLUDE [delegation-no](../../../includes/delegation-no.md)]

## Syntax
**Remove**( *DataSource*, *Record1* [, *Record2*, ... ] [, **All** ] )

* *DataSource* – Required. The data source that contains the record or records that you want to remove.
* *Record(s)* – Required. The record or records to remove.
* **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument to remove all copies of the record.

**Remove**( *DataSource*, *Table* [, **All** ] )

* *DataSource* – Required. The data source that contains the records that you want to remove.
* *Table* – Required. A table of records to remove.
* **All** – Optional. In a collection, the same record may appear more than once.  You can add the **All** argument to remove all copies of the record.

**RemoveIf**( *DataSource*, *Condition* [, ... ] )

* *DataSource* – Required. The data source that contains the record or records that you want to remove.
* *Condition(s)* – Required. A formula that evaluates to **true** for the record or records to remove.  You can use column names from the *DataSource* in the formula.  If you specify multiple *Conditions*, all must evaluate to **true** for the record or records to be removed.

## Examples
In these examples, you'll remove a record or records in a data source that's named **IceCream** and that starts with the data in this table:

![](media/function-remove-removeif/icecream.png)

| Formula | Description | Result |
| --- | --- | --- |
| **Remove(&nbsp;IceCream,<br>First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Chocolate"&nbsp;)&nbsp;) )** |Removes the **Chocolate** record from the data source. |<style> img { max-width: none } </style> ![](media/function-remove-removeif/icecream-no-chocolate.png)<br><br>The **IceCream** data source has been modified. |
| **Remove(&nbsp;IceCream,<br>First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Chocolate"&nbsp;)&nbsp;) First(&nbsp;Filter(&nbsp;IceCream,&nbsp;Flavor="Strawberry"&nbsp;)&nbsp;) )** |Removes two records from the data source. |![](media/function-remove-removeif/icecream-only-vanilla.png)<br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity&nbsp;>&nbsp;150 )** |Removes records that have a **Quantity** that's greater than **150**. |![](media/function-remove-removeif/icecream-only-chocolate.png)<br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, Quantity&nbsp;>&nbsp;150, Left(&nbsp;Flavor,&nbsp;1&nbsp;) = "S" )** |Removes records that have a **Quantity** that's greater than 150 and **Flavor** starts with an **S**. |![](media/function-remove-removeif/icecream-no-strawberry.png)<br><br><br>The **IceCream** data source has been modified. |
| **RemoveIf(&nbsp;IceCream, true )** |Removes all records from the data source. |![](media/function-remove-removeif/icecream-empty.png)<br><br>The **IceCream** data source has been modified. |

### Step by step
1. Import or create a collection named **Inventory**, and show it in a gallery as [Show data in a gallery](../show-images-text-gallery-sort-filter.md) describes.
2. In the gallery, set the **[OnSelect](../controls/properties-core.md)** property of the image to this expression:<br>**Remove(Inventory, ThisItem)**
3. Press F5, and then select an image in the gallery.<br>The item is removed from the gallery and the collection.

