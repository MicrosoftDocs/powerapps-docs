---
title: "data.refresh (Client API Reference) in Model-Driven Apps"
description: Learn how to use the data.refresh method to refresh form data in model-driven apps, with an option to save first. See syntax, parameters, and callbacks.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
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

## Parameters

|Name|Type|Required|Description|
|--|--|--|--|
|`save`|Boolean|No|`true` to save the data before refreshing, otherwise `false`.|
|`successCallback`|Function|No|A function to call when the operation succeeds.|
|`errorCallback`|Function|No|A function to call when the operation fails.|

### Related articles

[formContext](../../clientapi-form-context.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
