---
title: LookupOptions | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 89807b09-92ee-43cf-8db5-8da838131923
---

# LookupOptions

Provides all the information about options used when opening a lookup dialog.

## Available for 

Model-driven apps

## Properties

### allowMultiSelect

Whether the lookup allows more than one item to be selected.

**Type**: `boolean`

### defaultEntityType

The default entity type.

**Type**: `string`

### defaultViewId

The default view to use.

**Type**: `string`

### entityTypes

The entity types to display.

**Type**: `string[]`

### viewIds

The views to be available in the view picker. Only System views are supported (not user views).

**Type**: `string[]`


### Related topics

[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework overview](../overview.md)