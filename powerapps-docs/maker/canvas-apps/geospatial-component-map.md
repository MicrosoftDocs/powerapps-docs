---
title: 
description: 
author: iaanw
manager: shellha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 6/01/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
ms.custom: ce06032020
---


# Interactive map component (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

Easily bring dynamic mapping capabilities into your canvas apps by viewing the physical position of entities from a data source, or by inputting new physical locations. 

Pan, tilt, zoom, and drag to center your map view. As you zoom out, the markers will optionally cluster to represent dense groups of data. 

The current location of the user can also be represented on the map on mobile devices or web experiences. 

The map component also supports road and satellite views.

![](./media/augmented-geospatial/geospatial-map-component.png)

To use the component, you need to [enable the geospatial features for the environment](geospatial-overview.md#enable-the-geospatial-features-for-the-environment) as well as [enable the geospatial features for each app](geospatial-overview.md#enable-the-geospatial-features-for-each-app) that you want to use it in.

Make sure to also [review the prerequisites for using geospatial components](geospatial-overview.md#prerequisites).

## Use the component

Insert the component into your app as you normally would for any other control or component.

With an app open for editing in the [Power Apps studio](https://create.powerapps.com):

1. Open the **Insert** tab.
2. Expand **Media**.
3. Select the component **Map** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.
4. (Optional) Select **Allow** on the prompt that asks to know your location. This enables the component to display the user's current location.

    ![Allow highlighted on the window that asks to know your location](./media/geospatial/address-allow.png "Allow highlighted on the window that asks to know your location")

You can modify the component with a number of properties.

### Properties

The following properties can be defined and configured in the component's **Properties** pane.

![](./media/augmented-geospatial/geospatial-controls.png)

Note that some properties are only available in the **Advanced** tab on the **Properties** pane, under the **More options** button.

Property | Description | Type | Location
- | - | - | -
Data source(Items) | Data source (table) that lists a pre-defined set of longitudes and latitudes to display as map pin on the map when it's loaded. Map each of the columns in your data with the *ItemAddresses*, *ItemLongitudes*, *ItemLatitudes*, and *ItemLabels*. | Not applicable | Properties
Use default location | Whether the map initializes at a default location set by the user or not. | Boolean | Properties
Default longitude | Longitude at which the map would go to when it's loaded if **Use default location** is enabled. | Floating point number | Properties
Default latitude | Latitude at which the map would go to when it's loaded if **Use default location** is enabled. | Floating point number | Properties
Default zoom level | Zoom level at which the map would be set to when it's loaded if **Use default location** is enabled. | Integer | Properties
Show current location | Whether the map should display the current location of the user (if it has permission). | Boolean | Properties
Satellite view | Whether the style of the map is a satellite view or a road view. | Boolean | Properties
Cluster pins | Whether the map pins are clustered or not. | Boolean | Properties
Zoom control | Whether the zoom component appears on the map or not. | Boolean | Properties
Compass control | Whether the compass component appears on the map or not. | Boolean | Properties
Pitch control | Whether the pitch component appears on the map or not. | Boolean | Properties
Pin color | The color of the pins. | Color picker | Properties
Maximum map pins | Maximum number of pins displayed on the map. | Integer | Properties
ItemsLabels | A column in Items with the strings you want to use as labels for the pins. | TableName.ColumnName | Advanced
ItemsAddresses | A column in Items with the strings that represent the location of the pins. Does not work with **ItemsLongitudes** or **ItemsLatitudes**. | TableName.ColumnName | Advanced
ItemsLongitudes | Name of the column in the table in your data source with floating-point numbers that represent the longitude position of the pins. Does not work with **ItemsAddresses**. | TableName.ColumnName | Advanced
ItemsLatitudes | Name of the column in the table in your data source with floating-point numbers that represent the latitude position of the pins. Does not work with **ItemsAddresses**. | TableName.ColumnName | Advanced
Items_Items | Name of the table in your data source that contains all the records that you want to plot in the map using pins. Each row must have an entry for the label, longitude, and latitude for each row. | TableName | Advanced

### Additional properties

**[BorderColor](./controls/properties-color-border.md)** - The color of a control's border.

**BorderRadius** - The radius of a control's border.

**[BorderStyle](./controls/properties-color-border.md)** - Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](./controls/properties-color-border.md)** - The thickness of a control's border.

**[Color](./controls/properties-color-border.md)** - The color of text in a control.

**[DisplayMode](./controls/properties-core.md)** - Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](./controls/properties-size-location.md)** - The distance between a control's top and bottom edges.

**[TabIndex](./controls/properties-accessibility.md)** - Keyboard navigation order.

**[Tooltip](./controls/properties-core.md)** - Explanatory text that appears when the user hovers over a control.

**Transparency** - How transparent the component is as a percentage.

**[Visible](./controls/properties-core.md)** - Whether a control appears or is hidden.

**[Width](./controls/properties-size-location.md)** - The distance between a control's left and right edges.

**[X](./controls/properties-size-location.md)** - The distance between the left edge of a control and the left edge of its parent container (or the screen if there's no parent container).

**[Y](./controls/properties-size-location.md)** - The distance between the top edge of a control and the top edge of the parent container (or the screen if there's no parent container).

## Other geospatial components

- See dynamic address suggestions as you type with the **[Address input](geospatial-component-input-address.md)** component.
