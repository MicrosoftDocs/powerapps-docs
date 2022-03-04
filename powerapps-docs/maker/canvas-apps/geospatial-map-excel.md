---
title: Add pins to a map from a data source
description: Import an Excel table to place customized pins on a map in Power Apps.
author: anuitz
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: mkaur
ms.date: 3/3/2022
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

# Use a data source to place pins on a map

The map control in a canvas app can import location data from a named table in an Excel workbook. Each row is plotted as a pin on the map. Each column corresponds to an advanced property of the map control. Together, the columns determine the placement and appearance of the pins.

| Column name | Corresponds to | Required |
| - | - | - |
| Name (or Label) | ItemsLabels | Required |
| Longitude | ItemsLongitudes | Required |
| Latitude | ItemsLatitudes | Required |
| Address | ItemsAddresses | Required if Longitude and Latitude aren't given |
| Color | ItemsColors | Optional |
| Icon | ItemsIcons | Optional |

>[!Tip]
> Specify the color using a [name, CSS color definition, or RGBA value](/functions/>function-colors). Specify the icon using an [image template](/azure/azure-maps/how-to-use-image-templates-web-sdk#list-of-image-templates). If an icon or color isn't provided, then the pins will use the app's defaults.

## Import pins from an Excel table

In this example, we'll import pins from an Excel table named *TestData*. The table contains location information for a company's top customers.

:::image type="content" source="media/geospatial/sample-excel.png" alt-text="An example Excel worksheet with a table named TestData that contains information needed to place pins on a map.":::

### Create a data source

1. [Create a table](https://go.microsoft.com/fwlink/?linkid=2186917) in Excel with the following data. Name the table **TestData**.

    | Name | Longitude | Latitude | Address | Color | Icon |
    | - | - | - | - | - | - |
    | Fourth Coffee | -98.29277 | 26.2774 | 706 South Orange Street, Alton, TX 78573 | Blue | marker-flat |
    | Bellows College | -96.85572 | 32.55253 | | #ffefcd | hexagon-thick |
    | Adventure Works | -96.99952 | 32.72058 | | | car |
    | Fabrikam, Inc. | -118.30746 | 34.86543 | 7989 Edwards Avenue, Rosamond, CA 93560 | | |
    | Margie's Travel | -118.66184 | 34.17553 | 6074 John Muir Road, Hidden Hills, CA 91302 | | |
    | Relecloud | -113.46184 | 37.15363 | 1704 North Ranch View Drive, Washington, UT 84780 | Red | car |
    | Contoso Pharmaceuticals | -115.17241  | 36.11947 | 3475 Las Vegas Blvd S, Las Vegas, NV 89109 | | |
    | Alpine Ski House | -102.63908 | 35.20919 | | | |
    | Adatum Corporation | -89.39433 | 40.71025 | | | |
    | Tailwind Traders | -116.97751 | 32.87466 | | | |

2. Save the workbook to your OneDrive for Business and close the file.

### Bind the data source to a map control

1. [Create a canvas app](./create-blank-app.md). Make sure it meets the [geospatial prerequisites](geospatial-overview.md#prerequisites).
2. [Insert a map control](geospatial-component-map.md).
3. On the control's **Properties** tab, select the **Locations(Items)** dropdown list and type **excel**.
4. Select **Excel Online (Business)**. Add a connection if needed, or select your Excel Online (Business) connection.
5. Navigate to your OneDrive for Business and select the Excel workbook you saved earlier.
6. Select the table **TestData**, and then select **Connect**.
7. Select **Connect** again to accept the default identifier (auto-generated ID).
8. On the **Advanced** tab, find **ItemsLabels**, **ItemsLatitudes**, **ItemsLongitudes**, **ItemsAddresses**, **ItemsColors**, and **ItemsIcons** and enter the name of the corresponding column in the table. (In this example, enter *Name* in **ItemsLabels**, *Latitude* in **ItemsLatitude**, and so on.) Enclose the column name in quotation marks.

    :::image type="content" source="media/geospatial/advanced-properties.png" alt-text="A screenshot of a map control under construction in Microsoft Power Apps Studio, shown alongside its ItemsLabels, ItemsLatitudes, and ItemsLongitudes properties.":::

Pins appear on the map at the locations described by the coordinates or addresses in the table.

Depending on the pins' locations and the map's zoom level, you may see numbered clusters instead of individual pins. The number indicates how many pins are represented in a cluster. Preview the app and zoom in to see the individual pins. If the table included colors and icons, the pins are customized from the default.

:::image type="content" source="media/geospatial/pins-map.png" alt-text="A screenshot of a map with two default pins, one customized pin, and one cluster of two pins.":::

## Save geocoded addresses back to the data source

You can place up to 5,000 pins on a map using latitude/longitude pairs, but only up to 50 pins using a physical address. That's because the map control must geocode physical addresses, converting them to latitude/longitude pairs, before they can be pinned. When both an address and coordinates are provided in the data source, the map control prioritizes latitude and longitude to avoid needlessly geocoding the address.

After a map runs the first time, you can save the coordinates of geocoded addresses back to the original data source. Then the map control will use the latitude and longitude to place the pins, instead of geocoding the addresses again.

To save geocoded addresses back to the data source, use the [**Patch**](./functions/function-patch.md) function bound to a button control.

Continuing with the *TestData* table from our earlier example, enter the following formula in the button control's **OnSelect** property:

```text
 ForAll(Map1.GeocodedItems, Patch(TestData, LookUp(TestData, ThisRecord.Address = Address), {Latitude: Latitude, Longitude: Longitude }))
```



## Other interactive map features

- [Add info cards to pins](geospatial-map-infocards.md)
- [Draw and insert shapes onto maps](geospatial-map-draw-shapes.md)

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
