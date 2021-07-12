---
title: "Add the team table as a lookup option in your app | MicrosoftDocs"
description: "Learn how to add the team table as a lookup option in your app"
ms.custom: ""
ms.date: 07/24/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 25
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Add a table as a lookup option in your app

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

With Unified Interface apps, for a table to be available in a lookup it must be added to the app. For example, contact rows have the ability to be assigned to a user or a team.  

> [!div class="mx-imgBorder"] 
> ![Entity lookup with both users and teams available.](media/entity-lookup-teams.png "Entity lookup with both users and teams available")

However, if the user table is included in the app but the team table is not, only user rows will appear in a lookup. 

> [!div class="mx-imgBorder"] 
> ![Entity lookup with users only.](media/entity-lookup-user-only.png "Entity lookup with users only")

## Add the team table to an app

1. Open the app in the App Designer. 
2. Select the **Components** tab, select **Entities**, and then select **Team**.    

    > [!div class="mx-imgBorder"] 
    > ![Add the team table to the app.](media/add-team-entity-app.png "Add the team table to the app")

3. Select **Save**, and then select **Publish** to make your change available to app users.   



[!INCLUDE[footer-include](../../includes/footer-banner.md)]