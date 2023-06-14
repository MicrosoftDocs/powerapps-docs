---
title: Embed a model-driven app as a personal app (preview)
description: You can embed a model-driven app created in Power Apps in Microsoft Teams to share it.
author: aorth
ms.topic: how-to
ms.custom: model
ms.collection: get-started
ms.reviewer: matp
ms.date: 01/09/2021
ms.subservice: teams
ms.author: aorth
search.audienceType: 
  - maker
contributors:
---
# Embed a model-driven app as personal app in Teams (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

You can share an app you've created by embedding it directly into Microsoft Teams. When completed, users can select **+** to add your app to any of **your** team channels or conversations in the team you are in. The app appears as a tile under **Tabs for your team**.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../includes/cc-preview-features-definition.md)]

## Prerequisites

- You need a valid [Power Apps license](/power-platform/admin/pricing-billing-skus).
- To embed an app into Teams, you need an existing app [created using Power Apps](../maker/model-driven-apps/build-first-model-driven-app.md).

## Add the app as a personal app

1. Sign into [Power Apps](https://make.powerapps.com), and then select **Apps** in the menu.

    ![Show list of apps.](media/embed-teams-app/file-apps2.png "Show list of apps")

1. Select **More actions** (...) for the app you want to share in Teams, and then select **Add to Teams**.

    ![Add to Teams.](media/embed-teams-app/add-to-teams.png "Add to Teams")

1. **Add to Teams** panel opens on the right-side of the screen.

   :::image type="content" source="media/embed-teams-app/add-to-teams-model.png" alt-text="Add to Teams panel":::

1. (Optional) If the app doesn't have any description, select **Edit details** to open the app in add designer to add.

1. (Optional) Select **Advanced settings** to add additional details such as *Name*, *Website*, *Terms of Use*, *Privacy Policy*, *MPN ID* (Microsoft Partner Network ID).

    ![Add additional details.](media/embed-teams-app/additional-settings-embed.png "Add additional details")

1. Select **Add to Teams** to add the app as a personal app or select **Add to a team** or **Add to a chat** to add the app as a tab within an existing channel or conversation.

## Download app

You can also **Download app** in Power Apps. Power Apps will then generate your Teams manifest file using the app description and logo you've already set in your app.

1. To add the app as a personal app or as a tab to any channel or conversation, select **Apps** in the left navigation and then select **Upload a custom app**.

    > [!NOTE]
    > The **Upload a custom app** only appears if your Teams administrator has created a [custom app policy](/microsoftteams/teams-app-setup-policies) and turned on **Allow uploading of custom apps**.

    ![Add app as tab.](media/embed-teams-app/upload-custom-app.png "Upload a custom app")

2. Select **Add** to add the app as a personal app or select **Add to team** to add the app as a tab within an existing channel or conversation.

## Publish the app to the Teams catalog

If you're an admin, you can use the **Download app** option to also [publish the app](/microsoftteams/tenant-apps-catalog-teams#publish-a-custom-app-to-your-organizations-app-store) to the Microsoft Teams catalog.

## Features currently unavailable

- Running **Model-driven apps** on the Microsoft Teams mobile app is currently not supported.
- Embedded canvas apps are not supported.
- Custom pages are not supported.

### See also

[Welcome to Microsoft Teams](/MicrosoftTeams/teams-overview)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
