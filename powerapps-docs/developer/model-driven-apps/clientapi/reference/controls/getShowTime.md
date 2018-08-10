---
title: "getShowTime (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 43341b96-ca2c-4c7e-b6d5-fe7a5fd3c8b2
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getShowTime (Client API reference)



Get whether a date control shows the time portion of the date. 

## Control types supported

standard control for **datetime** attributes.

## Syntax

`formContext.getControl(arg).getShowTime();`

## Return Value

**Type**: Boolean

**Description**: true if shows the time portion of the date; false otherwise.

### Related topics

[setShowTime](setShowTime.md)

