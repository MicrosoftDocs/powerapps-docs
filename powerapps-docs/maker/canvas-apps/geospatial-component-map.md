---
title: Use an interactive map control in Power Apps
description: View an interactive map with customized pins, dynamic routing, and shapes with the geospatial controls in Power Apps.
author: anuitz
ms.topic: how-to
ms.custom: canvas, ce06122020
ms.date: 3/3/2022
ms.reviewer: mduelae
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
---

# Interactive map control

Easily add an interactive map to your canvas apps. Plot markers from a data source containing addresses or latitude and longitude pairs. As you zoom out, the markers will optionally cluster to condense groups of data. On mobile devices and web experiences, a map can show the user's current position and calculate a route to the user's destination. Maps can be switched between road and satellite views.

:::image type="content" source="./media/augmented-geospatial/geospatial-map-component.png" alt-text="A screenshot of a tablet app in which a map control is under construction in Microsoft Power Apps Studio.":::

## Interactive map features

- [Use a data source to insert pins](geospatial-map-excel.md)
- [Display information about map pins](geospatial-map-infocards.md)
- [Show routes between waypoints](geospatial-map-routing.md)
- [Draw and insert shapes](geospatial-map-draw-shapes.md)

## Prerequisites

You'll need to satisfy a few [prerequisites](geospatial-overview.md#prerequisites-for-full-support) before you can use maps in your canvas apps. Refer to the [privacy and security table](geospatial-overview.md#privacy-and-security-considerations) for more details on how different map features use data.

## Add a map to an app screen

