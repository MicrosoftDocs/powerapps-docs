---
title: "getIsDirty (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5f75ecae-a946-47a0-b748-96525b556f31
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getIsDirty (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns a Boolean value indicating if there are unsaved changes to the attribute value. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getIsDirty()`

## Return Value

**Type**: Boolean. 

**Description**: True if there are unsaved changes, otherwise false.