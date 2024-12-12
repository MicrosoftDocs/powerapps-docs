---
title: "getPageContext (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getPageContext method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getPageContext (Client API reference)


[!INCLUDE[./includes/getPageContext-description.md](./includes/getPageContext-description.md)]


> [!NOTE]
> This method is supported only on Unified Interface.

## Syntax

`Xrm.Utility.getPageContext();`

## Returns

The method returns an object with the `input` property. The `input` property is an object with the following values depending on whether you are currently on the *entity form* or *entity list*:

### Entity form

|Name |Type |Description|
|--|--|--|
|`pageType`|String|The current page type. The value returned is `entityrecord`.|
|`entityName`|String|Logical name of the table currently displayed.|
|`entityId`|String|ID of the table record currently displayed in the form.|
|`createFromEntity`|Lookup|The parent record that provides default values based on mapped column values. The lookup object has the following String properties: `entityType`, `id`, and `name`.|
|`formId`|String|ID of the currently displayed form.|


### Entity list

|Name |Type |Description|
|--|--|--|
|`pageType`|String|The current page type. The value returned is `entitylist`.|
|`entityName`|String|Logical name of the table currently displayed.|
|`viewId`|String|ID of the view currently displayed.|
|`viewType`|String|Type of the view currently displayed. Possible values are `savedquery` or `userquery`.|

> [!NOTE]
> Only the `pageType` and `entityName` parameters will return values every time; all other parameters will return values only if specified by the logic that opened the page.

### Related articles

[Xrm.Utility](../xrm-utility.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
