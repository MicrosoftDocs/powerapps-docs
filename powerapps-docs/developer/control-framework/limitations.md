---
title: "Limitations of PowerApps Component Framework | MicrosoftDocs"
description: "Limitations using powerapps Component framework"
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Limitations of PowerApps Component Framework

With the release of the PowerApps Component Framework, you can now create your own custom controls to improve the user experience in Model-driven Apps. Even though you can create your own controls, there are some limitations that restrict developers implementing some features in the custom controls.Below are some of the limitations:

### Multiple controls in single manifest file

It is not possible to define multiple controls in a single manifest file. There is a workaround to achieve this, but it is not recommended until Microsoft releases a generic way.

### Calling Processes/Actions

This is not supported yet. For now you can only call dialog boxes using the [Navigation](reference/navigation.md) method.

### Support for external libraries

The PowerApps Component Framework supports all the external libraries for implementing custom controls. 

> [!NOTE]
> When you use JQuery for implementing the custom controls, at run time, it loads the platform version of the JQuery not the version you used to implement. 

### Calling controls within another control

This is not supported yet.

### Font Resource

Currently font resource (.tff) is not supported in PCF.

### Custom controls on header section on a form

When you add a custom control in the header section of a form, the form editor stops working and sometimes prevent you from removing control.
