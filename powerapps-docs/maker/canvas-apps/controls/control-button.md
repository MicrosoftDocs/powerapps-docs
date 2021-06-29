---
title: Button control in Power Apps
description: Learn about the details, properties and examples of the button control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 01/28/2021
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Button control in Power Apps
A control that the user can click or tap to interact with the app.

## Description
Configure the **[OnSelect](properties-core.md)** property of a **Button** control to run one or more formulas when the user clicks or taps the control.

## Key properties
**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties
**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoDisableOnSelect** – Automatically disables the control while the **OnSelect** behavior is running.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**Pressed** – *True* while a control is being pressed, *false* otherwise.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
**[Navigate( *ScreenName*, *ScreenTransitionValue* )](../functions/function-navigate.md)**

## Examples
### Add a basic formula to a button
1. Add a **[Text input](control-text-input.md)** control, and name it **Source**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **Button** control, set its **[Text](properties-core.md)** property to "Add", and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **UpdateContext({Total:Total + Value(Source.Text)})**
   
    Want more information about the **[UpdateContext](../functions/function-updatecontext.md)** function or [other functions](../formula-reference.md)?
3. Add a **[Label](control-text-box.md)** control, set its **[Text](properties-core.md)** property in the formula bar to **Value(Total)**, and then press **F5**.
4. Clear the default text from **Source**, type a number in it, and then click or tap **Add**.
   
    The **[Label](control-text-box.md)** control shows the number that you typed.
5. Clear the number from **Source**, type another number in it, and then click or tap **Add**.
   
    The **[Label](control-text-box.md)** control shows the sum of the two numbers that you typed.
6. (optional) Repeat the previous step one or more times.
7. To return to the default workspace, press Esc (or click or tap the close icon in the upper-right corner).

### Configure a button with multiple formulas
Add a formula that clears the **Text input** control between entries.

1. Set the **[HintText](control-text-input.md)** property of **Source** to "Enter a number".
2. Set the **[OnSelect](properties-core.md)** property of **Add** to this formula:
   
    **UpdateContext({Total:Total + Value(Source.Text)});<br>UpdateContext({ClearInput: ""})**
   
    > [!NOTE]
   > Separate multiple formulas with a semi-colon “**;**”.
3. Set the **[Default](properties-core.md)** property of **Source** to **ClearInput**.
4. Press **F5**, and then test the app by adding several numbers together.

### Add another button to reset the total
Add a second button to clear the total between calculations.

1. Add another **Button** control, set its **[Text](properties-core.md)** property to "Clear", and set its **[OnSelect](properties-core.md)** property to this formula:
   
    **UpdateContext({Total:0})**
2. Press **F5**, add several numbers together, and then click or tap **Clear** to reset the total.

### Change a button's appearance
#### Change a button's shape
By default, Power Apps creates a rectangular **Button** control with rounded corners. You can make basic modifications to the shape of a **Button** control by setting its **[Height](properties-size-location.md)**, **[Width](properties-size-location.md)**, and **[Radius](properties-size-location.md)** properties.

> [!NOTE]
> [Icons and Shapes](control-shapes-icons.md) provide a wide variety of designs and can perform some of the same basic functions that **Button** controls do. However, **[Icons and Shapes](control-shapes-icons.md)** don’t have a **[Text](properties-core.md)** property.

1. Add a **Button** control, and set its **[Height](properties-size-location.md)** and **[Width](properties-size-location.md)** properties to **300** to make a large square button.
2. Modify the **[RadiusTopLeft](properties-size-location.md)**, **[RadiusTopRight](properties-size-location.md)**, **[RadiusBottomLeft](properties-size-location.md)**, and **[RadiusBottomRight](properties-size-location.md)** properties to adjust the amount of curvature on each corner. Here are some examples of different shapes, each one starting from a 300 x 300 square button:
   
   * Set all four **[Radius](properties-size-location.md)** values to **150** to create a circle.
   * Set the values for **[RadiusTopLeft](properties-size-location.md)** and **[RadiusBottomRight](properties-size-location.md)** to **300** to create a leaf-shaped **Button**.
   * Set the values for **[RadiusTopLeft](properties-size-location.md)** and **[RadiusTopRight](properties-size-location.md)** to **300**, and the values for **[RadiusBottomLeft](properties-size-location.md)** and **[RadiusBottomRight](properties-size-location.md)** to **100** to create a tab-shaped button.

#### Change a button's color when you hover over it
By default, the fill color of a **Button** control will dim by 20% when you hover over it with a mouse. You can adjust this behavior by changing the **[HoverFill](properties-color-border.md)** property, which uses the **[ColorFade](../functions/function-colors.md)** function. If you set the **[ColorFade](../functions/function-colors.md)** formula to a positive percentage, the color becomes lighter when you hover over the button, while a negative percentage makes the color darker.

* Change the **[ColorFade](../functions/function-colors.md)** percentage in the **[HoverFill](properties-color-border.md)** property of one of the buttons that you created, and observe the effects.

You can also specify the color of a **Button** control by setting its **[HoverFill](properties-color-border.md)** property to a formula that contains the **[ColorValue](../functions/function-colors.md)** function instead of the **[ColorFade](../functions/function-colors.md)** function, as in **ColorValue("Red")**.

> [!NOTE]
> The color value can be any CSS color definition, either a name or a hex value.

* Replace the **[ColorFade](../functions/function-colors.md)** function with a **[ColorValue](../functions/function-colors.md)** function in one of the buttons that you created, and observe the effects.


## Accessibility guidelines
### Color contrast
* [Standard color contrast requirements](../accessible-apps-color.md) apply.

### Screen reader support
* **[Text](properties-core.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]