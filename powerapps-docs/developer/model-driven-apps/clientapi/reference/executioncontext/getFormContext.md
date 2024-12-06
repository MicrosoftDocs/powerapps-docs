---
title: "getFormContext (Client API reference) in model-driven apps"
description: "Learn about the getFormContext method that returns a reference to the form or an item on the form depending on where the method was called." 
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getFormContext (Client API reference)

Returns a reference to the form or an item on the form depending on where the method was called.

## Syntax

`ExecutionContextObj.getFormContext()`

## Return value

**Type**: Object

**Description**: Returns a reference to the form or an item on the form such as editable grid depending on where the method was called. This method enables you to create common event handlers that can operate either on a form or an item on the form depending on where its called.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Example

The following sample code demonstrates how you can create a method that sets notification on a form column or editable grid cell depending on where you registered the script ([Column OnChange](../events/attribute-onchange.md) event or editable grid [OnChange](../events/grid-onchange.md) event):

```JavaScript
function commonEventHandler(executionContext) {
    var formContext = executionContext.getFormContext();    
    var telephoneAttr = formContext.data.entity.attributes.get('telephone1');
    var isNumberWithCountryCode = telephoneAttr.getValue().substring(0,1) === '+';

    // telephoneField will be a form control if invoked from a form OnChange event;
    // telephoneField will be a editable grid GridCell object if invoked from editable grid OnChange event.
    var telephoneField = telephoneAttr.controls.get(0);

    if (!isNumberWithCountryCode) {
        telephoneField.setNotification('Please include the country code beginning with '+'.', 'countryCodeNotification');
    }
    else {
        telephoneField.clearNotification('countryCodeNotification');
    }
}
```


### Related articles

[Execution context](../execution-context.md)   
[Form context](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
