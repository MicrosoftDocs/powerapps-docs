---
title: "setSearchQuery (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 99e82b80-b6c3-4ee8-83cc-637b13ed8498
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setSearchQuery (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

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


