---
title: Column chart and Line chart controls in Power Apps
description: Learn about the details, properties and examples of the Column chart, and Line chart controls in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Column chart and Line chart controls in Power Apps
Controls that show data as graphs with x- and y-axes.

## Description
**Column chart** and **Line chart** are grouped controls. Each group contains three controls: a **[Label](control-text-box.md)** for the title, the chart graphic, and a **Legend**.

## Chart key properties
**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**NumberOfSeries** – How many columns of data are reflected in a column or line chart.

## Additional chart properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

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

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

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

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**XLabelAngle** – The angle of the labels below the x-axis of a column or line chart.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**YAxisMax** – The maximum value of the y-axis for a line chart.

* The **YAxisMax** property is available for the **Line chart** control but not the **Column chart** control.

**YAxisMin** – The minimum value of the y-axis for a line chart.

* The **YAxisMin** property is available for the **Line chart** control but not the **Column chart** control.

**YLabelAngle** – The angle of the labels next to the y-axis of a line or column chart.

## Related functions
[**Max**( *DataSource*, *ColumnName* )](../functions/function-aggregates.md)

## Example
1. Add a **[Button](control-button.md)** control, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(Revenue, {Year:"2013", Europa:24000, Ganymede:22300, Callisto:21200}, {Year:"2014", Europa:26500, Ganymede:25700, Callisto:24700},{Year:"2014", Europa:27900, Ganymede:28300, Callisto:25600})**
   
    Don't know how to [add and configure a control](../add-configure-controls.md)?
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Press F5, click or tap the **[Button](control-button.md)** control, and then press Esc to return to the default workspace.
3. Add a **Column chart** control or a **Line chart** control, set its **[Items](properties-core.md)** property to **Revenue**, and set its **NumberOfSeries** property to **3**.
   
    The control shows revenue data for each product over three years.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* each item in **ItemColorSet**
* every item in **ItemColorSet** and the background color
* **[Color](properties-color-border.md)** and the background color

### Screen reader support
* There must be a **[Label](control-text-box.md)** immediately before the chart graphic to serve as the title.
* Consider adding a summary of the chart graphic. For example, "The line chart shows a steady increase in sales between March and August this year."

    > [!NOTE]
  > Chart graphics and **Legend** are hidden from screen reader users. As an alternative, a tabular form of the data is presented to them. They can also cycle through buttons that select data in the chart.

### Low vision support
* There must be a **Legend** if more than one series is shown.
* Consider setting **GridStyle** to GridStyle.All, which shows both axes. This helps all users accurately determine the scale of the data.
* For **Column chart**, consider setting **Markers** to **true**. This helps low-vision users determine the value of a column.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.

    > [!NOTE]
  > When keyboard users navigate to the chart, they can cycle through buttons that select data in the chart.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]