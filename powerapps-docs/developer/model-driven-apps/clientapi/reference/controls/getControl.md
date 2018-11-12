---
title: "getControl (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 34715e1f-35c0-4b7f-971e-e0a6518f0722
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getControl (Client API reference)



Gets a control on the form. 

## Syntax

`formContext.getControl(arg);`

The **formContext.getControl(arg)** method is a shortcut method to access **formContext.ui.controls.get**.

## Parameter

**arg**: Optional. You can access a ontrol on a form by passing an argument as either the **name** or the **index valu**e of the control on a form. For example: `formContext.getControl("firstname")` or `formContext.getControl(0)`


## Return Value

**Type**: Object or Object collection.

**Description**: Object if you use the method with parameter; object collection if you use the method without any parameters.



### Related topics

[formContext](../../clientapi-form-Context.md)



