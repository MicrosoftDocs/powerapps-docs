<properties
	pageTitle="PowerApps: Refresh function"
	description="Reference information for the Refresh function in PowerApps, including syntax and examples"
	services="powerapps"
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

# Refresh function in PowerApps #

Refreshes [records](working-with-tables.md) a [data source](working-with-data-sources.md), including changes made by other users.

## Description ##

The **Refresh** function retrieves a fresh copy of the data source.  You will see changes made by other users. 

If a conflict is reported by the **[Errors](function-errors.md)** function after a **[Patch](function-patch.md)** or other data operation, **Refresh** the data source and reapply the change.

**Refresh** has no return value.  It can only be used in [behavior](file-name.md) formulas. 

## Syntax ##

**Refresh**( *DataSource* )

- *DataSource* – Required. The data source that you wish to refresh.

## Examples ##

In these examples, you'll refresh the data source named **IceCream**. The data source begins with this data:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | "Chocolate" | 100      |
| 2   | "Vanilla"   | 200      |
| 3   | "Strawberry" | 300 |

A user on another device makes a modification to the Strawberry record, changing the **Quantity** to 400.  You will not see this change until a **Refresh** is performed:

- **Refresh( IceCream )** 

After this has been done, galleries that are bound to the **IceCream** data source will show the new value for Strawberry:

| ID (automatically generated<br>primary key) | Flavor    | Quantity |
|-----|-----------|----------|
| 1   | "Chocolate" | 100      |
| 2   | "Vanilla"   | 200      |
| 3   | "Strawberry" | 400 |