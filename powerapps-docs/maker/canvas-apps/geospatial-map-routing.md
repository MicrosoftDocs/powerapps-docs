---
title: Calculate routes between waypoint pins on a map (preview)
description: Add waypoint pins to a map and calculate routes between them in Power Apps.
author: anuitz
ms.topic: how-to
ms.custom: canvas, ce06122020
ms.reviewer: mduelae
ms.date: 3/3/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
---

# Calculate routes between waypoint pins on a map (preview)

[!INCLUDE[Preview disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The map control in a canvas app can add waypoint pins using data imported from a table in an Excel workbook. The control can calculate routes between waypoints, reorder waypoints, and recalculate a route to improve travel time or distance.

>[!IMPORTANT]
>
>- This is a preview feature.
>- [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

You'll need a data source that contains a named table with the following columns. Each column corresponds to an advanced property of the map control. Each row is pinned as a waypoint on the map.

| Column name | Corresponds to | Required |
| - | - | - |
| Name (or Label) | RouteWaypointsLabels | Optional |
| Longitude | RouteWaypointsLongitudes | Optional (required if Address isn't given) |
| Latitude | RouteWaypointsLatitudes | Optional (required if Address isn't given) |
| Address | RouteWaypointsAddresses | Optional (required if Longitude and Latitude aren't given) |


> [!NOTE]
> All properties are technically optional. However, at least one of an address or a latitude/longitude pair must be provided for the waypoint location to be plotted.


## Import waypoint pins from an Excel table

In this example, we'll import waypoint data from an Excel table named *TestData*.

### Create a data source

1. [Create a table](https://go.microsoft.com/fwlink/?linkid=2186917) in Excel with the following data. Name the table **TestData**.

    | Name | Longitude | Latitude | Address |
    | - | - | - | - |
    | Work | -122.156481 | 47.663448 | 1 Microsoft Way, Redmond, WA 98052 |
    | Meet up | -122.221037 | 47.57137 |
    | Swimming | -122.144133 | 47.600373 |
    | Tennis | -122.137265 | 47.616115 |

    Your table should look something like this:

    :::image type="content" source="./media/geospatial/map-routing-table.png" alt-text="An example Excel worksheet with a table named TestData that contains information needed to place waypoint pins on a map.":::

1. Save the workbook to your OneDrive for Business and close the file.

### Bind the data source to a map control

1. [Create a canvas app](./create-blank-app.md). Make sure it meets the [geospatial prerequisites](./geospatial-overview.md#prerequisites-for-full-support).
1. [Insert a map control](./geospatial-component-map.md).
1. On the control's **Properties** tab, select the **Route waypoints(Items)** box and type *excel*.

    :::image type="content" source="./media/geospatial/map-routing-property.png" alt-text="A screenshot that shows how to search for a waypoint data source to connect to a map control in Power Apps Studio.":::

1. Select **Import from Excel**.
1. Navigate to your OneDrive for Business and select the Excel workbook you saved earlier.
1. Select the table **TestData**, and then select **Connect**.

    :::image type="content" source="./media/geospatial/select-table.png" alt-text="Screenshot of the table selection panel.":::

1. On the **Advanced** tab, find **RouteWaypointsLabels**, **RouteWaypointsLatitudes**, **RouteWaypointsLongitudes**, and **RouteWaypointsAddresses** and enter the name of the corresponding column in the table. (In this example, enter *Name* in **RouteWaypointsLabels**, *Latitude* in **RouteWaypointsLatitudes**, and so on.) Enclose the column name in quotation marks.

    >[!NOTE]
    >Address is interchangeable with Latitude and Longitude. If Latitude and Longitude are provided, then Address isn't used. If Address is provided, then Latitude and Longitude aren't needed. There is a limit to the number of waypoints that can be displayed when using address, so use Latitude and Longitude when possible. 

Pins appear on the map at the locations described by the coordinates or addresses in the table. If the table included labels, the pins are labeled. The pins are numbered in the order the waypoint locations appear in the table.

:::image type="content" source="./media/geospatial/map-routing-pins.png" alt-text="A screenshot of a map with pinned and labeled waypoints shown next to the map's properties.":::

## Calculate routes between the waypoints

With the map control selected, open the **Properties** tab and turn on **Enable routing**.

The control calculates routes between the pinned waypoints.

:::image type="content" source="./media/geospatial/map-routing-directions.png" alt-text="A screenshot of a map with routes between pinned waypoints.":::

>[!NOTE]
>By default, the map control reorders the middle waypoints to decrease travel time or travel distance. The first and last waypoints are considered the origin and destination and can't be reordered. To keep the waypoints in the order given in the data source, turn on the control's **Maintain waypoint order** property.

### Properties

Change how a route is calculated using properties.

| Property | Description | Type | Tab |
| - | - | - | - |
| Enable routing | Calculates routes between waypoints. | Boolean | Properties; Advanced: **UseRouting** |
| Maintain waypoint order | Determines whether a calculated route maintains waypoints in the order provided in the data source. | Boolean | Properties; Advanced: **RouteMaintainOrder** |
| Optimize route | Determines whether a calculated route is optimized for distance, time, or isn't optimized. | Dropdown list | Properties; Advanced: **RouteOptimization** |
| Route travel mode | Determines whether a route is calculated for a car or a truck, which may require avoiding bridges with certain height or weight restrictions. | Dropdown list | Properties; Advanced: **RouteTravelMode** |
| Show route pins | Determines whether pins are shown over the route waypoints. | Boolean | Properties; Advanced: **ShowRoutePins** |

### Output Properties

Some properties become available only when a calculated route changes. These *output properties* are placed in the **RouteDirection** object. The **OnRouteDirectionChange** event is a recommended way to use the output in other controls or to customize the app experience.

| Property | Description | Type | Tab |
| - | - | - | - |
| OnRouteDirectionChange | Contains code that runs when the route is changed. | Event | Advanced |
| RouteDirection | Describes the routing outputs:<ul><li>LengthInMeters: The length in meters of the entire route</li><li>TravelTimeInSeconds: The expected travel time in seconds of the entire route</li><li>RouteGeoJSON: A string that describes the route in GeoJSON format</li><li>RouteLegs: A table that describes each leg of the route:<ul><li>Index: A number that represents the leg's order in the route</li><li>LengthInMeters: The length of the leg in meters</li><li>TravelTimeInSeconds: The expected travel time of the leg in seconds</li><li>StartLabel: The label of the leg's starting point</li><li>StartLatitude: The latitude of the leg's starting point</li><li>StartLongitude: The longitude of the leg's starting point</li><li>StartAddress: The address of the leg's starting point</li><li>EndLabel: The label of the leg's ending point</li><li>EndLatitude: The latitude of the leg's ending point</li><li>EndLongitude: The longitude of the leg's ending point</li><li>EndAddress: The address of the leg's ending point</li></ul><li>OrderedWaypoints: A table that describes each waypoint after the waypoints are ordered:<ul><li>Index: A number that represents the waypoint's order in the route</li><li>Label: The label of the waypoint</li><li>Latitude: The latitude of the waypoint</li><li>Longitude: The longitude of the waypoint</li><li>Address: The address of the waypoint</li></ul></ul> | Object | Not applicable (output property only)

### See also

[Interactive map control](./geospatial-component-map.md)
