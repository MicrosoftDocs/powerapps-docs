---
title: "getEntityTypes (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c20ba958-821f-4168-a518-e39431603b28
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getEntityTypes (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

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
