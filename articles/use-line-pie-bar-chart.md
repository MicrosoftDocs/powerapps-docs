<properties
	pageTitle="Create and add line charts, pie charts, and bar charts in PowerApps | Microsoft Azure"
	description="Create collections and add columns to existing collections"
	services=""
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
   ms.date="11/02/2015"
   ms.author="mandia"/>

# Show data in a line, pie, or bar chart in your app
Use line charts, pie charts, and bar charts to display your data. When working with charts, the data that you import should be structured like the following:

- Each series should be in the first row
- Labels should be in the leftmost column


For example, your data should look similar to the following:  
![][9]

You can create and use these charts within PowerApps. Let's get started.

### Prerequisites
- Install [PowerApps Studio](http://aka.ms/powerappsinstall). Create a new app or open an existing app in PowerApps. 
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).
- These steps use the [ChartData](https://gallery.technet.microsoft.com/Sample-data-for-Show-a-set-5933d4c7) as sample input data. You can use this sample data, or import your own.

## Add a pie chart to display your data
In these steps, we download a sample file. Using a collection, we import this sample data and display it in a pie chart and a column chart.

1. Download the [ChartData](https://gallery.technet.microsoft.com/Sample-data-for-Show-a-set-5933d4c7) zip file.
2. Create a collection named **ProductRevenue**. Steps include:  
	a) On the **Insert** tab, select **Controls**, and then select **Import**.  
	b) Set the **OnSelect** property to the following function:  
```Collect(ProductRevenue, Import1!Data)```  
	c) Double-click the **Import Data** button to open Windows Explorer. Select *ChartData.zip*, and select **Open**.  

	In the **File** menu, select **Collections**. The ProductRevenue collection is listed with the chart data you imported:    
![][1]  

3. Go back to your designer.
4. On the **Insert** tab, select **Charts**, and then select **Pie Chart**. Click-and-drag to move the pie chart under the **Import data** button. 
4. In the pie chart control, select the middle so the pie chart circle is selected:   
![][10]  
5. Set the **Items** property of the pie chart to **ProductRevenue**:  
![][2]  

	When you do this, the pie chart shows the revenue of the products:  
![][3]  

Now, let's use thie ProductRevenue collection in a bar chart: 

1. On the **Home** tab, create a new screen.
2. On the **Insert** tab, select **Charts**, and then select **Column Chart**. 
3. Select the middle of the column chart. Set the **Items** property of the column chart to **ProductRevenue**:  
![][2]  

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
