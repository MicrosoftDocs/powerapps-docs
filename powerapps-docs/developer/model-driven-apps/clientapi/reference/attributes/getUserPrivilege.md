---
title: "getUserPrivilege (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0a3f0349-af9a-418a-b99d-5085999884eb
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getUserPrivilege (Client API reference)



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

