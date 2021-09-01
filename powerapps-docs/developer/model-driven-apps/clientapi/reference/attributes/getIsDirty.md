---
title: "getIsDirty (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getIsDirty method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5f75ecae-a946-47a0-b748-96525b556f31
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getIsDirty (Client API reference)

Returns a boolean value indicating if there are unsaved changes to the column value. An unsaved change to a column value means the client value is different from the last known committed value retrieved from Dataverse by the client from runtime.

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getIsDirty()`

## Return Value

**Type**: Boolean. 

**Description**: True if there are unsaved changes, otherwise false.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
