---
title: Display information about map pins
description: Add info cards to your maps to show information about pinned locations in Power Apps.
author: anuitz
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: tapanm
ms.date: 02/22/2022
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

# Add informational cards to map pins

Use info cards to show selected details about pinned locations in your canvas apps. When a user selects a pin on a map, a card pops up with information from the [dataset you bound to the control](./geospatial-component-map.md). Any column in the data source (for example, an Excel table) can be included as a field to show on the card.

## Prerequisites

1. [Create a canvas app](./create-blank-app.md) and make sure it meets the [geospatial prerequisites](./geospatial-overview.md#prerequisites).
1. [Insert a map](geospatial-component-map.md#use-the-control).

## Add info cards to pins

1. [Bind the map to a data source](geospatial-map-excel.md#add-pin-data-from-an-excel-workbook).
1. In the **Properties** pane, change the **Show info cards** property to **On click** if the user must select a pin to show the info card. Change the property to **On hover** if an info card should appear when the user hovers over the pin.

    :::image type="content" source="./media/geospatial/map-info-card-type.png" alt-text="A screenshot of a map control's Properties pane, with the Show info cards property open to show the On click and On hover options.":::

1. In the **Properties** pane, next to **Fields**, select **Edit**.
1. Select **Add field**, and then select the fields you want to show in the card. Select **Add**.

    :::image type="content" source="./media/geospatial/map-choose-fields.png" alt-text="A screenshot of a map control's field selection options.":::

An info card shows the selected fields when the user selects or hovers over the pin.

:::image type="content" source="media/geospatial/map-info-card-example.png" alt-text="A screenshot of a map with a pin's info card open to show Name, Occupancy, and Phone from the associated data source.":::

## Other interactive map features

- [Use data from Excel to insert pins](./geospatial-map-excel.md)
- [Draw and insert shapes onto maps](./geospatial-map-draw-shapes.md)

## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
