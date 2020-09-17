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

To manage an app, select **Apps** from the solution explorer. And then, select the app that you want to manage, or select the *Commands* (**…**) option for the app, and then select the options from the drop-down menu.

![Select apps](media/manage-apps-1.png "Select apps")

## Edit an app

Select **Edit** an app to edit the app in Power Apps Studio. For more information about editing an app, go to [edit a canvas app in Power Apps](../maker/canvas-apps/edit-app.md). For more information about Power Apps Studio, go to [Understanding Power Apps Studio](understand-power-apps-studio.md).

## Play an app

Select **Play** to run an app’s latest [published](../maker/canvas-apps/save-publish-app.md) version. For more details about publishing an app, go to [Publish an app](publish-and-share-apps.md).

## App details

The **Details** option shows the owner of the app, when the app was created and last modified, app ID and license designation.

![App details](media/app-details.png "App details")

## Restore an app

A canvas app can have multiple versions. You can restore an app to an available published version.

To restore an app to a specific version:

1. Select **Versions** from the [app details](#app-details) screen.

    ![App versions](media/app-versions.png "App versions")

1. Select a version other than *Live* that you want to restore.

1. Select ![Ellipsis](media/ellipsis.png "Ellipsis").

1. Select **Restore**.

    ![Restore a version](media/restore-version.png "Restore a version")

    > [!NOTE]
    > The restored app becomes the latest version of the app. However, the latest version is not yet live. You must publish the restored version to make the restored version available to all users.

1. Select ![Ellipsis to publish restored version](media/ellipsis.png "Ellipsis to publish restored version") for the restored version.

1. Select **Publish this version**.

    ![Publish restored version](media/publish-restored-version.png "Publish restored version")

1. Review the app preview and select **Publish this version** to confirm.

    ![Confirm publish restored version](media/confirm-publish-restored-version.png "Confirm publish restored version")

The **Versions** tab now shows the restored version as *Live*:

![Confirm restored app](media/confirm-restored-app.png "Confirm restored app")

For more details about restoring an app, go to [Restore an app](../maker/canvas-apps/restore-an-app.md).

## Delete an app

Select **Delete** to delete an app. When prompted, select **Delete from cloud** to delete the app.

![Delete app](media/manage-app-2.png "Delete app")

For more information about deleting an app, go to [Delete an app](../maker/canvas-apps/delete-app.md).

### See also

[Publish and share your apps](publish-and-share-apps.md)
