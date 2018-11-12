---
title: "getCurrentAppName (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a8f83718-41a4-4958-a5ac-9b28cc2f8dba
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getCurrentAppName (Client API reference)



Returns the name of the current business app in model-driven apps.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getCurrentAppName().then(successCallback, errorCallback);
``` 

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|successCallback |Function |Yes |A function to call when the business app name is returned.  |
|errorCallback |Function |Yes |A function to call when the operation fails.  |

## Return Value

If this method is called in the context of a business app, returns the name of the business app. Otherwise, it fails with an error.

### Related topics

[Create, manage, and publish model-driven apps using code](../../../../create-manage-model-driven-apps-using-code.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


