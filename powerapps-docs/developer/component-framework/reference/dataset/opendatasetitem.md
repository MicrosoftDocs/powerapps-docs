---
title: openDatasetItem | Microsoft Docs
description: Open dataset item for a given EntityReference. It checks if there is a command with command button id Mscrm.OpenRecordItem.
keywords:
author: adrianorth
ms.date: 03/07/2022
ms.author: jdaly
ms.reviewer: jdaly
manager: kvivek

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ec4d6f14-d08b-410f-aad7-6a040c2b1c6a
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
