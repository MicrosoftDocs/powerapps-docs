---
title: "getIsDirty (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5f75ecae-a946-47a0-b748-96525b556f31
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getIsDirty (Client API reference)



Returns a Boolean value indicating if there are unsaved changes to the attribute value. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getIsDirty()`

## Return Value

**Type**: Boolean. 

**Description**: True if there are unsaved changes, otherwise false.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]