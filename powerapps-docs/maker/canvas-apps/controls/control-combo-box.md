---
title: Combo box control in Power Apps
description: Learn about the details, properties and examples of the combo box control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/23/2025
ms.subservice: canvas-maker
ms.author: yogupt
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
---

# Combo box control in Power Apps
A control that allows users to make selections from provided choices.  Supports search and multiple selections.

## Description
A **Combo box** control allows you to search for items you will select.  The search is performed server-side on the SearchField property so performance is not affected by large data sources.  

Single or multi-select mode is configured via the SelectMultiple property.

When searching for items to select, for each item you can choose to show a single data value, two values, or a picture and two values (Person) by modifying the Layout settings in the Data pane.

When you view the control on small screens, the items list flyout becomes a full screen control for better usability.

> [!NOTE]
> If you want to search for items with *numbers*, convert numbers to text with [Text()](../functions/function-text.md) function. For example, *Text(12345)*.

## Limitations

The combo box control has these limitations:

- When you use a Combo box control inside a gallery, its selections aren't maintained when the user scrolls the gallery. This isn't an issue if you use a Combo box control inside a gallery that doesn't scroll. A workaround isn't currently available.

## People picker
To use **Combo box** as a people picker, choose the **Person** template from the Layout settings in the Data pane and configure the related data properties to be shown for the person below.

## Key properties
**[Items](properties-core.md)** – The source of data from which selections can be made.

**DefaultSelectedItems** – The initial selected item(s) before the user interacts with the control.

> [!NOTE]
> **Default** property is deprecated, use **DefaultSelectedItems** instead.

**SelectedItems** – List of selected items resulting from user interaction.

**Selected** – The last selected item resulting from user interaction.

**SelectMultiple** – Whether the user can select a single item or multiple items.

**IsSearchable** – Whether the user can search for items before selecting.

> [!NOTE]
> **IsSearchable** can be enabled only on a data source that contains at least one text field. The **Items** expression must be delegable for queries to be delegated with searching. That is, **If** statements within the **Items** expression are not supported.

**SearchFields** - The data fields of the data source searched when user is entering text.  

> [!NOTE]
> To search on multiple fields, set **SearchFields** property in this format: ["MyFirstColumn", "MySecondColumn"].  Only text fields are supported.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**DisplayFields** – List of fields shown for each item returned by the search.  Easiest to configure via the Data pane in the Properties option tab.

> [!NOTE]
> To update multiple display fields in given template, set **DisplayFields** property in this format: `["MyFirstColumn", "MySecondColumn"]`.

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

> [!NOTE]
> Flyout border properties are controlled by **Border** properties.

## Examples

### Basic Combo box

The steps in this example apply to any [data source that provides tables](../connections-list.md#tables), but to follow these steps exactly, use an environment with Microsoft Dataverse database having sample data.

1. Select **Insert** > **Input** > **Combo box**, and name it "Combobox1".  

1. On the **Properties** pane on the right-side of the screen, open the **Select a data source** list (next to **Items**), and then add or select a data source such as the Accounts table.

1. On the same pane, select **Edit** (next to **Fields**).

1. In the **Data** pane, open the **Primary text** list, and then select the **Primary Name** column that will show in the **Combo box** control.

1. While holding down the **Alt** key, select the down arrow to open the **Combo box** control.

    The control shows the data from the Primary Name that you specified in the data source that you specified.

#### (Optional) Show the first record by default

1. Set the **DefaultSelectedItems** property to this expression, replacing *DataSource* with the name of your data source:
    
    ```power-fx    
    First(DataSource)
    ```

#### (Optional) Display selected Account Name value in a label

1. Select **Insert** > **Text label**, and then select **Label**.  
1. Set the **Text** property to this expression, replacing *Text* with the following formula:

    ```power-fx
    If(CountRows(ComboBox1.SelectedItems)>0, Concat(ComboBox1.SelectedItems,'Account Name',", "), "NO SELECTED ITEM")
    ```

    > [!NOTE]
    > The If statement will check to see how may selected items exist and display them in a comma delimited label or a "NO SELECTED ITEM" message when empty.

### Simulate simple drop-down behavior

By setting **IsSearchable** to false and **SelectMultiple** to false, you can achieve the same functionality of a drop-down.

1. Select **Insert** > **Input**, and then select **Combo box**.  

1. On the **Properties** pane on the right-side of the screen, open the **Select a data source** list (next to **Items**), and then add or select a data source.

1. On the same pane, select **Edit** (next to **Fields**).

1. In the **Data** pane, open the **Primary text** list, and then select the column that you want to show in the **Combo box** control.

1. Set the **IsSearchable** property to false.

1. Set the **SelectMultiple** property to false.

1. While holding down the **Alt** key, select the down arrow to open the **Combo box** control.

    The control shows the data from the column that you specified in the data source that you specified.
    
    > [!NOTE]
    > "Find items" text has disappeared, and that you'll only be able to select a single item.

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
  > The tab key navigates to or away from the combo box. Arrow keys navigate the contents of the combo box. The escape key closes the drop-down when opened.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
