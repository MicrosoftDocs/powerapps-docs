---
title: "getCurrentAppName (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getCurrentAppName method.
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
|`successCallback` |Function |Yes |A function to call when the business app name is returned.  |
|`errorCallback` |Function |Yes |A function to call when the operation fails.  |

## Return Value

If this method is called in the context of a business app, returns the name of the business app. Otherwise, it fails with an error.

### Related articles

[Create, manage, and publish model-driven apps using code](../../../../create-manage-model-driven-apps-using-code.md)   
[Xrm.Utility.getGlobalContext](../getGlobalContext.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
