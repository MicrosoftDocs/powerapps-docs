---
title: "getTotalResultCount (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1f9169ce-cba3-4bb6-af20-f86140139cfe
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getTotalResultCount (Client API reference)



Gets the count of results found in the search control. 

## Control types supported

knowledge base search control

## Syntax

```
var kbSearchControl = formContext.getControl("<name>");
var searchCount = kbSearchControl.getTotalResultCount();
```

## Return Value

**Type**: Number

**Description**: The count of the search result.