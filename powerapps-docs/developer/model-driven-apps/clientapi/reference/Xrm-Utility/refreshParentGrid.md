---
title: "refreshParentGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the refreshParentGrid method.
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