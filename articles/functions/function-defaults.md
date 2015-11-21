<properties
	pageTitle="PowerApps: Defaults function"
	description="Reference information for the Defaults function in PowerApps, including syntax and examples"
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
   ms.date="11/01/2015"
   ms.author="gregli"/>

# Defaults function in PowerApps #

The **Defaults** function returns the default values for a [Data Source](working-with-data-sources.md).  

## Description ##

Use the **Defaults** function to pre-populate a data entry form, making it easier to fill. 

This function returns a [record](file-name.md) that contains the default values for the data source.  If a [Column](file-name.md) within the data source doesn't have a default value, that property won't be present.

Data sources vary in how much default information they provide, including not providing any at all.  When you work with a [Collection](file-name.md) or another data source that does not support default values, the **Defaults** function will return an [empty](file-name.md) record.

The **Defaults** function will not return any values for columns that are part of a [Primary Key](file-name.md).  You can combine this behavior with the **[Patch](function-patch.md)** function to [create a record](working-with-data-sources.md).

## Syntax ##

**Defaults**( *DataSource* )

- *DataSource* – Required. Defaults are returned for this data source.

## Examples ##

| Formula                                 | Description                                                                                                                                           | Result              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| **Defaults( Scores )** | Returns the default values for the **Scores** data source. | **{ Score: 0 }** |

