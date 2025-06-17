---
title: Create a canvas app with data from a list
description: Create a Power Apps canvas app to manage data in Microsoft Lists or SharePoint Online.
author: mduelae

ms.topic: how-to
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 6/17/2025
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

# Create a canvas app with data from a list


 This article explains how to create a canvas app in Power Apps using data from Microsoft Lists or SharePoint. Learn how to build an app from a list, customize it, and manage your data efficiently. You can also [connect to on-premises SharePoint lists](connections/connection-sharepoint-online.md#create-a-sharepoint-connection) through a data gateway.

The app you create contains three screens:

- **Browse screen**: scroll through all items in the list.
- **Details screen**: show all information about a single item in the list.
- **Edit screen**: create an item or update information about an existing item.

You can also watch this video to learn how to create a canvas app from a list:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=de3b0fbc-f5b6-4958-855e-109f9c3692ac]

> [!NOTE]
> When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list can always be found in both Lists and SharePoint. Learn more in [What is a list in Microsoft 365?](https://support.microsoft.com/en-us/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5)

## Prerequisites

You need access to SharePoint and Power Apps through a [subscription](https://www.microsoft.com/licensing/terms/productoffering) to [Microsoft 365](https://www.microsoft.com/licensing/terms/productoffering/Microsoft365/all) and [Microsoft Power Platform](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerPlatform/all).

## Create a list

Before you create an app from a list, you must [create a list](https://support.microsoft.com/office/create-a-list-0d397414-d95f-41eb-addd-5e6eff41b083).

For example create a list to track device orders for your company. In the list add and fill in the following columns:

1. Employee name
1. Device type
1. Request date
1. Reason for the order
1. Approved or denied
1. Status

    :::image type="content" source="media/app-from-sharepoint/sample-list.png" alt-text="Screenshot of a sample list that's created in Microsoft Lists." lightbox="media/app-from-sharepoint/sample-list.png":::


## Create an app from your list

Now that you have a list, lets create an app from the list.

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. On the left naviation pane, select **Create** > **Start with a page design** > **Gallery connected to external data**.

1. Select **From SharePoint**.

1. Enter the SharePoint URL and then select **Connect**. Or, select a recent site.
 
1. Select a list and then select, **Create app**.

   Your app opens in Power Apps Studio where you can design, build, and manage your app. Learn more in [Understand Power Apps Studio](power-apps-studio.md).

1. Save your work by selecting the **Save** icon in the upper-right corner. Give your app a name, and then select **Save**.



## Create an app from a list

If you create an app from a list in SharePoint or Microsoft Lists, the app appears as a view of that list. You can also run the app on an iOS or Android device, in addition to a web browser.

1. Sign in to SharePoint: `https://yourorganizationname.sharepoint.com`

1. Open a list in either SharePoint or Microsoft Lists. If you open the list from SharePoint, you're taken to Lists to view the list.
1. Select **Integrate** > **Power Apps** > **Create an app**.

   :::image type="content" source="./media/app-from-sharepoint/generate-new-app.png" alt-text="Screenshot that shows the Integrate menu in Lists that lets you create an app in Power Apps.":::

   You're taken to Power Apps Studio and can see your list in an app as a vertical gallery on the **BrowseScreen1** screen.

1. Select the **Save** icon in the upper-right menu bar and name your app and then select **Save**.

## Manage your app

Once you create an app, you can play it, save, share, and publish it.

Learn more about these [App actions](power-apps-studio.md#2--app-actions) in the Power Apps Studio interface.

## Related information

[Move SharePoint Custom Forms with Power Apps (white paper)](https://go.microsoft.com/fwlink/?linkid=2263521)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
