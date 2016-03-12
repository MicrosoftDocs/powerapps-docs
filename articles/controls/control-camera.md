<properties
    pageTitle="Camera control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the camera control"
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

[AZURE.INCLUDE [short-camera](../../includes/short-camera.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-brightness](../../includes/short-brightness.md)]

[AZURE.INCLUDE [short-camera](../../includes/short-camera.md)]

[AZURE.INCLUDE [short-contrast](../../includes/short-contrast.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-onstream](../../includes/short-onstream.md)]

[AZURE.INCLUDE [short-streamrate](../../includes/short-streamrate.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

[AZURE.INCLUDE [short-zoom](../../includes/short-zoom.md)]

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](function-patch.md)

## Example ##
### Add photos to a gallery ###
1. Add a camera, name it **MyCamera**, and set its **OnSelect** property to this formula:<br>
**Collect(MyPix, MyCamera.Photo)**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add an image gallery, and then resize its image control, its template, and the gallery itself to fit in the screen.

1. Set the gallery's **Items** property to **MyPix**, press F5, and then take a photo by selecting **MyCamera**.

	The image that you selected appears in the gallery.

1. Add as many photos as you want, and then return to the default workspace by pressing Esc.

1. (optional) Set the **OnSelect** property of the gallery's image control to **Remove(MyPix, ThisItem)**, press F5, and then select an image to remove it.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the data set locally or the [**Patch** function](function-patch.md) to update a data source.
