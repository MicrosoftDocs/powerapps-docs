---
title: 'Text-input control: reference | Microsoft Docs'
description: Information, including properties and examples, about the text-input control
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
# Text input control in PowerApps
A box in which the user can type text, numbers, and other data.

## Description
The user can specify data by typing into a text-input control. Depending on how you configure the app, that data might be added to a data source, used to calculate a temporary value, or incorporated in some other way.

## Key properties
**[Default](../../controls/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](../../controls/properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties
**[Align](../../controls/properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](../../controls/properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**Clear** – Whether a text-input control shows an "X" that the user can tap or click to clear the contents of that control.

**[Color](../../controls/properties-color-border.md)** – The color of text in a control.

**DelayOutput** – When set to true, user input is registered after half a second delay.  Useful for delaying expensive operations until user completes inputting text (i.e. for filtering when input is used in other formulas).

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](../../controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledColor](../../controls/properties-color-border.md)** – The color of text in a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](../../controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[Fill](../../controls/properties-color-border.md)** – The background color of a control.

**[Font](../../controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../../controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**Format** – Whether the user input is restricted to numbers only or can be any text.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**HintText** – Light-grey text that appears in an input-text control if it's empty.

**[HoverBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../../controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../../controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../../controls/properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](../../controls/properties-text.md)** – The distance between, for example, lines of text or items in a list.

**MaxLength** – The number of characters that the user can type into a text-input control.

**Mode** – The control is in **SingleLine**, **MultiLine**, or **Password** mode.

**[OnChange](../../controls/properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../../controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../../controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](../../controls/properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](../../controls/properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](../../controls/properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](../../controls/properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Reset](../../controls/properties-core.md)** – Whether a control reverts to its default value.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../../controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../../controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**DateTimeValue**( *String* )](../../functions/function-datevalue-timevalue.md)

## Examples
### Collect data
1. Add two text-input controls, and name them **inputFirst** and **inputLast**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a button, set its **[Text](../../controls/properties-core.md)** property to **Add**, and set its **[OnSelect](../../controls/properties-core.md)** property to this formula:<br>
   **Collect(Names, {FirstName:inputFirst.Text, LastName:inputLast.Text})**
   
    Want more information about the **[Collect](../../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
3. Add a text gallery in portrait/vertical orientation, set its **[Items](../../controls/properties-core.md)** property to **Names**, and set the **[Text](../../controls/properties-core.md)** property of **Subtitle1** to **ThisItem.FirstName**.
4. (optional) In the template gallery, delete the bottom label, named **Body1**, and set the **[TemplateSize](control-gallery.md)** property of the gallery to **80**.
5. Press F5, type a string of text into **inputFirst** and **inputLast**, and then click or tap the **Add** button.
6. (optional) Add more names to the collection, and then press Esc to return to the default workspace.

### Prompt for a password
1. Add a text-input control, name it **inputPassword**, and set its **Mode** property to **Password**.
2. Add a label, and set its **[Text](../../controls/properties-core.md)** property to this formula:<br>
   **If(inputPassword.Text = "P@ssw0rd", "Access granted", "Access denied")**
   
    Want more information about the **[If](../../functions/function-if.md)** function or [other functions](../formula-reference.md)?
3. Press F5, and then type **P@ssw0rd** in **inputPassword**.
   
    When you finish typing the password, the label stops showing **Access denied** and starts to show **Access granted**.
4. To return to the default workspace, press Esc.
5. (optional) Add a control such as an arrow, configure it to navigate to another screen, and show it only after the user types the password.
6. (optional) Add a button, configure its **[Text](../../controls/properties-core.md)** property to show **Sign in**, add a timer, and disable the input-text control for a certain amount of time if the user types the wrong password and then clicks or taps the **Sign in** button.

