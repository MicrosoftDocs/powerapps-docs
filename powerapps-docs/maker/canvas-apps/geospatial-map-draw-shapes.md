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
ms.subservice: canvas-maker
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - iaanw
---


# Draw and insert shapes in the map component (Preview)

[!INCLUDE[Preview disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can add a drawing panel to your interactive maps that lets your users draw and label shapes in the app.

You can also create and label shapes on maps you insert into your Power Apps app with the interactive map component.

Inserting pre-defined shapes is useful to highlight specific regions or areas of interest, such as a sales district or shipping zone.

:::image type="content" source="media/geospatial/custom-geojson-shape-example.png" alt-text="Screenshot of map with example shapes drawn and labeled.":::

## Prerequisites
1. Create a Canvas app and make sure it meets the [Geospatial prerequisites](geospatial-overview.md#prerequisites). 

2. In your app, [insert a map](geospatial-component-map.md#use-the-component). 

## Draw and label shapes on interactive maps
To draw and label shapes on maps, you first need to enable the following settings:

1. Open the **Properties** pane with a map selected.

2. Switch the toggles to **On** for the following settings:
    -  **(Preview) Enable Shape Drawing**
    - **(Preview) Enable Shape Deleting and Label Editing**
 
 
    :::image type="content" source="media/geospatial/enable-feature.png" alt-text="Screenshot of the properties pane the features turned to On.":::

You will now see the drawing panel on the top left corner of the map component. The panel consists of three tools:

- A polygon drawing tool that allows you to create freeform custom shapes, indicated by a square icon with a broken top.
- A square drawing tool that lets you draw squares and rectangles, indicated by a square icon.
- A circle drawing tool that lest you draw circles and ovals, indicated by a circle icon.

:::image type="content" source="media/geospatial/drawing-panel.png" alt-text="Screenshot of the map component, with the drawing panel highlighted.":::

>[!NOTE]
>When you've finished drawing a freeform custom shape, double-click to indicate the last point in the shape.

Drawn shapes are automatically labeled. To change the labels, enter the new name for the label in label editing bar on the top right corner of the map. 

To delete a shape, select it, then select the Delete button, indicated by a trashcan icon, in the drawing panel. 
 
:::image type="content" source="media/geospatial/example-shapes.png" alt-text="Screenshot of the map component with sample shapes and labels, with the trashcan icon and label panel highlighted.":::

## Import GeoJSON shapes into the map component

If you already have shapes defined in GeoJSON format, you can import them directly into your map. For example, you might have an existing shape that defines a specific geographical area or sales district that you want to highlight on the map.

The GeoJSON string for each shape in the dataset needs to be in [the correct format](https://en.wikipedia.org/wiki/GeoJSON), within a single cell.

To import shapes, you first connect your dataset in the map component, and then refer to the appropriate dataset columns, as in the following screenshot example:

:::image type="content" source="media/geospatial/custom-geojson-shape.png" alt-text="Screenshot of the advanced properties pane showing dataset fields filled in and the resulting custom shapes on the map.":::


In your dataset, you'll need three columns, as defined in the following table:

Column description | Maps to property | Required
--|--
Column with the shape's GeoJSON coordinates in [the correct format](https://en.wikipedia.org/wiki/GeoJSON) | **ShapeGeoJSONObjects** | Required
Column with the shape's label | **ShapeLabels** | Optional
Column with the shape's color | **ShapeColors** | Optional

You will also need the name of the dataset. If you're using an Excel workbook as the dataset source, this is the name of the table that contains the data.

The following screenshot shows how the data might look in an Excel workbook:


:::image type="content" source="media/geospatial/custom-geojson-shape-excel.png" alt-text="Screenshot of an excel table with a GeoJSON column.":::


You can copy the following sample data into an Excel workbook to test this feature. 

1. Copy the following data into an Excel workbook, name the table, and then connect the workbook as a dataset, similar to how it is described in the [Use data from Excel to insert pins](geospatial-map-excel.md#add-pin-data-from-an-excel-workbook) topic.

    County | GeoJSON | TotalCases | Color
    --| -- | -- | --
    Adams | {"type":"FeatureCollection","properties":{"kind":"state","state":"WA"},"features":[{"type":"Feature","properties":{"kind":"county","name":"Adams","state":"WA"},"geometry":{"type":"MultiPolygon","coordinates":[[[[-118.9503,47.2640],[-117.9590,47.2586],[-117.9699,46.8697],[-118.0466,46.7711],[-118.2109,46.7383],[-119.2132,46.7383],[-119.3720,46.7383],[-119.3665,46.9135],[-118.9832,46.9135],[-118.9777,47.2640]]]]}}]} | 1689 | RGB(184,210,232)
    Asotin | {"type":"FeatureCollection","properties":{"kind":"state","state":"WA"},"features":[{"type":"Feature","properties":{"kind":"county","name":"Asotin","state":"WA"},"geometry":{"type":"MultiPolygon","coordinates":[[[[-117.0388,46.4261],[-117.0607,46.3549],[-116.9841,46.2946],[-116.9676,46.2015],[-116.9238,46.1687],[-116.9841,46.0920],[-116.9183,45.9934],[-117.4825,45.9989],[-117.4825,46.1194],[-117.4222,46.1194],[-117.4222,46.3823],[-117.2305,46.4096],[-117.2305,46.4644],[-117.1977,46.4206]]]]}}]} | 1096 | RGB(184,210,232)
    Benton | {"type":"FeatureCollection","properties":{"kind":"state","state":"WA"},"features":[{"type":"Feature","properties":{"kind":"county","name":"Benton","state":"WA"},"geometry":{"type":"MultiPolygon","coordinates":[[[[-119.8759,46.6287],[-119.6240,46.6452],[-119.5144,46.7273],[-119.4542,46.6780],[-119.2680,46.5192],[-119.2680,46.2727],[-119.0434,46.1906],[-118.9448,46.0756],[-118.9393,46.0263],[-118.9886,45.9989],[-119.1256,45.9332],[-119.4323,45.9167],[-119.5692,45.9277],[-119.6678,45.8565],[-119.8704,45.8346],[-119.8649,46.0427],[-119.8759,46.6287]]]]}}]} | 13111 | RGB(13,106,191)
    Chelan | {"type":"FeatureCollection","properties":{"kind":"state","state":"WA"},"features":[{"type":"Feature","properties":{"kind":"county","name":"Chelan","state":"WA"},"geometry":{"type":"MultiPolygon","coordinates":[[[[-120.7029,48.5292],[-120.6536,48.5347],[-120.6262,48.4964],[-120.6646,48.4471],[-120.6481,48.3978],[-120.5605,48.3704],[-120.5879,48.3211],[-120.5112,48.3101],[-120.3524,48.2170],[-120.3633,48.1568],[-120.3250,48.1294],[-120.1443,48.0637],[-120.1443,48.0363],[-120.0895,48.0199],[-120.0512,47.9596],[-119.8704,47.9596],[-119.9964,47.7789],[-120.2100,47.7515],[-120.1990,47.6803],[-120.2374,47.5872],[-120.3031,47.5215],[-120.3195,47.4557],[-120.2921,47.4010],[-120.0895,47.3407],[-120.0950,47.2640],[-120.3907,47.2586],[-120.5276,47.3352],[-120.5605,47.3079],[-120.8015,47.4229],[-120.9165,47.4284],[-121.1137,47.5981],[-121.1301,47.6748],[-121.0644,47.7132],[-121.1192,47.7789],[-121.0699,47.8282],[-121.1520,47.8446],[-121.1739,47.8884],[-121.1630,47.9541],[-121.1192,47.9980],[-121.1520,48.0418],[-121.0151,48.0746],[-120.9439,48.1130],[-120.9548,48.1513],[-120.9056,48.1623],[-121.0041,48.2937],[-121.0699,48.3156],[-121.0425,48.3485],[-121.0644,48.3923],[-121.0370,48.4306],[-121.0480,48.4854],[-120.8563,48.5511],[-120.7851,48.5073]]]]}}]} | 5324 | RGB(112,187,255)

1. Bind the columns in the dataset as indicated in this table:

    Map component field | Column in sample data
    -- | --
    ShapeGeoJSONObjects | GeoJSON
    ShapeLabels | County
    ShapeColors | Color

The map will now highlight four counties in Washington state in the US, with different colors. The following screenshot shows how this appears with all counties filled in:

:::image type="content" source="media/geospatial/cusotm-geojson-counties.png" alt-text="Screenshot of an app with a map that highlights the various counties of Washington state in the US.":::


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
