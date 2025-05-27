---
title: Save and publish canvas apps
description: Step-by-step instructions for saving and publishing canvas apps.
author: amchern
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 5/27/2025
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

When you save changes to a canvas app, those changes are saved for you and anyone else who can edit the app. To make your changes accessible to everyone the app is shared with, you need to publish the app. To learn how to share an app, see [Share an app](share-app.md).

## Save your app

With your app open for editing in [Power Apps](https://make.powerapps.com), save your work in several ways:

- Select **Save** :::image type="icon" source="media/save-publish-app/save-icon.png"::: to save any unsaved changes to your app. Each time you save, a new version appears in App version history.

- In the dropdown menu, choose one of the following options:

  - **Save with version notes**: Save and add notes about your updates.
  - **Save as**: Duplicate the app with a different name.
  - **Download a copy**: Download a local copy of the app.

## Switch AutoSave on or off

Power Apps can automatically save your work every two minutes.

1. Select **More** **...** > **Settings**.

   :::image type="content" source="media/save-publish-app/autosave.png" alt-text="Screenshot of the ellipsis menu in Power Apps that opens a dropdown to reveal the Settings option.":::

1. Select the **General** tab.

1. In the **Auto save** section, set the **Auto save** toggle to **On** or **Off**.

   :::image type="content" source="media/save-publish-app/autosave2.png" alt-text="Screenshot of the Auto save toggle location in Power Apps settings.":::

> [!NOTE]
>
> - When you publish a canvas app, your app updates and runs on the latest version of Power Apps. Your app gets all the latest features and performance upgrades added since you last published. If you haven’t published an update in several months, you see an immediate performance benefit when you republish the app.
> - To retrieve app details faster during startup, some data stores locally on user devices in the browser cache. Information stored includes app environment and connection details. This data stays in the browser based on browser storage limits. Users can clear stored data based on these [instructions for each browser](/troubleshoot/power-platform/power-apps/troubleshooting-startup-issues#clear-your-browser-cache).

## Create an app description with Copilot (preview)

If your app is in a [managed environment](/power-platform/admin/managed-environment-overview), you can use AI to help you create a description for your app.

When you save and publish your app, in the **Getting ready to publishing** dialog box, select **Create descriptions using AI**.

You can also generate an app description by going to **Settings** > **General**. Under **Description**, select **Create descriptions using AI**.

Admins can disable this feature for managed environments in Power Platform admin. For more information, see [Managed Environments panel](/power-platform/admin/managed-environment-enable).

> [!NOTE]
> If you don't add a description before publishing the app, Copilot generates one after the app is published. Makers can edit this description if Copilot doesn't get it right.

> [!IMPORTANT]
>
> - To use this capability, your app must be in a [managed environment](/power-platform/admin/managed-environment-overview).
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability might not be available in your region yet or can be subject to usage limits or capacity throttling.
> - To learn about capabilities and limitations of of AI-powered and Copilot features in Power Apps, see [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)

## Identify the live version

To see all versions of an app:

1. Go to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) > **Apps**.
1. Select the :::image type="icon" source="media/save-publish-app/vertical-ellipses.png"::: next to the app name.
1. Select **Details**, and then select the **Versions** tab.

The **Live** version is published for everyone the app is shared with. Only users with edit permissions can access the most recent version of the app.

:::image type="content" source="media/save-publish-app/publish-portal.png" alt-text="Screenshot that shows where different versions of the app are located and how to publish a specific version." lightbox="media/save-publish-app/publish-portal.png":::

To publish the most recent version, select the publish icon :::image type="icon" source="media/save-publish-app/publish-icon.png"::: while you're editing your app.

> [!NOTE]
>
> - New published changes to an app can take a few seconds to show when you launch the app. Publish time depends on the app's complexity, and it can take a few more minutes to finish publishing.
> - If you already have an app open when a new version is published, reload the app to get the latest changes.
> - To reduce wait time when accessing your app, the app preload capability is turned on. You can turn it off. For more information, see [Overview of creating performant apps](create-performant-apps-overview.md).

## In-app notifications for an updated version of the app

When users are waiting for an app to update, they will see a notification that says **A new version of this app is coming. We'll let you know when it's available.**

When the published changes are ready, users see a notification that says **You're using an old version of this app. Refresh to use the latest version.** Users select the **Refresh** button to use the latest version of the app.

### Notification availability

| Scenario | Availability |
| - | - |
| Canvas app on web | Generally available |
| Customized SharePoint forms | Not available |
| Canvas app embedded in Teams | Not available |
| Canvas app embedded in Power BI | Not available |
| Power Apps web part | Not available |
| Canvas app embedded in an iframe | Generally available |

## Next steps

- Find and run the app in a [browser](../../user/run-app-browser.md) or on a [phone](../../mobile/run-powerapps-on-mobile.md).
- [Rename an app](set-name-tile.md) from [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
- [Restore an app](restore-an-app.md) if you have more than one version of the app.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
