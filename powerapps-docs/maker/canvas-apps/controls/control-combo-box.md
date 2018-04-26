---
title: 'Combo box control: reference | Microsoft Docs'
description: Information, including properties and examples, about the combo box control
documentationcenter: na
author: fikaradz
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 09/13/2017
ms.author: fikaradz

---
# Combo box control in PowerApps
A control that allows users to make selections from provided choices.  Supports search and multiple selections.

## Description
A **Combo box** control allows you to search for items you will select.  The search is performed server-side on the SearchField property so performance is not affected by very large data sources.  

Single or multi-select mode is configured via the SelectMultiple property.

When searching for items to select, for each item you can choose to show a single data value, two values, or a picture and two values (Person) by modifying the Layout settings in the Data pane.

## People picker
To use **Combo box** as a people picker, choose the **Person** template from the Layout settings in the Data pane and configure the related data properties to be shown for the person below.

## Key properties
**[Items](properties-core.md)** – The source of data from which selections can be made.

**DefaultItems** – The initial selected item(s) before the user interacts with the control.

**SelectedItems** – List of selected items resulting from user interaction.

**SelectMultiple** – Whether the user can select a single item or multiple items.

**IsSearchable** – Whether the user can search for items before selecting.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Default](properties-core.md)** – The initial selection before it is changed by the user in single-select mode.

**DisplayFields** – List of fields shown for each item returned by the search.  Easiest to configure via the Data pane in the Properties option tab.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**InputTextPlaceholder** – Instructional text shown to end-users when no items are selected.

**OnChange** – How the app responds when the user changes a selection.

**OnNavigate** – How the app responds when the user clicks on an item.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example
1. Add a **Combo box** control from the Insert tab, Controls menu.  
2. In the Properties options tab, click on Data.  
3. Select the data source, layout and related properties below.
4. Set the **SelectMultiple** property in the Advanced tab.

    A functional **Combo box** will appear in your app.

    Don't know how to [add and configure a control](../add-configure-controls.md)?.


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
