<properties
    pageTitle="Check Box control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Check Box control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="03/09/2016"
   ms.author="anneta"/>

# Check box control in PowerApps #
A control that the user can select or clear to set its value to **true** or **false**.

## Description ##
The user can specify a Boolean value by using this familiar control, which has been used in GUIs for decades.

## Key properties ##

**[Default](../properties/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](../properties/properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Value](../properties/properties-core.md)** – The value of an input control.

## Additional properties ##

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**CheckboxBackgroundFill** – The background color of the box that surrounds the checkmark in a checkbox control.

**CheckboxBorderColor** – The color of the border that surrounds the checkmark in a checkbox control.

**CheckboxSize** – The width and height of the box that surrounds the checkmark in a checkbox control.

**CheckmarkFill** – The color of the checkmark in a checkbox control.

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **Disabled** property is set to **true**.

**[DisabledColor](../properties/properties-color-border.md)** – The color of text in a control if its **Disabled** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **Disabled** property is set to **true**.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Font](../properties/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../properties/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../properties/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../properties/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../properties/properties-text.md)** – Whether the text in a control is italic.

**OnCheck** – How an app responds when the value of a checkbox or a toggle changes to **true**.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnUncheck** – How an app responds when the value of a checkbox or a toggle changes to **false**.

**[PaddingBottom](../properties/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../properties/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../properties/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../properties/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../properties/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../properties/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](../properties/properties-core.md)** – Whether a control reverts to its default value.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../properties/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../properties/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](../properties/properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**If**( *Condition*, *Result* )](function-if.md)

## Example ##
1. Add a **Check box** control, name it **chkReserve**, and set its **Text** property to show **Reserve now**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a **Date picker** control, and set its **Visible** property to this formula:
<br>**If(chkReserve.Value = true, true)**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, click or tap **chkReserve** to set its **Value** property to **true**, and then click or tap **chkReserve** again to set its **Value** property to **false**.

	The **Date Picker** control appears when the **Value** property of **chkReserve** is **true** but not when it's **false**.

1. To return to the default workspace, press Esc.
