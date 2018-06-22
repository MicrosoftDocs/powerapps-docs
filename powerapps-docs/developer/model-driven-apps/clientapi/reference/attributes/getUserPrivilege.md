---
title: "getUserPrivilege (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0a3f0349-af9a-418a-b99d-5085999884eb
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getUserPrivilege (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns an object with three Boolean properties corresponding to privileges indicating if the user can create, read or update data values for an attribute. This function is intended for use when Field Level Security modifies a user’s privileges for a particular attribute 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getUserPrivilege()`

## Return Value

**Type**: Object. 

**Description**: The object has three Boolean properties:
- canRead
- canUpdate
- canCreate

