---
title: Revert function in Power Apps
description: Reference information including syntax and examples for the Revert function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 10/21/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# Revert function in Power Apps
Refreshes and clears errors for the [records](../working-with-tables.md#records) of a [data source](../working-with-data-sources.md).

## Description
The **Revert** function refreshes an entire data source or a single record in that data source. You'll see changes that other users made.

For the records reverted, **Revert** also clears any errors from the [table](../working-with-tables.md) that the **[Errors](function-errors.md)** function returned.

If the **[Errors](function-errors.md)** function reports a conflict after a **[Patch](function-patch.md)** or other data operation, **Revert** the record to start with the conflicting version and reapply the change.

**Revert** has no return value. You can use it only in a [behavior formula](../working-with-formulas-in-depth.md).

## Syntax
**Revert**( *DataSource* [, *Record* ] )

* *DataSource* – Required. The data source that you want to revert.
* *Record* - Optional.  The record that you want to revert.  If you don't specify a record, the entire data source is reverted.

## Example
In this example, you'll revert the data source named **IceCream**, which starts with the data in this table:

![IceCream example.](media/function-revert/icecream.png)

A user on another device changes the **Quantity** property of the **Strawberry** record to **400**.  At about the same time, you change the same property of the same record to **500**, not knowing about the other change.

You use the **[Patch](function-patch.md)** function to update the record:<br>
**Patch( IceCream, First( Filter( IceCream, Flavor = "Strawberry" ) ), { Quantity: 500 } )**

You check the **[Errors](function-errors.md)** table and find an error:

| Record | [Column](../working-with-tables.md#columns) | Message | Error |
| --- | --- | --- | --- |
| **{ ID: 1, Flavor: "Strawberry", Quantity: 300 }** |*blank* |**"The record you are trying to modify has been modified by another user.  Please revert the record and try again."** |**ErrorKind.Conflict** |

Based on the **Error** column, you have a **Reload** button for which the **[OnSelect](../controls/properties-core.md)** property to set to this formula:<br>
**Revert( IceCream, First( Filter( IceCream, Flavor = "Strawberry" ) ) )**

After you select the **Reload** button, the **[Errors](function-errors.md)** table is [empty](function-isblank-isempty.md), and the new value for **Strawberry** has been loaded:

![New value for Strawberry ice cream.](media/function-revert/icecream-after.png)

You reapply your change on top of the previous change, and your change succeed because the conflict has been resolved.

![Reapplied changes with resolved conflict.](media/function-revert/icecream-success.png)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]