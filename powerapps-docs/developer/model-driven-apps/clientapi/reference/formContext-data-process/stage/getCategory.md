---
title: "getCategory (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getCategory method.
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
# getCategory (Client API reference)



[!INCLUDE[./includes/getCategory-description.md](./includes/getCategory-description.md)]

## Syntax

`var stageCategoryNumber = stageObj.getCategory().getValue();`

## Return Value

**Type**: Number. 

**Description**: Here is the list of possible values.

|Value |Description|
|--|--|
|0|Qualify|
|1|Develop|
|2|Propose|
|3|Close|
|4|Identify|
|5|Research|
|6|Resolve|

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]