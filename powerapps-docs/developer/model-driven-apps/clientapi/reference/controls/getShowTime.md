---
title: "getShowTime (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getShowTime method.
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