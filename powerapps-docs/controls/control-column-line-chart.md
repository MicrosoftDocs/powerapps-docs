---
title: 'Column chart control and Line chart control: reference | Microsoft Docs'
description: Information, including properties and examples, about Column chart controls and Line chart controls
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: fikaradz

---
# Column chart and Line chart controls in PowerApps
Controls that show data as graphs with x- and y-axes.

## Description
By default, a **Column chart** control or a **Line chart** control comprises multiple controls grouped together. These controls show a title, data, and a legend.

## Key properties
**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**NumberOfSeries** – How many columns of data are reflected in a column or line chart.

## All properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**GridStyle** – Whether a column or line chart shows its x-axis, its y-axis, both, or neither.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**ItemColorSet** – The color of each data point in a chart.

**ItemsGap** – The distance between columns in a column chart.

* The **ItemsGap** property is available for the **Column chart** control but not the **Line chart** control.

**Markers** – Whether a column or line chart shows the value of each data point.

**MarkerSuffix** – Text that appears after each value in a column chart for which the **Markers** property is set to **true**.

* The **MarkerSuffix** property is available for the **Column chart** control but not the **Line chart** control.

**MinimumBarWidth** – The narrowest possible width of columns in a column chart.

* The **MinimumBarWidth** property is available for the **Column chart** control but not the **Line chart** control.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**SeriesAxisMax** – The maximum value of the y-axis for a column or line chart.

* The **SeriesAxisMax** property is available for the **Column chart** control but not the **Line chart** control.

**SeriesAxisMin** – A number that determines the minimum value of the y-axis for a column chart.

* The **SeriesAxisMin** property is available for the **Column chart** control but not the **Line chart** control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**XLabelAngle** – The angle of the labels below the x-axis of a column or line chart.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**YAxisMax** – The maximum value of the y-axis for a line chart.

* The **YAxisMax** property is available for the **Column chart** control but not the **Line chart** control.

**YAxisMin** – The minimum value of the y-axis for a line chart.

* The **YAxisMin** property is available for the **Column chart** control but not the **Line chart** control.

**YLabelAngle** – The angle of the labels next to the y-axis of a line or column chart.

## Related functions
[**Max**( *DataSource*, *ColumnName* )](../functions/function-aggregates.md)

## Example
1. Add a **[Button](control-button.md)** control, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(Revenue, {Year:"2013", Europa:24000, Ganymede:22300, Callisto:21200}, {Year:"2014", Europa:26500, Ganymede:25700, Callisto:24700},{Year:"2014", Europa:27900, Ganymede:28300, Callisto:25600})**
   
    Don't know how to [add and configure a control](../maker/add-configure-controls.md)?
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../maker/formula-reference.md)?
2. Press F5, click or tap the **[Button](control-button.md)** control, and then press Esc to return to the default workspace.
3. Add a **Column chart** control or a **Line chart** control, set its **[Items](properties-core.md)** property to **Revenue**, and set its **NumberOfSeries** property to **3**.
   
    The control shows revenue data for each product over three years.

