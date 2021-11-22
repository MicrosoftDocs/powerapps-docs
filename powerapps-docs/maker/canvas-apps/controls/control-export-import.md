---
title: Export and Import controls in Power Apps
description: Learn about the details, properties and examples of the Export and Import controls in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/09/2020
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Export and Import controls in Power Apps
Controls for exporting data to a local file and then importing that data into another app in Power Apps.

## Description
If you want to create more than one app that uses the same data but not share that data outside those apps, you can export it and import it by using an **Export** control and an **Import** control. When you export data, you create a compressed file that you can copy to another machine, but you can't read it in any program other than Power Apps.

## Warning
Enabling this functionality in your app may expose it to security vulnerabilities and data leakage.  It is recommended to advise users to import only recognized and trusted files and only export data that is not confidential or sensitive.

## Limitations
The export functionality isn't supported in web browsers.

## Key properties
**Data** – The name of a collection that you want to export to a local file.

* The **Data** property is available for an **Export** control but not an **Import** control.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

## Additional properties
**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[Padding](properties-size-location.md)** – The distance between the text on an import or export button and the edges of that button.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example
1. Add a **[Button](control-button.md)** control, and set its **[OnSelect](properties-core.md)** property to this formula: <br>
   ```
   ClearCollect(Products, {Name:"Europa", Price:"10.99"}, {Name:"Ganymede", Price:"12.49"}, {Name:"Callisto", Price:"11.79"})
   ```
   For more details, read [adding, naming, and configuring a control](../add-configure-controls.md), **[ClearCollect](../functions/function-clear-collect-clearcollect.md)** and [other functions](../formula-reference.md).
2. Press F5 and select **[Button](control-button.md)** control, and then press Esc.
3. Add an **Export** control, and set its **Data** property to **Products**.
4. Press F5 and select the **Export** control to download the file *Data.zip*.
5. Select **Save**, then press Esc to return to the default workspace.
6. In a new or existing app, add an **Import** control, name it **MyData**, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(ImportedProducts, MyData.Data)**
7. Press F5 and select **MyData**, then select the file that you exported, and then select **Open**.
8. Press Esc and select **Collections** on the **File** menu, and confirm that the current app has the data that you exported.


## Accessibility guidelines
The same guidelines for **[Button](control-button.md)**  apply because **Export** and **Import** are just specialized buttons.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]