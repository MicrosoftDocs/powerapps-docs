<properties
    pageTitle="Add picture control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Add picture control"
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
   ms.date="03/10/2016"
   ms.author="anneta"/>

# Add picture control in PowerApps #
[AZURE.INCLUDE [control-summary-add-picture](../../includes/control-summary-add-picture.md)]

## Description ##
If you add this control, your app can upload image files from the user and update your data source with fresh content.

## Properties ##

[**Align**](properties\properties-text.md) – The location of text in relation to the horizontal center of its control.

[**BorderColor**](properties\properties-color-border.md) – The color of a control's border.

[**BorderStyle**](properties\properties-color-border.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[**BorderThickness**](properties\properties-color-border.md) – The thickness of a control's border.

[**DisabledBorderColor**](properties\properties-color-border.md) – The color of a control's border if the control's **Disabled** property is set to **true**.

[**DisabledFill**](properties\properties-color-border.md) – The background color of a control if its **Disabled** property is set to **true**.

**Error** - If there is a problem uploading an image, this property will contain an appropriate error string.

[**Fill**](properties\properties-color-border.md) – The background color of a control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.

[**HoverBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user keeps the mouse pointer on that control.

[**HoverFill**](properties\properties-color-border.md) – The background color of a control when the user keeps the mouse pointer on it.

**Media** – An identifier for the clip that an audio or video control plays.

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.

[**PressedBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user taps or clicks that control.

[**PressedFill**](properties\properties-color-border.md) – The background color of a control when the user taps or clicks that control.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](..\functions\function-patch.md)

## Example ##
### Add images to an Image gallery control ###
1. Add an **Add picture** control, and then triple-click it.

	Don't know how to [add, name, and configure a control](..\add-configure-controls.md)?

1. In the **Open** dialog box, click or tap an image file, and then click or tap **Open**.

1. Add a **Button** control, move it under the **Add picture** control, and set the **OnSelect** property for the **Button** control to this formula:<br>
**Collect(MyPix, AddMediaButton1.Media)**

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add an **Image gallery** control, and set its **Items** property to **MyPix**.

1. Press F5, and then click or tap the **Button** control.

	The image from the **Add picture** control appears in the **Image gallery** control. If your image doesn't have the same aspect ratio as the **Image** control in the **Image gallery** control, set the **ImagePosition** property of the **Image** control to **Fit**.

1. Click or tap the **Add picture** control, click or tap another image file, click or tap **Open**, and then click or tap the **Button** control that you added.

	The second image appears in the **Image gallery** control.

1. (optional) Repeat the previous step one or more times, and then return to the default workspace by pressing Esc.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the images locally or the [**Patch** function](function-patch.md) to update a data source.
