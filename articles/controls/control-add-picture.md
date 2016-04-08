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
### Add images to an Image gallery control ###
1. Add an **Add picture** control, and then triple-click it.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

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
