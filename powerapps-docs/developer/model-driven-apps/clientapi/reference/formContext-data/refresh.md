---
title: "data.refresh (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the data.refresh method.
author: MitiJ
ms.author: mijosh
ms.date: 05/05/2025
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
> File columns aren't currently refreshed.

## Syntax

`formContext.data.refresh(save).then(successCallback, errorCallback);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`save`|Boolean|No|`true` to save the data before refreshing, otherwise `false`.|
|`successCallback`|Function|No|A function to call when the operation succeeds.|
|`errorCallback`|Function|No|A function to call when the operation fails.|

### Related articles

[formContext](../../clientapi-form-context.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
