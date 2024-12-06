---
title: "formContext.getControl (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the formContext.getControl method.
author: MitiJ
ms.author: mijosh
ms.date: 04/15/2024
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

> [!NOTE]
> `getControl` only works on controls in the form body and header. It's not supported for controls elsewhere on the page, even if they refer to the same column.
> - For controls inside [business process flows](../../../../../user/work-with-business-processes.md), refer to them with the prefix [`header_process_`](../attributes/controls-collection.md).
> - Controls inside other controls like [subgrids](../../../../../maker/model-driven-apps/form-designer-add-configure-subgrid.md) and [timeline controls](../../../../../maker/model-driven-apps/set-up-timeline-control.md) are not supported.

## Syntax

`formContext.getControl(arg);`

The **formContext.getControl(arg)** method is a shortcut method to access **formContext.ui.controls.get**.

## Parameter

**arg**: Optional. You can access a control on a form by passing an argument as either the **name** or the **index value** of the control on a form. For example: `formContext.getControl("firstname")` or `formContext.getControl(0)`. If the `arg` name is spelled wrong and isn't on the form, it returns null value.

When the `arg` value isn't provided, it returns an array of all the controls on the form.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Object collection, Object or null.

**Description**: Object collection if you use the method without any parameters. Object or null if you use the method with a parameter. If you use the **name** as a parameter and there are multiple controls for the same column, then only the first control is returned.

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
