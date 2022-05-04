---
title: AttributeMetadata | Microsoft Docs
description: Provides all the information about attributes/columns definitions.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# AttributeMetadata

Provides all the information about attributes/columns definitions.

## Available for

Canvas apps

## Properties

| Name          | Type                              | Description                                       |
| ------------- | --------------------------------- | ------------------------------------------------- |
| DefaultValue  | string                            | Default value of the column.                      |
| DisplayName   | string                            | Display name of the column.                       |
| IsEditable    | boolean                           | Determines whether the column is editable or not. |
| LogicalName   | string                            | Logical name of the column.                       |
| MaxLength     | number                            | Maximum length of the column.                     |
| RequiredLevel | number                            | Required level of the column.                     |
| Type          | [AttributeType](AttributeType.md) | Column data type.                                 |

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
