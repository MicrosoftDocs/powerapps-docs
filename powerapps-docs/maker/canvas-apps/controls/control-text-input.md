---
title: Text input control in Power Apps
description: Learn about the details, properties and examples of the text input control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/22/2019
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Text input control in Power Apps
A box in which the user can type text, numbers, and other data.

## Description
The user can specify data by typing into a text-input control. Depending on how you configure the app, that data might be added to a data source, used to calculate a temporary value, or incorporated in some other way.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**Clear** – Whether a text-input control shows an "X" that the user can tap or click to clear the contents of that control.

**[Color](properties-color-border.md)** – The color of text in a control.

**DelayOutput** – When set to true, user input is registered after half a second delay.  Useful for delaying expensive operations until user completes inputting text (i.e. for filtering when input is used in other formulas).

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**EnableSpellCheck** – Whether a text-input control should use the browser spell check function. Power Apps for Windows doesn't support this property.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**Format** – Whether the user input is restricted to numbers only or can be any text.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**HintText** – Light-grey text that appears in an input-text control if it's empty.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](properties-text.md)** – The distance between, for example, lines of text or items in a list.

**MaxLength** – The number of characters that the user can type into a text-input control.

**Mode** – The control is in **SingleLine**, **MultiLine**, or **Password** mode.

**[OnChange](properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**VirtualKeyboardMode** – Type of virtual keyboard, text or numeric, that appears on an app user's touch screen. The **Format** property determines the default value. Device support varies. Devices that are running iOS must have at least version 12.2. The recommended version of Android is 9.0, and capabilities of numeric keyboards vary for Android devices. Windows 10 doesn't support this property.  

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**DateTimeValue**( *String* )](../functions/function-datevalue-timevalue.md)

## Examples
### Collect data
1. Add two text-input controls, and name them **inputFirst** and **inputLast**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a button, set its **[Text](properties-core.md)** property to **Add**, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(Names, {FirstName:inputFirst.Text, LastName:inputLast.Text})**
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
3. Add a text gallery in portrait/vertical orientation, set its **[Items](properties-core.md)** property to **Names**, and set the **[Text](properties-core.md)** property of **Subtitle1** to **ThisItem.FirstName**.
4. (optional) In the template gallery, delete the bottom label, named **Body1**, and set the **[TemplateSize](control-gallery.md)** property of the gallery to **80**.
5. Press F5, type a string of text into **inputFirst** and **inputLast**, and then click or tap the **Add** button.
6. (optional) Add more names to the collection, and then press Esc to return to the default workspace.

### Prompt for a password

1. Add a text-input control, name it **inputPassword**, and set its **Mode** property to **Password**.

1. Add a label, and set its **[Text](properties-core.md)** property to this formula:<br>
   **If(inputPassword.Text = "P@ssw0rd", "Access granted", "Access denied")**

    Want more information about the **[If](../functions/function-if.md)** function or [other functions](../formula-reference.md)?

1. Press F5, and then type **P\@ssw0rd** in **inputPassword**.

    When you finish typing the password, the label stops showing **Access denied** and starts to show **Access granted**.

1. To return to the default workspace, press Esc.

1. (optional) Add a control such as an arrow, configure it to navigate to another screen, and show it only after the user types the password.

1. (optional) Add a button, configure its **[Text](properties-core.md)** property to show **Sign in**, add a timer, and disable the input-text control for a certain amount of time if the user types the wrong password and then clicks or taps the **Sign in** button.


## Accessibility guidelines
### Color contrast
* [Standard color contrast requirements](../accessible-apps-color.md) apply.

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]