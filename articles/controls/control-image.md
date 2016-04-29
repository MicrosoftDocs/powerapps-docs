<properties
    pageTitle="Image control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Image control"
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

# Image control in PowerApps #
[AZURE.INCLUDE [control-summary-image](../../includes/control-summary-image.md)]

## Description ##
If you add one or more **Image** controls to your app, you can show individual images that aren't part of a data set, or you can incorporate images from records in data sources.

## Key properties ##

[**Image**](../properties/properties-visual.md) – The name of the image that appears in an image, audio, or microphone control.

## Additional properties ##

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.

[**BorderColor**](../properties/properties-color-border.md) – The color of a control's border.

[**BorderStyle**](../properties/properties-color-border.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[**BorderThickness**](../properties/properties-color-border.md) – The thickness of a control's border.

**CalculateOriginalDimensions** – Enables the **OriginalHeight** and **OriginalWidth** properties.

[**Disabled**](../properties/properties-core.md) – Whether the user can interact with the control.

[**DisabledBorderColor**](../properties/properties-color-border.md) – The color of a control's border if the control's **Disabled** property is set to **true**.

[**DisabledFill**](../properties/properties-color-border.md) – The background color of a control if its **Disabled** property is set to **true**.

[**Fill**](../properties/properties-color-border.md) – The background color of a control.

[**Height**](../properties/properties-size-location.md) – The distance between a control's top and bottom edges.

[**HoverBorderColor**](../properties/properties-color-border.md) – The color of a control's border when the user keeps the mouse pointer on that control.

[**HoverFill**](../properties/properties-color-border.md) – The background color of a control when the user keeps the mouse pointer on it.

[**ImagePosition**](../properties/properties-visual.md) – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

[**OnSelect**](../properties/properties-core.md) – How the app responds when the user taps or clicks a control.

**OriginalHeight** – Original height of an image, enabled with the **CalculateOriginalDimensions** property.

**OriginalWidth** – Original width of an image, enabled with the **CalculateOriginalDimensions** property.

[**PaddingBottom**](../properties/properties-size-location.md) – The distance between text in a control and the bottom edge of that control.

[**PaddingLeft**](../properties/properties-size-location.md) – The distance between text in a control and the left edge of that control.

[**PaddingRight**](../properties/properties-size-location.md) – The distance between text in a control and the right edge of that control.

[**PaddingTop**](../properties/properties-size-location.md) – The distance between text in a control and the top edge of that control.

[**PressedBorderColor**](../properties/properties-color-border.md) – The color of a control's border when the user taps or clicks that control.

[**PressedFill**](../properties/properties-color-border.md) – The background color of a control when the user taps or clicks that control.

[**RadiusBottomLeft**](../properties/properties-size-location.md) – The degree to which the bottom-left corner of a control is rounded.

[**RadiusBottomRight**](../properties/properties-size-location.md) – The degree to which the bottom-right corner of a control is rounded.

[**RadiusTopLeft**](../properties/properties-size-location.md) – The degree to which the top-left corner of a control is rounded.

[**RadiusTopRight**](../properties/properties-size-location.md) – The degree to which the top-right corner of a control is rounded.

[**Tooltip**](../properties/properties-core.md) – Explanatory text that appears when the user hovers over a control.

**Transparency** – The degree to which controls behind an image remain visible.

[**Visible**](../properties/properties-core.md) – Whether a control appears or is hidden.

[**Width**](../properties/properties-size-location.md) – The distance between a control's left and right edges.

[**X**](../properties/properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](../properties/properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Remove**( *DataSource*, ThisItem )](function-remove-removeif.md)

## Examples ##
### Show an image from a local file ###
1. On the **Content** tab, click or tap **Media**, and then click or tap **Browse**.

1. Click or tap the image file that you want to add, click or tap **Open**, and then press Esc to return to the default workspace.

1. Add an **Image** control, and set its **Items** property to the name of the file that you added.

	Don't know how to [add and configure a control](add-configure-controls.md)?

	The **Image** control shows the image that you specified.

### Show a set of images from a data source ###
1. Download this [Excel file](https://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx), and save it on your local device.

1. In PowerApps, click or tap a screen in the left navigation bar, click or tap **Options** near the lower-right corner, and then click or tap **Insert your data**.

1. Click or tap **Import from Excel**, click or tap the Excel file that you downloaded, and then click or tap **Open**.

1. In the right pane, click or tap the **Flooring Estimates** check box, and then click or tap **Insert**.

1. Add an **Image gallery** control, and set its **Items** property to **FlooringEstimates**.

	Don't know how to [add and configure a control](add-configure-controls.md)?

	The **Image gallery** control shows images of carpet, hardwood, and tile products based on links in the Excel file that you downloaded.
