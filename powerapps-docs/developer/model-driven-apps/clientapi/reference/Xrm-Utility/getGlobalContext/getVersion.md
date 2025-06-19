---
title: "getVersion (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getVersion method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getVersion (Client API reference)

Returns the version number of the model-driven apps instance.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getVersion();
``` 

## Return Value

**Type**: String

**Description**: Version of the model-driven apps instance. For example:

`"9.0.0.1103"`

### Related articles

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
