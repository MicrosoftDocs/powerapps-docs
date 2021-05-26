---
title: Insert pins from data stored in Excel
description: Add customized pins to your map component in Power Apps by using a dataset you've created in Excel.
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


# Use data from Excel to insert pins

You can load a table that contains existing data from an Excel workbook into the map component. The component will then plot each row in your table as a map pin.

## Prerequisites
1. Create a Canvas app and make sure it meets the [Geospatial prerequisites](geospatial-overview.md#prerequisites). 
2. In your app, [insert a map](geospatial-component-map.md#use-the-component). 


## Add pin data from an Excel workbook

Your Excel workbook needs to contain a named table with the following columns that should then be mapped to the associated property in the component's **Advanced** pane.

Column description | Maps to property | Required
-- | -- | --
Label for the pin | ItemsLabels | Required
Longitude of the pin | ItemsLongitudes | Required
Latitude of the pin | ItemsLatitudes | Required
Color of the pin | ItemsColors | Optional
Icon for the pin | ItemsIcons | Optional



The color field accepts any CSS string, as defined in [Color enumeration and ColorFade, ColorValue, and RGBA functions in Power Apps](/functions/function-colors).

You can use the icons described in the [List of image templates](/azure/azure-maps/how-to-use-image-templates-web-sdk#list-of-image-templates) topic as your icon.


The following Excel table shows the required columns:


:::image type="content" source="media/geospatial/sample-excel.png" alt-text="Sample excel file with a table named TestData and containing Name, Longitude, and Latitude columns":::

You can copy the following sample data to test this functionality:

Name | Longitude | Latitude | Color | Icon
-- | -- | -- | -- | --
Fourth Coffee (sample) | -98.29277 | 26.2774 | Blue | marker-flat
Litware, Inc. (sample) | -96.85572 | 32.55253 | #ffefcd| hexagon-thick
Adventure Works (sample) | -96.99952 | 32.72058 | | car
Fabrikam, Inc. (sample) | -118.30746 | 34.86543 | |
Blue Yonder Airlines (sample) | -118.66184 | 34.17553 | |
City Power & Light (sample) | -113.46184 | 37.15363 | |
Contoso Pharmaceuticals (sample) | -80.26711 | 40.19918 | |
Alpine Ski House (sample) | -102.63908 | 35.20919 | |
A Datum Corporation (sample) | -89.39433 | 40.71025 | |
Coho Winery (sample) | -116.97751 | 32.87466 | |




1. Copy and paste the table into a new Excel workbook.

1. Select one of the cells, and then on the Home tab in the ribbon, select **Format as Table** and choose any style, and then **OK**.

    ![Screenshot highlighting the format as table option in Excel](./media/geospatial/convert-table.png)

1. Select the table, and then go to the **Table Design** tab on the ribbon. Enter a name for the table under **Table Name:**, for example *TestData*.

    ![Screenshot highlighting the table name in Excel](./media/geospatial/table-name.png)

1. Save the workbook.

1. Open or create a new app in Power Apps, and insert the map component.

1. On the **Properties** pane, select the **Locations(Items)** field and then search for *excel* and select **Import from Excel**.

    :::image type="content" source="media/geospatial/select-excel.png" alt-text="Screenshot of the Import from Excel option.":::


1. Locate the Excel workbook and then select **Open**. Select the table that contains the information, **TestData**, and then **Connect**.

    ![Screenshot of the table selection panel](./media/geospatial/select-table.png)

1. On the **Properties** pane, go to the **Advanced** tab, and select **More options**.

1. Set the following properties:

    - **ItemsLabels** as *TestData.Name*
    - **ItemLatitudes** as *TestData.Latitude*
    - **ItemsLongitudes** as *TestData.Longitude*
    - (Optional) **ItemsColors** as *TestData.Colors*
    - (Optional) **ItemsIcons** as *TestData.Icons*

1. The map component will now show each row in the table as a pin, labeled with its *Name* as defined in the Excel table, and using the provided icons and colors. If an icon or color isn't provided, then the component will use the default icon and color.

    ![A screenshot of the map component with custom icons and different colors.](./media/geospatial/pins-map.png)



## Other interactive map features

- [Add info cards to pins](geospatial-map-infocards.md)
- [Draw and insert shapes onto maps](geospatial-map-draw-shapes.md)


## Other geospatial components

To see dynamic address suggestions as you type, use the **[Address input](geospatial-component-input-address.md)** component.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]