<properties
	pageTitle="Create and add line charts, pie charts, and bar charts in PowerApps | Microsoft PowerApps"
	description="Add and configure collections, add columns to existing collections in your PowerApps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/27/2016"
   ms.author="mandia"/>

# Show data in a line, pie, or bar chart in your app
Use line charts, pie charts, and bar charts to display your data. When working with charts, the data that you import should be structured like the following:

- Each series should be in the first row
- Labels should be in the leftmost column


For example, your data should look similar to the following:  
![][9]

You can create and use these charts within PowerApps. Let's get started.

## Prerequisites
- [Sign up](signup-for-powerapps.md) for PowerApps and [install](http://aka.ms/powerappsinstall) PowerApps. When you open PowerApps, sign-in using the same credentials that you used to sign up.
- Create an app from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md).
- Learn how to [configure a control](add-configure-controls.md) in PowerApps.
- These steps use the [ChartData.zip](http://pwrappssamples.blob.core.windows.net/samples/ChartData.zip) file as sample input data. The zip file includes an XML file that can be converted to Excel. Otherwise, PowerApps automatically reads the files in the .zip files and imports it successfully. You can download and use this sample data, or import your own. 

## Add a pie chart to display your data
In these steps, we download a sample file. Using a collection, we import this sample data and display it in a pie chart and a column chart.

1. Download the [ChartData](http://pwrappssamples.blob.core.windows.net/samples/ChartData.zip) zip file.
2. Create a collection named **ProductRevenue** using the following steps:  

	1. On the **Insert** tab, select **Controls**, and then select **Import**:  
	![][11]  
	2. Set the **OnSelect** property to the following function:  
```Collect(ProductRevenue, Import1.Data)```  
	3. Double-click the **Import Data** button to open Windows Explorer. Select *ChartData.zip*, and select **Open**.  
	In the **File** menu, select **Collections**. The ProductRevenue collection is listed with the chart data you imported:  
	![][1]  

	> [AZURE.NOTE] The import control is used to import Excel-like data and create the collection. The import control imports data when you are creating your app, and previewing your app. Currently, the import control does not import data when you publish your app.

3. Go back to your designer.
4. On the **Insert** tab, select **Charts**, and then select **Pie Chart**. Click-and-drag to move the pie chart under the **Import data** button.
5. In the pie chart control, select the middle of the pie chart:   
![][10]  
6. Set the **Items** property of the pie chart to the ```ProductRevenue.Revenue2014``` collection you created:  
![][2]  

	When you do this, the pie chart shows the 2014 revenue of the products:  
![][3]  

## Add a bar chart to display your data
Now, let's use this ProductRevenue collection in a bar chart:

1. On the **Home** tab, create a new screen.
2. On the **Insert** tab, select **Charts**, and then select **Column Chart**.
3. Select the middle of the column chart. Set the **Items** property of the column chart to ```ProductRevenue```:  
![][12]  

	When you do this, the column chart shows the 2012 revenue for the products:  
![][4]  
4. In the column chart, select the center square:  
![][5]  
5. On the **Chart** tab, select **Number of Series**, and then enter **3** in the Function Bar:  
![][6]  

	The column chart shows revenue data for each product over three years:  
![][7]  

## Tips and Tricks
- At anytime, you can select the Preview button (![][8]) to view your charts, and to see how they look with data.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Select the middle of the column chart. In the property list, you can set the **GridStyle** to All, XOnly, YOnly, and even None.

## What you learned
In this topic, you:

- Used the import control to import sample data in your app.
- Added a pie chart and bar chart to display the data that you imported.
- In the column chart, you used the **Number of Series** property to show data for three years; with each year having its own column.



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