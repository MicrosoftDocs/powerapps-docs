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
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Add a table as a lookup option in your app



## Lookup functionality
With model-driven apps, for a table to be available in a lookup it must be added to the app. For example, contact records have the ability to be assigned to a user or a team.  Both of these tables have a relationship with the contacts table.

> [!div class="mx-imgBorder"] 
> ![Entity lookup with both users and teams available.](media/entity-lookup-teams.png "Entity lookup with both users and teams available")

However, if the **User** table is included in the app but the **Team** table is not, only user rows will appear in a lookup.

> [!div class="mx-imgBorder"] 
> ![Entity lookup with users only.](media/entity-lookup-user-only.png "Entity lookup with users only")

This can be resolved by adding the **Team** table to the app using the [App Designer](model-driven-app-glossary.md#app-designer).

## Add a related table to an app to enable the lookup

1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions**.
1. Open the solution you want, and then select the model-driven app. This opens the app in the app designer.
1. Select the **Components** tab, select **Entities** (tables), and then select **Team**.

    > [!div class="mx-imgBorder"]
    > ![Add the team table to the app.](media/add-team-entity-app.png "Add the team table to the app")

1. Select **Save**, and then select **Publish** to make the change available to app users within the organization.

## Next Steps
[Share a model driven app](share-model-driven-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]