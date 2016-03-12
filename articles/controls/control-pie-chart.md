<properties
    pageTitle="Pie charts: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about pie charts"
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

# Pie charts in PowerApps #
[AZURE.INCLUDE [control-summary-pie-charts](../../includes/control-summary-pie-charts.md)]

## Description ##
Add a pie chart if you want to show a data from a table that contains labels in the leftmost column and values in the second column from the left.

## Key properties ##

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-showlabels](../../includes/short-showlabels.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-explode](../../includes/short-explode.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-itembordercolor](../../includes/short-itembordercolor.md)]

[AZURE.INCLUDE [short-itemborderthickness](../../includes/short-itemborderthickness.md)]

[AZURE.INCLUDE [short-itemcolorset](../../includes/short-itemcolorset.md)]

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-labelposition](../../includes/short-labelposition.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-showlabels](../../includes/short-showlabels.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Max**( *DataSource*, *ColumnName* )](function-aggregates.md)

## Example ##
1. Add a button, and set its **OnSelect** property to this formula:<br>
**Collect(Revenue2015, {Product:"Europa", Revenue:27000}, {Product:"Ganymede", Revenue:26300}, {Product:"Callisto", Revenue:29200})**

	Don't know how to [add and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, select the button, and then press Esc to return to the default workspace.

1. Add a pie chart, and set its **Items** property to **Revenue2015**.

	The chart shows revenue data for each product in relation to the other products.
