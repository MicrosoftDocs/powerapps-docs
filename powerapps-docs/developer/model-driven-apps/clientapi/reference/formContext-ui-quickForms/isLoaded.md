---
title: "isLoaded (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isLoaded method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1870151d-6029-4733-ac35-6ee4d43f9553
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# isLoaded (Client API reference)



[!INCLUDE[./includes/isLoaded-description.md](./includes/isLoaded-description.md)]

## Syntax

`quickViewControl.isLoaded();`

## Return Value

**Type**: Boolean.

**Description**: true is the data binding for a constituent control is complete; false otherwise. 

## Remarks

The data binding for the constituent controls in a quick view control may not be complete during the main form **OnLoad** event because the quick view form that the control is bound to may not have loaded completely. As a result, using the [getAttribute](../controls/getattribute.md) or any data-related methods on a constituent control might not work. The **isLoaded** method for the quick view control helps determine the data binding status for constituent controls in a quick view control.

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
        else {
            // Wait for some time and check again
            setTimeout(getAttributeValue, 10, executionContext);
        }
    }
    else {
        console.log("No data to display in the quick view control.");
        return;
    }
}
```

### Related topics

[formContext.ui.quickForms](../formContext-ui-quickForms.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]