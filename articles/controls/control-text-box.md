<properties
    pageTitle="Text-box control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the text-box control"
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

# Text box control in PowerApps #
A box that shows data such as text, numbers, dates, or currency.

## Description ##
A text box shows data that you specify as a literal string of text, which appears exactly the way you type it, or as a formula that evaluates to a string of text. Text boxes often appear outside of any other control (such as a banner that identifies a screen), as a label that identifies another control (such as a rating or audio control), or in a gallery to show a specific type of information about an item.

## Key properties ##

**[Color](properties-color-border.md)** – The color of text in a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

## Additional properties ##

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoHeight** – Whether a text box automatically increases its **[Height](properties-size-location.md)** property if its **[Text](properties-core.md)** property contains more characters than the control can show at one time.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Disabled](properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[Disabled](properties-core.md)** property is set to **true**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[Disabled](properties-core.md)** property is set to **true**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[Disabled](properties-core.md)** property is set to **true**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](properties-text.md)** – The distance between, for example, lines of text or items in a list.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**Overflow** – Whether a scrollbar appears in a text box if its **Wrap** property is set to **true** and the value of the control's **[Text](properties-core.md)** property contains more characters than the control can show at one time.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**Wrap** – Whether text that's too long to fit in a text box wraps to the next line.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**[Text](properties-core.md)**( *Number*, "*FormatCodes*" )](function-text.md)

## Examples ##

### Show a literal string ###
- Add a text box, and set its **[Text](properties-core.md)** property to **"Hello, world"** (including the double quotation marks).

	Don't know how to [add and configure a control](../add-configure-controls.md)?

### Show the result of a formula ###

- Add a text box, and set its **[Text](properties-core.md)** property to a formula such as this one:<br>
**Today()**

	**Note:** When you specify a formula, you don't use quotation marks unless an argument of the formula is a literal string. In that case, enclose the argument, not the formula, in double quotation marks.

	Want more information about the **[Today](../functions/function-now-today-istoday.md)** function or [other functions](../formula-reference.md)?

### Show data in a gallery ###
In this procedure, you'll create a collection, called **CityPopulations**, that contains data about the population of various cities in Europe. Next, you'll show that data in a gallery that contains three text boxes, and you'll specify the type of data that each text box will show.

1. Add a button, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**

1. Press F5, select the button, and then press Esc.

1. Add a text gallery, and set its **[Items](properties-core.md)** property to **CityPopulations**.

	When the gallery is selected, the right pane shows options for that gallery.

1. In the **Gallery1** pane, set the top list to **Population**, set the middle list to **City**, and set the bottom list to **Country**.
