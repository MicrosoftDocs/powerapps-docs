---
title: Metadata | Microsoft Docs
description: Provides all the information about  column definitions.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0a11feb1-0b7d-4591-b7b3-8e45d4e58805
---

# Metadata

Provides all the information about  column definitions.

## Available for 

Model-driven apps

## Properties

### DisplayName

The display name of the column.

**Type**: `string`

### LogicalName 

The logical name of the column.

**Type**: `string`

### IsSecured

Defines whether the column is secured or not.

**Type**: `boolean`

### SourceType

**Type**: `number`

### Description

The description of the column.

**Type**: `string`

### RequiredLevel

Defines whether the column is required or not.

**Type**: `RequiredLevel`

The `RequiredLevel` has following values:

|value|RequiredLevel|
|---|---|
|-1|Unknown|
|0|None|
|1|SystemRequired|
|2|Applicationrequired|
|3|Recommended|


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]