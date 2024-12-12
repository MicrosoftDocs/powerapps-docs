---
title: "refreshParentGrid (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the refreshParentGrid method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# refreshParentGrid (Client API reference)

[!INCLUDE[./includes/refreshParentGrid-description.md](./includes/refreshParentGrid-description.md)] 

## Syntax

`Xrm.Utility.refreshParentGrid(lookupOptions)`

## Parameters

**lookupOptions**: An object with the following properties to specify the record:

|Property Name |Type |Required  |Description |
|---|---|---|---|
|`entityType`|String|Yes |Table type of the record.|
|`id`|String|Yes |ID of the record.|
|`name`|String|No |Name of the record.|

### Related articles

[Xrm.Utility](../xrm-utility.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
