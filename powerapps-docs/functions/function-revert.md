---
title: Revert function | Microsoft Docs
description: Reference information, including syntax and an example, for the Revert function in PowerApps
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/21/2015
ms.author: gregli

---
# Revert function in PowerApps
Refreshes and clears errors for the [records](../maker/working-with-tables.md#records) of a [data source](../maker/working-with-data-sources.md).

## Description
The **Revert** function refreshes an entire data source or a single record in that data source. You'll see changes that other users made.

For the records reverted, **Revert** also clears any errors from the [table](../maker/working-with-tables.md) that the **[Errors](../maker/functions/function-errors.md)** function returned.

If the **[Errors](../maker/functions/function-errors.md)** function reports a conflict after a **[Patch](function-patch.md)** or other data operation, **Revert** the record to start with the conflicting version and reapply the change.

**Revert** has no return value. You can use it only in a [behavior formula](../maker/working-with-formulas-in-depth.md).

## Syntax
**Revert**( *DataSource* [, *Record* ] )

* *DataSource* – Required. The data source that you want to revert.
* *Record* - Optional.  The record that you want to revert.  If you don't specify a record, the entire data source is reverted.

## Example
In this example, you'll revert the data source named **IceCream**, which starts with the data in this table:

![](media/function-revert/icecream.png)

A user on another device changes the **Quantity** property of the **Strawberry** record to **400**.  At about the same time, you change the same property of the same record to **500**, not knowing about the other change.

You use the **[Patch](function-patch.md)** function to update the record:<br>
**Patch( IceCream, First( Filter( IceCream, Flavor = "Strawberry" ) ), { Quantity: 500 } )**

You check the **[Errors](../maker/functions/function-errors.md)** table and find an error:

| Record | [Column](../maker/working-with-tables.md#columns) | Message | Error |
| --- | --- | --- | --- |
| **{ ID: 1, Flavor: "Strawberry", Quantity: 300 }** |*blank* |**"The record you are trying to modify has been modified by another user.  Please revert the record and try again."** |**ErrorKind.Conflict** |

Based on the **Error** column, you have a **Reload** button for which the **[OnSelect](../maker/controls/properties-core.md)** property to set to this formula:<br>
**Revert( IceCream, First( Filter( IceCream, Flavor = "Strawberry" ) ) )**

After you select the **Reload** button, the **[Errors](../maker/functions/function-errors.md)** table is [empty](../maker/functions/function-isblank-isempty.md), and the new value for **Strawberry** has been loaded:

![](media/function-revert/icecream-after.png)

You reapply your change on top of the previous change, and your change succeed because the conflict has been resolved.

![](media/function-revert/icecream-success.png)

