---
title: AttributeMetadata (Power Apps component framework API reference) | Microsoft Docs
description: Provides all the information about attributes/columns definitions.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 07/20/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# AttributeMetadata

Provides all the information about attributes/columns definitions.

## Available for

Model-driven and canvas apps

## Properties

| Name          | Type                              | Description                                       |
| ------------- | --------------------------------- | ------------------------------------------------- |
| DefaultValue  | string                            | Default value of the column.                      |
| DisplayName   | string                            | Display name of the column.                       |
| IsEditable    | boolean                           | Determines whether the column is editable or not. |
| LogicalName   | string                            | Logical name of the column.                       |
| MaxLength     | number                            | Maximum length of the column.                     |
| RequiredLevel | number                            | Required level of the column.                     |
| Type          | [AttributeType](attributetype.md) | Column data type.                                 |

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
