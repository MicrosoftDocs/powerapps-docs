---
title: "invokeProcessAction (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e71012ba-249d-4ae7-8891-f7d3ae16a20a
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# invokeProcessAction (Client API reference)



[!INCLUDE[./includes/invokeProcessAction-description.md](./includes/invokeProcessAction-description.md)] 

For more information about actions, see [Actions overview](../../../../customize/actions.md)

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

[Actions overview](../../../../customize/actions.md)

[Xrm.Utility](../xrm-utility.md)


