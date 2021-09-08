---
title: "refreshParentGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the refreshParentGrid method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# refreshParentGrid (Client API reference)



[!INCLUDE[./includes/refreshParentGrid-description.md](./includes/refreshParentGrid-description.md)] 

## Syntax

`Xrm.Utility.refreshParentGrid(lookupOptions)`

## Parameters

**lookupOptions**: An object with the following properties to specify the record:

|Property Name |Type |Required  |Description |
|---|---|---|---|
|entityType|String|Yes |Table type of the record.|
|id|String|Yes |ID of the record.|
|name|String|No |Name of the record.|

### Related topics

[Xrm.Utility](../xrm-utility.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]