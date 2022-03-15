---
title: Use an interactive map control in Power Apps
description: Insert maps, and add customized pins, with augmented reality controls in Power Apps.
author: anuitz
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.date: 3/3/2022
ms.reviewer: mduelae
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
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
- [Draw and insert shapes](geospatial-map-draw-shapes.md)

## Prerequisites

You'll need to satisfy a few [prerequisites](geospatial-overview.md#prerequisites) before you can use maps in your canvas apps.

## Add a map to an app screen

With your app open for [editing](edit-app.md) in [Power Apps Studio](https://create.powerapps.com):

1. Select the **Insert** tab and expand **Media**.
2. Select **Map** to place a map in the app screen, or drag the control to the screen to position it more precisely.

## Properties

Change a map's behavior and appearance using properties. Some properties are only available on the **Advanced** tab.

:::image type="content" source="./media/augmented-geospatial/geospatial-controls.png" alt-text="A screenshot of a phone app in which a map control is shown next to the Properties tab in Microsoft Power Apps Studio.":::

| Property | Description | Type | Tab |
| - | - | - | - |
| Locations(Items) | Identifies a [data source](./geospatial-map-excel.md) (**Items**) in the form of a table in an Excel workbook from which to get locations to show on the map. The table lists sets of longitudes and latitudes, or physical addresses, to display as pins. Each row must have an entry for label, longitude, and latitude, or a physical address, and optionally the pin color and icon. | Not applicable | Properties; Advanced: **Items** |
| Transparency | Determines the map's transparency, from 0 (opaque) to 100 (transparent).| Integer| Properties; Advanced: **Transparency** |
| [Visible](./controls/properties-core.md) | Shows or hides the map. | Boolean | Properties; Advanced: **Visible** |
| Position | Places the upper-left corner of the map at the screen coordinates specified in *x* and *y*. | Floating point number | Properties; Advanced: **[X](./controls/properties-size-location.md)**, **[Y](./controls/properties-size-location.md)** |
| Size | Determines the size of the map using the pixel values provided in *Width* and *Height*. | Integer | Properties; Advanced: **[Width](./controls/properties-size-location.md)**, **[Height](./controls/properties-size-location.md)** |
| Use default location | Initializes the map at a default location. | Boolean | Properties; Advanced: **DefaultLocation** |
| Default latitude | Sets the latitude coordinate the map shows if **Use default location** is enabled. | Floating point number | Properties; Advanced: **DefaultLatitude** |
| Default longitude | Sets the longitude coordinate the map shows if **Use default location** is enabled. | Floating point number | Properties; Advanced: **DefaultLongitude** |
| Default zoom level | Sets the zoom level if **Use default location** is enabled, from 0 to 22. | Integer | Properties; Advanced: **DefaultZoomLevel** |
| Show current location | Displays the user's current location. | Boolean | Properties; Advanced: **CurrentLocation** |
| Current location latitude | Sets the latitude coordinate the map shows if **Show current location** is enabled. To place the pin at the user's current location, set this property to [Location.Latitude](/functions/signals#location). | Floating point number | Properties; Advanced: **CurrentLocationLatitude** |
| Current location longitude | Sets the longitude coordinate the map shows if **Show current location** is enabled. To place the pin at the user's current location, set this property to [Location.Longitude](/functions/signals#location). | Floating point number | Properties; Advanced: **CurrentLocationLongitude** |
| Satellite view | Displays the map in satellite view. Leave this property off to display the map in road view. | Boolean | Properties; Advanced: **SatelliteView** |
| Cluster pins | Groups nearby map pins instead of displaying them individually. | Boolean | Properties; Advanced: **Clustering** |
| Zoom control | Shows the zoom control. | Boolean | Properties; Advanced: **Zoom** |
| Compass control | Shows the compass control. | Boolean | Properties; Advanced: **Compass** |
| Pitch control | Shows the pitch (tilt) control. | Boolean | Properties; Advanced: **Pitch** |
| Show info cards | [Shows information](./geospatial-map-infocards.md) about a mapped location when the user selects it (*On click*) or points to it (*On hover*). If *None*, no information is shown. | Enum | Properties; Advanced: **InfoCards** |
| Pin color | Determines the color of pins shown on the map. | Color picker | Properties; Advanced: **PinColor** |
| Route waypoints(Items) | Shows route waypoints, as provided in a data source (**RouteWaypoints_Items**) in the form of a table in an Excel workbook. If *None*, no waypoints are shown. | Enum | Properties; Advanced: **RouteWaypoints_Items** |
| Enable routing | Determines whether the user can request directions to a specified location. | Boolean | Properties; Advanced: **UseRouting** |
| Maintain waypoint order | Determines whether a calculated route maintains waypoints in the order provided.| Boolean | Properties; Advanced: **RouteMaintainOrder** |
| Optimize route | Determines whether a calculated route is optimized for distance, time, or isn't optimized. | Enum | Properties; Advanced: **RouteOptimization** |
| Route travel mode | Determines whether a route is calculated for a car or a truck, which may require avoiding bridges with certain height or weight restrictions. | Enum | Properties; Advanced: **RouteTravelMode** |
| Show shapes | Shows the shapes in **Shapes_Items**. | Boolean | Properties; Advanced: **ShowShapes** |
| Show shape labels | Shows the shape labels, if provided. | Boolean | Properties; Advanced: **ShowShapeLabels** |
| Enable shape drawing | Shows drawing tools on the map. | Boolean | Properties; Advanced: **ShapeDrawing** |
| Enable shape deleting and label editing | Determines whether the user can delete shapes and edit their labels. | Boolean | Properties; Advanced: **ShapeEditingDeleting** |
| Border radius | Determines the corner radius of the map border. | Floating point number | Properties; Advanced: **BorderRadius** |
| Border | Determines the style, width, and color of the map border. | Not applicable | Properties; Advanced: **[BorderStyle](./controls/properties-color-border.md)**, **[BorderThickness](./controls/properties-color-border.md)**, **[BorderColor](./controls/properties-color-border.md)** |
| [TabIndex](./controls/properties-accessibility.md) | Specifies the order the map is selected if the user navigates the app using the Tab key. | Integer | Properties; Advanced: **Tab index** |
| OnItemsChange | Contains code that runs when pins on the map are changed. | Event | Advanced |
| OnLoad | Contains code that runs when the map is loaded. | Event | Advanced |
| OnMapClick | Contains code that runs when the user selects the map. | Event | Advanced
| OnShapeCreated | Contains code that runs when the user adds a shape to the map. | Event | Advanced |
| OnShapeSelected | Contains code that runs when the user selects a shape on the map. | Event | Advanced |
| OnShapeEdited | Contains code that runs when the user modifies a shape on the map. | Event | Advanced |
| OnShapeDeleted | Contains code that runs when the user deletes a shape on the map. | Event | Advanced |
| OnRouteDirectionChange | Contains code that runs when the app detects the user has changed direction while on a computed route.| Event | Advanced |
| OnChange | Contains code that runs when any aspect of the map is changed. | Event | Advanced |
| OnSelect | Contains code that runs when the user selects something on the map. | Event | Advanced |
| ItemsLabels | Identifies the column in **Items** that contains the labels for the pins. | ColumnName | Advanced |
| ItemsLatitudes | Identifies the column in **Items** that contains the latitude position of the pins. | ColumnName | Advanced |
| ItemsLongitudes | Identifies the column in **Items** that contains the longitude position of the pins.  | ColumnName | Advanced |
| ItemsAddresses | Identifies the column in **Items** that contains addresses that represent the location of the pins. | ColumnName | Advanced |
| ItemsColors | Identifies the column in **Items** that contains the colors of the pins. | ColumnName | Advanced |
| ItemsIcons | Identifies the column in **Items** that contains the icons of the pins. | ColumnName | Advanced |
| Shapes_Items | Identifies a [data source](./geospatial-map-excel.md) (**Shapes_Items**) in the form of a table in an Excel workbook from which to get shapes to show on the map. Each row must have an entry for the shape (GeoJSON object) and (optionally) a label and color. | TableName | Advanced |
| ShapeGeoJSONObjects | Identifies the column in **Shapes_Items** with strings that represent the GeoJSON objects of the shapes, in shape collection or single shape GeoJSON format. | ColumnName | Advanced |
| ShapeLabels | Identifies the column in **Shapes_Items** that contains the labels for the shapes. | ColumnName | Advanced |
| ShapeColors | Identifies the column in **Shapes_Items** that contains the colors of the shapes. | ColumnName | Advanced |
| RouteWaypoints_Items | Identifies a [data source](./geospatial-map-excel.md) (**RouteWaypoints_Items**) in the form of a table in an Excel workbook from which to get waypoints to show on the map. Each row must have an entry for label, longitude, and latitude (or a physical address). | TableName | Advanced |
| RouteWaypointsLabels | Identifies the column in **RouteWaypoints_Items** that contains the labels for the waypoints. | ColumnName | Advanced
| RouteWaypointsLatitudes | Identifies the column in **RouteWaypoints_Items** that contains the latitude position of the waypoints. | ColumnName | Advanced |
| RouteWaypointsLongitudes | Identifies the column in **RouteWaypoints_Items** that contains the longitude position of the waypoints.  | ColumnName | Advanced |
| RouteWaypointsAddresses | Identifies the column in **RouteWaypoints_Items** that contains addresses that represent the location of waypoints. | ColumnName | Advanced |
| [Tooltip](./controls/properties-core.md) | Determines the text to display when the user hovers over a visual. | String | Advanced |
| ContentLanguage | Determines the display language of the map, if it's different from the language used in the app. | String | Advanced |
| [DisplayMode](./controls/properties-core.md) |  Determines whether the control allows user input (*Edit*), only displays data (*View*), or is disabled (*Disabled*). | Enum | Advanced |

### Output properties

Other properties become available when a user interacts with a map. You can use these *output properties* in other controls or to customize the app experience.

| Property | Description | Type |
| - | - | - |
| CenterLocation | Captures the map's center point. | Not Applicable |
| OnMapClick | Captures the last location the user selected. | Not Applicable |
| Selected | Captures the selected pin. | Record |
| SelectedItems | Captures the selected pin or pins in the selected cluster. | Table |
| GeocodedItems | Captures the geocoded locations of the pins. | Table |
| ClickedLocation | Captures the last location the user selected, either *.Latitude* or *.Longitude*. | Record |
| Shapes_Selected | Corresponds to the record of the selected shape in **Shapes_Items**. | Record |
| Shapes_SelectedItems | Corresponds to the records of the selected overlapping shapes in **Shapes_Items**. | Table |
| SelectedShape | Captures the *.Perimeter* and *.Area* of the selected shape. | Record |
| DeletedShape | Captures the *.Perimeter* and *.Area* of the last deleted shape. | Record |
| GeoJSON | Captures the list of shapes in Feature Collection GeoJSON format. | String |

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

### See also

[Create an app with address input and map controls](how-to/mobile-apps-address-map.md)
