<properties
	pageTitle="PowerApps: ClearCollect function"
	description="Reference information for the ClearCollect function in PowerApps, including syntax and examples"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="bills"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/01/2015"
   ms.author="gregli"/>

# ClearCollect function in PowerApps #

The **ClearCollect** function clears and then collects into a [Data Source](file-name.md).  

## Description ##

ClearCollect is shorthand for calling the [Clear](file-name.md) function and then the [Collect](file-name.md) function.  "ClearCollect( DS, ... )" is equivalent to "Clear( DS ); Collect( DS, ... )".  The data source is first emptied before adding new items.

## Syntax ##

**ClearCollect**( *DataSource*, *Item*, ... )

- DataSource – Required. This data source is cleared with new items added.

- Item - Required.  Items to add to the data source.

## Examples ##

| Formula                                 | Description                                                                                                                                           | Result              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
