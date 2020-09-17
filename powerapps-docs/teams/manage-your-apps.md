---
title: Manage your apps | Microsoft Docs
description: Learn how to manage your apps using Power Apps app from Teams.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/03/2020
ms.author: tapanm
ms.reviewer: 
---

# Manage your apps

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

To manage an app, select **Apps** from the solution explorer. Then select the app that you want to manage, or select **Commands** (**…**) next to the app name, and then select commands from the drop-down menu.

![Select apps](media/manage-apps-1.png "Select apps")

## Edit an app

Select **Edit** to edit the app in Power Apps Studio. More information: [Edit a canvas app in Power Apps](../maker/canvas-apps/edit-app.md) and [Understanding Power Apps Studio](understand-power-apps-studio.md)

## Play an app

Select **Play** to run the latest [published version](../maker/canvas-apps/save-publish-app.md) of the app. More information: [Publish an app](publish-and-share-apps.md)

## App details

**Details** shows you the information such as the owner of the app, when the app was created and last modified, app ID, app licensing information, and the app's web link.

> [!TIP]
> The web link for an app can be very useful when you want to run an app in the browser for testing, or open an app from a browser or through another app (such as when using the [Launch() function](../maker/canvas-apps/functions/function-param.md)).

## Delete an app

Select **Delete** to delete an app. When prompted, select **Delete from cloud**.

![Delete an app](media/manage-app-2.png "Delete an app")

More information: [Delete an app](../maker/canvas-apps/delete-app.md)
<a name="restore-an-app"></a>
## Restore an app

A canvas app can have multiple versions. You can restore an app to an available published version.

To restore an app to a specific version:

1. Edit the app in Power Apps Studio.

1. Select **Version history** from the upper-right corner of the screen.

    ![Select version history](media/manage-apps-3.png "Select version history")

1. Select **Details**.<!--You can also select *Commands (…)* and then select **Delete** from the drop-down menu instead. note from editor: No need to document every method, just tell the reader what to do.-->

    ![Select details](media/manage-apps-4.png "Select details")

1. Select **Versions**.

    ![Select versions](media/manage-apps-5.png "Select versions")

1. Select the app version that you want to restore. The currently published version that's available to users is marked as **Live**.

    ![Select an app version](media/manage-app-6.png "Select an app version")

1. Select **Restore**.<!--You can also select *Commands (…)* and then select **Restore** from the drop-down menu.-->

    ![Select restore from menu](media/manage-app-7.png "Select restore from menu")

1. Select **Restore** to confirm.

    ![Select restore](media/manage-app-8.png "Select restore")

The app version is now restored.

![Restored version](media/manage-app-9.png "Restored version")

More information: [Restore an app](../maker/canvas-apps/restore-an-app.md)

### See also

[Publish and share your apps](publish-and-share-apps.md)
