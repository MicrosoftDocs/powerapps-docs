---
title: "Create or edit model-driven app dashboards | MicrosoftDocs"
description: Learn how to create and edit dashboards for model-driven apps
ms.custom: ""
ms.date: 04/08/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 641885d2-4a08-41b8-b914-d9a244e4d5b1
caps.latest.revision: 10
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create or edit model-driven app dashboards

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]
## Dashboard types

Dashboards are effectively collections of charts relating to app tables.

There are two types of dashboards, user dashboards and system dashboards. An app user can create a dashboard visible only to them in the app areas that to which they have privileges.

An admin or customizer creates or customizes system dashboards that, when published, are visible to all app users. A user can choose to set their user dashboard as their default dashboard and override the system dashboard.

## Dashboard interactivity

Dashboards can be standard or interactive.

**Standard** dashboards support adding one or more unrelated components such as charts or lists.

**Interactive** dashboards provide the capability for users to act on a particular row directly from the dashboard. This topic focuses on standard system dashboards. For information about interactive dashboards, see [Configure model-driven app interactive experience dashboards](configure-interactive-experience-dashboards.md).
  
## Create a new standard dashboard  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
  
1. Select **Solutions**, and then open the required solution.

1. On the toolbar select **New**, select **Dashboard**, and then choose one of the following layouts:

   - 2-column overview
   - 3-column overview
   - 3-column overview (varied width)
   - 4-column overview
   - Power BI embedded
  
    :::image type="content" source="media/create-new-dashboard-layouts.png" alt-text="{alt-text}":::

1. In the **Dashboard: New** page enter a name for the dashboard.
1. Select one of the component areas and then select the icon for a chart or a list.  
  
     Up to six components can be included in a dashboard.  
  
1. For example, to add a chart, select the chart icon on the tile of the dashboard canvas where chart needs to appear. Then, in the **Add Component** dialog box select values for **Row Type**, **View**, and **Chart**, and then select **Add** to add the chart to the dashboard. For information about how to create a chart, see [Create a model-driven app system chart](create-edit-system-chart.md).
:::image type="content" source="media/add-dashboard-component-dialog.png" alt-text="Add dashboard component dialog":::  

1. When finished adding components to the dashboard, select **Save** and then **Close**.  

1. On the solution toolbar, select **Publish**.
  
## Edit an existing dashboard  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Select **Solutions**, and then open the required solution.  

1. In the list of solution components, open the dashboard, select one of the component areas, and then on the toolbar select **Edit Component**.  
  
1. In the **Set Properties** dialog box, make changes to a chart or list such as change the table, default view, add a chart selector, or make the dashboard available on the mobile apps. When done, select **OK**.  
  
     For more information about setting dashboard component properties, see [Set properties for a chart or list included in a dashboard](set-properties-chart-list-included-dashboard.md).  
  
1. When the changes are complete select **Save** and then select **Close**.

1. On the solution toolbar, select **Publish**.  
  
## Next steps

[Configure interactive experience dashboards](configure-interactive-experience-dashboards.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
