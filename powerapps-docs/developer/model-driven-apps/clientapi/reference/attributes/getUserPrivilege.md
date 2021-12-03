---
title: "getUserPrivilege (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getUserPrivilege method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0a3f0349-af9a-418a-b99d-5085999884eb
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
# getUserPrivilege (Client API reference)



Returns an object with three boolean properties corresponding to privileges indicating if the user can create, read or update data values for a column. This function is intended for use when Field Level Security modifies a user’s privileges for a particular column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getUserPrivilege()`

## Return Value

**Type**: Object. 

**Description**: The object has three boolean properties:
- canRead
- canUpdate
- canCreate



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]