<properties
    pageTitle="PDF viewer control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the PDF viewer control"
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
   ms.date="03/11/2016"
   ms.author="anneta"/>

# PDF viewer control in PowerApps #
[AZURE.INCLUDE [control-summary-pdf-viewer](../../includes/control-summary-pdf-viewer.md)]

## Description ##
Show text, graphics, and other content in a PDF file by adding this type of control and setting its **Document** property to the URL, enclosed in double quotation marks, of the file that you want to show.

## Key properties ##

**Document** – The URL, enclosed in double-quotation marks, of a PDF file.

## Additional properties ##
[**BorderColor**](properties\properties-color-border.md) – The color of a control's border.

[**BorderStyle**](properties\properties-size-location.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[**BorderThickness**](properties\properties-size-location.md) – The thickness of a control's border.

[**Disabled**](properties\properties-core.md) – Whether the user can interact with the control.

[**DisabledBorderColor**](properties\properties-color-border.md) – The color of a control's border if the control's **Disabled** property is set to **true**.

[**Fill**](properties\properties-color-border.md) – The background color of a control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.

[**HoverBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user keeps the mouse pointer on that control.

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.

[**PaddingBottom**](properties\properties-size-location.md) – The distance between text in a control and the bottom edge of that control.

[**PaddingLeft**](properties\properties-size-location.md) – The distance between text in a control and the left edge of that control.

[**PaddingRight**](properties\properties-size-location.md) – The distance between text in a control and the right edge of that control.

[**PaddingTop**](properties\properties-size-location.md) – The distance between text in a control and the top edge of that control.

**Page** – The number of the page in a PDF file that you want to show.

[**PressedBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user taps or clicks that control.

[**Tooltip**](properties\properties-core.md) – Explanatory text that appears when the user hovers over a control.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.

## Related functions ##

[**Remove**( *DataSource*, ThisItem )](function-remove-removeif.md)

## Example ##
- Add a **PDF viewer** control, and set its **Document** property to the URL, enclosed in double quotation marks, of a PDF file as in this example:<br>
**"http://www.who.int/gho/publications/world_health_statistics/EN_WHS2015_TOC.pdf?ua=1"**

	The control shows the PDF file.

	Don't know how to [add and configure a control](add-configure-controls.md)?
