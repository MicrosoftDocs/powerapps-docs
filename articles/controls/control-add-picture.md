<properties
    pageTitle="Add-picture control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the add-picture control"
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

# Add-picture control in PowerApps #
[AZURE.INCLUDE [control-summary-add-picture](../../includes/control-summary-add-picture.md)]

## Description ##
If you add this control, your app can upload image files from the user and update your data source with fresh content.

## Key properties ##

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](function-patch.md)

## Example ##
### Add images to a gallery ###
1. Add an add-picture control, and then triple-click it.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. In the **Open** dialog box, select an image file, and then select **Open**.

1. Add a button, move it under the add-picture control, and set the button's **OnSelect** property to this formula:<br>
**Collect(MyPix, AddMediaButton1.Media)**

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add an image gallery, and set its **Items** property to **MyPix**.

1. Press F5, and then select the button.

	The image from the add-picture control appears in the gallery. If your image doesn't have the same aspect ratio as the image control, set its **ImagePosition** property to **Fit**.

1. Select the add-picture control, select another image file, select **Open**, and then select the button that you added.

	The second image appears in the gallery.

1. (optional) Repeat the previous step one or more times, and then return to the default workspace by pressing Esc.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the data set locally or the [**Patch** function](function-patch.md) to update a data source.
