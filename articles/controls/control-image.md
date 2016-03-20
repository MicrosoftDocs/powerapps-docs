<properties
    pageTitle="Image control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the image control"
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
If you add one or more image controls to your app, you can show individual images that aren't part of a data set, or you can incorporate images from records in data sources.

## Key properties ##

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

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

[AZURE.INCLUDE [short-image](../../includes/short-image.md)]

[AZURE.INCLUDE [short-imageposition](../../includes/short-imageposition.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-radiusbottomleft](../../includes/short-radiusbottomleft.md)]

[AZURE.INCLUDE [short-radiusbottomright](../../includes/short-radiusbottomright.md)]

[AZURE.INCLUDE [short-radiustopleft](../../includes/short-radiustopleft.md)]

[AZURE.INCLUDE [short-radiustopright](../../includes/short-radiustopright.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-transparency](../../includes/short-transparency.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Remove**( *DataSource*, ThisItem )](function-remove-removeif.md)

## Examples ##
### Show an image from a local file ###
1. On the **Content** tab, select **Media**, and then select **Browse**.

1. Select the image file that you want to add, select **Open**, and then press Esc to return to the default workspace.

1. Add an image control, and set its **Items** property to the name of the file that you added.

	Don't know how to [add and configure a control](add-configure-controls.md)?

	The control shows the image that you specified.

### Show a set of images from a data source ###
1. Download this [Excel file](https://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx), and save it on your local device.

1. In PowerApps, select a screen in the left navigation bar, select **Options** near the lower-right corner, and then select **Insert your data**.

1. Select **Import from Excel**, select the Excel file that you downloaded, and then select **Open**.

1. In the right pane, select the **Flooring Estimates** check box, and then select **Insert**.

1. Add an image gallery, and set its **Items** property to **FlooringEstimates**.

	Don't know how to [add and configure a control](add-configure-controls.md)?

	The gallery shows images of carpet, hardwood, and tile products based on links in the Excel file that you downloaded.
