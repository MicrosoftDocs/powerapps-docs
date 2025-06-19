---
title: "isAvailableOffline (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the isAvailableOffline method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# isAvailableOffline (Client API reference)

[!INCLUDE[./includes/isAvailableOffline-description.md](./includes/isAvailableOffline-description.md)] 

## Syntax

`Xrm.WebApi.offline.isAvailableOffline(entityLogicalName);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|Logical name of the table. For example: `account`.|

## Return Value

**Type**: Boolean.

**Description**: true if the table is present in user's profile and is currently available for use in offline mode; otherwise false.

### Related articles

[Xrm.WebApi.offline](offline.md)   
[Xrm.WebApi](../xrm-webapi.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
