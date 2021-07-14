---
title: HTML text control in Power Apps
description: Learn about the details, properties, and examples of the HTML text control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.subservice: canvas-maker
ms.date: 07/13/2021
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# HTML text control in Power Apps
A box that shows text and converts HTML tags to formatting.

## Description
An **HTML text** control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

> [!NOTE]
> HTML text control assumes the HtmlText is relatively positioned. If you need to use an absolute position for your HTML text, wrap the text around a relatively positioned div. For example, `"<div style='position:relative'>" & varPageContent & "</div>"`

## Key properties
**[Color](properties-color-border.md)** – The color of text in a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**HtmlText** – Text that appears in an HTML text control and that may contain HTML tags.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](properties-core.md)** – Actions to do when the user selects a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Find**( *FindString*, *WithinString* )](../functions/function-find.md)

## Example

1. Add a **[Label](control-text-box.md)** control, name it **Source**, and set its **[Text](properties-core.md)** property to this string:

    "\<p>We've\&nbsp;done an unusually \&quot;deep\&quot; globalization and localization.\<p>"

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add an **HTML text** control, and set its **HtmlText** property to this value:<br>
   **Source.Text**
   
     The **HTML text** control shows the same text as the **[Label](control-text-box.md)** control but converts the tags to the appropriate characters.

## Accessibility guidelines
**HTML text** isn't meant to be interactive. Use it only for text display.

### Color contrast
There must be adequate color contrast between:
* **[Color](properties-color-border.md)** and **[Fill](properties-color-border.md)**
* Text with custom colors and its background

### Screen reader support
* **HtmlText** must be present.

### Keyboard support
* **HtmlText** shouldn't contain interactive elements like `<button>`, `<a>`, or `<input>`. The **[TabIndex](properties-accessibility.md)** system in Power Apps doesn't consider elements inside **HtmlText**.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
