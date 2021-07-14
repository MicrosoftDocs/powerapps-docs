---
title: Refresh function in Power Apps
description: Reference information including syntax and examples for the Refresh function in Power Apps.
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
---
# Refresh function in Power Apps
Refreshes the [records](../working-with-tables.md#records) of a [data source](../working-with-data-sources.md).

## Description
The **Refresh** function retrieves a fresh copy of a data source.  You'll see changes that other users made.

**Refresh** has no return value, and you can use it only in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**Refresh**( *DataSource* )

* *DataSource* – Required. The data source that you want to refresh.

## Example
In this example, you'll refresh the data source named **IceCream**, which starts with this data:

![IceCream example.](media/function-refresh/icecream.png)

A user on another device changes the **Quantity** in the **Strawberry** record to **400**.  You won't see this change until this formula executes:

**Refresh( IceCream )**

After that formula executes, galleries that are bound to the **IceCream** data source will show the updated value for **Strawberry**:

![IceCream after refresh.](media/function-refresh/icecream-after.png)



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]