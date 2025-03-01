---
title: Connect to SharePoint from a canvas app
description: Connect to SharePoint from a canvas app in Microsoft Power Apps.
author: NickWaggoner
ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 3/1/2025
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType:
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# Connect to SharePoint from a canvas app

:::image type="icon" source="./media/connection-sharepoint-online/sharepointicon.png":::

There are different ways to connect to SharePoint in a canvas app:

- Connect to a SharePoint site to generate an app automatically from a list.
- Create a SharePoint connection before you add data to a new or existing app.

> [!NOTE]
> When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list can always be found in both Microsoft Lists and SharePoint. Learn more in [What is a list in Microsoft 365?](https://support.microsoft.com/en-us/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5).

## Connect SharePoint to an app by creating an app

If you have a SharePoint site with a SharePoint list, you can create an app in Power Apps through the list menu in Microsoft Lists.

The **Integrate** > **Power Apps** > **Create an app** menu in Microsoft Lists takes you to Power Apps and builds an app using your list as a data source.

Learn more in [Create a canvas app with data from Microsoft Lists](../app-from-sharepoint.md).

## Create a SharePoint connection

If you build a new app or have an existing app, you can connect to SharePoint through the **Data** menu in Power Apps.

1. [Sign in to Power Apps](https://make.powerapps.com/).
1. Select **More** > **Connections** in the left navigation bar.

   :::image type="content" source="./media/connection-sharepoint-online/connections-menu.png" alt-text="Screenshot that shows the location of the Connections menu option in the More menu.":::

1. Select **+ New connection** and choose **SharePoint**. A popup appears.

1. Choose either the cloud-services or on-premises option:

    - To connect to SharePoint Online, select **Connect directly (cloud services)** and then **Create**. Provide credentials (if prompted).

        ![To connect to SharePoint Online, select Connect directly (cloud services).](./media/connection-sharepoint-online/select-online.png "Connect to a site")

        The connection is created, and you can add data to an existing app or build an app from scratch.

    - To connect to an on-premises site, select **Connect using on-premises data gateway**.

      Choose **Windows** as the authentication type and add your credentials. If your credentials include a domain name, specify it as `domain\alias`.

      :::image type="content" source="./media/connection-sharepoint-online/specify-creds.png" alt-text="Screenshot of the popup showing how to connect using on-premises data gateway.":::

      Under **Choose a gateway**, select the gateway that you want to use, and then select **Create**.

      > [!NOTE]
      > If you don't have an on-premises data gateway installed, [install one](../gateway-reference.md), and then select the  refresh icon for a list of gateways.

      The connection is created. You can add data to an existing app or build an app from scratch.

## Add data to an existing app

1. In Power Apps Studio, open the app that you want to update, select **Data** on the left-pane.

1. Select **Add data** > **Connectors** > **SharePoint**.

   :::image type="content" source="./media/connection-sharepoint-online/select-sp-site.png" alt-text="Screenshot showing the menu path to connect to SharePoint from the Data menu.":::

1. A side panel opens. Under **Connect to a SharePoint site**, select an entry in the **Recent sites** list (or add your own URL), and then select **Connect**.

1. Under **Choose a list**, select the check box for one or more lists, then select **Connect**:

   :::image type="content" source="./media/connection-sharepoint-online/select-sp-tables.png" alt-text="Screenshot that shows lists you can choose to include.":::

   > [!NOTE]
   > Power Apps supports lists, not template-based lists. If you don't see your list, type the list name in **Enter custom table name** box.
   > :::image type="content" source="./media/connection-sharepoint-online/custom-list.png" alt-text="Screenshot that shows the box where you can add a list name.":::

   You see a confirmation banner that your data source was added to your app.

## Related information

Learn more about working with lists in Power Apps in
[Integrate SharePoint Online into Power Apps overview](../sharepoint-list-integration-overview.md).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
