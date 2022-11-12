---
title: Save and publish canvas apps
description: Step-by-step instructions for saving and publishing canvas apps.
author: amchern

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/09/2022
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - emcoope-msft
  - amchern
---
# Save and publish canvas apps

Whenever you save changes to a canvas app, you automatically publish them only for yourself and anyone else who has permissions to edit the app. When you finish making changes, you must explicitly publish them to make them available to everyone with whom the app is shared.

For information about how to share an app, see [Share an app](share-app.md).

## Save changes to an app

In Power Apps Studio, select **Save** on the **File** menu (on the left edge), and then follow either of these steps:

* If you've never saved the app before, selecting **Save** from the **File** menu automatically takes you to **Save as**. Select location as **The cloud**, provide a name for it, and then select **Save**. <br> 

    ![Save new app.](./media/save-publish-app/save-as.png)
* If the app has ever been saved, select **Save**. You can also leave version specific notes or comments.  

    ![Save updated app.](./media/save-publish-app/save-app.png)

Power Apps can also periodically save the app every 2 minutes. If you've saved the app once, Power Apps will continue to save a version of the app periodically without requiring the user to press or tap the Save action. Authors can enable or disable the **Auto save** setting from the **Account** tab on the **File** menu.

![Auto save setting.](./media/save-publish-app/autosave.png)

## Publish an app

1. In Power Apps Studio, select **Save** on the **File** menu (on the left edge), and then select **Publish**.

    ![Publish app.](./media/save-publish-app/publish-app.png)
2. In the **Publish** dialog box, select **Publish this version** to publish the app to all users with whom the app is shared.

   ![Review Publish.](./media/save-publish-app/publish-review.png)

   > [!NOTE]
   > - Whenever you publish a canvas app, your app will be upgraded to run on the latest version of Power Apps – which means it will get the benefit of all the latest features and performance upgrades we’ve added since you last published. If you haven’t published an update in several months, you’ll likely see an immediate performance benefit from republishing now.
   > - To allow users to retrieve app details faster on app startup, certain data will be locally stored on users' devices in the browser cache. Information that will be stored includes app, environment, and connection details. This data will stay stored in the browser based on each browsers’ storage limits. Users can clear stored data based on [instructions for each browser](/troubleshoot/power-platform/power-apps/troubleshooting-startup-issues)

## Identify the live version

To see all versions of an app, go to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) > **Apps** > select your app > **Details** > **Versions**.

The **Live** version is published for everyone with whom the app is shared. The most recent version of any app is available only to those users who have edit permissions for it.

![Publish from portal.](./media/save-publish-app/publish-portal.png)

To publish the most recent version, highlight the version and select ellipsis (...). Then select **Publish this version** from the drop-down menu.

> [!NOTE]
> - Changes from a newly published version of an app may take a few seconds to reflect when launching the app. Occasionally, it may take a few minutes.
> - If you already have an app open while a new version is published, you must reload the app to get the latest changes.
> - To reduce the time users wait to access your app, the app preload capability is turned on. You can chose to turn it off. Learn more [here](performance-tips.md#enable-preload-app-for-enhanced-performance).

## Next steps

* Find and run the app in a [browser](../../user/run-app-browser.md) or on a [phone](../../mobile/run-powerapps-on-mobile.md).
* [Rename an app](set-name-tile.md) from [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
* [Restore an app](restore-an-app.md) if you have multiple versions of an app.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
