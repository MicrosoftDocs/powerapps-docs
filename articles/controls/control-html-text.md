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
   ms.date="02/29/2016"
   ms.author="anneta"/>

# HTML text control in PowerApps #
[AZURE.INCLUDE [control-summary-html-text](../../includes/control-summary-html-text.md)]

## Description ##
An **HTML text** control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

## Key properties ##

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Font](../properties/properties-text.md)** – The name of the family of fonts in which text appears.

**HTMLText** – Text that appears in an HTML text control and that may contain HTML tags.

## Additional properties ##
**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **Disabled** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **Disabled** property is set to **true**.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../properties/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../properties/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../properties/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../properties/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Find**( *FindString*, *WithinString* )](function-find.md)

## Example ##

1. Add a **Text box** control, name it **Source**, and set its **Text** property to this string:

\<p> We have done an unusually \&nbsp; \&quot; deep \&quot; globalization and localization. \<p>

Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add an **HTML text** control, and set its **HTMLText** property to this value:<br>
**Source.Text**

 	The **HTML text** control shows the same text as the **Text box** control but converts the tags to the appropriate characters.
