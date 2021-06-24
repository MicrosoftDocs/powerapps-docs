---
title: "getShowTime (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getShowTime method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 43341b96-ca2c-4c7e-b6d5-fe7a5fd3c8b2
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getShowTime (Client API reference)

Get whether a date control shows the time portion of the date. 

## Control types supported

standard control for **datetime** columns.

## Syntax

`formContext.getControl(arg).getShowTime();`

## Return Value

**Type**: Boolean

**Description**: true if shows the time portion of the date; false otherwise.

### Related topics

[setShowTime](setShowTime.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]