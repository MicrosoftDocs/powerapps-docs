---
title: "invokeProcessAction (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
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

For more information about actions, see [Use actions](https://docs.microsoft.com/powerapps/maker/common-data-service/actions)

## Syntax

`Xrm.Utility.invokeProcessAction(name,parameters).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|name|String|Yes|Name of the process action to invoke.|
|parameters|object|No|An object containing input parameters for the action. You define an object using `key:value` pairs of items, where `key` is of **String** type.|
|successCallback |Function |Yes |A function to call when the action is invoked.  |
|errorCallback |Function |Yes |A function to call when the operation fails.  |

## Returns

On success, returns Web API result along with any action output.

### Related topics

[Use actions](https://docs.microsoft.com/powerapps/maker/common-data-service/actions)

[Xrm.Utility](../xrm-utility.md)


