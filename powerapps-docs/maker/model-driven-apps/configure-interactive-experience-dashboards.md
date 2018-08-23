---
title: "Configure model-driven app interactive experience dashboards in PowerApps | Microsoft Docs"
description: "Know how to configure interactive experience dashboards in PowerApps"
keywords: Interactive dashboards; Customer Service; Microsoft Dynamics 365; Interactive service hub
author: Mattp123
ms.author: matp
manager: kvivek
ms.custom: ""
ms.date: 05/21/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: d1446a95-14bf-4b15-a905-72fce07f4c76
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Configure model-driven app interactive experience dashboards

Interactive experience dashboards can be a one-stop workplace for app users, such as service reps, to see workload information and take action. They're fully configurable, security-role based, and deliver workload information across multiple streams in real time. Interactive dashboard users don't need to page through the application looking for a particular record; they can act on a it directly from the dashboard. 

 The interactive experience dashboards come in two forms: multi-stream and single-stream. In addition, multi-stream dashboards can be home page or entity-specific dashboards. The entity-specific dashboards are configured in a different part of the user interface and partially preloaded with the entity-specific configuration information.  
  
 The multi-stream dashboards display data in real time over multiple data streams. There’s no limit on how many streams you can configure on the dashboard. The data in a stream can be based only on one entity, but, each stream can be based on a different entity. In the entity-specific dashboards, all streams are based on the same entity. The data flows from various views or queues, such as **My Activities**, **My Cases**, or **Cases in the Banking Queue**. 
  
 The single-stream dashboards display real-time data over one stream based on an entity view or queue. The tiles are positioned on the right side of the dashboards and are always shown. The single-stream dashboards are typically helpful to Tier 2 service leads or managers, who monitor fewer, but more complex or escalated cases.  
  
 Multi-stream and single-stream dashboards contain interactive charts that provide a count of relevant records, such as cases by priority or by status. These charts also act as visual filters. The visual filters (interactive charts) are based on multiple entities and in the single-stream dashboards, the entity in the data stream defines the visual filter entity.   
  
 Users can apply additional filtering with global filter and timeframe filter. The global filter works at a field level on all charts, and also on streams and tiles that are based on the filter entity (you specify the filter entity when you configure the visual filters). 
  
> [!NOTE]
>  The interactive dashboards are solution aware and can be exported and then imported into a different environment as a solution. However, the queues that the streams and tiles are based on aren’t solution aware. Before importing the dashboard solution into the target system, the queues have to be manually created in the target system in **Settings** > **Service Management** > **Queues**. After you create the queues, import the dashboard solution to the target system, and then edit the streams or tiles that are based on the queues  to assign the newly created queues appropriately.  
  
 The illustrations in this topic show multi-stream and single-stream dashboards with the header pane. Below the header you see visual filters and streams. In the single-stream dashboard, you also see tiles. For each dashboard type, you can choose from several different layouts that are also shown. The dashboard header contains the following controls and select-able icons, from left to right: dashboard picker, refresh, visual filter icon, global filter icon, and timeframe filter.  
  
### Multi-stream dashboard standard view  
 In the multi-stream dashboard, you see a row of visual filters at the top with the data streams below them.  
 
![Multi-stream interactive dashboard](../model-driven-apps/media/interactive-dashboards-multi-stream.png) 
   
### Multi-stream dashboard tile view  
 The same dashboard, only in the tile view.  
  
 ![Multi-stream dashboard tile view](../model-driven-apps/media/interactive-dashboards-multi-stream-tiles.png "Multi-stream dashboard tile view")  
  
### Multi-stream dashboard layouts  
 For multi-stream dashboards, you can choose from four different layouts.  

 > [!div class="mx-imgBorder"] 
 > ![Multi-stream dashboard layouts](../model-driven-apps/media/interactive-dashboards-multi-stream-layout.png "Multi-stream dashboard layouts")  
  
### Multi-stream entity-specific dashboard  
 The entity-specific dashboard for the `Case` entity is shown here.  
  
 ![Open cases dashboard](../model-driven-apps/media/interactive-dashboard-cases-dashboard.PNG "Open cases dashboard")  
  
