---
title: Show data in a line, pie, or bar chart in canvas apps
description: Learn about how to show categories of data as line charts, pie charts, or bar charts in a canvas app.
author: fikaradz
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/23/2016
ms.subservice: canvas-maker
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - fikaradz
---
# Show data in a line, pie, or bar chart in canvas apps

Use line charts, pie charts, and bar charts to display your data in a canvas app. When you work with charts, the data that you import should be structured based on these criteria:

* Each series should be in the first row.
* Labels should be in the leftmost column.

For example, your data should look similar to the following:

![Data example][9]

You can create and use these charts within Power Apps. Let's get started.

## Prerequisites

* [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.
* Create an app from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md).
* Learn how to [configure a control](add-configure-controls.md) in Power Apps.
* Download [ChartData.zip](https://pwrappssamples.blob.core.windows.net/samples/ChartData.zip), which contains sample data as an XML file. Follow the steps in this topic to import it directly into your app. As an alternative, decompress the .zip file, open the XML file in Excel, and save it to a [cloud-storage account](connections/cloud-storage-blob-connections.md).

## Import the sample data
In these steps, we import the sample data into a collection, named **ProductRevenue**.

1. On the **Insert** tab, select **Controls**, and then select **Import**:  

    ![Insert controls][11]  

2. Set the control's **[OnSelect](controls/properties-core.md)** property to the following function:  

   ```Collect(ProductRevenue, Import1.Data)```

3. Press F5 to open Preview mode, and then select the **Import Data** button.

4. In the **Open** dialog box, select ChartData.zip, select **Open**, and then press Esc.

5. On the **File** menu, select **Collections**.

    The ProductRevenue collection is listed with the chart data you imported:

    ![File - collections][1]  

   > [!NOTE]
   > The import control is used to import Excel-like data and create the collection. The import control imports data when you are creating your app, and previewing your app. Currently, the import control does not import data when you publish your app.
   >

6. Press Esc to return to the default workspace.

## Add a pie chart
1. On the **Insert** tab, select **Charts**, and then select **Pie Chart**.

2. Move the pie chart under the **Import data** button.

3. In the pie-chart control, select the middle of the pie chart:   

    ![Pie chart control][10]

4. Set the **[Items](controls/properties-core.md)** property of the pie chart to this expression: `ProductRevenue.Revenue2014`

    ![Items property][2]  

    The pie chart shows the revenue data from 2014.

    ![Pie chart updated][3]  

## Add a bar chart to display your data
Now, let's use this ProductRevenue collection in a bar chart:

1. On the **Home** tab, add a screen.]

2. On the **Insert** tab, select **Charts**, and then select **Column Chart**.

3. Select the middle of the column chart. Set the **[Items](controls/properties-core.md)** property of the column chart to ```ProductRevenue```:

    ![Items property to ProductRevenue][12]  

    The column chart shows the revenue data from 2012:

    ![Column updated][4]  

4. In the column chart, select the center square:

    ![Select center square][5]

5. On the **Chart** tab, select **Number of Series**, and then enter **3** in the formula bar:

    ![Select number of series and enter 3][6]  

    The column chart shows revenue data for each product over three years:

    ![Updated chart][7]  

[1]: ./media/use-line-pie-bar-chart/productrevenuecollection.png
[2]: ./media/use-line-pie-bar-chart/itemsexpression.png
[3]: ./media/use-line-pie-bar-chart/piechart.png
[4]: ./media/use-line-pie-bar-chart/columnchart.png
[5]: ./media/use-line-pie-bar-chart/columnchartseries.png
[6]: ./media/use-line-pie-bar-chart/columnchartseriesfunction.png
[7]: ./media/use-line-pie-bar-chart/columnchartthreeyears.png
[8]: ./media/use-line-pie-bar-chart/preview.png
[9]: ./media/use-line-pie-bar-chart/tableformat.png
[10]: ./media/use-line-pie-bar-chart/middlepiechart.png
[11]: ./media/use-line-pie-bar-chart/import.png
[12]: ./media/use-line-pie-bar-chart/itemscolumnchart.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]