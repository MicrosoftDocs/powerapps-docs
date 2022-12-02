---
title: "setEntityTypes (Client API reference) in model-driven apps| MicrosoftDocs"
description: Sets the types of tables allowed in the lookup control.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# setEntityTypes (Client API reference)



Sets the types of tables allowed in the lookup control.

## Control types supported

Lookup control

## Syntax

`formContext.getControl(arg).setEntityTypes([entityLogicalNames]);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|entityLogicalNames|Array of String|Yes|Specify the logical name of the tables allowed in the lookup control.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

### Related topics

[getEntityTypes](getEntityTypes.md)

 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]