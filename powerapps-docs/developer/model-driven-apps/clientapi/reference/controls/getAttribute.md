---
title: "getAttribute (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5ba037da-59f3-4e10-80f8-4e46d5410f81
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getAttribute (Client API reference)



Returns the attribute that the control is bound to.

Controls that aren’t bound to an attribute (subgrid, web resource, and IFRAME) don’t have this method. An error will be thrown if you attempt to use this method on one of these controls. 

## Control types supported

Standard, Lookup, OptionSet

## Syntax

`formContext.getControl(arg).getAttribute();`

## Return Value

**Type**: Object

**Description**: An attribute

## Remarks

The constituent controls within a [quick view control](../formContext-ui-quickForms.md) are included in the controls collection and these controls have the **getAttribute** method. However, the attribute is not part of the attribute collection for the entity. While you can retrieve the value for that attribute using [getValue](getValue.md) and even change the value using [setValue](setValue.md), changes you make will not be saved with the entity.
 
The following code shows using the value the contact **mobilephone** attribute when displayed on an account entity form using a quick view control named **contactQuickForm**. This code hides the control when the value of the attribute is **null**.

```JavaScript
var quickViewMobilePhoneControl = formContext.getControl("contactQuickForm_contactQuickForm_contact_mobilephone");
if (quickViewMobilePhoneControl.getAttribute().getValue() == null) {
    quickViewMobilePhoneControl.setVisible(false);
}
```


[Quick view control](../formContext-ui-quickForms.md)

[Attributes](../attributes.md)


