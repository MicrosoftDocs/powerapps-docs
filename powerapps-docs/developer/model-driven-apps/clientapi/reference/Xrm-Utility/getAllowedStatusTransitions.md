---
title: "getAllowedStatusTransitions (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getAllowedStatusTransitions method.
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

# getAllowedStatusTransitions (Client API reference)


[!INCLUDE[./includes/getAllowedStatusTransitions-description.md](./includes/getAllowedStatusTransitions-description.md)] 

## Syntax

`Xrm.Utility.getAllowedStatusTransitions(entityName,statusCode).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|`entityName`|String|Yes|The logical name of the table.|
|`statusCode`|Number|Yes|The status code to find out the allowed status transition values.|
|`successCallback`|Function|No|The function to execute when the operation succeeds.|
|`errorCallback`|Function|No|The function to execute when the operation fails.|

## Return value

Returns an object with `.then()` function. The parameter to the delegate is an array of numbers representing the valid status transitions.

### Related articles

[Xrm.Utility](../xrm-utility.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
