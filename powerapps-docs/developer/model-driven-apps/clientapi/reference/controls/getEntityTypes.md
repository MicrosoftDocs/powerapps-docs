---
title: "getEntityTypes (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets the types of tables allowed in the lookup control.
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

### Related topics

[setEntityTypes](setEntityTypes.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]