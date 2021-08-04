---
title: Power BI tile control in Power Apps
description: Learn about the details, properties, and examples of the Power BI tile control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/04/2021
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

## Sharing and security

When you share an app that contains Power BI content, you must share not only the app itself but also the [dashboard](/power-bi/service-how-to-collaborate-distribute-dashboards-reports) where the tile comes from. Otherwise, the Power BI content won't appear even for users who open the app. Apps that contain Power BI content respect the permissions for that content.

## Performance

It's not recommended to have more than three Power BI tiles loaded at the same time within an app. You can control tile loading and unloading by setting the **LoadPowerBIContent** property.

## Embedding Options

Embedding is different between versions of the Power BI API. Because of the new Power BI API authentication scheme, your tile may not be accessible on mobile or within other embedded scenarios (Teams or SharePoint).

You can control the use of API version using the AllowNewAPI value. See [Key properties](#key-properties) for more information.

| AllowNewAPI property value | Behavior |
| - | - |
| True | You can embed a dashboard, report, or tile by taking the **Embed URL** from Power BI and making it the **TileUrl** value. |
| False | You can embed a dashboard tile either by **Embed URL** and making it the **TileUrl** value, or using the graphical interface provided.

## Filtering

Filtering differs between the versions of the Power BI API. See the appropriate sections below depending on how you configure the control.

### When using the new API to call Power BI service

When **AllowNewAPI** property is set to "True", you're using new API to call Power BI service. For more information, see [Filter a report using query string parameters in the URL](/power-bi/collaborate-share/service-url-filters).

### When using the original API to call Power BI service

When **AllowNewAPI** property is set to "False", you're using the original API to call Power BI service. In this case, by passing a single parameter from the app, you can filter the results that appear in a Power BI tile. However, only string values and the equals operator are supported, and the filter might not work if the table name or the column name contains spaces.

To pass a single filter value, modify the value of the **TileURL** property, which follows this syntax:

```
"https://app.powerbi.com/embed?dashboardId=<DashboardID>&tileId=<TileID>&config=<SomeHash>"
```

To that value, append this syntax:

```
&$filter=<TableName>/<ColumnName> eq '<Value>'
```

For example, using a value from a list box: 
```
"&$filter=Store/Territory eq '" & ListBox1.Selected.Abbr & "'"
```

The parameter will filter a value in the dataset of the report where the tile originates. However, filtering feature has the following limitations:

- Only one filter can be applied.
- Only the `eq` operator is supported.
- Field type must be string.
- Filtering is only available on pinned visualization tiles. It's not supported for pinned reports.
- R and Python script visuals cannot be filtered.

You can use computed fields in the Power BI report to convert other value types to string or combines multiple fields into one.

## Key properties

**AllowNewAPI** - Whether to use the new API when calling the Power BI service. Setting the value to **True** will allow the use of the new Power BI API (which isn't supported in mobile and some embedded scenarios, but allows some more advanced filtering). **False** will use the original API. Default value is **false**.

**Dashboard** – The Power BI dashboard where the tile comes from.

**LoadPowerBIContent** – When set to **True**, the Power BI content is loaded and shown. When set to **False**, the Power BI content is unloaded, which releases memory and optimizes performance.

**Tile** – The name of the Power BI tile that you want to display.

**Workspace** – The Power BI workspace where the tile comes from.

## Additional properties

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – Actions to perform when the user selects a control. By default, the Power BI report that's associated with the tile opens.

**TileUrl** – The URL by which the tile is requested from the Power BI service. To add query string filtering to your URL, see the [filtering](#filtering) section above.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example

1. On the **Insert** tab, open the **Charts** menu, and then add a **Power BI tile** control.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

2. On the **Data** tab of the options panel, select **My Workspace** for the **Workspace** setting.

3. Select a dashboard in the list of dashboards, and then select a tile in the list of tiles.

    The control renders the Power BI tile.

## Accessibility guidelines

The **Power BI tile** is simply a container for Power BI content. Learn how to create accessible content with these [Power BI accessibility tips](/power-bi/desktop-accessibility).

If the Power BI content doesn't have a title, consider adding a heading using a **[Label](control-text-box.md)** control to support screen readers. You can position the label immediately before the Power BI tile.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
