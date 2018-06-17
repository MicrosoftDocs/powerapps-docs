---
title: "Create or edit dashboards | MicrosoftDocs"
ms.custom: ""
ms.date: 05/23/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 641885d2-4a08-41b8-b914-d9a244e4d5b1
caps.latest.revision: 10
ms.author: "matp"
manager: "kvivek"
---
# Create or edit dashboards

There are two types of dashboards, user dashboards and system dashboards. An app user can create a dashboard visible only to them in the app areas that they have privileges to. An admin or customizer creates or customizes system dashboards that, when published, are visible to all app users. A user can choose to set their user dashboard as their default dashboard and override the system dashboard. This topic focuses on system dashboards.  
  
<a name="BKMK_createdashboard"></a>   
## Create a new dashboard  
  
1.  On the [PowerApps](https://web.powerapps.com) site select **Model-driven** (lower left of the navigation pane).

    ![Model-driven design mode](media/model-driven-switch.png)

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).   
  
2. Expand **Data**, select **Entities**, select the entity that you want base the dashboard on, such as the **Account** entity, and then select the **Dashboards** tab. 

3. On the toolbar select **Add a dashboard**, and then choose a 2, 3, or 4 column layout.  
  
4.  In the **Dashboard: New** dialog box enter a name for the dashboard.  
  
5.  Select one of the component areas and then select the icon for a chart or a list.  
  
     You can have up to six components in the dashboard.  
  
6.  For example, to add a chart, in the **Add Component** dialog box, select values for **Record Type**, **View**, and **Chart**, and then select **Add** to add the chart to the dashboard.  
  
7.  When you are finished adding components to your dashboard, select **Save** and then **Publish**.  
  
<a name="BKMK_editdashboard"></a>   
## Edit an existing dashboard  
  
1. On the [PowerApps](https://web.powerapps.com) site select **Model-driven** (lower left of the navigation pane).

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).    
  
2. Expand **Data**, select **Entities**, select the entity that you want base the dashboard on, such as the **Account** entity, and then select the **Dashboards** tab.  

3. Open a dashboard, select one of the component areas, and then on the toolbar select **Edit Component**.  
  
4.  In the **Set Properties** dialog box, you can make changes to a chart or list such as change the entity, default view, add a chart selector, or make the dashboard available on the mobile apps. When you’re done, select **Set**.  
  
     For more information about setting dashboard component properties, see [Set properties for a chart or list included in a dashboard](set-properties-chart-list-included-dashboard.md).  
  
4.  When you’ve completed your changes be sure to save them, and then publish them.  
  
 Additional system dashboards tasks you can perform include:  
  
-   Remove a list or chart from a dashboard  
  
-   Add a list or chart to a dashboard  
  
-   Set the default dashboard  
  
-   Use security roles to make a dashboard visible to just certain roles    
  
### Next steps  
[Set properties for a chart or list included in a dashboard](set-properties-chart-list-included-dashboard.md)
