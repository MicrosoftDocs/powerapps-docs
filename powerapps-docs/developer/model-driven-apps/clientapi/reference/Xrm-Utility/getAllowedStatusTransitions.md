---
title: "getAllowedStatusTransitions (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getAllowedStatusTransitions method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 28c36741-0070-435c-a42f-49f4dda2ef7f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# getAllowedStatusTransitions (Client API reference)


[!INCLUDE[./includes/getAllowedStatusTransitions-description.md](./includes/getAllowedStatusTransitions-description.md)] 

## Syntax

`Xrm.Utility.getAllowedStatusTransitions(entityName,statusCode).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|entityName|String|Yes|The logical name of the table.|
|statusCode|Number|Yes|The status code to find out the allowed status transition values.|
|successCallback|Function|No|The function to execute when the operation succeeds.|
|errorCallback|Function|No|The function to execute when the operation fails.|

## Return value

Returns an object with `.then()` function. The parameter to the delegate is an array of numbers representing the valid status transitions.

### Related topics

[Xrm.Utility](../xrm-utility.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]