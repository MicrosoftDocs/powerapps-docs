---
title: LookupOptions in Microsoft Dataverse| Microsoft Docs
description: Learn how to use different methods and properties available for LookupOptions in Power Apps component framework.
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

The default table type.

**Type**: `string`

### defaultViewId

The default view to use.

**Type**: `string`

### entityTypes

The table types to display.

**Type**: `string[]`

### viewIds

The views to be available in the view picker. Only System views are supported (not user views).

**Type**: `string[]`


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]