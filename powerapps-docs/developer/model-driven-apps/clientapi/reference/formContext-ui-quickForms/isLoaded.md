---
title: "isLoaded (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the isLoaded method.
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
# isLoaded (Client API reference)

[!INCLUDE[./includes/isLoaded-description.md](./includes/isLoaded-description.md)]

## Syntax

`quickViewControl.isLoaded();`

## Return Value

**Type**: Boolean.

**Description**: true is the data binding for a constituent control is complete; false otherwise. 

## Remarks

The data binding for the constituent controls in a quick view control might not be complete during the main form **OnLoad** event because the quick view form that the control is bound to might not be loaded. As a result, using the [getAttribute](../controls/getattribute.md) or any data-related methods on a constituent control might not work. The **isLoaded** method for the quick view control helps determine the data binding status for constituent controls in a quick view control.

## Example

The following sample code demonstrates how you can use the **isLoaded** method to check the binding status, and then retrieve the value of the column that a constituent control in a quick view control is bound to.

```JavaScript
function getAttributeValue(executionContext) {
    var formContext = executionContext.getFormContext();
    var quickViewControl = formContext.ui.quickForms.get("<QuickViewControlName>");
    if (quickViewControl != undefined) {
        if (quickViewControl.isLoaded()) {
            // Access the value of the column bound to the constituent control
            var myValue = quickViewControl.getControl(0).getAttribute().getValue();
            console.log(myValue);
            
            // Search by a specific column present in the control
            var myValue2 =  quickViewControl.getControl().find(control => control.getName() == "<AttributeSchemaName>").getAttribute().getValue();
            console.log(myValue2);
            
            return;
        }
    }
    else {
        console.log("No data to display in the quick view control.");
        return;
    }
}
```

### Related articles

[formContext.ui.quickForms](../formContext-ui-quickForms.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
