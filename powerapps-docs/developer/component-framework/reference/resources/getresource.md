---
title: getResource | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5c04ba7c-acfe-4375-8dd8-6c537ded9352
---

# getResource

[!INCLUDE [getresource-description](includes/getresource-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.resources.getResource(id, success, failure)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|id|`String`|Yes|The resource string identifier.|
|success|`String`|no|The success callback. Resource data is returned in base 64 encoded format.|
|failure|`String`|no|The failure callback.|


### Related topics

[Resources](../resources.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)