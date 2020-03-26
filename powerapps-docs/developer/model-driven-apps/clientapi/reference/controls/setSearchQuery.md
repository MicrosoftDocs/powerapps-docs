---
title: "setSearchQuery (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 99e82b80-b6c3-4ee8-83cc-637b13ed8498
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setSearchQuery (Client API reference)



Sets the text used as the search criteria for the knowledge base search control.

## Control types supported

knowledge base search control

## Syntax

```
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.setSearchQuery(searchString);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|searchString |String |Yes|The text for the search query.| 

### Related topics

[getSearchQuery](getSearchQuery.md)


