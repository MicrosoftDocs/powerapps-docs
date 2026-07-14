---
title: Display information about map pins
description: Add cards that display information about pinned locations in your canvas apps.
author: anuitz
ms.service: powerapps
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


# Add informational cards to pins on a map


Easily add cards to maps in your canvas apps to show details about pinned locations. When a user selects a pin, a card pops up with information from the [data source you bound to the map control](./geospatial-map-excel.md). Any column in the data source (for example, an Excel table) can be shown as a field on the card.

## Prerequisites

1. [Create a canvas app](./create-blank-app.md) and make sure it meets the [geospatial prerequisites](./geospatial-overview.md#prerequisites-for-full-support).
1. [Insert a map](./geospatial-component-map.md).


## Add info cards to pins

1. [Bind the map to a data source](./geospatial-map-excel.md).
1. In the map control's **Properties** pane, select **Show info cards**. Select **On click** to show the info card when the user selects a pin, or **On hover** if it should appear when the user hovers over the pin.

    :::image type="content" source="./media/geospatial/map-info-card-type.png" alt-text="A screenshot of a map control's Properties pane with the Show info cards property open to show the On click and On hover options.":::

1. In the **Properties** pane, next to **Fields**, select **Edit**.
1. Select **Add field**, and then select the fields from the data source that you want to show in the card. Select **Add**.

    :::image type="content" source="./media/geospatial/map-choose-fields.png" alt-text="A screenshot of a map control's Properties pane, showing the data source fields.":::

When the user selects a pin, an info card shows the fields you selected.

  :::image type="content" source="./media/geospatial/map-info-card-example.png" alt-text="A screenshot of a map pin selected in a canvas app, with an info card that shows the location Name, Occupancy, and Phone data.":::

## Other interactive map features

- [Use data from Excel to insert pins](./geospatial-map-excel.md)
- [Show routes between waypoints](geospatial-map-routing.md)
- [Draw and insert shapes onto maps](./geospatial-map-draw-shapes.md)

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

