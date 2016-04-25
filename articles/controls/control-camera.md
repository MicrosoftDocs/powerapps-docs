<properties
    pageTitle="Camera control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Camera control"
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

# Camera control in PowerApps #
[AZURE.INCLUDE [control-summary-camera](../../includes/control-summary-camera.md)]

## Description ##
If you add this control, the user can update a data source with one or more photos from wherever the app is running.

## Key properties ##

**Camera** – On a device that has more than one camera, the numeric ID of the camera that the app uses.

## Additional properties ##

[**BorderColor**](properties\properties-color-border.md) – The color of a control's border.

[**BorderStyle**](properties\properties-size-location.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[**BorderThickness**](properties\properties-size-location.md) – The thickness of a control's border.

**Brightness** – How much light the user is likely to perceive in an image.

**Contrast** – How easily the user can distinguish between similar colors in an image.

[**Disabled**](properties\properties-core.md) – Whether the user can interact with the control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.

**OnStream** – OnStream.

**StreamRate** –

[**Tooltip**](properties\properties-core.md) – Explanatory text that appears when the user hovers over a control.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](function-patch.md)

## Example ##
### Add photos to an Image gallery control ###
1. Add a **Camera** control, name it **MyCamera**, and set its **OnSelect** property to this formula:<br>
**Collect(MyPix, MyCamera.Photo)**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add an **Image gallery** control, and then resize its **Image** control, its template, and the **Image gallery** control itself to fit in the screen.

1. Set the **Items** property of the **Image gallery** control to **MyPix**, press F5, and then take a photo by clicking or tapping **MyCamera**.

	The photo that you took appears in the **Image gallery** control.

1. Take as many photos as you want, and then return to the default workspace by pressing Esc.

1. (optional) Set the **OnSelect** property of the **Image** control in the **Image gallery** control to **Remove(MyPix, ThisItem)**, press F5, and then click or tap a photo to remove it.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the photos locally or the [**Patch** function](function-patch.md) to update a data source.
