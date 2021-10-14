---
title: "getControl (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getControl method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 57eb6b4b-90c1-4d56-b4b0-a7160af17f8f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getControl (Client API reference)



[!INCLUDE[./includes/getControl-description.md](./includes/getControl-description.md)]

## Syntax

`quickViewControl.getControl(arg);`

## Parameter

**arg**: Optional. You can access a single control in the constituent controls collection by passing an argument as either the name or the index value of the constituent control in a quick view control. For example: `quickViewControl.getControl("firstname")` or `quickViewControl.getControl(0)`


## Return Value

**Type**: Object or Object collection.

**Description**: Object if you use the method with parameter; object collection if you use the method without any parameters.

## Remarks

After you have retrieved a constituent control in a quick view control, you can use any of the methods supported for a control in model-driven apps on the constituent control that does not alter the constituent control data. This is because constituent controls in a quick view control are read only. For example, you can use: 

`quickViewControl.getControl(0).getAttribute()` 

For more information about methods supported for a control, see [Controls](../controls.md).

>[!IMPORTANT]
>The [getAttribute](../controls/getAttribute.md) or any data related methods on a constituent control might not work on the main form [OnLoad](../events/form-onload.md) event because the quick view form that its bound to might not have loaded completely when the main form has loaded. You must use the [isLoaded](isLoaded.md) method for the quick view control instance to help you determine if the bounded quick view form has loaded completely. 

>Also, the way you retrieve constituent controls in a quick view control on forms using the new form rendering engine is different from the legacy forms. So, if you are using legacy forms and have code targeting constituent controls in a quick view control, you must update your code when you decide to use the new form rendering engine.

### Related topics

[formContext.ui.quickForms](../formContext-ui-quickForms.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]