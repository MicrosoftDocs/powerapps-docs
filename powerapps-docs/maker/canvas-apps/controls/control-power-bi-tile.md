---
title: 'Power BI tile control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Power BI tile control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 07/07/2016
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Power BI tile control in PowerApps

A control that shows a [Power BI](https://powerbi.microsoft.com) tile inside an app.

Don't have have Power BI? [Sign up](https://docs.microsoft.com/power-bi/service-self-service-signup-for-power-bi).

## Description

Take advantage of your existing data analysis and reporting by displaying your **[Power BI tiles](https://docs.microsoft.com/power-bi/service-dashboard-tiles)** inside your apps. Specify the tile that you want to show by setting its **Workspace**, **Dashboard**, and **Tile** properties in the **Data** tab of the options panel.

## Sharing and security

When you share an app that contains Power BI content, you must share not only the app itself but also the [dashboard](https://docs.microsoft.com/power-bi/service-how-to-collaborate-distribute-dashboards-reports) where the tile comes from. Otherwise, the Power BI content won't appear even for users who open the app. Apps that contain Power BI content respect the permissions for that content.

## Performance

It's not recommended to have more than three Power BI tiles loaded at the same time within an app. You can control tile loading and unloading by setting the **LoadPowerBIContent** property.

## Pass a parameter

By passing a single parameter from the app, you can filter the results that appear in a Power BI tile. However, only string values and the equals operator are supported, and the filter might not work if the table name or the column name contains spaces.

To pass a single filter value, modify the value of the **TileURL** property, which follows this syntax:

```"https://msit.powerbi.com/embed?dashboardId=<DashboardID>&tileId=<TileID>&config=<SomeHash>" ```

To that value, append this syntax:

```&$filter=<TableName>/<ColumnName> eq "<Value>" ```

The parameter will filter a value in the dataset of the report where the tile originates.

## Key properties

**Workspace** – The Power BI workspace where the tile comes from.

**Dashboard** – The Power BI dashboard where the tile comes from.

**Tile** – The name of the Power BI tile that you want to display.

**LoadPowerBIContent** – When set to true, the Power BI content is loaded and shown. When set to false, the Power BI content is unloaded, which releases memory and optimizes performance.

## Additional properties

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control. By default, the Power BI report that's associated with the tile opens.

**TileUrl** – The URL by which the tile is requested from the Power BI service. You can pass a single parameter into the Power BI tile by appending the parameter to the URL (for example: … & "&$filter=Town/Province eq '" & ListBox1.Selected.Abbr & "'"). You can use only the equals operator in the parameter.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example

1. On the **Insert** tab, open the **Controls** menu, and then add a **Power BI tile** control.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

2. On the **Data** tab of the options panel, click or tap **My Workspace** for the **Workspace** setting.

3. Select a dashboard in the list of dashboards, and then select a tile in the list of tiles.

    The control renders the Power BI tile.

## Accessibility guidelines

The **Power BI tile** is simply a container for Power BI content. Learn how to create accessible content with these [Power BI accessibility tips](https://docs.microsoft.com/power-bi/desktop-accessibility).

If the Power BI content doesn't have a title, consider adding a heading using a **[Label](control-text-box.md)** control to support screen readers. You can position the label immediately before the Power BI tile.
