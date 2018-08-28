---
title: Add and manage connections from canvas apps | Microsoft Docs
description: Add, delete, and update connections from canvas apps to data sources such as SharePoint, SQL Server, and OneDrive for Business
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 03/09/2017
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Manage canvas-app connections in PowerApps
In [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), create a connection to one or more data sources, delete a connection, or update its credentials.

Your canvas app's data connection can connect to SharePoint, SQL Server, Office 365, OneDrive for Business, Salesforce, Excel, and many other [data sources](connections-list.md).

Your next step after this article is to display and manage data from the data source in your app, as in these examples:

* Connect to OneDrive for Business, and manage data in an Excel workbook in your app.
* Update a list on a SharePoint site.
* Connect to SQL Server, and update a table from your app.
* Send email in Office 365.
* Send a tweet.
* Connect to Twilio, and send an SMS message from your app.

## Prerequisites
1. [Sign up](../signup-for-powerapps.md) for PowerApps.
2. Sign in to [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.

## Background on data connections
Most PowerApps apps use external information called **Data Sources** that is stored in cloud services. A common example is a table in an Excel file stored in OneDrive for Business. Apps are able to access these data sources by using **Connections**.

The commonest type of data source is the table, which you can use to retrieve and store information. You can use connections to data sources to read and write data in Microsoft Excel workbooks, SharePoint lists, SQL tables, and many other formats, which can be stored in cloud services like OneDrive for Business, DropBox, SQL Server, etc.

There are other kinds of data sources that are not tables, such as email, calendars, twitter, and (coming soon) notifications.

Using the **[Gallery](controls/control-gallery.md)**, **[Display form](controls/control-form-detail.md)**, and **[Edit form](controls/control-form-detail.md)** controls, it is easy to create an app that reads and writes data from a data source. To get started, read the article [Understand data forms](working-with-forms.md).

In addition to creating and managing connections in [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), you also create connections when you do these tasks:

* Automatically generate an [app from data](app-from-sharepoint.md), such as a custom SharePoint list.
* Update an existing app, or create one from scratch as [add a connection](add-data-connection.md) describes.
* Open an app that another user created and [shared with you](share-app.md).

> [!NOTE]
> If you want to use PowerApps Studio instead, open the **File** menu, and then click or tap **Connections**, [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) opens so that you can create and manage connections there.

## Create a new connection
1. If you have not already done so, log in to [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. In the left navigation bar, click or tap **Connections**.
   
    ![Connections Manage](./media/add-manage-connections/open-connections.png)
3. In the upper-right corner, click or tap **New connection**.
   
    ![Connections Add](./media/add-manage-connections/add-connection.png)
4. Click or tap a connector in the list that appears, and then follow the prompts.
   
   ![Connections Add](./media/add-manage-connections/choose-connection.png)
5. Click or tap the **Create** button.
   
   ![Connections Add](./media/add-manage-connections/create-connection.png)
6. Follow the prompts. Some connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. Others such as **Microsoft Translator**, do not.
   
   For example, these connectors require additional information before you can use them.
   
   * [SharePoint](connections/connection-sharepoint-online.md)
   * [SQL Server](connections/connection-azure-sqldatabase.md)

The new connector appears under **Connections**, and you can [add it to an app](add-data-connection.md).

## Update or delete a connection
In the list of connections, find the connection that you want to update or delete, and then click or tap the ellipsis (3-dots-symbol) on the right of the connection.

![Update connection](./media/add-manage-connections/auth-or-delete.png)

* To update the credentials for a connection, click or tap the key icon, and then provide credentials for that connection.
* To delete the connection, click or tap the trash-can icon.

