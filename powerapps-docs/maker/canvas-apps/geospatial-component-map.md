---
title: Insert interactive maps into apps
description: Insert maps, and add customized pins, in Power Apps.
author: anuitz
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: tapanm
ms.date: 1/19/2021
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - anuitz
---


# Interactive map control

You can easily add an interactive map to your canvas apps. Plot markers from a data source containing addresses or latitude and longitude pairs. As you zoom out, the markers will optionally cluster to condense groups of data. On mobile devices and web experiences, a map can show the user's current position. Maps can be switched between road and satellite views.

![A map control shown in Power Apps Studio.](./media/augmented-geospatial/geospatial-map-component.png "Map control in Power Apps Studio")

You'll need to [enable geospatial features](geospatial-overview.md#enable-the-geospatial-features-for-the-environment) before you can add a map control to your apps. You should also [review the prerequisites for using geospatial controls](geospatial-overview.md#prerequisites).

## Add a map to an app screen

With your app open for editing in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab and expand **Media**.
3. Select **Map** to place a map in the app screen, or drag the control to the screen to position it more precisely.

Use the [Properties](#input-properties) tab to modify the map's appearance and behavior.

For example, to show the user's current location:

1. Turn on **Show current location**.
2. In **Current location latitude**, insert [Location.Latitude](/functions/signals#location).
3. In **Current location longitude**, insert [Location.Longitude](/functions/signals#location).

The current location pin should appear on the map.

### Show locations from an Excel workbook

Your map can take location data from an Excel table. Each row is plotted as a pin on the map.

Create a named table with the following columns. The columns determine the placement and appearance of the pins and correspond to properties on the **Advanced** tab.

| Column name | Corresponds to | Required |
| -- | -- | -- |
| Name (or Label) | ItemsLabels | Required |
| Longitude | ItemsLongitudes | Required |
| Latitude | ItemsLatitudes | Required |
| Color | ItemsColors | Optional |
| Icon | ItemsIcons | Optional |

Specify the color using a name or a CSS string as defined in [Color enumeration and ColorFade, ColorValue, and RGBA functions in Power Apps](/functions/function-colors). For example, "Blue" and "ffefcd" are equally valid.

You can find icon names in the [List of image templates](/azure/azure-maps/how-to-use-image-templates-web-sdk#list-of-image-templates) in the Azure maps documentation.

Here's an example of a table named "TestData" that contains location information for a company's top customers:

:::image type="content" source="media/geospatial/sample-excel.png" alt-text="Example Excel worksheet with a table named TestData that contains Name, Longitude, Latitude, Color, and Icon columns":::

To try this example, first create a table in Excel that contains the location data.

1. Copy the sample data in the following table and paste it in cell A1 of a new Excel worksheet.

| Name | Longitude | Latitude | Color | Icon |
| -- | -- | -- | -- | -- |
| Fourth Coffee (sample) | -98.29277 | 26.2774 | Blue | marker-flat |
| Litware, Inc. (sample) | -96.85572 | 32.55253 | #ffefcd| hexagon-thick |
| Adventure Works (sample) | -96.99952 | 32.72058 | | car |
| Fabrikam, Inc. (sample) | -118.30746 | 34.86543 | |
| Blue Yonder Airlines (sample) | -118.66184 | 34.17553 | |
| City Power & Light (sample) | -113.46184 | 37.15363 | |
| Contoso Pharmaceuticals (sample) | -80.26711 | 40.19918 | |
| Alpine Ski House (sample) | -102.63908 | 35.20919 | |
| A Datum Corporation (sample) | -89.39433 | 40.71025 | |
| Coho Winery (sample) | -116.97751 | 32.87466 | |

2. Select one of the pasted cells. On the **Home** tab, select **Format as Table**, choose a style, and then select **OK**.
3. On the **Table Design** tab under **Table Name**, enter a name such as *TestData*.
4. Save the workbook and close it.

Next, add the table as a data source for your map. You can add a data source when you create a map or modify an existing map.
 
1. Add a map or select an existing map in Power Apps Studio.
2. Type *excel* in the search box under **Select a data source**, and then select **Import from Excel**.
3. Locate the Excel workbook you saved earlier and open it.
4. Select the name you gave the table in Excel and then select **Connect**.
5. On the **Advanced** tab, find **ItemsLabels**, **ItemsLatitudes**, **ItemsLongitudes**, **ItemsColors**, and **ItemsIcons** and enter the name of the corresponding column in the table. (In this example, enter *Name* in **ItemsLabels**, *Latitude* in **ItemsLatitude**, and so on.) Enclose the column name in quotation marks.

Pins will appear on the map at the locations described by the coordinates in the table. Depending on the pins' locations and the map's zoom level, you may see numbered clusters of pins. The number indicates how many pins are represented in a cluster. Zoom in to see the individual pins.

## Interactive map features

- [Use a data source to insert pins](geospatial-map-excel.md)
- [Display information about map pins](geospatial-map-infocards.md)
- [Draw and insert shapes](geospatial-map-draw-shapes.md)

## Properties

Change a map's behavior and appearance using properties. Some properties are only available on the **Advanced** tab.

![A map control displayed next to the Advanced tab of the Properties pane in Power Apps Studio.](./media/augmented-geospatial/geospatial-controls.png "A map control displayed next to the Advanced properties tab in Power Apps Studio")

### Input properties

Input properties control what the map looks like and shows before a user interacts with it.

| Property | Description | Type | Tab |
| - | - | - | - |
| Locations(Items) | Identifies a data source (table) that lists a set of longitudes and latitudes, or physical addresses, to display as pins on the map. Enter the corresponding column name in the **ItemsLabels**, **ItemsLatitudes**, **ItemsLongitudes**, **ItemsAddresses**, **ItemsColors**, and **ItemsIcons** advanced properties. If *None*, no locations are pinned. | Not applicable | Properties; Advanced: **Items** |
| Transparency | Determines the map's transparency, from 0 (opaque) to 100 (transparent).| Integer| Properties; Advanced: **Transparency** |
| **[Visible](./controls/properties-core.md)** | Shows or hides the map. | Boolean | Properties; Advanced: **[Visible](./controls/properties-core.md)** |
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
| Show info cards | Shows information about a mapped location when the location is selected (*On click*) or is pointed to (*On hover*). If *None*, no information is shown. | Enum | Properties; Advanced: **InfoCards** |
| Pin color | Determines the color of pins shown on the map. | Color picker | Properties; Advanced: **PinColor** |
| Route waypoints(Items) | Shows route waypoints, as provided in a data source (**RouteWaypoints_Items**). If *None*, no waypoints are shown. | Enum | Properties; Advanced: **RouteWaypoints_Items** |
| Enable routing | Determines whether the user can request directions to a specified location. | Boolean | Properties; Advanced: **UseRouting** |
| Maintain waypoint order | Determines whether a calculated route maintains waypoints in the order provided.| Boolean | Properties; Advanced: **RouteMaintainOrder** |
| Optimize route | Determines whether a calculated route is optimized for distance, time, or is not optimized. | Enum | Properties; Advanced: **RouteOptimization** |
| Route travel mode | Determines whether a route is calculated for a car or a truck, which may require avoiding bridges with certain height or weight restrictions. | Enum | Properties; Advanced: **RouteTravelMode** |
| Show shapes | Shows the shapes in **Shapes_Items**. | Boolean | Properties; Advanced: **ShowShapes** |
| Show shape labels | Shows the shape labels, if provided. | Boolean | Properties; Advanced: **ShowShapeLabels** |
| Enable shape drawing | Shows drawing tools on the map. | Boolean | Properties; Advanced: **ShapeDrawing** |
| Enable shape deleting and label editing | Determines whether the user can delete shapes and edit their labels. | Boolean | Properties; Advanced: **ShapeEditingDeleting** |
| Border radius | Determines the corner radius of the map border. If *0*, the corners are right angles; if *360*, the map is shown as a circle.| Floating point number | Properties; Advanced: **BorderRadius** |
| Border | Determines the style, width, and color of the map border. | Not applicable | Properties; Advanced: **[BorderStyle](./controls/properties-color-border.md)**, **[BorderThickness](./controls/properties-color-border.md)**, **[BorderColor](./controls/properties-color-border.md)** |
| **[TabIndex](./controls/properties-accessibility.md)** | Specifies the order the map is selected if the user navigates the app using the Tab key. | Integer | Properties; Advanced: **TabIndex** |
| OnItemsChange | NEEDS DESCRIPTION. | Event | Advanced |
| OnLoad | NEEDS DESCRIPTION. | Event | Advanced |
| OnMapClick | NEEDS DESCRIPTION. | Event | Advanced
| OnShapeCreated | NEEDS DESCRIPTION. | Event | Advanced |
| OnShapeSelected | NEEDS DESCRIPTION. | Event | Advanced |
| OnShapeEdited | NEEDS DESCRIPTION. | Event | Advanced |
| OnShapeDeleted | NEEDS DESCRIPTION. | Event | Advanced |
| OnRouteDirectionChange | NEEDS DESCRIPTION.| ? | Advanced |
| OnChange | NEEDS DESCRIPTION. | ? | Advanced |
| OnSelect | NEEDS DESCRIPTION. | ? | Advanced |
| Items | Identifies the table in your data source that contains locations to plot on the map using pins. Each row must have an entry for label, longitude, and latitude (or a physical address), and (optionally) the pin color and icon. | TableName | Advanced |
| ItemsLabels | Identifies the column in **Items** that contains the labels for the pins. | ColumnName | Advanced |
| ItemsLatitudes | Identifies the column in **Items** that contains the latitude position of the pins. | ColumnName | Advanced |
| ItemsLongitudes | Identifies the column in **Items** that contains the longitude position of the pins.  | ColumnName | Advanced |
| ItemsAddresses | Identifies the column in **Items** that contains addresses that represent the location of the pins. | ColumnName | Advanced |
| ItemsColors | Identifies the column in **Items** that contains the colors of the pins. | ColumnName | Advanced |
| ItemsIcons | Identifies the column in **Items** that contains the icons of the pins. | ColumnName | Advanced |
| Shapes_Items | Identifies the table in your data source that contains shapes to show on the map. Each row must have an entry for the shape (GeoJSON object) and (optionally) a label and color. | TableName | Advanced |
| ShapeGeoJSONObjects | Identifies the column in **Shapes_Items** with strings that represent the GeoJSON objects of the shapes, in shape collection or single shape GeoJSON format. | ColumnName | Advanced |
| ShapeLabels | Identifies the column in **Shapes_Items** that contains the labels for the shapes. | ColumnName | Advanced |
| ShapeColors | Identifies the column in **Shapes_Items** that contains the colors of the shapes. | ColumnName | Advanced |
| RouteWaypoints_Items | Identifies the table in your data source that contains waypoints to show on the map. Each row must have an entry for label, longitude, and latitude (or a physical address). | TableName | Advanced |
| RouteWaypointsLabels | Identifies the column in **RouteWaypoints_Items** that contains the labels for the waypoints. | ColumnName | Advanced
| RouteWaypointsLatitudes | Identifies the column in **RouteWaypoints_Items** that contains the latitude position of the waypoints. | ColumnName | Advanced |
| RouteWaypointsLongitudes | Identifies the column in **RouteWaypoints_Items** that contains the longitude position of the waypoints.  | ColumnName | Advanced |
| RouteWaypointsAddresses | Identifies the column in **RouteWaypoints_Items** that contains addresses that represent the location of waypoints. | ColumnName | Advanced |
| **[Tooltip](./controls/properties-core.md)** | Determines the text to display when the user hovers over a visual. BRIEFLY, WHERE DOES THIS COME FROM? | ? | Advanced |
| ContentLanguage | Determines the display language of the map, if it's different from the language used in the app. | ? | Advanced |
| **[DisplayMode](./controls/properties-core.md)** |  Determines whether the control allows user input (*Edit*), only displays data (*View*), or is disabled (*Disabled*). | Enum | Advanced |

### Output properties

Your app can make use of more properties when a user interacts with a map. These are known as output properties. You can use these properties in other controls or to customize the app experience.

| Property | Description | Type |
| -- | -- | -- |
| CenterLocation | The map's center point | Not Applicable |
| OnMapClick | The last location selected | Not Applicable |
| Selected | The selected pin | Record |
| SelectedItems | The selected pin or pins in the selected cluster | Table |
| GeocodedItems | The geocoded locations of the pins | Table |
| ClickedLocation | The last location selected as either `.Latitude` or `.Longitude` | Record |
| Shapes_Selected | The record of the selected shape from **Shapes_Items** | Record |
| Shapes_SelectedItems | The records of the selected overlapping shapes from **Shapes_Items** | Table |
| SelectedShape | The selected shape with `.Perimeter` and `.Area` | Record |
| DeletedShape | The last deleted shape with `.Perimeter and `.Area` | Record |
| GeoJSON | The list of shapes in Feature Collection GeoJSON format | String |

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

### See also

[Create an app with address input and map controls](how-to/mobile-apps-address-map.md)
