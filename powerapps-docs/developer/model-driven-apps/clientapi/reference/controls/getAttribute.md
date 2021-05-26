---
title: "getAttribute (Client API reference) in model-driven apps| MicrosoftDocs"
description: Returns the column that the control is bound to.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5ba037da-59f3-4e10-80f8-4e46d5410f81
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getAttribute (Client API reference)

Returns the column that the control is bound to.

Controls that aren’t bound to a column (subgrid, web resource, and IFRAME) don’t have this method. An error will be thrown if you attempt to use this method on one of these controls. 

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Control types supported

Standard, Lookup, OptionSet

## Syntax

`formContext.getControl(arg).getAttribute();`

## Return Value

**Type**: Object

**Description**: A column

## Remarks

The constituent controls within a [quick view control](../formContext-ui-quickForms.md) are included in the controls collection and these controls have the **getAttribute** method. However, the column is not part of the column collection for the table. While you can retrieve the value for that column using [getValue](../attributes/getValue.md) and even change the value using [setValue](../attributes/setValue.md), changes you make will not be saved with the table.
 
The following code shows using the value the contact **mobilephone** column when displayed on an account form using a quick view control named **contactQuickForm**. This code hides the control when the value of the column is **null**.

```JavaScript
var quickViewMobilePhoneControl = formContext.getControl("contactQuickForm_contactQuickForm_contact_mobilephone");
if (quickViewMobilePhoneControl.getAttribute().getValue() == null) {
    quickViewMobilePhoneControl.setVisible(false);
}
```


[Quick view control](../formContext-ui-quickForms.md)

[Columns](../attributes.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]