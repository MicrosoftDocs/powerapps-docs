---
title: "Tutorial to add or edit model-driven app components with Power Apps | MicrosoftDocs"
description: "Use the Power Apps app designer to add or edit components"
keywords: ""
ms.date: 03/05/2020
ms.service: powerapps
ms.custom: 
ms.topic: tutorial
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.assetid: be93b9d7-f1c2-4ee7-8d7c-0f5c34dfa5f7
ms.author: matp
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 17
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add or edit model-driven app components in the Power Apps app designer

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In this tutorial you learn how to add components to and remove components from a model-driven app. 

A model-driven app is composed of various components. You can add two types of components to an app: components and table assets. In the context of the app designer, tables, dashboard, and business process flows are all components of an app. Table assets consist of forms, views, charts, and dashboards.  
  
The app designer refers to existing metadata in the default solution. You can use it to create components like forms, views, charts, and dashboards.  
  
## App designer layout  
 The app designer has two main areas. On the left side is the canvas where you add app components.  
  
 > [!div class="mx-imgBorder"]
 > ![App designer canvas.](../model-driven-apps/media/app-designer-canvas-pane.png "App designer canvas")

 On the right side are tabs that you'll use to select components and set component properties.  
 
 > [!div class="mx-imgBorder"]
 > ![App designer components.](../model-driven-apps/media/app-designer-canvas-components-tab.png "App designer components")  
  
 On the canvas, you'll see areas for the site map, business process flow, dashboard, and tables. When you select a dashboard or business process flow, or configure a site map, the app designer automatically adds the tables that are used in these components to the canvas. After the tables are in place, all you need to do is select each table and add required table assets such as forms, views, and charts to it.
 
 You can also use **Search Canvas** to search for components on the canvas. When you select **Search Canvas**, a new search tab opens to the right of the tabs in the rightmost pane.   
 
 > [!div class="mx-imgBorder"]
 > ![Canvas search option.](media/app-designer-search-tab.png "Canvas search")

