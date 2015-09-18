<properties
	pageTitle="Create and add line charts, pie charts, and bar charts in PowerApps | Microsoft Azure"
	description="Create collections and add columns to existing collections"
	services="power-apps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="power-apps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="" 
   ms.date="09/17/2015"
   ms.author="mandia"/>

# Show data in a line, pie, or bar chart in your app
Use line charts, pie charts, and bar charts to display your data. When working with charts, the data that you import should be structured like the following:

- Each series should be in the first row
- Labels should be in the leftmost column


For example, your data should look similar to the following:  
![][9]

You can create and use these charts within PowerApps. Let's get started.

### Prerequisites 
- Install PowerApps. Create a new app or open an existing app in PowerApps.
- To familiarize yourself with PowerApps and creating apps, step through the [Get Started](get-started-test-drive.md ). It walks you through performing some key tasks, including adding controls.
- These steps use the [ChartData](https://gallery.technet.microsoft.com/Sample-data-for-Show-a-set-5933d4c7) as sample input data. You can use this sample data, or import your own.

## Add a pie chart to display your data
In these steps, we download a sample file. Using a collection, we import this sample data and display it in a pie chart and a column chart. 

1. Download the [ChartData](https://gallery.technet.microsoft.com/Sample-data-for-Show-a-set-5933d4c7) zip file.
2. Create a collection named **ProductRevenue**. Steps include:  
	a) Open your app in PowerApps.
	b) On the **Insert** tab, select **Controls**, and then select **Import**.
	c) Set the **OnSelect** property to the following function:  
```Collect(ProductRevenue, Import1!Data)```  
	d) Select the **Import Data** button to open Windows Explorer. Select *ChartData.zip*, and select **Open**.  

	In the **File** menu, select **Collections**. The ProductRevenue collection is listed with the chart data you imported:    
![][1]  


3. On the **Insert** tab, select **Charts**, and then select **Pie Chart**.
4. Set the **Items** property of the pie chart to **ProductRevenue**:  
![][2]  

	When you do this, the pie chart shows the relative revenue of the products:  
![][3]  
5. On the **Insert** tab, click **Charts**, and then click **Column Chart**.
6. Set the **Items** property of the column chart to **ProductRevenue**:  
![][2]  

	When you do this, the column chart shows the revenue for each product:  
![][4]  
7. In the column chart, select the center square:  
![][5]  
8. On the **Chart** tab, select **Number of Series**, and then enter **3** in the Function Bar:  
![][6]  

	The column chart shows revenue data for each product over three years:  
![][7]  


## Tips and Tricks
- At anytime, you can select the Preview button (![][8]) to view your charts, and to see how they look with data.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- You can set the **X** and **Y** values for your charts.


## Next Steps
[Create and update a collection](create-update-collection.md)

Check out some getting started tutorials:
[Create a PowerFlow from scratch](powerapps-tutorial-blankpowerflow.md) 
[Create an app from scratch](powerapps-tutorial-pcselector.md) 
[Using Templates in PowerApps](powerapps-tutorial-templates.md)


[1]: ./media/use-line-pie-bar-chart/productrevenuecollection.png
[2]: ./media/use-line-pie-bar-chart/itemsexpression.png
[3]: ./media/use-line-pie-bar-chart/piechart.png
[4]: ./media/use-line-pie-bar-chart/columnchart.png
[5]: ./media/use-line-pie-bar-chart/columnchartseries.png
[6]: ./media/use-line-pie-bar-chart/columnchartseriesfunction.png
[7]: ./media/use-line-pie-bar-chart/columnchartthreeyears.png
[8]: ./media/use-line-pie-bar-chart/preview.png
[9]: ./media/use-line-pie-bar-chart/tableformat.png