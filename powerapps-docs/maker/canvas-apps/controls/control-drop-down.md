---
title: Drop down control in Power Apps
description: Learn about the details, properties and examples of the drop down control in Power Apps.
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
# Drop down control in Power Apps
A list that shows only the first item unless the user opens it.

## Description
A **Drop down** control conserves screen real estate, especially when the list contains a large number of choices. The control takes up only one line unless the user selects the chevron to reveal more choices.  The control will show a maximum of 500 items.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before the user specifies a different value.

**[Items](properties-core.md)** – The source of data that contains the items that appear in the control. If the source has multiple columns, set the control's **Value** property to the column of data that you want to show.
  
**Value** – The column of data that you want to show in the control (for example, if a data source has multiple columns).

**Selected** – The data record that represents the selected item.

**AllowEmptySelection** – Whether the control shows an empty selection if no item has been selected. App users can also clear their choices by selecting the blank item.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**ChevronBackground** – The color behind the down arrow in a dropdown list.

**ChevronFill** – The color of the down arrow in a dropdown list.

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

**[OnChange](properties-core.md)** – Actions to perform when the user changes the value of the drop-down.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**SelectedText (Deprecated)** – A string value that represents the selected item.

**[SelectionColor](properties-color-border.md)** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.

**[SelectionFill](properties-color-border.md)** – The background color of a selected item or items in a list or a selected area of a pen control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Examples

### Simple list

1. Add a **Drop down** control, and then set its **[Items](properties-core.md)** property to this expression:

    `["Seattle", "Tokyo", "London", "Johannesburg", "Rio de Janeiro"]`

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Show the items in the list by selecting the control's down arrow while pressing the Alt key.

### List from a data source
The principles in this procedure apply to any [data source that provides tables](../connections-list.md#tables) but, to follow these steps exactly, you must open an environment for which a Microsoft Dataverse database has been created and sample data added.

1. [Open a blank app](../data-platform-create-app-scratch.md#open-a-blank-app), and then [specify the **Accounts** table](../data-platform-create-app-scratch.md#specify-a-table).

1. Add a **Drop down** control, and set its **[Items](properties-core.md)** property to this formula:

    `Distinct(Accounts, 'Address 1: City')`

    This formula shows all the cities in the **Accounts** table. If more than one record has the same city, the **[Distinct](../functions/function-distinct.md)** function hides the duplication in your drop-down control.

1. (optional) Rename your **Drop down** control to **Cities**, add a vertical **Gallery** control, and set the gallery's **[Items](properties-core.md)** property to this formula:

    `Filter(Accounts, address1_city = Cities.Selected.Result)`

    This **[Filter](../functions/function-filter-lookup.md)** function shows only those records in the **Accounts** table for which the city matches the selected value in the **Cities** control.

## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **ChevronFill** and **ChevronBackground**
* **ChevronHoverFill** and **ChevronHoverBackground**
* **SelectionColor** and **SelectionFill**
* **SelectionFill** and **[Fill](properties-color-border.md)**

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
