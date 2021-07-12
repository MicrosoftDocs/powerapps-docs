---
title: Pie chart control in Power Apps
description: Learn about the details, properties and examples of the Pie chart control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/25/2016
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Pie chart control in Power Apps
A control that shows relative values in comparison to each other.

## Description
Add a **Pie chart** control if you want to show relative data from a table that contains labels in the leftmost column and values in the second column from the left.

This control is a grouped control containing three controls: a **[Label](control-text-box.md)** for the title, the chart graphic, and a **Legend**.

## Chart key properties
**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**ShowLabels** – Whether a pie chart shows the value that's associated with each of its wedges.

## Additional chart properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**Explode** – The distance between wedges in a pie chart.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**ItemBorderColor** – The color of the border around each wedge in a pie chart.

**ItemBorderThickness** – The thickness of the border around each wedge in a pie chart.

**ItemColorSet** – The color of each data point in a chart.

**LabelPosition** – The location of labels in a pie chart relative to its wedges.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Max**( *DataSource*, *ColumnName* )](../functions/function-aggregates.md)

## Example
1. Add a **[Button](control-button.md)** control, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(Revenue2015, {Product:"Europa", Revenue:27000}, {Product:"Ganymede", Revenue:26300}, {Product:"Callisto", Revenue:29200})**
   
    Don't know how to [add and configure a control](../add-configure-controls.md)?
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Press F5, click or tap the **[Button](control-button.md)** control, and then press Esc to return to the default workspace.
3. Add a **Pie chart** control, and set its **[Items](properties-core.md)** property to **Revenue2015**.
   
    The **Pie chart** control shows revenue data for each product in relation to the other products.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* each item in **ItemColorSet**
* every item in **ItemColorSet** and the background color
* **[Color](properties-color-border.md)** and the background color

### Screen reader support
* There must be a **[Label](control-text-box.md)** immediately before the chart graphic to serve as the title.

    > [!NOTE]
  > Chart graphics and **Legend** are hidden from screen reader users. As an alternative, a tabular form of the data is presented to them. They can also cycle through buttons that select data in the chart.

### Low vision support
* There must be a **Legend**.
* Consider setting **ShowLabels** to **true**. This helps low-vision users quickly determine what each pie slice represents.
* Consider setting **LabelPosition** to **LabelPosition.Outside**. This increases legibility of labels because of a more consistent color contrast.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.

    > [!NOTE]
  > When keyboard users navigate to the chart, they can cycle through buttons that select data in the chart.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]