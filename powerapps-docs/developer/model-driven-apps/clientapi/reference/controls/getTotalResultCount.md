---
title: "getTotalResultCount (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getTotalResultCount method.
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
# getTotalResultCount (Client API reference)

Gets the count of results found in the search control. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
var searchCount = kbSearchControl.getTotalResultCount();
```

## Return Value

**Type**: Number

**Description**: The count of the search result.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
