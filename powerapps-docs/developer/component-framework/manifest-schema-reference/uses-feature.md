---
title: uses-feature | Microsoft Docs
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
ms.assetid: 87f5e921-4114-4710-a362-db741426a69b
---

# uses-feature element

## Parent Element

|Element|Description|
|--|--|
|feature-usage||

## Child Elements

|Element|Description|
|--|--|
|name|Name of the feature that is declared in the component|
|required|Indicates if the component requires that feature or not|


### Example 

```XML
<feature-usage>
<uses-feature name="WebAPI" required="true" />
</feature-usage>
```