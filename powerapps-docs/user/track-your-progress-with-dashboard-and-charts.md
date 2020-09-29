---
title: "Track your progress with dashboards and charts in model-driven apps| MicrosoftDocs"
description: How to use charts in Power Apps
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 9/14/2020
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Track your progress with dashboards and charts

A dashboard is made up of a collection of easy-to-read charts and graphs that provide visual representation of filtered app data. The interactive charts and graphs on a dashboard display important data that gives you a 360-degree view of your business and helps you to understand key performance indicators (KPI).

Dashboards are available for all record types. Charts are available on the Dashboard page, Grid page, Associated Home page, and on Edit Form page. 

> [!div class="mx-imgBorder"]
> ![Dashboard](media/dashboard_sample.png "Sample Dashboard") 


## View dashboards

There is two types of dashboards, **System Dashboards** and **My Dashboards**.


![Choose between personal or system dashboard](media/select_dashboard.png "Choose between personal or system dashboard") 

Legend: 
1. **My Dashboards**: My dashboards are personal dashboards that can only be seen by the user who creates them. The user can also share their personal dashboard with other users if the user has sharing privileges for their security role.

2. **System Dashboards**: System dashboards are created by your administrator. By default, these dashboards are visible to all users. 



## Expand, refresh, and view records


![Expand chart view](media/chart_more_button.png "Expand chart view")


Legend:

1. **Expand Chart**: Shows the chart in full screen mode. The chart is still interactive in expanded mode.  
2. **Refresh**: Refreshes the records in the chart.
3. **View Records**: See the chart and the underlying records together. This opens the chart for the corresponding records.
4. **Tool tips**: Hover your mouse over the chart to see a tooltip that provides quick information about that area of the chart.      


## Create a dashboard with charts

1. Go to **Dashboards** and then on the command bar select **New** > **Dynamics 365 Dashboard**. 

   > [!div class="mx-imgBorder"]
   > ![Add a new dashboard](media/add_new_dashboard.png "Add a new dashboard")
   
2. Choose a layout and then select **Create**. This is how your dashboard displays the charts, graphics, and numbers. 

   > [!div class="mx-imgBorder"]
   > ![Choose a dashboard layout](media/dashboard_layout.png "Choose a dashboard layout")
 
3. Type in a name for the dashboard. 

   > [!div class="mx-imgBorder"]
   > ![Name your dashboard](media/name_dashboard.png "Name your dashboard")
   
   
4. Add what you want to each area of your dashboard. For example, let's add a chart. 

   > [!div class="mx-imgBorder"]
   > ![Add a chart](media/insert_chart.png "Add a chart")
 
5. On the **Add Component** dialog box, select your options. 
 
      |  |  |
      | --- | --- |
      | **Record Type** |Select a record.  |
      | **View** |Select a view for the record.  |
      | **Chart** |Select the type of chart that you want use. |


      > [!div class="mx-imgBorder"]
      > ![Add components](media/add_componet_to_dashboard.png "Add components")

 
6. When you're done adding each component, select **Add**.
 

7. Continue adding components to the dashboard. You can add up to six components.   
 
   > [!div class="mx-imgBorder"]
   > ![Add more charts](media/add_more_charts.png "Add more charts")
 
8. When you are done, on the command bar select **Save**. 
 
9. The dashboard that you created will appear in the drop-down menu under **My Dashboards**.

   > [!div class="mx-imgBorder"]
   > ![View your dashboards](media/my_dashboards.png "View your dashboards")


## Edit the properties of a chart

When you add a chart on a dashboard you can edit the chart properties and modify the chart view and display options. The screenshot below shows how a chart will display based on the chart properties that you selected.

   > [!div class="mx-imgBorder"]
   > ![Select a view](media/all_chart_views.png "Select a view on a chart")

Legend:

 1. View title with **View Selector** turned off. You cannot toggle between different views. You only see the title.
 2. Chart title with **Display Chart Selection** turned off. You cannot toggle between different charts for the entity. You only see the title.
 3. Only **View Selector** is turned. You can toggle to a different view and the chart will render based on the underline data for the selected view.
 4. Both **View Selector** and **Display Chart Selection** is turned. You can toggle a different views and chart for the entity


To edit the chart properties, you need to edit the dashboard that the chart is in. If you're in the process of adding a new chart on a dashboard, then you're already in edit mode and can skip to step 2.


1. Go to the dashboard that the chart is in and on the command bar, select **Edit**.


   > [!div class="mx-imgBorder"]
   > ![Edit dashboard](media/edit_dashboard_prop.png "Edit your dashboard")
   
2. Double select the chart that you want to edit. 

   > [!div class="mx-imgBorder"]
   > ![Select the chart to edit](media/select_chart_to_edit.png "Select the chart to edit")

3. On the **Set Properties** dialog box select a **View Selector** option. 

	- **Off**: Do not show view selector, show the view title only.
	- **Show All Views**: Show the view selector on chart and display all views in the view selector.
	- **Show Selected Views**: Show the view selector on chart and display only the selected views in the view selector.
 
   > [!div class="mx-imgBorder"]
   > ![Edit view selector](media/edit_view_selector.png "Edit view selector")

4. Once **View Selector** is turned on, you can select different views, to see how the chart renders with different data associated with the view.

   > [!div class="mx-imgBorder"]
   > ![Select view selector](media/charts_select_views.png "Select view selector")


5. Select the **Display Chart Selection** check box to show the chart selector. When chart selector is enabled, you can toggle to a different chart for the entity and see  different visualizations of the data. If the box is unchecked, then you only see the chart title.

   > [!div class="mx-imgBorder"]
   > ![Display chart selection](media/chart_options_1.png "Display chart selection")

6. When you're done, select **OK**.


## Drill-down in a chart

You can drill-down into a segment on a chart and filter the data for that segment. For example, you can drill-down on one segment of a chart and change the chart type as you drill-down.

The chart drilldown feature is only available on the browser. It is not available on the mobile app for phones or tablets.

In the example below, let's further drill-down into the chart.

1. Select a data point on the chart to bring the **Drill down by** dialog box.

   > [!div class="mx-imgBorder"]
   > ![Drill down by](media/chart_drilldown.png "Select data point on Drill down by dialog box")

2. Select the drop-down menu and choose how to want to group the data.

   > [!div class="mx-imgBorder"]
   > ![Select how to drill down into the chart](media/chart_drilldown_1.png "Select how to drill-down into the chart")
   
3. Select the type of chart that you want to see the drill-down data.

   > [!div class="mx-imgBorder"]
   > ![Select the type of chart](media/chart_drilldown_2.png "Select the type of chart")

4. The chart with the drilled down data will show. The breadcrumb at the top shows the filter criteria of the drilldown. You can select the breadcrumb to go back Home or to the previous screen.

   > [!div class="mx-imgBorder"]
   > ![Drill down showing breadcrumbs](media/chart_drilldown_3.png "Drill down showing breadcrumbs")


You can continue drilling further into the chart data. As you drill-down deeper, the breadcrumb will expand and you can go back to the previous screen or select the Home button to go back to the Home screen.

   ![Drill down further](media/chart_drilldown_4.png "Drill-down further")

## Known issues  
In the chart designer, adding an order by on certain calculated fields is not supported and will cause an error. The calculated fields causing this are using another calculated fields, a related entity field, or a local field on the entity.



