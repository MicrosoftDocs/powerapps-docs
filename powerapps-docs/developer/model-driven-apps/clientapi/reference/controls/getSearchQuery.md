---
title: "getSearchQuery (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getSearchQuery (Client API reference)



Gets the text used as the search criteria for the knowledge base management control. 

## Control types supported

knowledge base search control

## Syntax

```
var kbSearchControl = formContext.getControl("<name>");
var searchQuery = kbSearchControl.getSearchQuery();
```

## Return Value

**Type**: String

**Description**: The text of the search query.

### Related topics

[setSearchQuery](setSearchQuery.md)

