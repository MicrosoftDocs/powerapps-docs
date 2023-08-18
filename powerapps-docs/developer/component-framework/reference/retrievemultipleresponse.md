---
title: RetrieveMultipleResponse (Power Apps component framework API reference)| Microsoft Docs
description: Learn how to use different methods and properties available for RetrieveMultipleResponse in Power Apps component framework.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# RetrieveMultipleResponse

## Available for 

Model-driven apps

## Properties

### entities

An array of JSON objects, where each object represents the retrieved table record containing columns and their values.

**Type**: `Entity[]`

### nextLink

If the number of records being retrieved is more than the value specified in the `maxPageSize` parameter in the request, this column returns the URL to return next set of records.

**Type**: `string`


### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
