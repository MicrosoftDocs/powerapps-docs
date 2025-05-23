---
title: Save and publish canvas apps
description: Step-by-step instructions for saving and publishing canvas apps.
author: amchern
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 11/19/2024
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
contributors:
  - mduelae
  - emcoope-msft
  - amchern
ms.collection: 
    - bap-ai-copilot
---

# Save and publish canvas apps

Whenever you save changes to a canvas app, you automatically publish them only for yourself and anyone else who has permissions to edit the app. When you finish making changes, you must explicitly publish them to make them available to everyone with whom the app is shared.

For information about how to share an app, see [Share an app](share-app.md) 

## Save your app

With your app open for editing in [Power Apps](https://make.powerapps.com), you can save in several ways:

- Select **Save** :::image type="icon" source="media/save-publish-app/save-icon.png"::: to save any unsaved changes you made to your app. With each Save, a new version is created in App version history.

- Or, in the dropdown menu, choose one of the following options:

  - **Save with version notes**: Save and add notes about your updates.
  - **Save as**: Duplicate the app with a different name.
  - **Download a copy**: Download a local copy of the app.

## Switch AutoSave on or off

You can also set Power Apps to automatically save every two minutes.

1. Select **More** **...** > **Settings**.

   :::image type="content" source="media/save-publish-app/autosave.png" alt-text="Screenshot that shows where the ellipses points are located that opens a dropdown menu to reveal the Settings option.":::

1. Select the **General** tab.

1. In the **Auto save** section, set the **Auto save** toggle to **On** or **Off**.

   :::image type="content" source="media/save-publish-app/autosave2.png" alt-text="Screenshot that shows where the Auto save toggle is located.":::

> [!NOTE]
>
> - When you publish a canvas app, your app is updated and runs on the latest version of Power Apps. Your app gets the benefit of all the latest features and performance upgrades added since you last published. If you haven’t published an update in several months, you might see an immediate performance benefit when you republish the app.
> - To retrieve app details faster during startup, some data is stored locally on user devices in the browser cache. Information stored includes app environment and connection details. This data stays stored in the browser based on browser storage limits. Users can clear stored data based on these [instructions for each browser](/troubleshoot/power-platform/power-apps/troubleshooting-startup-issues#clear-your-browser-cache).

## Create an app description with Copilot (preview)

If your app is in a [managed  environment](/power-platform/admin/managed-environment-overview), you can use AI to help you create a description for your app.

When you save and publish your app, on the **Getting ready to publishing** dialog box select, **Create descriptions using AI**.

You can also generate an app description by going to, **Settings** > **General**. Under **Description** select, **Create descriptions using AI**.

Admins can disable this feature for Managed Environments in the Power Platform admin. For more information, see [Managed Environments panel](/power-platform/admin/managed-environment-enable).

> [!NOTE]
> If a description is not added before the app is published, Copilot generates one for the app once the app is published. Makers can always go back and edit this description if Copilot didn't quite get it right.

> [!IMPORTANT]
>
> - To use this capability your app must be in a [managed  environment](/power-platform/admin/managed-environment-overview).
> - Preview features aren’t meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability might not be available in your region yet or be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, see [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)

## Identify the live version

To see all versions of an app:

1. Go to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) > **Apps**.
1. Select the :::image type="icon" source="media/save-publish-app/vertical-ellipses.png"::: next to an app name.
1. Select **Details**, then the **Versions** tab.

The **Live** version is published for everyone with whom the app is shared. The most recent version of any app is available only to those users who have edit permissions for it.

:::image type="content" source="media/save-publish-app/publish-portal.png" alt-text="Screenshot that shows where different versions of the app are located and how to publish a specific version." lightbox="media/save-publish-app/publish-portal.png":::

To publish the most recent version, select the publish icon :::image type="icon" source="media/save-publish-app/publish-icon.png"::: while in editing mode for your app.

> [!NOTE]
>
> - New published changes of an app might take a few seconds to display when launching the app. Publish time depends on the complexity of apps, which might take a few more minutes to publish.
> - If you already have an app open while a new version is published, you must reload the app to get the latest changes.
> - To reduce wait time to access your app, the app preload capability is turned on. You can turn it off. For more information, see [Overview of creating performant apps](create-performant-apps-overview.md).

## In-app notifications for an updated version of the app

If users are waiting for an app to update, they get a notification stating **A new version of this app is coming. We'll let you know when it's available.**

When the published changes are ready, users see a notification stating **You're using an old version of this app. Refresh to use the latest version.**. Users can select the **Refresh** button to see the latest version of the app.

### Notification availability

| Scenario | Availability |
| - | - |
| Canvas app on web | Generally available |
| Customized SharePoint Forms | Not available |
| Canvas app embedded in Teams | Not available |
| Canvas app embedded in Power BI | Not available |
| Power Apps web part | Not available |
| Canvas app embedded in iframe | Generally available |

## Next steps

- Find and run the app in a [browser](../../user/run-app-browser.md) or on a [phone](../../mobile/run-powerapps-on-mobile.md).
- [Rename an app](set-name-tile.md) from [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
- [Restore an app](restore-an-app.md) if you have multiple versions of an app.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
