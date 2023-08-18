---
title: Metadata (Power Apps component framework API reference) | Microsoft Docs
description: Provides all the information about  column definitions.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Metadata

[!INCLUDE [metadata-description](includes/metadata-description.md)]

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


### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
