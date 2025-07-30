---
title: "Create or edit model-driven app dashboards | MicrosoftDocs"
description: Learn how to create and edit dashboards for model-driven apps
ms.custom: ""
ms.date: 12/19/2024
ms.reviewer: ""
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
contributors: jasongre
author: "Mattp123"
search.audienceType: 
  - maker
---
# Create or edit model-driven app dashboards

Dashboards are collections of charts relating to Microsoft Dataverse tables.

There are two types of dashboards, user dashboards and system dashboards. An app user can create a dashboard visible only to them in the app areas where they have privileges.

An admin or customizer creates or customizes system dashboards that, when published, are visible to all app users. A user can choose to set their user dashboard as their default dashboard and override the system dashboard.

## Dashboard interactivity

Dashboards can be standard or interactive.

**Standard** dashboards support adding one or more unrelated components such as charts or lists.

**Interactive** dashboards provide the capability for users to act on a particular row directly from the dashboard. This article focuses on standard system dashboards. For information about interactive dashboards, see [Configure model-driven app interactive experience dashboards](configure-interactive-experience-dashboards.md).
  
## Create a new standard dashboard  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
  
1. Select **Solutions** on the left navigation pane, and then open the required solution. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. On the toolbar select **New**, select **Dashboard**, and then choose one of the following layouts:

   - 2-column overview
   - 3-column overview
   - 3-column overview (varied width)
   - 4-column overview
   - Power BI embedded
  
    :::image type="content" source="media/create-new-dashboard-layouts.png" alt-text="{alt-text}":::

1. In the **Dashboard: New** page, enter a name for the dashboard.

1. Select one of the component areas and then select the icon for a chart or a list.  
  
     Up to six components can be included in a dashboard.  
  
1. For example, to add a chart, select the chart icon on the tile of the dashboard canvas where the chart needs to appear. Then, in the **Add Component** dialog, select values for **Row Type**, **View**, and **Chart**. Then select **Add** to add the chart to the dashboard. For information about how to create a chart, see [Create a model-driven app system chart](create-edit-system-chart.md).
:::image type="content" source="media/add-dashboard-component-dialog.png" alt-text="Add dashboard component dialog":::  

   > [!NOTE]
   > The **Enable for mobile** option on the **Dashboard Properties** dialog only works with the legacy web client. The property has no effect on the Unified Interface where all dashboards are available on mobile and browser.  

1. When finished adding components to the dashboard, select **Save** and then **Close**.  

1. On the solution toolbar, select **Publish**.
  
## Edit an existing dashboard  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Select **Solutions** on the left navigation pane, and then open the required solution. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. In the list of solution components, open the dashboard, select one of the component areas, and then on the toolbar select **Edit Component**.  
  
1. In the **Set Properties** dialog box, make changes to a chart or list such as change the table, default view, or add a chart selector. When done, select **OK**.  
  
     For more information about setting dashboard component properties, see [Set properties for a chart or list included in a dashboard](set-properties-chart-list-included-dashboard.md).  

     > [!NOTE]
     > The *Available on phone** option on the **Set Properties** dialog **Availability** section only works with the legacy web client. The property has no effect on the Unified Interface where all dashboards are available on mobile and browser. 
  
1. When the changes are complete select **Save** and then select **Close**.

1. On the solution toolbar, select **Publish**.

> [!NOTE]
> Lists in the dashboard designer don't display a data preview.
  
## Next steps

[Configure interactive experience dashboards](configure-interactive-experience-dashboards.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
