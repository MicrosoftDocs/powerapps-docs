---
title: openDatasetItem (Power Apps component framework API reference) | Microsoft Docs
description: Open dataset item for a given EntityReference. It checks if there's a command with command button ID `Mscrm.OpenRecordItem`. If exists, it executes the command, otherwise it just navigates to the associated form of the EntityReference.
author: clromano
ms.author: clromano
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# openDatasetItem

[!INCLUDE[./includes/opendatasetitem-description.md](./includes/opendatasetitem-description.md)]

## Available for

Model-driven and canvas apps

## Syntax

`context.parameters.dataset.openDatasetItem(entityReference)`

## Parameters

| Parameter Name  | Type                                       | Required | description                    |
| --------------- | ------------------------------------------ | -------- | ------------------------------ |
| entityReference | [Entityreference](../entityreference.md) | Yes      | Reference that is opened. |

### Related articles

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