## Open an app
1. Sign in to [Power Apps](https://make.powerapps.com/). 

2. Select an existing model-driven app. For information about how to create an app, see [Create or edit a model-driven app by using the app designer](create-edit-app.md#create-an-app).

## Add or edit a site map

Before you can add app components to a newly created app, a site map must be defined. More information: [Create a model-driven app site map using the site map designer](create-site-map-app.md)

## Add a component 

 When you add a dashboard or business process flow to an app, the tables they use are automatically added to the app. When you add a table, the tiles for its assets are automatically added. There are two ways you can add components to the designer canvas: by using the **Add** button  ![Add button on the designer.](../model-driven-apps/media/dynamics365-designer-addbutton.PNG "Add button on the designer") on the command bar or by using the tiles on the **Components** tab.  
  
 Here are the steps for adding a dashboard to the app. Use the same steps to add a business process flow or table.  
  
1.  On the app designer canvas, select the **Dashboards** tile.  
  
     On the app designer canvas, the rightmost pane shows you dashboards that are available in the default solution.  
  
    > [!TIP]
    >  Alternatively, you can also do one of the following:  
    >   
    > - Select **Add** ![Add button on the designer.](../model-driven-apps/media/dynamics365-designer-addbutton.PNG "Add button on the designer"), and then select **Dashboards**.  
    > - On the **Components** tab, under **Artifacts**, select **Dashboards**.  
  
2.  In the **search** box, type a few keywords for the dashboard name you're looking for.  
  
     The dashboard list will be filtered to show results that match your keywords.  
  
3.  If you want your users to use only selected dashboards, select the check box for the dashboards you want to add. You can select from the following types of dashboards:
    - **Classic Dashboards** appear on both the web app and the Unified Interface app.
    - **Interactive Dashboards** appear only on the Unified Interface app. If you have selected the client type for the app as web app, the **Interactive Dashboards** option will not be displayed.

     Those dashboards will be added to the **Dashboard** tile on the app designer canvas. The **Dashboard** tile also shows a count of the number of dashboards you added to the app. If you don't select a dashboard, **All** will appear instead of the dashboard count, and all dashboards will be available to users when they use the app.  
  
     All tables the dashboard uses are also added to the **Entity View** area. For example, if you add the Customer Service Manager dashboard, the Case, Entitlement, and Queue Item tables are added to the Table View area. For each table, tiles for its assets are also added. You can use these tiles to add forms, views, and charts. More information: [Add or edit app components in the Power Apps app designer](add-edit-app-components.md#bkmk_AddEntityAssets)   
  
    > [!div class="mx-imgBorder"]
    > ![Add table to the app designer canvas.](../model-driven-apps/media/add-entity-app-designer-canvas.png "Add a table to the app designer canvas")  
  
4.  If the dashboard you want doesn't exist in the default solution, create a dashboard by selecting **Create New** on the **Components** tab to the right of the canvas.  
  
     > [!div class="mx-imgBorder"]
     > ![Create New link on the Components tab of app designer.](../model-driven-apps/media/app-designer-components-tab-create-new.png "Create New link on the Components tab of the app designer")  
  
     The dashboard designer opens. More information: [Create and edit dashboards](create-edit-dashboards.md)  
  
    > [!NOTE]
    > - When you're adding a business process flow or table, the **Create New** option opens the corresponding designer. To learn more about creating business process flows or tables, see [Create a business process flow](/flow/create-business-process-flow) and  [Create a custom table](../data-platform/data-platform-create-entity.md).  
      
  
5.  When you're done adding components, on the command bar, select **Save**.  
  
<a name="bkmk_AddEntityAssets"></a>   
## Add table assets (forms, views, charts, or dashboards)  
 With the components in place, you can start adding table assets like forms, views, charts, and dashboards to the app.
 Additionally, if you're using the Unified Interface client, you can also add table dashboard assets to the app.  
  
 This section describes the steps for adding a form to the app. Use the same steps to add a view or chart to the app.  
  
1.  On the app designer canvas, select the **Forms** tile for the table you want to add a form to.  
  
     On the app designer canvas, the entire row for the table is selected. On the right side, you'll see all existing forms for the selected table.  
  
    > [!NOTE]
    >  Alternatively, you can also do one of the following:  
    >   
    > - Select **Add** ![Add button on the designer.](../model-driven-apps/media/dynamics365-designer-addbutton.PNG "Add button on the designer"), and then select **Forms**.  
    > - On the **Components** tab, under **Entity Assets**, select **Forms**.  
  
    > [!TIP]
    >  For all tables selected for the app, a **More Options** button (**...**) appears in the **Select Entities** list on the **Components** tab. To add all assets for the selected table, select **More Options** (**...**), and then select **Add All Assets**.  
  
2.  If you want your app users to use only selected forms, select the check boxes for the forms you want to add. The forms define how users will see and interact with data in the app. 
 
     The form tile of the selected table will display the number of forms added.  
  
     ![Form tile for case table.](../model-driven-apps/media/add-forms-entity.png "Form tile for case table")  
  
     For example, if you don't select any form for a table, all the forms for that table will be displayed to end users while they use the app. This behavior is similar for views and charts also, if no view or chart is selected. This helps to create apps quickly when you need to work with all available components; there's no need to select each component during app design.  

     If no dashboards or business process flows are selected, all the dashboards and business process flows will be available for users while they use the app.
  
    > [!NOTE]
    > For the app to run, each table that you add must have at least one active form. If you've selected multiple forms, the first active form that appears in the default solution will be used when users run the app.  
  
3.  If you want to add a new form that's not available in the list, select **Create New**.  
  
     In the drop-down list, select the type of form you want to create.  
  
    > [!NOTE]
    >  The drop-down list is available only when you're adding forms. It isn't available for views and charts.  
  
     The form designer opens. More information: [Create and design forms](create-design-forms.md)  
  
     When you're adding a view or a chart, the **Create New** option opens the corresponding designer. More information: [Understand views](create-edit-views.md) and [Create or edit a system chart](create-edit-system-chart.md)  
  
    > [!NOTE]
    >  When you're adding a view, you can reference only public views that are listed under the **Views** node in the solution explorer.  
  
4. Select the down arrow ![Drop down icon.](../model-driven-apps/media/drop-down-icon.png "down arrow") to expand the tile and see a list of forms that have been added.  
  
     ![Form tile expanded in app designer.](../model-driven-apps/media/app-designer-expanded-form-tile.png "Form tile expanded in the app designer")  
  
5.  Repeat these steps to add table views and charts to the app.  
  
6.  Select **Save**.  
  
## Edit or remove components  
  
- To edit a dashboard or a business process flow, select the down arrow ![Drop down icon.](../model-driven-apps/media/drop-down-icon.png "down arrow") to expand the tile, and then select the site map designer button ![Open Site Map Designer button.](../model-driven-apps/media/dynamics365-open-designer.PNG "Open Site Map Designer button") corresponding to the dashboard or business process flow that you want to edit.  
  
     The designer for the selected artifact opens.  
  
- To remove a dashboard or a business process flow, select the down arrow ![Drop down icon.](../model-driven-apps/media/drop-down-icon.png "down arrow") to expand the tile, and then select the dashboard or business process flow that you want to remove. On the command bar, select **Remove**.  

    Another way to remove a dashboard or business process flow is by clearing the corresponding check box on the **Components** tab.
  
- To edit or remove a table, select the table tile, and then on the command bar, select **Edit** or **Remove**. When you edit a table, the solution explorer opens, where you can make changes to the table.  
  
     Another way to remove a component is to select the dashboard, business process flow, or table tile. On the **Components** tab, clear the check boxes for the components you want to remove from the designer.  
  
    > [!NOTE]
    >  When you make any changes to a table&mdash;like changing a table display name or description&mdash;the changes don't appear in the app designer unless the changes are published in the solution explorer.  
  
## Edit or remove table assets  

### Edit table assets
  
1. Select the down arrow ![Drop down icon.](../model-driven-apps/media/drop-down-icon.png "down arrow") to expand the tile for forms, views, charts, or dashboards.  
  
2. Select the form, view, chart, or dashboard that you want to edit.  
  
3. On the command bar, select **Edit**.

   or

   Select the site map designer button ![Open Site Map Designer button](../model-driven-apps/media/dynamics365-open-designer.PNG "Open Site Map Designer button") corresponding to the form, view, chart, or dashboard.  

### Remove table assets  

1. Select the down arrow ![Drop down icon](../model-driven-apps/media/drop-down-icon.png "down arrow") to expand the tile for forms, views, charts, or dashboards.  
  
2. Select the form, view, chart, or dashboard that you want to edit.

3. On the command bar, select **Remove**. 

Alternatively, you can select the forms, views, charts, or dashboards tile, and then on the **Components** tab, clear the check boxes for the assets you want to remove from the designer.  
  
## Next steps  
 [Create a site map for an app](create-site-map-app.md) </br>  
 [Validate and publish an app](validate-app.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]