---
title: Manage connections in canvas apps
description: Add, delete, and update connections from canvas apps to data sources such as SharePoint, SQL Server, and OneDrive for Business.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/05/2020
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedmicrosoft
---
# Manage connections in canvas apps

In [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), create a connection to one or more data sources, delete a connection, or update its credentials.

Your canvas app's data connection can connect to SharePoint, SQL Server, Office 365, OneDrive for Business, Salesforce, Excel, and many other [data sources](connections-list.md).

Your next step after this article is to display and manage data from the data source in your app, as in these examples:

* Connect to OneDrive for Business, and manage data in an Excel workbook in your app.
* Update a list on a SharePoint site.
* Connect to SQL Server, and update a table from your app.
* Send email in Office 365.
* Send a tweet.
* Connect to Twilio, and send an SMS message from your app.

## Prerequisites
1. [Sign up](../signup-for-powerapps.md) for Power Apps.
2. Sign in to [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.

## Background on data connections
Most Power Apps apps use external information called **Data Sources** that is stored in cloud services. A common example is a table in an Excel file stored in OneDrive for Business. Apps are able to access these data sources by using **Connections**.

The most common type of data source is the table, which you can use to retrieve and store information. You can use connections to data sources to read and write data in Microsoft Excel workbooks, SharePoint lists, SQL tables, and many other formats, which can be stored in cloud services like OneDrive for Business, DropBox, SQL Server, etc.

There are other kinds of data sources that are not tables, such as email, calendars, twitter, and notifications.

Using the **[Gallery](controls/control-gallery.md)**, **[Display form](controls/control-form-detail.md)**, and **[Edit form](controls/control-form-detail.md)** controls, it is easy to create an app that reads and writes data from a data source. To get started, read the article [Understand data forms](working-with-forms.md).

In addition to creating and managing connections in [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), you also create connections when you do these tasks:

* Automatically generate an [app from data](app-from-sharepoint.md), such as a custom SharePoint list.
* Update an existing app, or create one from scratch as [add a connection](add-data-connection.md) describes.
* Open an app that another user created and [shared with you](share-app.md).

> [!NOTE]
> If you want to use Power Apps Studio instead, open the **File** menu, and then click or tap **Connections**, [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) opens so that you can create and manage connections there.

## Create a new connection
1. If you have not already done so, log in to [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. In the left navigation, expand **Data** and select **Connections**.
   
    ![Connections Manage.](./media/add-manage-connections/open-connections.png)
3. Select **New connection**.
   
    ![New connection.](./media/add-manage-connections/add-connection.png)
4. Select a connector in the list that appears, and then follow the prompts.
   
   ![Select a connector.](./media/add-manage-connections/choose-connection.png)
5. Select the **Create** button.
   
   ![Select Create.](./media/add-manage-connections/create-connection.png)
6. Follow the prompts. Some connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. Others such as **Microsoft Translator**, do not.
   
   For example, these connectors require additional information before you can use them.
   
   * [SharePoint](connections/connection-sharepoint-online.md)
   * [SQL Server](connections/connection-azure-sqldatabase.md)

The new connector appears under **Connections**, and you can [add it to an app](add-data-connection.md).

## Update or delete a connection
In the list of connections, find the connection that you want to update or delete, and then select the ellipsis (...) on the right of the connection.

![Update connection.](./media/add-manage-connections/auth-or-delete.png)

* To update the credentials for a connection, select the key icon, and then provide credentials for that connection.
* To delete the connection, select delete.
* Select the information icon to see the connection details.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]