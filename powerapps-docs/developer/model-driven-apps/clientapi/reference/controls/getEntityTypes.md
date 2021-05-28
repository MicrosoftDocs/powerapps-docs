---
title: "getEntityTypes (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets the types of tables allowed in the lookup control.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c20ba958-821f-4168-a518-e39431603b28
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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