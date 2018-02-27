---
title: 'HTML text control: reference | Microsoft Docs'
description: Information, including properties and examples, about the HTML text control
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
# HTML text control in PowerApps
A box that shows text and converts HTML tags to formatting.

## Description
An **HTML text** control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

## Key properties
**[Color](../../controls/properties-color-border.md)** – The color of text in a control.

**[Font](../../controls/properties-text.md)** – The name of the family of fonts in which text appears.

**HTMLText** – Text that appears in an HTML text control and that may contain HTML tags.

## Additional properties
**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](../../controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](../../controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[Fill](../../controls/properties-color-border.md)** – The background color of a control.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Find**( *FindString*, *WithinString* )](../../functions/function-find.md)

## Example
1. Add a **[Label](control-text-box.md)** control, name it **Source**, and set its **[Text](../../controls/properties-core.md)** property to this string:

\<p> We have done an unusually \&nbsp; \&quot; deep \&quot; globalization and localization. \<p>

Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add an **HTML text** control, and set its **HTMLText** property to this value:<br>
   **Source.Text**
   
     The **HTML text** control shows the same text as the **[Label](control-text-box.md)** control but converts the tags to the appropriate characters.

