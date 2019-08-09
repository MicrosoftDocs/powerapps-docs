---
title: SetFocus function | Microsoft Docs
description: Reference information, including syntax, for the SetFocus function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/09/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# SetFocus function in PowerApps
Moves input focus to a specific control. 

## Description
The **SetFocus** function gives a control the input focus.  The user's keystrokes are then received by that control, allowing them to type into a text input control or use the *Enter* key to select a button.  The control with focus may be visually different based on the [**FocusedBorderColor**](../controls/properties-color-border.md) and [**FocusedBorderThickness**](../controls/properties-color-border.md) properties.  The user can also use the *Tab* key to move the input focus themselves. 

Use the **SetFocus** function within the **OnVisible** property of the [**Screen**](../controls/control-screen.md) to set the focus when a screen is displayed.  For example, when entering a screen you may always want the first text input control to have the focus.

**SetFocus** can be used with:
- [**Button**](../controls/control-button.md) control
- [**Icon**](../controls/control-shapes-icons.md) control
- [**Image**](../controls/control-image.md) control
- [**Label**](../controls/control-text-box.md) control
- [**TextInput**](../controls/control-text-input.md) control

You cannot set the focus to controls that are within a [**Gallery**](../controls/control-gallery.md) control, [**Edit form**](../controls/control-form-detail.md) control, or [Component](../create-component.md) from outside those containers.

You can only set the focus to controls on the same screen as the formula containing the **SetFocus** call.

Attempting to set the focus to a control that has its [**DisplayMode**](../controls/properties-core.md) property set to **Disabled** has no effect.  Focus will remain where it was previously.

On Apple iOS, the soft keyboard will not be displayed automatically. 

You can use **SetFocus** only in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**SetFocus**( *Control* )

* *Control* – Required.  The control to give the input focus.

