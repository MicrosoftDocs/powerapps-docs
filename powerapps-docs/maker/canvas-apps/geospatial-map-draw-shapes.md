---
title: Let users draw and insert shapes into maps
description: Allow users of your app to draw shapes onto maps, or insert predefined shapes and display their measurements.
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: tapanm
ms.date: 3/2/2021
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---


# Draw and insert shapes onto maps (Preview)

[!INCLUDE[Preview disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can add a drawing panel to your interactive maps that lets your users draw and label shapes in the app.

You can also create and label shapes on maps you insert into your Power Apps app with the interactive map component.

This can be useful for pre-defining special regions or areas of interest to your map users, for example a sales district or shipping zone.

    :::image type="content" source="media/geospatial/custom-geojson-shape-example.png" alt-text="Screenshot of map with example shapes drawn and labeled.":::

## Prerequisites
1. Create a Canvas app and make sure it meets the [Geospatial prerequisites](geospatial-overview.md#prerequisites). 

2. In your app, [insert a map](geospatial-component-map.md#use-the-component). 

## Draw and label shapes on interactive maps
To draw and label shapes on maps you first need to enable the following settings:

1. Open the **Properties** pane with a map selected.

2. Switch the toggles to **On** for the following:
    -  **(Preview) Enable Shape Drawing**
    - **(Preview) Enable Shape Deleting and Label Editing**
 
 
:::image type="content" source="media/geospatial/enable-feature.png" alt-text="Screenshot of the properties pane the features turned to On.":::

You will now see the drawing panel on the top left corner of the map component. The panel consists of three tools:

- A polygon drawing tool that allows you to create freeform custom shapes, indicated by a square icon with a broken top.
- A square drawing tool that lets you draw squares and rectangles, indicated by a square icon.
- A circle drawing tool that lest you draw circles and ovals, indicated by a circle icon.
- 
>[!NOTE]
>When you’ve finished drawing a freeform custom shape, double-click to indicate the last point in the shape.
 
:::image type="content" source="media/geospatial/drawing-panel.png" alt-text="Screenshot of the map component, with the drawing panel highlighted.":::

Drawn shapes are automatically labeled. To change the labels, enter the new name for the label in label editing bar on the top right corner of the map. 

To delete a shape, select it, then select the Delete button, indicated by a trashcan icon, in the drawing panel. 
 
:::image type="content" source="media/geospatial/example-shapes.png" alt-text="Screenshot of the map component with sample shapes and labels, with the trashcan icon and label panel highlighted.":::

## Import GeoJSON shapes into the map component

If you already have shapes defined in GeoJSON format, you can import them directly into your map. For example, you might have an existing shape that defines a specific geographical area or sales district that you want to highlight on the map.

In your dataset, you’ll need three columns, as defined in the following table:

Column description | Maps to property | Required
--|--
Column with the shape’s GeoJSON coordinates | **ShapeGeoJSONObjects** | Required
Column with the shape’s label | **ShapeLabels** | Optional
Column with the shape’s color | **ShapeColors** | Optional

1.	Under View tab, connect the Canvas app with the desired GeoJSON dataset. 

2.	In the **Advanced** properties pane, enter the GeoJSON dataset in the **Shapes_Items** field. In this example, we are using *Seattle1* as our dataset. 

3.	Bind the **ShapeGeoJSONObjects** column with geoJSON column in the dataset. 

4.	Bind the **ShapeLabels** and **ShapeColors** columns with the appropriate label and colors columns in the dataset. 
 
    :::image type="content" source="media/geospatial/custom-geojson-shape.png" alt-text="Screenshot of the advanced properties pane showing dataset fields filled in and the resulting custom shapes on the map.":::


## Measurement outputs from shapes drawn (Preview)

You can show the length of the perimeter (in feet) and volume of the area (square feet) of a selected shape in your app.

1. In your app, open the **Insert** tab, and expand **Display**.

2. Select the **Text label** component to insert a label. Adjust the size as you see fit.

3.	On the **Properties** pane, add *[Map].SelectedShape.Area* or *[Map].SelectedShape.Perimeter* in the **Text** field to display the area and perimeter of selected shape in the map component. 


In the following example we used multiple text labels to display both the area and perimeter of the selected shape.
 
:::image type="content" source="media/geospatial/measurement-display.png" alt-text="Screenshot of a map with two text labels next to it showing the area and perimeter measurements.":::




## Other interactive map features


- [Use data from Excel to insert pins](geospatial-map-excel.md)
- [Add info cards to pins](geospatial-map-infocards.md)


## Other geospatial components

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** component.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]