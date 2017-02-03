<properties
    pageTitle="Button control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Button control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="fikaradz"
    manager="anneta"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/25/2016"
   ms.author="fikaradz"/>

# Button control in PowerApps #
A control that the user can click or tap to interact with the app.

## Description ##
Configure the **[OnSelect](properties-core.md)** property of a **Button** control to run one or more formulas when the user clicks or taps the control.

## Key properties ##

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties ##

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**[Color](properties-color-border.md)** – The color of text in a control.

**[Disabled](properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[Disabled](properties-core.md)** property is set to **true**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[Disabled](properties-core.md)** property is set to **true**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[Disabled](properties-core.md)** property is set to **true**.

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

**[TabIndex](properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Navigate**( *ScreenName*, *ScreenTransitionValue* )](../functions/function-navigate.md)

## Example ##
1. Add a **[Text input](control-text-input.md)** control, and name it **Source**.

	Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add a **Button** control, set its **[Text](properties-core.md)** property to show **Add**, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
**UpdateContext({Total:Total + Value(Source.Text)})**

	Want more information about the **[UpdateContext](../functions/function-updatecontext.md)** function or [other functions](../formula-reference.md)?

1. Add a **[Text box](control-text-box.md)** control, set its **[Text](properties-core.md)** property to show **Total**, and then press F5.

1. Type a number in **Source**, and then click or tap **Add**.

	The **[Text box](control-text-box.md)** control shows the number that you typed.

1. Repeat the previous step one or more times.

	The **[Text box](control-text-box.md)** control shows the sum of the numbers that you typed.

1. To return to the default workspace, press Esc.
