---
title: "ui.removeOnLoad (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the ui.removeOnLoad method.
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
# ui.removeOnLoad (Client API reference)



[!INCLUDE[./includes/removeOnLoad-description.md](./includes/removeOnLoad-description.md)]

## Syntax

`formContext.ui.removeOnLoad(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be removed from the form [OnLoad](../events/form-onload.md) event.

### Related articles

[addOnLoad](addOnLoad.md)   
[Form data OnLoad event](../events/form-onload.md)   
[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
