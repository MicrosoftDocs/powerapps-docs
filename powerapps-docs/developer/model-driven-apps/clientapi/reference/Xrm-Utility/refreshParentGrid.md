---
title: "refreshParentGrid (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# refreshParentGrid (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/refreshParentGrid-description.md](./includes/refreshParentGrid-description.md)] 

## Syntax

`Xrm.Utility.refreshParentGrid(lookupOptions)`

## Parameters

**lookupOptions**: An object with the following properties to specify the record:

|Property Name |Type |Required  |Description |
|---|---|---|---|
|entityType|String|Yes |Entity type of the record.|
|id|String|Yes |ID of the record.|
|name|String|No |Name of the record.|

### Related topics

[Xrm.Utility](../xrm-utility.md)



