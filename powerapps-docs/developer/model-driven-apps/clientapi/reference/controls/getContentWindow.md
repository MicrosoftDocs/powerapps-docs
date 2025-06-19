---
title: "getContentWindow (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getContentWindow method.
author: MitiJ
ms.author: mijosh
ms.date: 08/15/2024
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - tahoon-ms
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
|`successCallback`|Function|No|A function to call when operation is executed successfully. A content window instance representing the IFRAME or web resource is passed to the function.|
|`errorCallback`|Function|No|A function to call when the operation fails.|


## Return Value

On success, returns a promise that contains a content window instance representing an IFRAME or web resource.

## Example

The following example shows how you can use this method with an HTML Web resource (new_myWebResource.htm).

First, add the following code in your HTML web resource:

```javascript
// This script should be in the HTML web resource.
function doStuff() {
    // Add desired script logic that executes on form load.
}
```

Next, add the following code in the form OnLoad event handler:

```javascript
// This should be in a script loaded on the form. 
// form_onload is a handler for the form onload event.
function form_onload(executionContext) {
    var formContext = executionContext.getFormContext();
    var wrControl = formContext.getControl("WebResource_CustomName");
    if (wrControl) {
        wrControl.getContentWindow().then(
            function (contentWindow) {
                contentWindow.doStuff();
            }
        )
    }
}
```

Similar initialization code should be added to a [TabStateChange event](../events/tabstatechange.md) handler if such initialization is necessary. Any initialization code should be idempotent if it's reused. For performance reasons, the form  might destroy and reinitialize the control during tab navigation.


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
