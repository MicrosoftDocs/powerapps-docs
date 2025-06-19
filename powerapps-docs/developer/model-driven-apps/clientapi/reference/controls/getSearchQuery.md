---
title: "getSearchQuery (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getSearchQuery method.
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
# getSearchQuery (Client API reference)

Gets the text used as the search criteria for the knowledge base management control. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
var searchQuery = kbSearchControl.getSearchQuery();
```

## Return Value

**Type**: String

**Description**: The text of the search query.

### Related articles

[setSearchQuery](setSearchQuery.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
