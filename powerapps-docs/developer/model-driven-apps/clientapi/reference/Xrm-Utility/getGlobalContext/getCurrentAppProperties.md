---
title: "getCurrentAppProperties (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getCurrentAppProperties method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5f8d91ff-ba0d-4e90-a79a-18e32d09baa3
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getCurrentAppProperties (Client API reference)



Returns the properties of the current business app in model-driven apps.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getCurrentAppProperties().then(successCallback, errorCallback);
``` 

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|successCallback |Function |Yes |A function to call when the business app property information is returned. An object with the following attributes (app properties) is passed to the function :<br/>- **appId**<br/>- **displayName**<br/>- **uniqueName**<br/>- **url**<br/>- **webResourceId**<br/>- **webResourceName**<br/>- **welcomePageId**<br/>- **welcomePageName**|
|errorCallback |Function |Yes |A function to call when the operation fails.  |

## Return Value

If this method is called in the context of a business app, returns the properties of the business app. Otherwise, it fails with an error.

### Related topics

[Create, manage, and publish model-driven apps using code](../../../../create-manage-model-driven-apps-using-code.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md) 





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]