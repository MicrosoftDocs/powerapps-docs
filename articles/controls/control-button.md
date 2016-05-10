<properties
    pageTitle="Button control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Button control"
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
   ms.date="02/29/2016"
   ms.author="anneta"/>

# Button control in PowerApps #
A control that the user can click or tap to interact with the app.

## Description ##
Configure the **OnSelect** property of a **Button** control to run one or more formulas when the user clicks or taps the control.

## Key properties ##

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[Text](../properties/properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties ##

**[Align](../properties/properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

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

**[PaddingBottom](../properties/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../properties/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../properties/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../properties/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**Pressed** – *True* while a control is being pressed, *false* otherwise.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../properties/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../properties/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](../properties/properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](../properties/properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](../properties/properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](../properties/properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

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

[**Navigate**( *ScreenName*, *ScreenTransitionValue* )](function-navigate.md)

## Example ##
1. Add a **Text input** control, and name it **Source**.

	Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add a **Button** control, set its **Text** property to show **Add**, and set its **OnSelect** property to this formula:<br>
**UpdateContext({Total:Total + Value(Source.Text)})**

	Want more information about the [**UpdateContext** function](function-updatecontext.md) or [other functions](../formula-reference.md)?

1. Add a **Text box** control, set its **Text** property to show **Total**, and then press F5.

1. Type a number in **Source**, and then click or tap **Add**.

	The **Text box** control shows the number that you typed.

1. Repeat the previous step one or more times.

	The **Text box** control shows the sum of the numbers that you typed.

1. To return to the default workspace, press Esc.
