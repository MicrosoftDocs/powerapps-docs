<properties
    pageTitle="Slider control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the slider control"
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
   ms.date="03/09/2016"
   ms.author="anneta"/>

# Slider control in PowerApps #
[AZURE.INCLUDE [control-summary-slider](../../includes/control-summary-slider.md)]

## Description ##
The user can indicate a value, between a minimum and a maximum value that you specify, by dragging the handle of a slider left-right or up-down, depending on the direction that you choose.

## Key properties ##

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-max](../../includes/short-max.md)]

[AZURE.INCLUDE [short-min](../../includes/short-min.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-handleactivefill](../../includes/short-handleactivefill.md)]

[AZURE.INCLUDE [short-handlefill](../../includes/short-handlefill.md)]

[AZURE.INCLUDE [short-handlehoverfill](../../includes/short-handlehoverfill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-layout](../../includes/short-layout.md)]

[AZURE.INCLUDE [short-max](../../includes/short-max.md)]

[AZURE.INCLUDE [short-min](../../includes/short-min.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-railfill](../../includes/short-railfill.md)]

[AZURE.INCLUDE [short-railhoverfill](../../includes/short-railhoverfill.md)]

[AZURE.INCLUDE [short-readonly](../../includes/short-readonly.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-showvalue](../../includes/short-showvalue.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-valuefill](../../includes/short-valuefill.md)]

[AZURE.INCLUDE [short-valuehoverfill](../../includes/short-valuehoverfill.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Sum**( *Value1*, *Value2* )](function-aggregates.md)

## Example ##
1. Add a button, and set its **OnSelect** property to this formula:
<br>**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**ClearCollect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, select the button, and then press Esc.

1. Add a slider, move it below the button, and name the slider **MinPopulation**.

1. Set the slider's **Max** property to **1000000** and its **Min** property to **5000000**.

1. Add a text gallery in vertical/portrait orientation, move it below the slider, and set the gallery's **Items** property to **Filter(CityPopulations, Population > MinPopulation)**.

1. In the first item of the gallery, set the **Text** property of the top text box to **ThisItem.City**, and set the **Text** property of the middle text box to **Text(ThisItem.Population, "##,###")**.

	**Note:** To select the middle text box more easily, you might want to select **Zoom in** a few times on the **View** tab.

1. (optional) In the first item of the gallery, delete the bottom text box, and set the **TemplateSize** property of the gallery to **80**.

1. Press F5, and then adjust **MinPopulation** to show only those cities that have a population that's greater than the value that you specify.

1. To return to the default workspace, press Esc.
