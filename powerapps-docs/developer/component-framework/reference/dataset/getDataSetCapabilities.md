---
title: getDataSetCapabilities | Microsoft Docs
description:
keywords:
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.reviewer: "nabuthuk"
ms.author: vilesyk
author: Nkrb
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 35d94cf8-eab3-4dee-82af-336f6b33b789
---

# getDataSetCapabilities

[!INCLUDE[./includes/getDataSetCapabilities-description.md](./includes/getDataSetCapabilities-description.md)]

## Available for

Model-driven and Canvas apps

## Syntax

`context.parameters.dataset.getDataSetCapabilities()`

## Return value

Type: `[DataProviderCapabilities]()`

ADD TYPE DataProviderCapabilities {
/\*\*
_ If the dataprovider has edit capabilities
_/
isEditable: boolean;

    /**
     * If the dataset can be filtered
     */
    isFilterable: boolean;

    /**
     * If the dataset can be sorted
     */
    isSortable: boolean;

    /**
     * If the dataset records can be paged.
     */
    canPaginate: boolean;

    /**
     * Whether adding new records is supported or not
     */
    canCreateNewRecords: boolean;

}

### Related topics

[Dataset](../dataset.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
