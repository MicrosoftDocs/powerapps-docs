---
title: "setSearchQuery (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setSearchQuery method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
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

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
kbSearchControl.setSearchQuery(searchString);
```

## Parameters

|Name | Type | Required | Description|
|--|--|--|--|
|searchString |String |Yes|The text for the search query.| 

### Related topics

[getSearchQuery](getSearchQuery.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]