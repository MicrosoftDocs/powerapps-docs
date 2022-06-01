---
title: getRelatedDataSet | Microsoft Docs
description: Gets the related dataset for this column (only if this is related table column like lookup).
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getRelatedDataSet

[!INCLUDE[./includes/getRelatedDataSet-description.md](./includes/getrelateddataset-description.md)]

## Available for

Canvas apps

## Syntax

`context.parameters.dataset.getRelatedDataSet(columnName, updateCallback, targetEntityName)`

## Parameters

| Parameter Name   | Type                       | Required | Description |
| ---------------- | -------------------------- | -------- | ----------- |
| columnName       | `string`                   | Yes      |             |
| updateCallback   | `onDataSetUpdatedCallback` | Yes      |             |
| targetEntityName | `string`                   | No       |             |

## Return value

Type: [Dataset](../dataset.md)

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
