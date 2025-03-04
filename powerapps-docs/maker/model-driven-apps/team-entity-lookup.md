---
title: "Add the team table as a lookup option in your app"
description: "Learn how to add the team table as a lookup option in your app with Power Apps"
ms.custom: ""
ms.date: 03/04/2025
ms.reviewer: ""
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
search.audienceType: 
  - maker
---
# Add a table as a lookup option in your app

This article describes a feature that uses the classic app designer.

> [!IMPORTANT]
> Starting in October 2023, the classic app, form, and view designers are deprecated and all model-driven apps, forms, and views only open in the modern designers. By default, the **Switch to classic** command to revert back to the classic designer from the modern designer is no longer available. More information: [Classic app, form, and view designers are deprecated](/power-platform/important-changes-coming#classic-app-form-and-view-designers-are-deprecated) 
>
> We recommend that you transition to use the modern designers to create and edit your model-driven apps and components.

With model-driven apps, for a table to be available in a lookup it must be added to the app. For example, contact records have the ability to be assigned to a user or a team. Both of these tables have a relationship with the contacts table.

> [!div class="mx-imgBorder"] 
> ![Entity lookup with both users and teams available.](media/entity-lookup-teams.png "Entity lookup with both users and teams available")

However, if the **User** table is included in the app but the **Team** table isn't, only user rows appear in a lookup.

> [!div class="mx-imgBorder"] 
> ![Entity lookup with users only.](media/entity-lookup-user-only.png "Entity lookup with users only")

This can be resolved by adding the **Team** table to the app using the app designer.

## Add a related table to an app to enable the lookup

1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution you want, and then select the model-driven app. This opens the app in the app designer.
1. Select the **Components** tab, select **Entities** (tables), and then select **Team**.

    > [!div class="mx-imgBorder"]
    > ![Add the team table to the app.](media/add-team-entity-app.png "Add the team table to the app")

1. Select **Save**, and then select **Publish** to make the change available to app users within the organization.

## Next steps

[Share a model driven app](share-model-driven-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
