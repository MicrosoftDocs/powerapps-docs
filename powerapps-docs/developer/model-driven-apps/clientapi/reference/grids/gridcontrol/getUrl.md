---
title: "getUrl (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getUrl method.
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
# getUrl (Client API reference)



[!INCLUDE[./includes/getUrl-description.md](./includes/getUrl-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.getUrl(client);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`client`|Number|No|Indicates the client type. You can specify one of the following values:<br/>0: Browser<br/>1: MobileApplication|

## Return Value

**Type**: String

**Description**: The Url of the current grid control.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
