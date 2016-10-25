<properties
    pageTitle="HTML text control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the HTML text control"
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
    ms.date="10/25/2016"
   ms.author="anneta"/>

# HTML text control in PowerApps #
A box that shows text and converts HTML tags to formatting.

## Description ##
An **HTML text** control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

## Key properties ##

**[Color](properties-color-border.md)** – The color of text in a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**HTMLText** – Text that appears in an HTML text control and that may contain HTML tags.

## Additional properties ##
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Disabled](properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[Disabled](properties-core.md)** property is set to **true**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[Disabled](properties-core.md)** property is set to **true**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Find**( *FindString*, *WithinString* )](../functions/function-find.md)

## Example ##

1. Add a **[Text box](control-text-box.md)** control, name it **Source**, and set its **[Text](properties-core.md)** property to this string:

\<p> We have done an unusually \&nbsp; \&quot; deep \&quot; globalization and localization. \<p>

Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add an **HTML text** control, and set its **HTMLText** property to this value:<br>
**Source.Text**

 	The **HTML text** control shows the same text as the **[Text box](control-text-box.md)** control but converts the tags to the appropriate characters.
