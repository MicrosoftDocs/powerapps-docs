---
title: "invokeProcessAction (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the invokeProcessAction method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e71012ba-249d-4ae7-8891-f7d3ae16a20a
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# invokeProcessAction (Client API reference)



[!INCLUDE[./includes/invokeProcessAction-description.md](./includes/invokeProcessAction-description.md)] 

For more information about actions, see [Use actions](../../../../../maker/data-platform/actions.md)

## Syntax

`Xrm.Utility.invokeProcessAction(name,parameters).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|name|String|Yes|Name of the process action to invoke.|
|parameters|object|No|An object containing input parameters for the action. You define an object using `key:value` pairs of items, where `key` is of **String** type. To specify a target, add a pair with `Target` as the key and an object with key values `entityName` and `id` as the value.  |
|successCallback |Function |Yes |A function to call when the action is invoked.  |
|errorCallback |Function |Yes |A function to call when the operation fails.  |

## Returns

On success, returns an object with the Web API result along with any action output.
On failure, returns an object with error details.

### Related topics
[Use actions](../../../../../maker/data-platform/actions.md)

[Xrm.Utility](../xrm-utility.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]