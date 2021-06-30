---
title: "getContentWindow (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getContentWindow method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: ad68d177-3715-468e-b4af-8cf9b3c77799
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getContentWindow (Client API reference)

Returns the content window that represents an IFRAME or web resource.

> [!NOTE]
> This method is supported only on [Unified Interface](../../../../../user/unified-interface.md).

## Control types supported

iframe, web resource

## Syntax

```JavaScript
formContext.getControl(arg).getContentWindow().then(successCallback, errorCallback);
```

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name |Type|Required|Description|
|---|---|---|---|
|successCallback|Function|No|A function to call when operation is executed successfully. A content window instance representing the IFRAME or web resource is passed to the function.|
|errorCallback|Function|No|A function to call when the operation fails.|


## Return Value

On success, returns a promise that contains a content window instance representing an IFRAME or web resource.

## Example

The following example shows how you can use this method with a HTML Web resource (new_myWebResource.htm).

First, add the following code in your HTML web resource:

```javascript
// This script should be in the HTML web resource.
// No usage of Xrm or formContext should happen until this method is called.
function setClientApiContext(xrm, formContext) {
    // Optionally set Xrm and formContext as global variables on the page.
    window.Xrm = xrm;
    window._formContext = formContext;
     
    // Add script logic here that uses xrm or the formContext.
}
```

Next, add the following code in the form OnLoad event handler:

```javascript
// This should be in a script loaded on the form. 
// form_onload is a handler for the form onload event.
function form_onload(executionContext) {
    var formContext = executionContext.getFormContext();
    var wrControl = formContext.getControl("new_myWebResource.htm");
    if (wrControl) {
        wrControl.getContentWindow().then(
            function (contentWindow) {
                contentWindow.setClientApiContext(Xrm, formContext);
            }
        )
    }
}
```

Similar initialization code should be added to a TabStateChange event handler if such initialization is necessary. Any initialization code should be idempotent if it is re-used. For performance reasons, the form may destroy and re-initialize the control during tab navigations.


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
