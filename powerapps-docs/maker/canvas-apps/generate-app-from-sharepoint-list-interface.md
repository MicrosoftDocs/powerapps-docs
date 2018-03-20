---
title: Generate an app from within a SharePoint list | Microsoft Docs
description: Generate a three-screen app to manage items from within a SharePoint list, whether the site is on-premises or in the cloud.
services: ''
suite: powerapps
documentationcenter: na
author: AFTOwen
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/18/2018
ms.author: anneta

---
# Generate an app from within SharePoint using PowerApps

In PowerApps, automatically generate an app in which users can manage items in a custom SharePoint Online list. The app will have three screens in which users can:

* browse through all records in the list (**BrowseScreen1**)
* view all fields for a specific record (**DetailsScreen1**)
* create or edit a record (**EditScreen1**)

If you create an app of a custom list from the SharePoint Online command bar, the app appears as a view of that list. You can also run the app on an iOS or Android device, in addition to a web browser.

> [!IMPORTANT]
> PowerApps doesn't support all types of SharePoint data. For more information, see [Known issues](connections/connection-sharepoint-online.md#known-issues).

## Generate an app
1. Open a custom list in SharePoint Online, click or tap **PowerApps** on the command bar, and then click or tap **Create an app**.

    ![Create an app](./media/generate-app-from-sharepoint-list-interface/generate-new-app.png)

2. In the panel that appears, type a name for your app, and then click or tap **Create**.

    ![Name the app](./media/generate-app-from-sharepoint-list-interface/app-name.png)

    A new tab appears in your web browser that shows the app that you automatically generated based on your SharePoint list. The app appears in PowerApps Studio, where you can customize it.

    ![Default app](./media/generate-app-from-sharepoint-list-interface/default-app.png)  
3. Click or tap the browser tab for your SharePoint list, and then click or tap **Open**.

> [!NOTE]
> You might need to refresh the browser window (for example, by pressing F5) before the app will open.

The app opens in a separate browser tab.

## Manage the app
![Command bar](./media/generate-app-from-sharepoint-list-interface/command-bar.png)

* If you click or tap **Edit in PowerApps**, the app opens in a separate browser tab where you can update the app in PowerApps Studio for the web.

* If you click or tap **Make this view public**, other people in your organization can view it. By default, only you can see views that you create. If you want to allow other people to edit your app, you need to [share it with them](share-app.md), and then grant **Can edit** permissions.

* If you click or tap **Remove this view**, you'll remove the view from SharePoint, but the app will remain in PowerApps unless you [delete it](delete-app.md).

## Next steps
* Customize the default [gallery](customize-layout-sharepoint.md), [forms](customize-forms-sharepoint.md), and [cards](customize-card.md).
