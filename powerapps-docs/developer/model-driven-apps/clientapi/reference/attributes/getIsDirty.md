---
title: "attribute.getIsDirty (Client API reference)"
description: Includes description and supported parameters for the attribute.getIsDirty method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# attribute.getIsDirty (Client API reference)

Returns a boolean value indicating if there are unsaved changes to the column value. An unsaved change to a column value means the client value is different from the last known committed value retrieved from Dataverse by the client from runtime.

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getIsDirty()`

## Return Value

**Type**: Boolean

**Description**: True if there are unsaved changes, otherwise false.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
