---
title: "getSearchQuery (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getSearchQuery method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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

### Related topics

[setSearchQuery](setSearchQuery.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]