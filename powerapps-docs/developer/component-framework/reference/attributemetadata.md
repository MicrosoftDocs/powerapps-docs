---
title: AttributeMetadata | Microsoft Docs
description: Provides all the information about attributes metadata.
keywords:
ms.author: nabuthuk
manager: kvivek
author: nkrb
ms.date: 14/19/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad8659f7-f566-43db-bed1-c8484c114a59
---

# AttributeMetadata

Provides all the information about attributes metadata.

## Available for

Model-driven apps and Canvas (check if same comves from canvas)

## Properties

| Name          | Type    | Description                                          |
| ------------- | ------- | ---------------------------------------------------- |
| Behaviour     | string  | Description of the attribute.                        |
| Description   | string  | Description of the attribute.                        |
| DisplayName   | string  | Display name of the attribute.                       |
| Format        | string  | Display name of the attribute.                       |
| ImeMode       | ImeMode | Display name of the attribute.                       |
| IsEditable    | boolean | Determines whether the attribute is editable or not  |
| IsSecured     | boolean | Determines whether the attribute is secure or not.   |
| IsReadable    | boolean | Determines whether the attribute is read-only or not |
| LogicalName   | string  | Logical name of the attribute.                       |
| MaxLength     | number  | Required level of the attribute.                     |
| RequiredLevel | number  | Required level of the attribute.                     |
| SourceType    | number  | Determines the source type.                          |
| Type          | string  | Attribute data type.                                 |
|               |         |                                                      |

ADD NEW TYPE:
/\*\*

- Ime Mode
- 0 - Auto,
- 1 - Inactive,
- 2 - Active,
- 3 - Disabled
  \*/
  type ImeMode = 0 | 1 | 2 | 3;

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
