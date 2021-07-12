---
title: Label control in Power Apps
description: Learn about the details, properties and examples of the label control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/25/2016
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Label control in Power Apps

A box that shows data such as text, numbers, dates, or currency.

## Description

A label shows data that you specify as a literal string of text, which appears exactly the way you type it, or as a formula that evaluates to a string of text. Labels often appear outside of any other control (such as a banner that identifies a screen), as a label that identifies another control (such as a rating or audio control), or in a gallery to show a specific type of information about an item.

## Key properties

**[AutoHeight](properties-core.md)** – Set to true to allow the label to auto-grow its height to show all text. Set to false to truncate the text to the height assigned.

**[Color](properties-color-border.md)** – The color of text in a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

**[DelayOutput](properties-core.md)** – Set to true to delay action during text input.

## Additional properties

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoHeight** – Whether a label automatically increases its **[Height](properties-size-location.md)** property if its **[Text](properties-core.md)** property contains more characters than the control can show at one time.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](properties-text.md)** – The distance between, for example, lines of text or items in a list.

**[Live](properties-accessibility.md)** – How a screen reader announces changes to the value of the label's **Text** property.

* When set to **Off**, the screen reader doesn't announce changes.
* When set to **Polite**, the screen reader finishes speaking before announcing any changes that occurred while the screen reader was speaking.
* When set to **Assertive**, the screen reader interrupts itself to announce any changes that occurred while the screen reader was speaking.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**Overflow** – Whether a scrollbar appears in a label if its **Wrap** property is set to **true** and the value of the control's **[Text](properties-core.md)** property contains more characters than the control can show at one time.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**Role** - The semantic role of the label text, such as Heading 1. Doesn't change the style of the label but makes the output semantically correct for interpretation by screen readers.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**Wrap** – Whether text that's too long to fit in a label wraps to the next line.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

[**Text**( *Number*, "*FormatCodes*" )](../functions/function-text.md)

## Examples

### Show a literal string

* Add a label, and set its **[Text](properties-core.md)** property to **"Hello, world"** (including the double quotation marks).
  
    Don't know how to [add and configure a control](../add-configure-controls.md)?

### Show the result of a formula

* Add a label, and set its **[Text](properties-core.md)** property to a formula such as this one:<br>
  **Today()**
  
    > [!NOTE]
  > When you specify a formula, you don't use quotation marks unless an argument of the formula is a literal string. In that case, enclose the argument, not the formula, in double quotation marks.
  
    Want more information about the **[Today](../functions/function-now-today-istoday.md)** function or [other functions](../formula-reference.md)?

### Show data in a gallery

In this procedure, you'll create a collection, called **CityPopulations**, that contains data about the population of various cities in Europe. Next, you'll show that data in a gallery that contains three labels, and you'll specify the type of data that each label will show.

1. Add a button, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**
2. Press F5, select the button, and then press Esc.
3. Add a text gallery, and set its **[Items](properties-core.md)** property to **CityPopulations**.

    When the gallery is selected, the right pane shows options for that gallery.
4. In the **Gallery1** pane, set the top list to **Population**, set the middle list to **City**, and set the bottom list to **Country**.

## Accessibility guidelines

Despite its name, a **Label** control does not have to be used as a label for another control. It can be used to display any piece of text.

A **Label** can be used as a button or link by specifying **[OnSelect](properties-core.md)** behavior. When used this way, there are similar accessibility considerations as with buttons.

### Color contrast

There must be adequate color contrast between:

* **[Color](properties-color-border.md)** and **[Fill](properties-color-border.md)**
* Other [standard color contrast requirements](../accessible-apps-color.md) apply (if used as a button or link)

### Screen-reader support

* **[Text](properties-core.md)** must be present.
* **[Live](properties-accessibility.md)** should be set to **Polite** or **Assertive** if a screen reader should announce changes to the value of the **Text** property.

  > [!NOTE]
  > Screen readers will treat **Label**s as buttons when **[TabIndex](properties-accessibility.md)** is zero or greater.

### Low vision support

* **Label** should look like a link, if it is used as a link.
  * Set **[Underline](properties-text.md)** to **true**
  * **[HoverColor](properties-color-border.md)** should be different from **[Color](properties-color-border.md)**

### Keyboard support

* **[TabIndex](properties-accessibility.md)** must be zero or greater, if the text is used as a button or link. This allows keyboard users to navigate to it.
* Focus indicators must be clearly visible, if the text is used as a button or link. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]