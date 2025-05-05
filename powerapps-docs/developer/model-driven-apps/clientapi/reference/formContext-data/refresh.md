---
title: "data.refresh (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the data.refresh method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# data.refresh (Client API reference)



[!INCLUDE[./includes/refresh-description.md](./includes/refresh-description.md)]

> [!NOTE]
> File columns are not currently refreshed by this API. 

## Syntax

`formContext.data.refresh(save).then(successCallback, errorCallback);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`save`|Boolean|No|true if the data should be saved before it is refreshed, otherwise false.|
|`successCallback`|Function|No|A function to call when the operation succeeds.|
|`errorCallback`|Function|No|A function to call when the operation fails.|

### Related articles

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
