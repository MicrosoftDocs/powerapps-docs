<properties
    pageTitle="Pen input: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the pen-input control"
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

# Pen input in PowerApps #
[AZURE.INCLUDE [control-summary-pen-input](../../includes/control-summary-pen-input.md)]

## Description ##
The user can use this control like a whiteboard, drawing diagrams and writing words that can be converted to typed text.

## Key properties ##

[AZURE.INCLUDE [long-mode](../../includes/long-mode.md)]

[AZURE.INCLUDE [long-color](../../includes/long-color.md)]

[AZURE.INCLUDE [long-reset](../../includes/long-reset.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-input](../../includes/short-input.md)]

[AZURE.INCLUDE [short-mode](../../includes/short-mode.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-selectioncolor](../../includes/short-selectioncolor.md)]

[AZURE.INCLUDE [short-selectionthickness](../../includes/short-selectionthickness.md)]

[AZURE.INCLUDE [short-showcontrols](../../includes/short-showcontrols.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Collect**( *CollectionName*, *DatatoCollect* )](function-clear-collect-clearcollect.md)

## Example ##

### Create a set of images ###
1. Add a pen-input control, name it **MyDoodles**, and set its **ShowControls** property to **true**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add a button, move it below **MyDoodles**, and set its **Text** property to show **Add**.

1. Set the **OnSelect** property of the **Add** button to this formula:<br>
**Collect(Doodles, {Sketch:MyDoodles.Image})**

1. Add an image gallery, move it below the **Add** button, and shrink the gallery's width until it shows three items.

1. Set the gallery's **Items** property to **Doodles**, and then  press F5.

1. Draw an image in **MyDoodles**, and then click or tap the **Add** button.

	The image that you drew appears in the gallery.

1. (optional) Click or tap the icon to clear the image that you drew, draw another image, and then click or tap the **Add** button.

1. In the gallery, set the **OnSelect** property of the image control to this formula:<br>
**Remove(Doodles, ThisItem)**

1. Remove an image by clicking or tapping it in the gallery.

Use the [**SaveData** function](function-savedata-loaddata.md) to save your images locally or the [**Patch** function](function-patch.md) to save them to a data source.
