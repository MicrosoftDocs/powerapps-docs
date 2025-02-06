---
title: Create a canvas app with data from Microsoft Lists
description: Create a canvas app to manage data in a Microsoft Lists list in Power Apps.
author: mduelae

ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 2/5/2025
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - Steven-Jia
  - mduelae
  - navjotm
  - emcoope-msft
---

# Create a canvas app with data from Microsoft Lists

In this article, you can create a canvas app in Power Apps from a Microsoft List list. You can create the app from within Power Apps or SharePoint Online. Alternatively, you can create the app based on a list in an on-premises SharePoint site if you [connect to it](connections/connection-sharepoint-online.md#create-a-connection) through a data gateway.

The app you create contains three screens:

- In the browse screen, you can scroll through all items in the list.
- In the details screen, you can show all information about a single item in the list.
- In the edit screen, you can create an item or update information about an existing item.

## Prerequisites

You need access to SharePoint Online and Power Apps through a [subscription](https://www.microsoft.com/licensing/terms/productoffering) to [Microsoft 365](https://www.microsoft.com/licensing/terms/productoffering/Microsoft365/all) and [Microsoft Power Platform](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerPlatform/all).

## Create a list

1. [Create a list](https://support.microsoft.com/office/create-a-list-0d397414-d95f-41eb-addd-5e6eff41b083) in Sharepoint Online or Microsoft Lists named, for example,  **SimpleList**.
1. In the list column named **Title**, add items to the list for **Vanilla**, **Chocolate**, and **Strawberry**.

> [!IMPORTANT]
> Power Apps doesn't support all types of SharePoint data. For more information, see [Known issues](connections/connection-sharepoint-online.md#known-issues).

Watch this video to learn how to create a canvas app from a list:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=de3b0fbc-f5b6-4958-855e-109f9c3692ac]

## Create an app in Power Apps

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. To create a single-page gallery app select **Start with a page design** > **Gallery connected to external data** > **From SharePoint**.
1. To create a three screen mobile app, select **Start with an app template** > **From SharePoint**.

   You see a SharePoint connection appear or are prompted to create a connection. To select a different connection, select on the **...** option to switch accounts or create a new connection.
1. Enter the SharePoint URL and then select **Connect**. Or, select a recent site.
1. Select a list and then select, **Create app**.

   Your app opens in Power Apps Studio where you can design, build, and manage your app. Learn more in [Understand Power Apps Studio](power-apps-studio.md).

1. Save your work by selecting the **Save** icon in the upper-right corner. Give your app a name, and then select **Save**.

## Create an app from SharePoint Online

If you create an app from a list in SharePoint Online, the app appears as a view of that list. You can also run the app on an iOS or Android device, in addition to a web browser.

1. Sign in to SharePoint Online: `https://yourorganizationname.sharepoint.com`

1. Open a list. You're taken to Microsoft Lists to view the list.
1. Select **Integrate** > **Power Apps** > **Create an app**.

   :::image type="content" source="./media/app-from-sharepoint/generate-new-app.png" alt-text="Screenshot that shows the Integrate menu in Microsoft Lists that lets you create an app in Power Apps.":::

   You're taken to Power Apps Studio and see your list in an app as a vertical gallery on the **BrowseScreen1** screen.

1. Select the **Save** icon in the upper-right menu bar and name your app **SimpleApp**. Select **Save**.

## Manage your app

Once you create an app, you can play it, save, share, and publish it.

Learn more about these [App actions](power-apps-studio.md#2--app-actions) in the Power Apps Studio interface.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
