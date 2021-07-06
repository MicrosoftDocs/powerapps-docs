---
title: 'Combo box control: reference | Microsoft Docs'
description: Information, including properties and examples, about the combo box control
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/11/2021
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Combo box control in Power Apps
A control that allows users to make selections from provided choices.  Supports search and multiple selections.

## Description
A **Combo box** control allows you to search for items you will select.  The search is performed server-side on the SearchField property so performance is not affected by large data sources.  

Single or multi-select mode is configured via the SelectMultiple property.

When searching for items to select, for each item you can choose to show a single data value, two values, or a picture and two values (Person) by modifying the Layout settings in the Data pane.

When viewing on small screens, the items list flyout will become a full screen control for better usability.

> [!NOTE]
> If you want to search for items with *numbers*, convert numbers to text with [Text()](../functions/function-text.md) function. For example, *Text(12345)*.

## People picker
To use **Combo box** as a people picker, choose the **Person** template from the Layout settings in the Data pane and configure the related data properties to be shown for the person below.

## Key properties
**[Items](properties-core.md)** – The source of data from which selections can be made.

**DefaultSelectedItems** – The initial selected item(s) before the user interacts with the control.

**SelectedItems** – List of selected items resulting from user interaction.

**SelectMultiple** – Whether the user can select a single item or multiple items.

**IsSearchable** – Whether the user can search for items before selecting.

> [!NOTE]
> **IsSearchable** can be enabled only on a data source that contains at least one text field. The **Items** expression must be delegable for queries to be delegated with searching. That is, **If** statements within the **Items** expression are not supported.

**SearchFields** - The data fields of the data source searched when user is entering text.  

> [!NOTE]
> To search on multiple fields, set ComboBox1.SearchFields = ["MyFirstColumn", "MySecondColumn"].  Only text fields are supported.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**DisplayFields** – List of fields shown for each item returned by the search.  Easiest to configure via the Data pane in the Properties option tab.

> [!NOTE]
> To update multiple display fields given template, set ComboBox1.DisplayFields = ["MyFirstColumn", "MySecondColumn"].

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**InputTextPlaceholder** – Instructional text shown to end users when no items are selected.

**OnChange** – Actions to perform when the user changes a selection.

**OnNavigate** – Actions to perform when the user selects an item.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or selects a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example
1. On the **Insert** tab, open the **Controls** menu, and then select **Combo box**.  

1. On the **Properties** tab of the right-hand pane, open the **Select a data source** list (next to **Items**), and then add or select a data source.

1. On the same tab, select **Edit** (next to **Fields**).

1. In the **Data** pane, open the **Primary text** list, and then select the column that you want to show in the **Combo box** control.

1. While holding down the Alt key, select the down arrow to open the **Combo box** control.

    The control shows the data from the column that you specified in the data source that you specified.
    
1. (optional) To show the first record by default, set the **DefaultSelectedItems** property to this expression, replacing *DataSource* with the name of your data source:

    `First(DataSource)`
    
## Drop Down Example

By setting **IsSearchable** to false and **SelectMultiple** to false, you can achieve the same functionality of a drop down.

1. On the **Insert** tab, open the **Controls** menu, and then select **Combo box**.  

1. On the **Properties** tab of the right-hand pane, open the **Select a data source** list (next to **Items**), and then add or select a data source.

1. On the same tab, select **Edit** (next to **Fields**).

1. In the **Data** pane, open the **Primary text** list, and then select the column that you want to show in the **Combo box** control.

1. Set the **IsSearchable** property to false.

1. Set the **SelectMultiple** property to false.

1. While holding down the Alt key, select the down arrow to open the **Combo box** control.

    The control shows the data from the column that you specified in the data source that you specified.
        
> [!NOTE]
> Notice that the "Find items" text has disappeared and that you'll only be able to select a single item.

## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **ChevronFill** and **ChevronBackground**
* **ChevronHoverFill** and **ChevronHoverBackground**
* **SelectionColor** and **SelectionFill**
* **SelectionFill** and **[Fill](properties-color-border.md)**
* **SelectionTagColor** and **SelectionTagFill**

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

    > [!NOTE]
  > On touch screens, screen reader users can navigate the contents of the combo box sequentially. The combo box acts as a button that shows or hides its contents when selected.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.

    > [!NOTE]
  > The tab key navigates to or away from the combo box. Arrow keys navigate the contents of the combo box. The escape key closes the drop down when opened.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
