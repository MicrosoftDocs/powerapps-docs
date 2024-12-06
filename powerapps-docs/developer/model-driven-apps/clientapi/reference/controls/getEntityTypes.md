---
title: "getEntityTypes (Client API reference) in model-driven apps"
description: Gets the types of tables allowed in the lookup control.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getEntityTypes (Client API reference)

Gets the types of tables allowed in the lookup control. 

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Control types supported

Lookup control

## Syntax

`formContext.getControl(arg).getEntityTypes();`

## Return Value

**Type**: Array of String

**Description**: The logical names of the tables allowed in this control.

### Related articles

[setEntityTypes](setEntityTypes.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
