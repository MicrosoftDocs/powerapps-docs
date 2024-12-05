---
title: "ui.refreshRibbon (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the ui.refreshRibbon method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# ui.refreshRibbon (Client API reference)

[!INCLUDE[./includes/refreshRibbon-description.md](./includes/refreshRibbon-description.md)]

## Syntax

`formContext.ui.refreshRibbon(refreshAll);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`refreshAll`|Boolean|No|Indicates whether all the ribbon command bars on the current page are refreshed. If you specify **false**, only the page-level ribbon command bar is refreshed. If you do not specify this parameter, by default **false** is passed.|

## Remarks

This function is used when a ribbon action `JavaScriptFunction` (RibbonDiffXml) changes the data in the form. For example, changing of state of the record via a ribbon action. After your code changes the data that is used by a rule, use this method to force the ribbon to reevaluate the data in the form so that the rule can be reapplied.

## Guidance

For optimal performance of your form loads, you should not use this function in `EnableRule` (RibbonDiffXml) or `onLoad` (FormXml). The form load itself triggers rules evaluation of all the ribbon actions. In case, if you want to control the visibility of a ribbon action, use promises and asynchronous pattern in `EnableRule`.


### Related articles

[formContext.ui](../formContext-ui.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
