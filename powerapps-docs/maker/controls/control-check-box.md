---
title: 'Check Box control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Check Box control
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: fikaradz

---
# Check box control in PowerApps
A control that the user can select or clear to set its value to **true** or **false**.

## Description
The user can specify a Boolean value by using this familiar control, which has been used in GUIs for decades.

## Key properties
**[Default](../../controls/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](../../controls/properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Value](../../controls/properties-core.md)** – The value of an input control.

## Additional properties
**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**CheckboxBackgroundFill** – The background color of the box that surrounds the checkmark in a checkbox control.

**CheckboxBorderColor** – The color of the border that surrounds the checkmark in a checkbox control.

**CheckboxSize** – The width and height of the box that surrounds the checkmark in a checkbox control.

**CheckmarkFill** – The color of the checkmark in a checkbox control.

**[Color](../../controls/properties-color-border.md)** – The color of text in a control.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](../../controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledColor](../../controls/properties-color-border.md)** – The color of text in a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](../../controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[Fill](../../controls/properties-color-border.md)** – The background color of a control.

**[Font](../../controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../../controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../../controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../../controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../../controls/properties-text.md)** – Whether the text in a control is italic.

**OnCheck** – How an app responds when the value of a checkbox or a toggle changes to **true**.

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnUncheck** – How an app responds when the value of a checkbox or a toggle changes to **false**.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../../controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../../controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](../../controls/properties-core.md)** – Whether a control reverts to its default value.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../../controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../../controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](../../controls/properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**If**( *Condition*, *Result* )](../../functions/function-if.md)

## Example
1. Add a **Check box** control, name it **chkReserve**, and set its **[Text](../../controls/properties-core.md)** property to show **Reserve now**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Date picker](control-date-picker.md)** control, and set its **[Visible](../../controls/properties-core.md)** property to this formula:
   <br>**If(chkReserve.Value = true, true)**
   
    Want more information about the **[If](../../functions/function-if.md)** function or [other functions](../formula-reference.md)?
3. Press F5, click or tap **chkReserve** to set its **[Value](../../controls/properties-core.md)** property to **true**, and then click or tap **chkReserve** again to set its **[Value](../../controls/properties-core.md)** property to **false**.
   
    The **[Date Picker](control-date-picker.md)** control appears when the **[Value](../../controls/properties-core.md)** property of **chkReserve** is **true** but not when it's **false**.
4. To return to the default workspace, press Esc.

