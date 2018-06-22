---
title: "getFormContext (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
description: "Learn about the getFormContext method that returns a reference to the form or an item on the form depending on where the method was called." 
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9f3b2fed-fde5-46e4-8c59-43aa51aa82df
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getFormContext (Client API reference)



Returns a reference to the form or an item on the form depending on where the method was called.

## Syntax

`ExecutionContextObj.getFormContext()`

## Return value

**Type**: Object

**Description**: Returns a reference to the form or an item on the form such as editable grid depending on where the method was called. This method enables you to create common event handlers that can operate either on a form or an item on the form depending on where its called.

## Example

The following sample code demonstrates how you can create a method that sets notification on a form field or editable grid cell depending on where you registered the script ([Field OnChange](../events/attribute-onchange.md) event or editable grid [OnChange](../events/grid-onchange.md) event):

```JavaScript
function commonEventHandler(executionContext) {
    var formContext = executionContext.getFormContext();    
    var telephoneAttr = formContext.data.entity.attributes.getByName('telephone1');
    var isNumberWithCountryCode = telephoneAttr.getValue().substring(0,1) === '+';

    // telephoneField will be a form control if invoked from a form OnChange event;
    // telephoneField will be a editable grid GridCell object if invoked from editable grid OnChange event.
    var telephoneField = telephoneAttr.controls.getByIndex(0);

    if (!isNumberWithCountryCode) {
        telephoneField.setNotification('Please include the country code beginning with ‘+’.', 'countryCodeNotification');
    }
    else {
        telephoneField.clearNotification('countryCodeNotification');
    }
}
```


### Related topics
[Execution context](../execution-context.md)

[Form context](../../clientapi-form-context.md)





