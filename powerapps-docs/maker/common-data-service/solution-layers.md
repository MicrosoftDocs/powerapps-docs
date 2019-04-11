---
title: "Solution layers | MicrosoftDocs"
description: "Learn how you can use solution layers"
keywords: 
ms.date: 04/10/2019
ms.service: powerapps
ms.custom: 
ms.topic: article
applies_to: 
  - Dynamics 365 for Customer Engagement (online)
  - Dynamics 365 for Customer Engagement Version 9.x
  - powerapps
ms.assetid: 
author: Mattp123
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use solution layers

[!INCLUDE [cc-applies-to-update-9-0-0](../includes/cc-applies-to-update-9-0-0.md)]

Solution layers allows you to view all component changes that occur due to solution upgrades over time. Within a solution layer, you can drill-down to view the specific changed and unchanged property details for a component. 

Solution layers provide the following benefits: 
-	Let’s you see the order in which a solution changed a component. 
-	Let’s you view all properties of a component within a specific solution including the changes to the component. 
-	Can be used to troubleshoot dependency or solution layering issues by displaying change details for a component that was introduced by a solution upgrade.

> [!NOTE]
> This feature is only available with [!INCLUDE [pn-microsoftcrm](../includes/pn-microsoftcrm.md)] (online).

## View the solution layers for a component
You can access solution layers from the **Components** list or from the **Dependency Details** dialog box in solution explorer. 

1. To view solution layers from the **Components** list, open solution explorer, in the **Components** list select a component, such as **Account**, and then select **Solution Layers** on the toolbar. 

   > [!div class="mx-imgBorder"] 
   > ![](media/solution-layers-toolbar.png "Solution layers button")

2. The solution layer page appears that displays each layer for the component, such as the account entity displayed here, with the most recent layer at the top. To view the details for a solution layer, select it. 

   > [!div class="mx-imgBorder"] 
   > ![](media/solution-layers-list.png "Solution layers list")

3. On the **Solution Layer** dialog box, the **Changed Properties** tab displays only those properties that were modified as part of the specific solution layer. 

   > [!div class="mx-imgBorder"] 
   > ![](media/solution-layers-change-prop.png "Solution layer changed properties")

4. Select the **All Properties** tab to view all properties, including changed and unchanged properties, for the solution layer. 

   > [!div class="mx-imgBorder"] 
   > ![](media/solution-layers-all-prop.png "Solution layer all properties")

## See also
[Solutions overview](solutions-overview.md)