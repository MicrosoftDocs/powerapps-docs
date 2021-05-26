---
title: Defaults function | Microsoft Docs
description: Reference information, including syntax and examples, for the Defaults function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/01/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Defaults function in Power Apps
Returns the default values for a [data source](../working-with-data-sources.md).  

## Description
Use the **Defaults** function to pre-populate a data entry form, making it easier to fill.

This function returns a [record](../working-with-tables.md#records) that contains the default values for the data source.  If a [column](../working-with-tables.md#columns) within the data source doesn't have a default value, that property won't be present.

Data sources vary in how much default information they provide, including not providing any at all.  When you work with a [collection](../working-with-data-sources.md#collections) or another data source that doesn't support default values, the **Defaults** function will return an [empty](function-isblank-isempty.md) record.

You can combine the **Defaults** function with the **[Patch](function-patch.md)** function to [create a record](../working-with-data-sources.md).

## Syntax
**Defaults**( *DataSource* )

* *DataSource* – Required. The data source for which you want default values.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Defaults(&nbsp;Scores&nbsp;)** |Returns the default values for the **Scores** data source. |**{ Score: 0 }** |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]