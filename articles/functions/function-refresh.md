<properties
	pageTitle="PowerApps: Refresh function"
	description="Reference information for the Refresh function in PowerApps, including syntax and examples"
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

# Refresh function in PowerApps #

Refreshes the [records](working-with-tables.md) of a [data source](working-with-data-sources.md).

## Description ##

The **Refresh** function retrieves a fresh copy of a data source.  You will see changes made by other users. 

**Refresh** has no return value.  It can only be used in [behavior](file-name.md) formulas. 

## Syntax ##

**Refresh**( *DataSource* )

- *DataSource* – Required. The data source that you wish to refresh.

## Examples ##

In these examples, you'll refresh the data source named **IceCream**. The data source begins with this data:

![](media/function-refresh/icecream.png)

A user on another device makes a modification to the Strawberry record, changing the **Quantity** to 400.  You will not see this change until a **Refresh** is performed:

- **Refresh( IceCream )** 

After this has been done, galleries that are bound to the **IceCream** data source will show the new value for Strawberry:

![](media/function-refresh/icecream-after.png)