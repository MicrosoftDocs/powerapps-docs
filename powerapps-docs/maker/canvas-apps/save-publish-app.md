---
title: Save and publish canvas apps
description: Step-by-step instructions for saving and publishing canvas apps.
author: amchern
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/27/2026
ms.update-cycle: 180-days
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

Saving and publishing are two different actions:

- **Save** stores your latest changes so you and other app editors can keep working on them. Saving doesn't change what end users see.
- **Publish** makes your saved changes available to everyone the app is shared with.

Use this article to save your work, turn AutoSave on or off, publish updates, and manage app versions. To share an app with users, see [Share a canvas app](share-app.md).

## Save your app

Open your app for editing in [Power Apps](https://make.powerapps.com), and then save your work in one of these ways:

- Select **Save** :::image type="icon" source="media/save-publish-app/save-icon.png"::: on the command bar to save any unsaved changes. Each save creates a new entry in the app's version history.

- Select the dropdown arrow next to **Save** and choose one of the following options:

  | Option | What it does |
  | --- | --- |
  | **Save with version notes** | Saves the app and lets you add notes that describe what changed in this version. |
  | **Save as** | Creates a copy of the app with a different name. |
  | **Download a copy** | Downloads a local `.msapp` file of the app for backup or offline editing. |

## Turn AutoSave on or off

By default, Power Apps saves your work automatically every two minutes. AutoSave helps prevent lost changes if your browser or device closes unexpectedly.

To change the setting:

1. On the command bar, select **Settings**, and then go to the **General** tab.
1. In the **Auto save** section, set the **Auto save** toggle to **On** or **Off**.

   :::image type="content" source="media/save-publish-app/autosave2.png" alt-text="Screenshot of the AutoSave toggle location in Power Apps settings.":::

> [!TIP]
> Even with AutoSave on, select **Save** before you close the browser tab to make sure your most recent changes are captured.

## Publish your app

Publishing your app pushes your latest saved changes to the users you've shared the app with.

1. On the command bar, select **Publish**. If you have unsaved changes, you're prompted to save first. After you save, select **Publish** again.
1. (Optional) Enter a description of what's new in this version.
1. Select **Publish this version**.

Users see the new version the next time they open or refresh the app.

> [!NOTE]
>
> - When you publish a canvas app, the app runs on the latest version of Power Apps and picks up the newest features and performance improvements. If you haven't published in several months, you usually see an immediate performance benefit when you republish.
> - To make app startup faster, Power Apps caches some details (such as environment and connection information) in the user's browser. Cached data stays until the browser clears it. For steps, see [Clear your browser cache](/troubleshoot/power-platform/power-apps/troubleshooting-startup-issues#clear-your-browser-cache).

### Create an app description with Copilot (preview)

If your app is in a [managed environment](/power-platform/admin/managed-environment-overview), you can use AI to help create a description for your app.

In the **Publishing** dialog box, select **Create descriptions using AI** when you save and publish your app.

You can also generate an app description by going to **Settings** > **General**. Under **Description**, select **Create descriptions using AI**.

Admins can disable this feature for managed environments in Power Platform admin. For more information, see [Managed Environments panel](/power-platform/admin/managed-environment-enable).

> [!NOTE]
> If you don't add a description before publishing the app, Copilot generates one after the app is published. Makers can edit this description if Copilot doesn't generate it correctly.

> [!IMPORTANT]
>
> - To use this capability, your app must be in a [managed environment](/power-platform/admin/managed-environment-overview).
> - Preview features aren't meant for production use and can have restricted functionality. These features are available before an official release so customers get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability isn't available in all regions yet and can be subject to usage limits or capacity throttling.
> - To learn about capabilities and limitations of AI-powered and Copilot features in Power Apps, see [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md).

## Identify and manage app versions

Each time you save the app, Power Apps adds a new entry to the version history. The version marked **Live** is the one your shared users currently run. Other versions are saved drafts that you can review or restore.

To view all versions of an app:

1. Go to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and in the left pane, select **Apps**.
1. Select the **More commands** icon :::image type="icon" source="media/save-publish-app/vertical-ellipses.png"::: next to the app name.
1. Select **Details** > **Details**.
1. Go to the **Versions** tab.

:::image type="content" source="media/save-publish-app/publish-portal.png" alt-text="Screenshot of where different versions of the app are located and how to publish a specific version." lightbox="media/save-publish-app/publish-portal.png":::

From this tab you can:

- See which version is **Live**.
- Select an earlier version and publish it to roll back. For details, see [Restore a canvas app to a previous version](restore-an-app.md).

To publish the most recent saved version, open the app in the studio and select the publish icon :::image type="icon" source="media/save-publish-app/publish-icon.png" alt-text="publish icon":::.

> [!NOTE]
>
> - Newly published changes can take a few seconds to appear when users launch the app. Publishing time depends on app complexity and can take a few minutes for large apps.
> - If users already have the app open when you publish, they need to reload the app to see the new version.
> - App preload is on by default to reduce wait time. You can turn it off if needed. For more information, see [Create performant apps](create-performant-apps-overview.md).

## In-app notifications for new versions

When you publish an update, users who currently have the app open see two notifications:

1. **A new version of this app is coming. We'll let you know when it's available.** &mdash; appears while the new version is being prepared.
1. **You're using an old version of this app. Refresh to use the latest version.** &mdash; appears when the new version is ready. Users select **Refresh** to load it.

### Where these notifications appear

| Scenario | Notification available? |
| --- | --- |
| Canvas app on web | Yes |
| Canvas app embedded in an iframe | Yes |
| Customized SharePoint forms | No |
| Canvas app embedded in Microsoft Teams | No |
| Canvas app embedded in Power BI | No |
| Power Apps web part | No |

## Related information

- Run an app in a [browser](../../user/run-app-browser.md) or on a [mobile device](../../mobile/run-powerapps-on-mobile.md).
- [Rename a canvas app](set-name-tile.md).
- [Restore a canvas app](restore-an-app.md) to an earlier version.
- [Share a canvas app](share-app.md) with other users.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
