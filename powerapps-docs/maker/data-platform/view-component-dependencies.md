---
title: "View dependencies for a component in Power Apps | MicrosoftDocs"
description: "Understand how to view dependencies for a component in Power Apps"
ms.custom: ""
ms.date: 05/27/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.assetid: 
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# View dependencies for a component
[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Solution components often depend on other solution components. You can’t delete any solution component that has dependencies from another solution component. You can view the dependent components from the **Solutions** area of Power Apps.  


1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. 
2. Open the solution you want, select the component you want, on the command bar select **...,** and then select **Show dependencies**. 

   > [!div class="mx-imgBorder"] 
   > ![Component dependency for the account table.](media/component-dependencies-account.png)

### See also
[For developers: Detect solution dependencies](/power-platform/alm/solution-api#detect-solution-dependencies)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]