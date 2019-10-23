---
title: RetrieveMultipleResponse | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 08ea66d3-b4af-44af-a3ae-cb2ebad043e8
---

# RetrieveMultipleResponse

## Available for 

Model-driven apps

## Properties

### entities

An array of JSON objects, where each object represents the retrieved entity record containing attributes and their values.

**Type**: `Entity[]`

### nextLink

If the number of records being retrieved is more than the value specified in the `maxPageSize` parameter in the request, this attribute returns the URL to return next set of records.

**Type**: `string`


### Related topics

[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework overview](../overview.md)