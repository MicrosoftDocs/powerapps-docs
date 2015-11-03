<properties
	pageTitle="PowerApps: Defaults function"
	description="Reference information for the Defaults function in PowerApps, including syntax and examples"
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
   ms.date="11/1/2015"
   ms.author="gregli"/>

# Defaults function in PowerApps #

The **Defaults** function returns the default values for a [Data Source](file-name.md).  

## Description ##

You can use the Defaults function to pre-populate a data entry form with values, making forms easier to fill. 

Defaults returns a [Record](file-name.md) that contains the default values for the data source.  If a [Column](file-name.md) within the data source does not have a default value, it will have no value in the Defaults return value.  

Data sources vary in how much default information they provide, including not providing any at all.  When working with a [Collection](file-name.md) or other data source that does not support default values, the Defaults function will return Blank.

Defaults will not return any values for columns that are part of a [Primary Key](file-name.md).  Without primary key information, when passed as the original record to the [Patch](file-name.md) function used with a data source, a new record will be created.

## Syntax ##

**Defaults**(*DataSource* )

- DataSource – Required. Defaults are returned for this data source.

## Examples ##

| Formula                                 | Description                                                                                                                                           | Result              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Defaults( Scores ) | Returns the default values for the Scores data source. | { Score: 0 } |