### Single-stream dashboard  
 The single-stream dashboard contains the data stream on the left and visual filters and tiles on the right.  
  
 ![Single-stream interactive service hub dashboard](../model-driven-apps/media/interactive-dashboards-single-stream.png "Single-stream interactive service hub dashboard")  
  
### Single-stream dashboard layouts  
 For single-stream dashboards, you can choose from four different layouts.  
 
 > [!div class="mx-imgBorder"] 
 > ![Single-stream dashboard layouts.](../model-driven-apps/media/interactive-dashboards-single-stream-layout.png "Single-stream dashboard layouts.")  
  
<a name="BKMK_Enable"></a>   
## Configure entities, fields, and security roles for the interactive dashboards  
 When you configure interactive dashboards, your first task is to enable entities, fields, and security roles for the interactive experience.  
  
### Entities enabled for interactive experience
 All entities supported in the Unified Interface are enabled for the interactive experience dashboards.
  
### Configure fields  
 For a field to appear in the global filter and be included in the data stream sort, you have to set two flags, as shown in the example below for the **IsEscalated** field of the Case entity.  

 > [!div class="mx-imgBorder"] 
 > ![Enable a field for global filter and sort](../model-driven-apps/media/global-filter-sort-8.png "Enable a field for global filter and sort")  
  
### Configure global filter fields  
 For a field to appear in the global filter, you have to set the **Appears in global filter in interactive experience** flag for this field. The fields that you configure will appear in the global filter flyout window when the global filter icon is clicked on the dashboard header. In the flyout window, the service reps can select the fields on which they want to filter globally, in charts, and also in streams and tiles that are based on the filter entity. For more information about the filter entity see the “Configure multi-stream interactive dashboard” section later in this topic.  
  
 The global filter flyout window is shown here:  
  
 ![Add two global filter fields](../model-driven-apps/media/interactive-dashboards-global-filter-two-fields.png "Add two global filter fields")  
  
> [!NOTE]
>  When you configure a visual filter (interactive chart) based on the fields like priority or status, a best practice is to also enable these fields (priority, status) to appear in the global filter.  
  
The following procedure provides the steps for setting the global filter flag:
  
