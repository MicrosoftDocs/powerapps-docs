---
title: openDatasetItem | Microsoft Docs
description: Open dataset item for a given EntityReference. It checks if there is a command with command button id Mscrm.OpenRecordItem.
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

# openDatasetItem

[!INCLUDE[./includes/opendatasetitem-description.md](./includes/opendatasetitem-description.md)]

## Available for

Model-driven and canvas apps

## Syntax

`context.parameters.dataset.openDatasetItem(entityReference)`

## Parameters

| Parameter Name  | Type                                       | Required | description                    |
| --------------- | ------------------------------------------ | -------- | ------------------------------ |
| entityReference | [Entityreference](../entityreference.md) | Yes      | Reference that will be opened. |

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
