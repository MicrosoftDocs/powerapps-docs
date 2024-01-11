---
title: HTML text control in Power Apps
description: Learn about the details, properties, and examples of the HTML text control in Power Apps.
author: chmoncay
ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.subservice: canvas-maker
ms.date: 07/19/2022
ms.author: chmoncay
search.audienceType:
  - maker
contributors:
  - mduelae
  - chmoncay
---
# HTML text control in Power Apps
A box that shows text and converts HTML tags to formatting.

## Description
An **HTML text** control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

> [!NOTE]
> HTML text control assumes the HtmlText is relatively positioned. If you need to use an absolute position for your HTML text, wrap the text around a relatively positioned div. For example, `"<div style='position:relative'>" & varPageContent & "</div>"`

> [!NOTE]
> For some HTML elements default browser styling might be deleted. For instance, for HTML list (`<ul>`, `<ol>`) you will need to write your own inline styles to get the default styling back. For example,
```html
<ul style='display: block;
           list-style-type: disc;
           margin-block-start: 1em;
           margin-block-end: 1em;
           margin-inline-start: 0px;
           margin-inline-end: 0px;
           padding-inline-start: 40px;'>
  ...
</ul>
```

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

> [!NOTE]
> **OnSelect** is ignored for hyperlinks within the content referenced inside **HtmlText** property.

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

ARIA mapping for elements inside the **HTML text** control are not defined automatically by Power Apps.

### Color contrast
There must be adequate color contrast between:
* **[Color](properties-color-border.md)** and **[Fill](properties-color-border.md)**
* Text with custom colors and its background

### Keyboard support
* The control can't act as a button. It doesn't have **TabIndex** and keyboard users won't be able to focus on it.
* The control can contain interactive parts in **HtmlText** like `<a>` elements, but the app setting **Simplified tab indexes" must be enabled. Otherwise, the tab navigation order will be wrong.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
