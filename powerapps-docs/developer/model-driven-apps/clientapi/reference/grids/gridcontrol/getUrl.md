---
title: "getUrl (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getUrl method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: f2023d7d-5877-4436-abe6-e81ca68b8ec0
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
|client|Number|No|Indicates the client type. You can specify one of the following values:<br/>0: Browser<br/>1: MobileApplication|

## Return Value

**Type**: String

**Description**: The Url of the current grid control.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]