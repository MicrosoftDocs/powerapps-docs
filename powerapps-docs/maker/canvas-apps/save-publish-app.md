---
title: Save and publish a canvas app | Microsoft Docs
description: Step-by-step instructions for saving and publishing canvas apps for app makers
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 09/14/2017
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Save and publish a canvas app in PowerApps
Whenever you save changes to a canvas app, you automatically publish them only for yourself and anyone else who has permissions to edit the app. When you finish making changes, you must explicitly publish them to make them available to everyone with whom the app is shared.

For information about how to share an app, see [Share an app](share-app.md).

## Save changes to an app
In PowerApps Studio, click or tap **Save** on the **File** menu (on the left edge), and then follow either of these steps:

* If you've never saved the app before, provide a name for it, and then click or tap **Save**.

    ![Save new app](./media/save-publish-app/save-as.png)
* If the app has ever been saved, click or tap **Save**.  

    ![Save updated app](./media/save-publish-app/save-app.png)

PowerApps can also periodically save the app every 2 minutes. If you have saved the app once, PowerApps will continue to save a version of the app periodically without requiring the user to press or tap the Save action. Authors can enable or disable the **Auto save** setting from the **Account** tab on the **File** menu.

![Auto save setting](./media/save-publish-app/autosave.png)

## Publish an app
1. In PowerApps Studio, click or tap **Save** on the **File** menu (on the left edge), and then click or tap **Publish this version**.

    ![Publish app](./media/save-publish-app/publish-app.png)
2. In the **Publish** dialog box, tap or click **Publish this version** to publish the app to all users with whom the app is shared.

   ![Review Publish](./media/save-publish-app/publish-review.png)

   > [!NOTE]
   > Whenever you publish a canvas app, your app will be upgraded to run on the latest version of PowerApps – which means it will get   the benefit of all the latest features and performance upgrades we’ve added since you last published. If you haven’t published an update in several months, you’ll likely see an immediate performance benefit from republishing now.

## Identify the live version
In [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), click or tap **Apps** on the **File** menu (on the left edge), click or tap the details icon for an app, and then click or tap the **Versions** tab.

The **Live** version is published for everyone with whom the app is shared. The most recent version of any app is available only to those who have edit permissions for it.

![Publish from portal](./media/save-publish-app/publish-portal.png)

To publish the most recent version, click or tap **Publish this version**, and then click or tap **Publish this version** in the **Publish** dialog box.

## Next steps
* Find and run the app in a [browser](../../user/run-app-browser.md) or on a [phone](../../user/run-app-client.md).
* [Rename an app](set-name-tile.md) from powerapps.com.
* [Restore an app](restore-an-app.md) if you have multiple versions of an app.