With your app open for [editing](edit-app.md) in [Power Apps Studio](https://create.powerapps.com):

1. Select the **Insert** tab and expand **Media**.
2. Select **Map** to place a map in the app screen, or drag the control to the screen to position it more precisely.

## Adding pins, routes, and shapes

Pins, routes, and shapes are data set properties that need to both identify a data source, which is a table from a collection or connector, and the relevant columns. The data source is set in the Items property (Items for pins, RouteWaypoints_Items for routes, Shape_Items for shapes) and the relevant columns are set in the related properties (e.g. ItemLatitudes, ItemLongitudes, etc for pins). The [Properties](#properties) section contains additional information about these data sets and their related properties.

For example, if you had a table collection named **Locations** with **Name**, **Longitude**, and **Latitude** columns:

| Name | Longitude | Latitude |
| - | - | - |
| Fourth Coffee (sample) | -98.29277 | 26.2774 |
| Litware, Inc. (sample) | -96.85572 | 32.55253 |
| Adventure Works (sample) | -96.99952 | 32.72058 |

To display these as labeled pins on the map:

1. Set the **Items** property to Locations
1. Set the **ItemLabels** property to "Name"
1. Set the **ItemLongitude** property to "Longitude"
1. Set the **ItemLatitude** property to "Latitude"

    >[!IMPORTANT]
    >
    >The relevant column names need to be in quotation marks in the related properties. The data source should not have quotation marks.

You can see how to do [display pins from an Excel sheet](geospatial-map-excel.md) or [build an app](how-to/mobile-apps-address-map.md) that uses the address input control to populate pins on the map control as additional examples.

 >[!NOTE]
 > - Each map control can display up to 5,000 pins from latitude or longitude and 50 pins from addresses. The pin limit is lower for addresses as the map needs to geocode these addresses into latitude or longitude to display them. We recommend not using addresses where possible. You can [save geocoded addresses back to your data source](geospatial-map-excel.md#save-geocoded-addresses-from-map-control-to-data-source).
 > - When both latitude or longitude and an address is given for a single pin, the map control will prioritize using the latitude or longitude to avoid geocoding the address.
 > - The maximum number of shapes that can be drawn in a map control is limited to 500.


## Properties

Change a map's behavior and appearance using properties. Some properties are only available on the **Advanced** tab.

:::image type="content" source="./media/augmented-geospatial/geospatial-controls.png" alt-text="A screenshot of a phone app in which a map control is shown next to the Properties tab in Microsoft Power Apps Studio.":::

The map control has six different types of properties:

1. [Styling properties](#styling-properties)
1. [Behavioral properties](#behavioral-properties)
1. [Pin properties](#pin-properties)
1. [Route properties](#route-properties)
1. [Shape properties](#shape-properties)
1. [Output properties](#output-properties)

### Styling properties

| Property | Description | Type | Tab |
| - | - | - | - |
| Satellite view | Displays the map in satellite view. Leave this property off to display the map in road view. | Boolean | Properties; Advanced: **SatelliteView** |
| Map style | Sets the map style. Options: Road, Night, Road shaded relief, Satellite, Satellite road labels, High contrast light, High contrast dark, Grayscale light, Grayscale dark. | Enum | Properties |
| Transparency | Determines the map's transparency, from 0 (opaque) to 100 (transparent).| Integer| Properties; Advanced: **Transparency** |
| [Visible](./controls/properties-core.md) | Shows or hides the map. | Boolean | Properties; Advanced: **Visible** |
| Position | Places the upper-left corner of the map at the screen coordinates specified in *x* and *y*. | Floating point number | Properties; Advanced: **[X](./controls/properties-size-location.md)**, **[Y](./controls/properties-size-location.md)** |
| Size | Determines the size of the map using the pixel values provided in *Width* and *Height*. | Integer | Properties; Advanced: **[Width](./controls/properties-size-location.md)**, **[Height](./controls/properties-size-location.md)** |
| Border radius | Determines the corner radius of the map border. | Floating point number | Properties; Advanced: **BorderRadius** |
| Border | Determines the style, width, and color of the map border. | Not applicable | Properties; Advanced: **[BorderStyle](./controls/properties-color-border.md)**, **[BorderThickness](./controls/properties-color-border.md)**, **[BorderColor](./controls/properties-color-border.md)** |
| [DisplayMode](./controls/properties-core.md) |  Determines whether the control allows user input (*Edit*), only displays data (*View*), or is disabled (*Disabled*). | Enum | Advanced |

### Behavioral properties

| Property | Description | Type | Tab |
| - | - | - | - |
| Show info cards | [Shows information](./geospatial-map-infocards.md) about a mapped location when the user selects it (*On click*) or points to it (*On hover*). If *None*, no information is shown. | Enum | Properties; Advanced: **InfoCards** |
| Use default location | Initializes the map at a default location. | Boolean | Properties; Advanced: **DefaultLocation** |
| Default latitude | Sets the latitude coordinate the map shows if **Use default location** is enabled. | Floating point number | Properties; Advanced: **DefaultLatitude** |
| Default longitude | Sets the longitude coordinate the map shows if **Use default location** is enabled. | Floating point number | Properties; Advanced: **DefaultLongitude** |
| Default zoom level | Sets the zoom level if **Use default location** is enabled, from 0 to 22. | Integer | Properties; Advanced: **DefaultZoomLevel** |
| Show current location | Displays the user's current location. | Boolean | Properties; Advanced: **CurrentLocation** |
| Current location latitude | Sets the latitude coordinate of the current location pin that the map shows if **Show current location** is enabled. To place the pin at the user's current location, set this property to [Location.Latitude](/power-platform/power-fx/reference/signals#locationn). | Floating point number | Properties; Advanced: **CurrentLocationLatitude** |
| Current location longitude | Sets the longitude coordinate of the current location pin that the map shows if **Show current location** is enabled. To place the pin at the user's current location, set this property to [Location.Longitude](/power-platform/power-fx/reference/signals#location). | Floating point number | Properties; Advanced: **CurrentLocationLongitude** |
| Zoom control | Shows the zoom control. | Boolean | Properties; Advanced: **Zoom** |
| Compass control | Shows the compass control. | Boolean | Properties; Advanced: **Compass** |
| Pitch control | Shows the pitch (tilt) control. | Boolean | Properties; Advanced: **Pitch** |
| [TabIndex](./controls/properties-accessibility.md) | Specifies the order the map is selected if the user navigates the app using the Tab key. | Integer | Properties; Advanced: **Tab index** |
| [Tooltip](./controls/properties-core.md) | Determines the text to display when the user hovers over a visual. | String | Advanced |
| ContentLanguage | Determines the display language of the map, if it's different from the language used in the app. | String | Advanced |
| OnLoad | Contains code that runs when the map is loaded. | Event | Advanced |
| OnMapClick | Contains code that runs when the user selects the map. The latitude and longitude of the clicked point is in the **ClickedLocation** output property. | Event | Advanced |
| OnChange | Contains code that runs when any aspect of the map is changed. | Event | Advanced |
| OnSelect | Contains code that runs when the user selects something on the map. | Event | Advanced |

### Pin properties

| Property | Description | Type | Tab |
| - | - | - | - |
| Locations(Items) | Identifies a [data source](./geospatial-map-excel.md) (**Items**) in the form of a table from which to get locations to show on the map. The table lists sets of longitudes and latitudes, or physical addresses, to display as pins. Using latitude or longitude is recommended as addresses need to be geocoded and so have a more restrictive pin limit. The table can be a collection or from a data source like Excel Online. Each row must have an entry for label, longitude, and latitude, or a physical address, and optionally the pin color and icon. | Not applicable | Properties; Advanced: **Items** |
| ItemsLabels | Identifies the column in **Items** that contains the labels for the pins. | ColumnName | Advanced |
| ItemsLatitudes | Identifies the column in **Items** that contains the latitude position of the pins. | ColumnName | Advanced |
| ItemsLongitudes | Identifies the column in **Items** that contains the longitude position of the pins.  | ColumnName | Advanced |
| ItemsAddresses | Identifies the column in **Items** that contains addresses that represent the location of the pins. There is a limit to how many pins can be displayed from addresses. We recommend geocoding your addresses to latitude, longitude pairs and using those to display pins when possible. | ColumnName | Advanced |
| ItemsColors | Identifies the column in **Items** that contains the colors of the pins. | ColumnName | Advanced |
| ItemsIcons | Identifies the column in **Items** that contains the icons of the pins. | ColumnName | Advanced |
| Cluster pins | Groups nearby map pins instead of displaying them individually. | Boolean | Properties; Advanced: **Clustering** |
| Pin color | Determines the default color of pins shown on the map. This color is overridden by the **ItemsColors** property if set | Color picker | Properties; Advanced: **PinColor** |
| OnItemsChange | Contains code that runs when pins on the map are changed. | Event | Advanced |

### Route properties

| Property | Description | Type | Tab |
| - | - | - | - |
| Enable routing | Determines whether the user can request directions to a specified location. | Boolean | Properties; Advanced: **UseRouting** |
| Route waypoints(Items) | Shows route waypoints, as provided in a data source (**RouteWaypoints_Items**) in the form of a table. The table can be a collection or from a data source like Excel Online. If *None*, no waypoints are shown. | Enum | Properties; Advanced: **RouteWaypoints_Items** |
| RouteWaypointsLabels | Identifies the column in **RouteWaypoints_Items** that contains the labels for the waypoints. | ColumnName | Advanced
| RouteWaypointsLatitudes | Identifies the column in **RouteWaypoints_Items** that contains the latitude position of the waypoints. | ColumnName | Advanced |
| RouteWaypointsLongitudes | Identifies the column in **RouteWaypoints_Items** that contains the longitude position of the waypoints.  | ColumnName | Advanced |
| RouteWaypointsAddresses | Identifies the column in **RouteWaypoints_Items** that contains addresses that represent the location of waypoints. | ColumnName | Advanced |
| Maintain waypoint order | Determines whether a calculated route maintains waypoints in the order provided.| Boolean | Properties; Advanced: **RouteMaintainOrder** |
| Optimize route | Determines whether a calculated route is optimized for distance, time, or isn't optimized. | Enum | Properties; Advanced: **RouteOptimization** |
| Route travel mode | Determines whether a route is calculated for a car or a truck, which may require avoiding bridges with certain height or weight restrictions. | Enum | Properties; Advanced: **RouteTravelMode** |
| OnRouteDirectionChange | Contains code that runs when the app detects the user has changed direction while on a computed route.| Event | Advanced |

### Shape properties

| Property | Description | Type | Tab |
| - | - | - | - |
| Show shapes | Shows the shapes in **Shapes_Items**. | Boolean | Properties; Advanced: **ShowShapes** |
| Shapes_Items | Identifies a data source (**Shapes_Items**) in the form of a table from which to get shapes to show on the map. The table can be a collection or from a data source like Excel Online. Each row must have an entry for the shape (GeoJSON object) and (optionally) a label and color. | TableName | Advanced |
| ShapeGeoJSONObjects | Identifies the column in **Shapes_Items** with strings that represent the GeoJSON objects of the shapes, in shape collection or single shape GeoJSON format. | ColumnName | Advanced |
| ShapeLabels | Identifies the column in **Shapes_Items** that contains the labels for the shapes. | ColumnName | Advanced |
| ShapeColors | Identifies the column in **Shapes_Items** that contains the colors of the shapes. | ColumnName | Advanced |
| Show shape labels | Shows the shape labels, if provided. | Boolean | Properties; Advanced: **ShowShapeLabels** |
| Enable shape drawing | Shows drawing tools on the map. | Boolean | Properties; Advanced: **ShapeDrawing** |
| Enable shape deleting and label editing | Determines whether the user can delete shapes and edit their labels. | Boolean | Properties; Advanced: **ShapeEditingDeleting** |
| OnShapeCreated | Contains code that runs when the user adds a shape to the map. | Event | Advanced |
| OnShapeSelected | Contains code that runs when the user selects a shape on the map. | Event | Advanced |
| OnShapeEdited | Contains code that runs when the user modifies a shape on the map. | Event | Advanced |
| OnShapeDeleted | Contains code that runs when the user deletes a shape on the map. | Event | Advanced |

### Output properties

Other properties become available when a user interacts with a map. You can use these *output properties* in other controls or to customize the app experience.

| Property | Description | Type |
| - | - | - |
| CenterLocation | Captures the map's center point. | Not Applicable |
| ClickedLocation | Captures the last location the user selected, either *.Latitude* or *.Longitude*. | Record |
| Selected | Captures the selected pin. | Record |
| SelectedItems | Captures the selected pin or pins in the selected cluster. | Table |
| GeocodedItems | Captures the geocoded locations of the pins. | Table |
| RouteWaypoints_Selected | Corresponds to the record of the selected shape in **RouteWaypoints_Items**. | Record |
| RouteWaypoints_SelectedItems | Corresponds to the records of the selected overlapping shapes in **RouteWaypoints_Items**. | Table |
| Shapes_Selected | Corresponds to the record of the selected shape in **Shapes_Items**. | Record |
| Shapes_SelectedItems | Corresponds to the records of the selected overlapping shapes in **Shapes_Items**. | Table |
| SelectedShape | Captures the *.Perimeter* and *.Area* of the selected shape. | Record |
| DeletedShape | Captures the *.Perimeter* and *.Area* of the last deleted shape. | Record |
| GeoJSON | Captures the list of shapes in Feature Collection GeoJSON format. | String |

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

## Known limitations

- Requires internet connection

### See also

[Create an app with address input and map controls](how-to/mobile-apps-address-map.md)
