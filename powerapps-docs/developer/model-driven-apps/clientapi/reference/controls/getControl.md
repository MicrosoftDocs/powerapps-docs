---
title: "formContext.getControl (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the formContext.getControl method.
author: chmoncay
ms.author: chmoncay
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# formContext.getControl (Client API reference)

Gets a control on the form. 

## Syntax

`formContext.getControl(arg);`

The **formContext.getControl(arg)** method is a shortcut method to access **formContext.ui.controls.get**.

## Parameter

**arg**: Optional. You can access a control on a form by passing an argument as either the **name** or the **index value** of the control on a form. For example: `formContext.getControl("firstname")` or `formContext.getControl(0)`.

When the `arg` value is not provided, it returns an array of all the controls on the form. If the `arg` name is spelled wrong and is not on the form, it simply returns null value.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Object or Object collection.

**Description**: Object if you use the method with parameter; object collection if you use the method without any parameters.

> [!TIP]
> If you want to modify the all the controls bound to a column on a form, use the controls collection inside the column type.
For example, to add notification to each control bound to the `name` column, you can do the following:
> ```JavaScript
>  const notification = {
>  messages: ['Sample Notification on Name Controls'],
>  notificationLevel: 'RECOMMENDATION',
>  uniqueId: 'my_unique_id'};
> formContext.getAttribute("name").controls.forEach(control => control.addNotification(notification));
> ```


### Related articles

[formContext](../../clientapi-form-Context.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
