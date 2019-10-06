---
title: "View solution layers | MicrosoftDocs"
description: "Learn how you can use solution layers"
keywords: 
ms.date: 04/18/2019
ms.service: powerapps
ms.custom: 
ms.topic: article
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

<!--note from editor: Best practice is that H1 title and title in metadata are different.    -->

# View solution layers
Solution layers allow you to view all component changes that occur due to solution changes over time. Within a solution layer, you can drill down to view specific changed and unchanged property details for a component. 

Solution layers: 
-	Let you see the order in which a solution changed a component. 
-	Let you view all properties of a component within a specific solution, including the changes to the component. 
-	Can be used to troubleshoot dependency or solution-layering issues by displaying change details for a component that was introduced by a solution change.

## View the solution layers for a component
You can access solution layers from the **Components** list or from the **Dependency Details** dialog box in solution explorer. 

<!--note from editor: In step 2 below, does the page display a name at top? If so, use the same capitalization in text. -->

1. To view solution layers from the **Components** list, open [solution explorer](../model-driven-apps/advanced-navigation.md#solution-explorer). In the **Components** list, select a component, such as **Account**, and then select **Solution Layers** on the toolbar. 

   > [!div class="mx-imgBorder"] 
   > ![Solution layers button](media/solution-layers-toolbar.png "Solution layers button")

2. The solution layer page appears. It displays each layer for the component, such as the **Account** entity displayed here, with the most recent layer at the top. To view the details for a solution layer, select it. 

   > [!div class="mx-imgBorder"] 
   > ![Solution layers list](media/solution-layers-list.png "Solution layers list")

3. In the **Solution Layer** dialog box, the **Changed Properties** tab displays only those properties that were modified as part of the specific solution layer. 

   > [!div class="mx-imgBorder"] 
   > ![Solution layer changed properties](media/solution-layers-change-prop.png "Solution layer changed properties")

4. Select the **All Properties** tab to view all properties, including changed and unchanged properties, for the solution layer. 

   > [!div class="mx-imgBorder"] 
   > ![Solution layer all properties](media/solution-layers-all-prop.png "Solution layer all properties")

### See also
[Solutions overview](solutions-overview.md)
