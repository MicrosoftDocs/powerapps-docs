---
title: Table control in Power Apps
description: Learn about the deprecation of the modern Table control and how to migrate to Data Grid.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 11/19/2026
ms.subservice: canvas-maker
ms.author: jasongre


ms.reviewer: joshuapa
search.audienceType: 
  - maker
contributors:
  - jasongre
  - noazarur-microsoft
reviewer: joshuapartlow
  
---
# Table modern control in Power Apps (deprecated)

[This article is pre-release document and is subject to change.]

A control that shows a set of data in a tabular or list format.

> [!IMPORTANT]
> The modern **Table** control is deprecated and is no longer under active development. Use the [Data Grid modern control](modern-control-data-grid.md) for new apps. Existing apps that use Table continue to work during the migration period. Migrate before **June 1, 2027**. The classic Data Table control is not affected.

## Deprecation

Data Grid replaces Table for modern tabular scenarios.

- Don't add Table to new apps.
- Replace existing Table controls with Data Grid before the removal date.
- Existing Table controls continue to run during the migration period.
- The classic Data Table control isn't affected.

### Migrate to Data Grid

1. Save a restorable version or copy of the app.
1. Select the Table control in the app.
1. In the properties pane, select **Update** to replace the Table control with a Data Grid control.
1. Review the converted Data Grid columns, properties, and formulas. Update any formulas that reference the old Table control or its selected records.
1. Test sorting, search, selection, responsive layouts, accessibility, data sources, and large datasets.
1. Publish the migrated app and monitor it.

## Description
The **Table** control is a modern responsive control that shows a set of data in a tabular or list format. The tabular format includes column headings for each displayed field and a footer that provides details about the dataset such as the record count. The list format presents the data in a single column and has three fields for each row. As an app maker, you have full control over what fields you add to the control including the order. Although all added fields are visible in the tabular format, only the initial three fields appear in the narrower list format.

Similar to the **Gallery** and **Data** table controls, the **Table** maintains a **Selected** property that points to the selected row and you can use it to link the **Table** control to other controls. The key properties for this control are **Items**, **ReflorBehavior**, **Selected**, and **OnSelect**.

## Supported capabilities

- Data in a **Table** control is read-only.
- The tabular format offers a modern data browsing experience with infinite scroll, eliminating the need for paging buttons.
- The **Table** control supports linking to Microsoft Dataverse tables and collections.
- When you connect a **Table** control to a compatible connector such as Microsoft Dataverse, it displays a predefined set of fields by default. You can also display or hide other fields based on your needs.
- The **Table** control can automatically switch between tabular and list formats. You can manually manage this behavior by using the **Reflow** property.
- When you run your app, you can adjust column width in the **Table** control. However, your changes aren't saved.
- Change the color palette for the **Table** via the Base palette color property. 

### Unsupported capabilities
The following capabilities aren't supported in the deprecated **Table** control. Use Data Grid for new tabular scenarios and review its current capabilities and limitations.

* Linking the **Table** to other data connectors.
* Customizing the style of the **Table** other than the color palette or modifying individual columns.


## General

**[Items](../properties-core.md)** - The source of data for the items that appear in the table.

**NoDataText** - The message shown to a user when there are no records to show in the **Table** control. 

**[Visible](../properties-core.md)** - Whether a control appears or is hidden.

## Behavior 

**ReflowBehavior** - The default responsive behavior of the table. **Reflow** means the table displays in tabular form when the control is 480 or more pixels wide and transitions to a list format in narrower conditions. **GridOnly** (or **ListOnly**) means the table always displays in a tabular (or list) format regardless of the control width. You can use Power Fx formulas to create your own breakpoints for defining the responsive behavior of the table.

**EnableSorting** – Allows users to sort the data in the table by using dropdowns from the column headers for supported data types. 

**EnableRangeSelection** – Whether users can select a portion of the table to copy its values. Default is **Yes**. 

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** – The distance between a control's top and bottom edges. 


## Style and theme 

**HeaderFont** - The font for the column headings. 

**HeaderFontSize** - The font size for the column headings. 

**HeaderFontColor** - The text color for the column headings. 

**HeaderFontWeight** - The font weight for the column headings. 

**BasePaletteColor** - The color palette you apply to a control. This color affects all surfaces of the control that render a theme color. 

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size for the text that appears on a control. If the value is null or zero, the selected Fluent theme determines the font size. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

## Additional properties

**Selected** – The selected row in the **Table** control.  

**DisplayMode** - Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

**OnSelect** – Defines the action triggered when a single record is selected.  

**ShowAvatar** - Whether the user’s avatar appears or is hidden in the list mode. 

**ShowColumnHeaders** – Whether the column headers appear or are hidden. 

**ShowFooter** - Whether the footer appears or is hidden.  

**[Size](../properties-text.md)** – The size of the control on the canvas.

**AccessibleLabel** – Label for screen readers. 











