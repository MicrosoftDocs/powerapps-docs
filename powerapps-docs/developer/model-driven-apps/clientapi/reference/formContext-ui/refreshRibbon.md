---
title: "refreshRibbon (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: dbd43d7b-c9b0-4ca5-943d-dd813d3bb049
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# refreshRibbon (Client API reference)



[!INCLUDE[./includes/refreshRibbon-description.md](./includes/refreshRibbon-description.md)]

## Syntax

`formContext.ui.refreshRibbon(refreshAll);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|refreshAll|Boolean|No|Indicates whether all the ribbon command bars on the current page are refreshed. If you specify **false**, only the page-level ribbon command bar is refreshed. If you do not specify this parameter, by default **false** is passed.|

## Remarks

 This function is typically used when a ribbon `<EnableRule>` (RibbonDiffXml) depends on a value in the form. After your code changes a value that is used by a rule, use this method to force the ribbon to re-evaluate the data in the form so that the rule can be applied.

### Related topics

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)

