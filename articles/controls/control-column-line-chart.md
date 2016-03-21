<properties
    pageTitle="Column and line charts: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about column and line charts"
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

# Column and line charts in PowerApps #
[AZURE.INCLUDE [control-summary-column-line-charts](../../includes/control-summary-column-line-charts.md)]

## Description ##
By default, a column or line chart comprises multiple controls grouped together. These controls show a title, data, and a legend.

## Key properties ##

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-numberofseries](../../includes/short-numberofseries.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-gridstyle](../../includes/short-gridstyle.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-itemcolorset](../../includes/short-itemcolorset.md)]

[AZURE.INCLUDE [short-items](../../includes/short-items.md)]

[AZURE.INCLUDE [short-itemsgap](../../includes/short-itemsgap.md)]

- The **ItemsGap** property is available for column charts but not line charts.

[AZURE.INCLUDE [short-markers](../../includes/short-markers.md)]

[AZURE.INCLUDE [short-markersuffix](../../includes/short-markersuffix.md)]

- The **MarkerSuffix** property is available for column charts but not line charts.

[AZURE.INCLUDE [short-minimumbarwidth](../../includes/short-minimumbarwidth.md)]

- The **MinimumBarWidth** property is available for column charts but not line charts.

[AZURE.INCLUDE [short-numberofseries](../../includes/short-numberofseries.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-seriesaxismax](../../includes/short-seriesaxismax.md)]

- The **SeriesAxisMax** property is available for column charts but not line charts.

[AZURE.INCLUDE [short-seriesaxismin](../../includes/short-seriesaxismin.md)]

- The **SeriesAxisMin** property is available for column charts but not line charts.

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-xlabelangle](../../includes/short-xlabelangle.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

[AZURE.INCLUDE [short-yaxismax](../../includes/short-yaxismax.md)]

- The **YAxisMax** property is available for line charts but not column charts.

[AZURE.INCLUDE [short-yaxismin](../../includes/short-yaxismin.md)]

- The **YAxisMin** property is available for line charts but not column charts.

[AZURE.INCLUDE [short-ylabelangle](../../includes/short-ylabelangle.md)]

## Related functions ##

[**Max**( *DataSource*, *ColumnName* )](function-aggregates.md)

## Example ##
1. Add a button, and set its **OnSelect** property to this formula:<br>
**Collect(Revenue, {Year:"2013", Europa:24000, Ganymede:22300, Callisto:21200}, {Year:"2014", Europa:26500, Ganymede:25700, Callisto:24700},{Year:"2014", Europa:27900, Ganymede:28300, Callisto:25600})**

	Don't know how to [add and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, select the button, and then press Esc to return to the default workspace.

1. Add a column or line chart, set its **Items** property to **Revenue**, and set its **NumberOfSeries** property to **3**.

	The chart shows revenue data for each product over three years.
