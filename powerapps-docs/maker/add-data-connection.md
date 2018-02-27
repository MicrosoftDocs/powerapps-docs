---
title: Add a data connection in an app | Microsoft Docs
description: Add a data connection in an existing app or a blank app
services: ''
suite: powerapps
documentationcenter: na
author: archnair
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/02/2017
ms.author: archanan

---
# Add a data connection in PowerApps
In PowerApps, add a data connection to an existing app or to an app that you're building from scratch. In this topic, you use PowerApps Studio, but you can also use [powerapps.com](https://web.powerapps.com), as the [Manage connections](add-manage-connections.md) topic describes.

Your app's data connection can connect to SharePoint, Salesforce, OneDrive, or [one of many other data sources](connections-list.md).

Your [next step](#next-steps) after this article is to display and manage data from that data source in your app, as in these examples:

* Connect to OneDrive, and manage data in an Excel workbook in your app.
* Connect to Twilio, and send an SMS message from your app.
* Connect to SQL Server, and update a table from your app.

## Prerequisites
[Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.

## Background on data connections
Most PowerApps apps use external information called **Data Sources** that is stored in cloud services. A common example is a table in an Excel file stored in OneDrive for Business. Apps are able to access these data sources by using **Connectors**.

The most common data sources are tables, which you can use to retrieve and store information. You can use connectors to data sources to read and write data in Microsoft Excel workbooks, SharePoint lists, SQL tables, and many other formats, which can be stored in cloud services such as OneDrive for Business, DropBox, SQL Server, etc.

Data sources other than tables include email, calendars, Twitter, and notifications.

Using the **[Gallery](../controls/control-gallery.md)**, **[Display form](../controls/control-form-detail.md)**, and **[Edit form](../controls/control-form-detail.md)** controls, it's easy to create an app that reads and writes data from a data source. To get started, read the article [Understand data forms](working-with-forms.md).

## Add a connection
1. Click or tap **New** on the **File** menu (near the left edge).

    ![New option on the File menu](./media/add-data-connection/file-new.png)

2. On the **Blank app** tile, click or tap **Phone layout** .

    ![Create an app from scratch](./media/add-data-connection/blank-app.png)

3. In the center pane, click or tap **connect to data**.

4. If the list of connections in the **Data** pane includes the one that you want, click or tap it to add it to the app. Otherwise, skip to the next step.

    ![Add data source](./media/add-data-connection/choose-existing-connections.png)

5. Click or tap **New connection** to display a list of connectors.

    ![Add connection](./media/add-data-connection/new-connection.png)

6. Scroll through the list of connectors until the type of connection that you want to create appears (for example, **Office 365 Outlook**), and then click or tap it.

    ![Choose connection](./media/add-data-connection/choose-connection.png)

7. Click or tap **Create** to both create the connection and add it to your app.

    Some connectors, such as **Microsoft Translator**, require no additional steps, and you can show data from them immediately. Other connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. For example, [SharePoint](../connections/connection-sharepoint-online.md) and [SQL Server](../connections/connection-azure-sqldatabase.md) require additional information before you can use them.

## View or change a data source
If you're updating an app, you might need to identify or change the source of data that appears in a gallery, a form, or another control that has an **Item** property. For example, you might be working on an app that someone else created, or you might want to remind yourself of a data source that you configured a while ago.

1. Select the control for which you want to identify the data source.

    For example, select a gallery (not a control within the gallery) by clicking or tapping it in the hierarchical list of screens and controls near the left edge.

    The name of the data source appears on the **Properties** tab of the right-hand pane.

    ![Data source on Properties tab](./media/add-data-connection/properties-tab.png)

2. To show more information about the data source or change it, click or tap **Data** in the right-hand pane.

    ![Data pane](./media/add-data-connection/data-pane.png)

3. To change the data source, click or tap the down arrow next to the data source, and then choose or create another source.

## Next steps
* To show and update data in a source such as Excel, SharePoint, or SQL Server, [add a gallery](add-gallery.md), and [add a form](add-form.md).
* For data in other sources, use connector-specific functions such as those for [Office 365 Outlook](../connections/connection-office365-outlook.md), [Twitter](../connections/connection-twitter.md), and [Microsoft Translator](../connections/connection-microsoft-translator.md).
