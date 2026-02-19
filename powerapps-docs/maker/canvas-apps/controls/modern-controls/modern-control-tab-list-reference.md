---
title: Tab List modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Tab List modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/18/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Tab List modern control in canvas apps

A tabbed navigation control that allows users to switch between different content sections by clicking tab headers.

## Description

Use the **Tab List** control to create tabbed interfaces where users can switch between different views or content sections. The control displays clickable tab headers that users can select to navigate between sections. Use this control in combination with conditional visibility on other controls to show/hide content based on the selected tab. Key properties for this control are **Items**, **Default**, **Selected**, and **Appearance**.

> [!NOTE]
> This article describes the Tab List modern control. For information about migrating from the previous version, see [Migrate to the Tab List modern control](tab-list-migration.md).

## General

**Items** – The data source that provides the list of tabs to display. Can be a table, collection, or list of values. Each item becomes a clickable tab header.

**Default** – The tab that is selected by default when the control first loads. Must match an item from the **Items** source.

**Selected** – The currently selected tab (output property). Use this in formulas to reference which tab the user has chosen and to control visibility of content sections.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnChange** – How the app responds when the user clicks a different tab. This event fires every time the selected tab changes. Use this to update variables, load data, or track navigation.

**OnSelect** – How the app responds when the user clicks any tab (including the currently selected one). Use this for additional interactions beyond navigation.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, tabs are displayed but cannot be clicked.

## Size and position

**Align** – The horizontal alignment of tab text within each tab button. Accepts `Align` enum values:

| Value | Description |
|-------|-------------|
| `Align.Left` | Aligns text to the left edge |
| `Align.Center` | Centers text horizontally (default) |
| `Align.Right` | Aligns text to the right edge |

**Alignment** – The alignment/positioning of the entire tab list. Accepts `TabListAlignment` enum values:

| Value | Description |
|-------|-------------|
| `TabListAlignment.Start` | Aligns tabs to the left/start edge |
| `TabListAlignment.Center` | Centers the tab list (default) |
| `TabListAlignment.End` | Aligns tabs to the right/end edge |

**X** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**Y** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **300**.

**Height** – Distance between the control's top and bottom edges. Default is **60**.

**PaddingTop** – Distance between the tab text and the top edge of each tab button.

**PaddingBottom** – Distance between the tab text and the bottom edge of each tab button.

**PaddingLeft** – Distance between the tab text and the left edge of each tab button.

**PaddingRight** – Distance between the tab text and the right edge of each tab button.

## Style and theme

**Appearance** – The visual style of the tabs. Accepts `TabListAppearance` enum values:

| Value | Description |
|-------|-------------|
| `TabListAppearance.Transparent` | Transparent background with text only |
| `TabListAppearance.Subtle` | Subtle background with minimal styling |
| `TabListAppearance.Underline` | Tabs with underline indicator for selection |
| `TabListAppearance.Filled` | Filled tab buttons with solid backgrounds |

**Font** – The name of the font family in which tab text appears.

**Size** – The font size of the tab text, in points.

**Color** – The color of the tab text in the control.

**FontWeight** – The weight (thickness) of the tab text. Accepts `FontWeight` enum values:

| Value | Description |
|-------|-------------|
| `FontWeight.Bold` | Bold text |
| `FontWeight.Semibold` | Semibold text |
| `FontWeight.Normal` | Normal weight (default) |
| `FontWeight.Lighter` | Lighter weight |

**Italic** – Whether the tab text appears in italic style.

**Underline** – Whether a line appears under the tab text.

**Strikethrough** – Whether a line appears through the middle of the tab text.

**BorderColor** – The color of the borders around tabs (when applicable based on Appearance).

**BorderStyle** – The style of the tab borders. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the tab borders in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of tab buttons.

**RadiusTopRight** – The corner radius for the top-right corner of tab buttons.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of tab buttons.

**RadiusBottomRight** – The corner radius for the bottom-right corner of tab buttons.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the tab list represents. Should describe the category or sections being navigated (e.g., "Product information sections" or "Report views").

**ContentLanguage** – The language used for the tab text. Inherits from app settings if not specified.

## Example

The following YAML example shows tab list controls with different appearance styles:

```yaml
- ProductTabs:
    Control: ModernTabList@1.0.0
    Properties:
      Items: =["Overview", "Specifications", "Reviews", "Support"]
      Default: ="Overview"
      Appearance: =TabListAppearance.Underline
      Alignment: =TabListAlignment.Center
      Size: =16
      FontWeight: =FontWeight.Semibold
      AccessibleLabel: ="Product information tabs"
      X: =40
      Y: =100
      Width: =600
      Height: =60

- DashboardTabs:
    Control: ModernTabList@1.0.0
    Properties:
      Items: =["Sales", "Inventory", "Reports"]
      Default: ="Sales"
      Appearance: =TabListAppearance.Filled
      Alignment: =TabListAlignment.Start
      Size: =15
      AccessibleLabel: ="Dashboard section tabs"
      X: =40
      Y: =180
      Width: =600
      Height: =60

- SettingsTabs:
    Control: ModernTabList@1.0.0
    Properties:
      Items: =["Account", "Privacy", "Notifications", "Billing"]
      Default: ="Account"
      Appearance: =TabListAppearance.Subtle
      Alignment: =TabListAlignment.Start
      Size: =14
      Align: =Align.Left
      AccessibleLabel: ="Settings categories"
      X: =40
      Y: =260
      Width: =250
      Height: =60
```

## What's new in this version

This new Tab List modern control includes the following improvements:

- **Appearance property**: New **Appearance** property with four visual styles (**Transparent**, **Subtle**, **Underline**, **Filled**) gives you more design flexibility for tabbed interfaces.
- **Item order preserved**: Tabs now display in the exact order specified in the **Items** property. Previously, tabs were sometimes reordered unexpectedly.
- **Items refresh fixed**: Updating the **Items** property now automatically refreshes the tab list. Previously, changes to Items didn't always trigger a visual update.
- **Default property**: New **Default** property allows you to specify which tab is selected when the control loads.
- **Alignment control**: New **Alignment** property controls the positioning of the entire tab list (start, center, end).
- **Improved tab sizing**: Tab buttons now size more consistently and responsively.

## Best practices

- **Clear tab labels**: Use short, descriptive labels for tabs (1-2 words). Avoid long phrases that make tabs too wide.
- **Reasonable tab count**: Use 2-7 tabs for optimal usability. For more sections, consider alternative navigation patterns like a tree view or menu.
- **Default selection**: Always set a **Default** value to ensure a tab is selected when the control loads.
- **Conditional visibility**: Use the **Selected** output property to control visibility of content sections:
  ```
  ContentSection.Visible = TabList1.Selected.Value = "Overview"
  ```
- **Accessible labels**: Provide descriptive **AccessibleLabel** text that explains what the tabs navigate between.
- **Consistent appearance**: Use the same **Appearance** style for all tab lists in your app for visual consistency.
- **OnChange for data loading**: Use **OnChange** to load data or update variables when tabs change, improving performance by loading only what's needed.

## Limitations

- The Tab List control provides navigation only - you must manually control content visibility using the **Selected** property.
- Very small or very large width and height values may not be fully respected by the control.
- Tab buttons do not automatically scroll horizontally if there are too many tabs to fit the width.

## See also

- [Migrate to the Tab List modern control](tab-list-migration.md)
- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
