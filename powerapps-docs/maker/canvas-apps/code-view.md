---
title: Code view for Canvas Apps (preview)
description: Learn about how to work with code with Power Apps.
author: marcelbf

ms.custom: canvas
ms.collection: get-started
ms.topic: conceptual
ms.reviewer: 
ms.date: 5/13/2024
ms.subservice: canvas-maker
ms.author: marcelbf
search.audienceType: 
  - maker
  - developer
---
# Code view for canvas apps (preview)

You can now view the underlying code to understand app functionality. 
All the controls of your screen will have a code representation. 
The format used is a subset of YAML, an update from the [YAML formula grammar](https://learn.microsoft.com/en-us/power-platform/power-fx/yaml-formula-grammar).

Because now we represent the canvas app in a code format, you can:

* View a code representation of your control.
* Copy the control as code, to be shared outside of Power Apps Studio.
* Paste a control as code, allowing you to create new controls from the code.

> [!IMPORTANT]
> 
> Format is subjected to change. We don’t guarantee compatibility with the final version.
> The current code format is not suitable to source control during the preview.

## Code view

> [!IMPORTANT]
> 
> To use this feature, Power Fx formula bar must be turned on.
>
> The formula bar is **ON** by default for new apps. For existing apps follow these steps to turn on the Power FX formula bar:
> - Open our app in Power Apps Studio, select **Settings** > **Upcoming features** > **Preview** > set the **Power Fx formula bar** toggle to **ON**.
>
> Your feedback is critical as we make this updated formula bar the default experience for all apps. 

To visualize the code of a given control, you can right click either in the Canvas/screen or in the Tree view, and select “Code View”.
Code view will show the code for the selected control and all controls underneath. You can use the shortcut Ctrl + F to find any string.

## Copy code

To copy the code of a given control, you can right click either in the Canvas/screen or in the Tree view, and select “copy code”
You can now paste the code in any windows outside of the browser. 

## Paste code

To create a new control from code, right click the control where you want to create a new item underneath and select Paste code.
You must use the YAML format that have been generated from Power Apps Studio. The code will be validated before the control is created.

## Know limitations

* You cannot copy, paste and there’s no code view for the App Object.
* You can’t edit the code in the code view.
* You can only copy controls within screens – copying screens are not supported yet.

This article provides only an overview of working with formulas. Browse the [formula reference](formula-reference.md) for more details and the complete list of functions, operators, and other building blocks you can use. 

### See also

[YAML format](formula-bar-find-replace.md)
[Formula bar](formula-bar-find-replace.md)
[Use Find and Replace capability in the formula bar](formula-bar-find-replace.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
