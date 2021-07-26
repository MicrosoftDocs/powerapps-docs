---
title: Power BI tile control in Power Apps
description: Learn about the details, properties and examples of the Power BI tile control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/26/2021
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
# Power BI tile control in Power Apps

A control that shows a [Power BI](https://powerbi.microsoft.com) tile inside an app.

Don't have Power BI? [Sign up](/power-bi/service-self-service-signup-for-power-bi).

## Description

Take advantage of your existing data analysis and reporting by displaying your **[Power BI tiles](/power-bi/service-dashboard-tiles)** inside your apps. Specify the tile that you want to show by setting its **Workspace**, **Dashboard**, and **Tile** properties in the **Data** tab of the options panel.

  > [!NOTE]
  > - Power BI tile control only supports tile visualizations pinned to a dashboard. To embed a report page, pin the page to the dashboard first. Then, you can embed that tile visualization.
  > - *Querystring parameter filtering* is only supported within pinned visualization tiles. It's not supported for pinned reports.

## Sharing and security

When you share an app that contains Power BI content, you must share not only the app itself but also the [dashboard](/power-bi/service-how-to-collaborate-distribute-dashboards-reports) where the tile comes from. Otherwise, the Power BI content won't appear even for users who open the app. Apps that contain Power BI content respect the permissions for that content.

## Performance

It's not recommended to have more than 3 Power BI tiles loaded at the same time within an app. You can control tile loading and unloading by setting the **LoadPowerBIContent** property.

## Pass a parameter

By passing a single parameter from the app, you can filter the results that appear in a Power BI tile. However, only string values and the equals operator are supported, and the filter might not work if the table name or the column name contains spaces.

To pass a single filter value, modify the value of the **TileURL** property, which follows this syntax:

```
"https://app.powerbi.com/embed?dashboardId=<DashboardID>&tileId=<TileID>&config=<SomeHash>"
```

To that value, append this syntax:

```
&$filter=<TableName>/<ColumnName> eq '<Value>'
```

The parameter will filter a value in the dataset of the report where the tile originates. However, filtering feature has the following limitations:

- Only one filter can be applied.
- Only the `eq` operator is supported.
- Field type must be string.
- Filtering is only available on pinned visualization tiles. It's not supported for pinned reports.
- R and Python script visuals cannot be filtered.

You can use computed fields in the Power BI report to convert other value types to string or combines multiple fields into one.

## Key properties

**AllowNewAPI** - Whether to use the new API when calling the Power BI service.  **True** will allow the use of the new Power BI API which is not supported in mobile and some embedded scenarios, but allows some more advanced filtering. **False** will use the original API.  Default **false**.

**Dashboard** – The Power BI dashboard where the tile comes from.

**LoadPowerBIContent** – When set to true, the Power BI content is loaded and shown. When set to false, the Power BI content is unloaded, which releases memory and optimizes performance.

**Tile** – The name of the Power BI tile that you want to display.

**Workspace** – The Power BI workspace where the tile comes from.

## Additional properties

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control. By default, the Power BI report that's associated with the tile opens.

**TileUrl** – The URL by which the tile is requested from the Power BI service. You can pass a single parameter into the Power BI tile by appending the parameter to the URL (for example: … & "&$filter=Town/Province eq '" & ListBox1.Selected.Abbr & "'"). You can use only the equals operator in the parameter. 
  > [!NOTE]
  > Filtering is only available on pinned visualization tiles.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example

1. On the **Insert** tab, open the **Charts** menu, and then add a **Power BI tile** control.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

2. On the **Data** tab of the options panel, click or tap **My Workspace** for the **Workspace** setting.

3. Select a dashboard in the list of dashboards, and then select a tile in the list of tiles.

    The control renders the Power BI tile.

## Accessibility guidelines

The **Power BI tile** is simply a container for Power BI content. Learn how to create accessible content with these [Power BI accessibility tips](/power-bi/desktop-accessibility).

If the Power BI content doesn't have a title, consider adding a heading using a **[Label](control-text-box.md)** control to support screen readers. You can position the label immediately before the Power BI tile.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