1. Open [solution explorer](advanced-navigation.md#solution-explorer).  
  
2. Under **Components**, expand **Entities**, and then expand the entity you want. If the entity you want isn't displayed select **Add Existing** to add it.  
  
3.  In the navigation pane, select **Fields** and in the grid, double-click the field you want to enable.  
  
4.  In the **General** tab, select the **Appears in global filter in interactive experience** check box. Select **Save and Close**.  
  
5.  Select **Publish** for your changes to take effect.  
  
6.  Select **Prepare Client Customizations**.  
  
### Configure sortable fields  
 For a field to be used in sorting stream data, you have to set the **Sortable in interactive experience dashboard** flag for this field. The fields that you configure for sorting will appear in the drop-down list in the **Edit Property** flyout dialog when the user selects **More (…)** on the stream header. The following illustration shows the flyout dialog with the list of the available fields for sorting, in the **Sort By** drop-down list. The default sort is always set on the **Modified On** field.  
  
 ![Sort by drop-down list](../model-driven-apps/media/interactive-dashboard-sortable-fields-dropdown.png "Sort by drop-down list")  
  
The following procedure provides the steps for setting the sort flag:
  
1. Open [solution explorer](advanced-navigation.md#solution-explorer).   
2. Under **Components**, expand **Entities**, and then expand the entity you want. If the standard entity you want isn't displayed select **Add Existing** to add it.  
  
3.  In the navigation pane, select **Fields** and in the grid, double-click the field you want to enable.  
  
4.  In the **General** tab, select the **Sortable in interactive experience dashboard** check box. Select **Save and Close**.  
  
5.  Select **Publish** for your changes to take effect.  
  
6.  Select **Prepare Client Customizations**.  
  
### Enable security roles  
 Select and enable security roles that will be able to view the interactive dashboards.  
  
The following procedure provides the steps to enable the security roles for the interactive experience:
  
1. Open [solution explorer](advanced-navigation.md#solution-explorer).  
  
2. Under **Components**, select **Dashboards**.  
  
4.  In the grid, select the interactive dashboard you want and select **Enable Security Roles** on the task bar.  
  
5.  In the **Assign Security Roles** dialog, select the **Display only to these selected security roles** option and select the roles that you want to enable. Select **OK**.  
  
6.  Select **Publish** for your changes to take effect.  
  
7.  Select **Prepare Client Customizations**.  
  
 ![Enable security roles](../model-driven-apps/media/interactive-dashboards-enable-security-roles.png "Enable security roles")  
  
 ![Assign security roles](../model-driven-apps/media/interactive-dashboards-assign-security-roles.png "Assign security roles")  
  
<a name="BKMK_Configure"></a>   
## Configure interactive experience dashboards  
 The following sections describe how to configure various types of the interactive dashboards.  
  
### Configure a multi-stream interactive dashboard using the 4-column layout  
 
1.	Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.	Select **Model-driven** (lower left).  
  
3.  Select **Data** > **Entities** > select the entity you want. 

4.  Select the **Dashboards** tab, and then on the toolbar select **Add dashboard**.  
  
5.  Choose the layout, either 2, 3, or 4 column width.  
  
6.  When the dashboard form opens, fill in the filtering information at the top of form, as shown here.  
 
 > [!div class="mx-imgBorder"] 
 > ![Add visual filters](../model-driven-apps/media/interactive-dashboards-add-visual-filters.png "Add visual filters")  
  
   - **Filter Entity**: The visual filters (interactive charts) and global filter attributes are based on this entity.  
      
    - **Entity View**: The visual filters (interactive charts) are based on this view.  
      
    - **Filter By**: The field that the time frame filter applies to.  
      
    - **Time Frame**: The default time frame filter value for the **Filter By** field.  
      
 After you  have specified the filtering information, start adding components for the charts and the data streams. To add a component, simply select the element in the center of the chart or stream, and when the dialog appears, enter the required information, as shown in the following illustrations.  
  
 Add the **Cases By Priority** doughnut chart.
  
 > [!div class="mx-imgBorder"] 
 > ![Add a doughnut chart component.](../model-driven-apps/media/interactive-dashboards-add-chart-circle.png "Add a doughnut chart component.")  
  
 Some charts, such as bar charts or pie charts, render showing the data stored in the system. The doughnut charts and tag charts load as static images and don’t show the preview of the actual data.  
  
> [!NOTE]
>  The charts configured for the visual filters can use the fields of the **Filter** entity as well as related entities. When you use charts based on related entity fields, the customer service representatives can filter charts using these related entity fields. The fields that are based on the related entity usually have the following format in the chart configuration window: “field name (entity name)”, such as the **Modified By (Delegate)** field. To create multi-entity charts, you must add  fields of a related entity to any of the views, and then use these fields while creating charts.  
 
 > [!div class="mx-imgBorder"] 
 > ![Creating charts for visual filters](../model-driven-apps/media/interactive-dashboard-visual-charts-x-y-axes.PNG "Creating charts for visual filters")  
  
 Next, configure the streams. Just like with adding components in the charts, select the element inside the stream panel. When the dialog appears, select **View** or **Queue** depending on what element you want the stream to use. Enter the required information, as shown in the following illustrations.  
  
> [!NOTE]
>  The **Queue** option is available in the dialog box only for queue-enabled entities. For entity dashboards, if the entity is not queue enabled, you won't see the **Queue** option in the dialog box. You can only use the **View option** in the stream of dashboards for entities that are not queue enabled.  
  
 Configure the stream for the **Items available to work on** as shown here:  
  
 ![Add a stream of my active cases.](../model-driven-apps/media/interactive-dashboards-add-stream-case.png "Add a stream of my active cases.")  
  
 The following illustration is an example of the chart panel, left to right: doughnut chart, tag chart, and bar chart:  
 
 > [!div class="mx-imgBorder"] 
 > ![All interactive charts](../model-driven-apps/media/interactive-dashboards-add-all-charts.png "All interactive charts")  
  
 This illustration is an example of the stream panel with several streams:  
 
 > [!div class="mx-imgBorder"] 
 > ![Add all streams](../model-driven-apps/media/interactive-dashboards-add-all-streams.png "Add all streams")  
  
 After you have completed configuring the dashboard, save it and publish the customizations for your changes to take effect. Also, make sure to select **Prepare Client Customizations**.  
  
#### Edit or delete individual streams of an existing dashboard  
  
1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).   
  
2. Select **Model-driven** (lower left), **Data** > **Entities** > select the entity you want. Select the **Dashboards** tab.  
  
     -OR-  
   
   Open [solution explorer](advanced-navigation.md#solution-explorer), and then under **Components** select **Dashboards**.
  
3.  In the grid, select the interactive dashboard that you want to edit to open it.  
  
4.  Select the stream that you want to edit to select it, and then select **Edit Component**.  
  
5.  Depending on whether you want to add a view or queue to the stream, select the view or queue details for the stream, and then select **Set**.  
  
6.  Select **Save**.  
  
 You can also delete an individual stream from a dashboard. To do this, select the stream, and then on the command bar, select **Delete**.  
  
### Configure an entity-specific dashboard  
 An entity-specific dashboard is a multi-stream dashboard. Configuring this dashboard is similar to configuring a home page multi-stream dashboard, but you do it in the different place in the UI and there are other minor differences. For example, instead of selecting an entity, some fields in the entity-specific dashboard are preset to the entity for which you are creating the dashboard.  
  
1.	Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.	Select **Model-driven** (lower left).  
  
3.  Select **Data** > **Entities** > select the entity you want. 

4.  Select the **Dashboards** tab, and then on the toolbar select **Add dashboard**.  
  
5.  Choose the layout, either 2, 3, or 4 column width.    
  
6.  When the dashboard form opens, the **Filter Entity** is preset to the entity for which you are creating the dashboard. The **Entity View** drop-down list contains the available views for the entity. Select the view and fill in the rest of the required information on the page.  
  
 The rest of the setup is very similar to the home page multi-stream dashboard setup described in the previous section.  
  
### Configure a single-stream dashboard  
 Configuring a single-stream dashboard is similar to the multi-stream dashboard. All UI navigation steps are the same as for the multi-stream dashboard. You can choose a layout that includes tiles or the layout that doesn’t include tiles. If the tiles are included, they are always displayed on the dashboard. To configure a tile, you select the icon in the center of the tile. When the **Add Tile** window opens, fill in the required data. The following illustration is an example of the tile setup.  
  
 ![Add a tile to the single-stream dashboard](../model-driven-apps/media/interactive-dashboard-add-tile-single-stream.png "Add a tile to the single-stream dashboard")  
  
<a name="BKMK_ConfigureColors"></a>   
## Configure dashboard colors  
 For all **Option Set** and **Two Options** type fields, such as the **Case Type**, **IsEscalated** or **Priority** of the `Case` entity, you can configure a particular color that will appear in the charts and streams for specific field values. For example, high priority cases can be shown in red, medium priority cases in blue, and low priority cases in green in the interactive charts. In the streams, there will be a thin vertical line in color next to the work item description.  
  
> [!NOTE]
>  The color coding isn’t available for the tag charts and doughnut charts. These charts appear on the dashboard in white, gray, and black shades.  
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer).  
2.  Under **Components**, expand **Entities**, and then expand the entity you want. If the entity you want isn't displayed select **Add Existing** to add it.  
  
3.  In the navigation pane, select **Fields**. In the grid, double-click the field that you want to configure the color for.  
  
4.  In the **General** tab, in the **Type** sub-area, select **Yes** and then select **Edit**.  
  
5.  When the **Modify List Value** dialog appears, set the new value in the **Color** text box. Select **OK**.  
  
     Select **Save and Close**.  
  
7.  Select **Publish** for your changes to take effect.  
  
In the following example, we’re changing the color for the **IsEscalated** field. Use the **Edit** button to open the **Modify List Value** dialog box:  
 
 > [!div class="mx-imgBorder"] 
 > ![Change color in the dashboard](../model-driven-apps/media/interactive-dashboards-change-color-edit-button.PNG "Change color in the dashboard")  
  
When the **Modify List Value** dialog box opens, choose the color as shown here:  
  
 ![Modify the dashboard color](../model-driven-apps/media/interactive-dashboards-modify-color-value.png "Modify the dashboard color")  
  
### Next steps  
 
[Create or edit dashboards](create-edit-dashboards.md)
 

