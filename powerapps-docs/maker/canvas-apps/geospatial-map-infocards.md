---
title: Display information about map pins
description: Insert info cards that display information about each pin in your map.
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

# Add informational cards to pins

You can add informational cards to each pin on the map. 

When a user selects the pin (either by hovering over it or selecting it directly), a small card will pop-up with information taken from the dataset you bound to the control, as described in the topic [Use a data source to place pins on a map](geospatial-map-excel.md).

Any column you add to the table in the data source (for example, the Excel table) will be available as a field to show on the card.

## Prerequisites
1. Create a Canvas app and make sure it meets the [Geospatial prerequisites](geospatial-overview.md#prerequisites). 
2. In your app, [insert a map](geospatial-component-map.md#use-the-control). 


**To add informational cards to pins:**

1. First, bind the map to a dataset as described in [Use a data source to place pins on a map](geospatial-map-excel.md).

2. In the **Properties** pane, select **Show info cards** and choose whether they should appear when a user hovers over the pin, or if the user has to select the pin.

    :::image type="content" source="media/geospatial/map-info-card-type.png" alt-text="Screenshot of the properties pane showing the drop-down selection menu to show the cards on hover or on click.":::

3. In the **Properties** pane, next to **Fields**, select **Edit**.

4. Select **Add field**, and then select each of the fields you want to show in the card. Select **Add**.

    :::image type="content" source="media/geospatial/map-choose-fields.png" alt-text="Screenshot showing the field selection options.":::

5. Each pin will now show the fields associated with that pin in an informational card.

    :::image type="content" source="media/geospatial/map-info-card-example.png" alt-text="Screenshot of the map control with an info card on top of a pin, showing information such as Name, Occupancy, and Phone.":::



## Other interactive map features


- [Use data from Excel to insert pins](geospatial-map-excel.md)
- [Draw and insert shapes onto maps](geospatial-map-draw-shapes.md)


## Other geospatial controls

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** control.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
