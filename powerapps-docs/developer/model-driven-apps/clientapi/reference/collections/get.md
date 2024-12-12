---
title: "get method for collections (Client API reference) in model-driven apps"
description: "Describes the get method used for collections."
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# get method for collections (Client API reference)


[!INCLUDE[./includes/get-description.md](./includes/get-description.md)]

## Syntax

`collection.get([String][Number][delegate function(attribute, index)])`

## Parameters

|Parameter  |Return value |Return type  |
|---------|------|-------|
|`None`  |All the objects in the collection  |Array|
|`String`  |The object where the name matches the argument<br/><br/>The objects returned in the **formContext.data.process** namespace don't contain names. So, using the string parameter for this method returns no objects.  |Object|
|`Number`  |The object where the index matches the number  |Object|
|delegate function(attribute, index)  |Any objects that cause the delegate function to return **true**.  |Array|


### Related articles

[Collections in Client API](../collections.md)   
[forEach](forEach.md)   
[getLength](getLength.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
