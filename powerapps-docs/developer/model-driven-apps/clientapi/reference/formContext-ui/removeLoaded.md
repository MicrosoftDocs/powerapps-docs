---
title: "ui.removeLoaded (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the ui.removeLoaded method.
author: MitiJ
ms.author: mijosh
ms.date: 07/08/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# ui.removeLoaded (Client API reference)

Removes a function from the form [Loaded](../events/form-loaded.md) event.

## Syntax

`formContext.ui.removeLoaded(myFunction)`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be removed from the form [Loaded](../events/form-loaded.md) event.

### Related articles

[addLoaded](addloaded.md)   
[Form Loaded event](../events/form-loaded.md)   
[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
