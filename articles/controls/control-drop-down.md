<properties
    pageTitle="Drop down control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Drop down control"
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
   ms.date="03/08/2016"
   ms.author="anneta"/>

# Drop down control in PowerApps #
[AZURE.INCLUDE [control-summary-list-box](../../includes/control-summary-drop-down.md)]

## Description ##
A **Drop down** control conserves screen real estate, especially when the list contains a large number of choices. The control takes up only one line unless the user selects the chevron to reveal more choices.

## Key properties ##

[AZURE.INCLUDE [long-items](../../includes/long-items.md)]

[AZURE.INCLUDE [long-default](../../includes/long-default.md)]

[AZURE.INCLUDE [long-reset](../../includes/long-reset.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-chevronbackground](../../includes/short-chevronbackground.md)]

[AZURE.INCLUDE [short-chevronfill](../../includes/short-chevronfill.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-fontweight](../../includes/short-fontweight.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-selectioncolor](../../includes/short-selectioncolor.md)]

[AZURE.INCLUDE [short-selectionfill](../../includes/short-selectionfill.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Distinct**( *DataSource*, *ColumnName* )](function-distinct.md)

## Example ##
1. Add a **Button** control, and set its **Text** property to show **Collect**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Set the **OnSelect** property of the **Button** control to this formula:
<br>**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**

	Want more information about the [**ClearCollect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, click or tap the **Button** control, and then press Esc.

1. Add a **Drop down** control, name it **Countries**, and set its **Items** property to this formula:
<br>**Distinct(CityPopulations, Country)**

1. Add a **Text gallery** control in vertical/portrait orientation, and set its **Items** property to this formula:
<br>**Filter(CityPopulations, Countries.Selected.Value in Country)**

1. In the first item of the **Text gallery** control, set the **Text** property of the upper **Text box** control to **ThisItem.City**, and delete the bottom **Text box** control.

1. Set the **TemplateSize** property of the **Text gallery** control to **80**.

1. Press F5, click or tap the chevron in the **Countries** list, and then choose an option in that list.

	The **Text gallery** control shows only those cities in the country that you chose.
