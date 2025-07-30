---
title: "removeTabStateChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeTabStateChange method.
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
# removeTabStateChange (Client API reference)

[!INCLUDE[./includes/removeTabStateChange-description.md](./includes/removeTabStateChange-description.md)].

## Syntax

`tabObj.removeTabStateChange(myFunction);` 

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|function reference|Yes|The function to be removed from the [TabStateChange](../events/tabstatechange.md) event.|

### Related articles

[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md) 

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
