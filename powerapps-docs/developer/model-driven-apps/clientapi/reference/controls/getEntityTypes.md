---
title: "getEntityTypes (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c20ba958-821f-4168-a518-e39431603b28
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEntityTypes (Client API reference)



Gets the types of entities allowed in the lookup control. 

## Control types supported

Lookup control

## Syntax

`formContext.getControl(arg).getEntityTypes();`

## Return Value

**Type**: Array of String

**Description**: The logical names of the entities allowed in this control.

### Related topics

[setEntityTypes](setEntityTypes.md)
