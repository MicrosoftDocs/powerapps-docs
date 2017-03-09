<properties	pageTitle="Add a data connection in an app | Microsoft PowerApps"
	description="Add a data connection in an existing app or a blank app"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="03/09/2017"
   ms.author="ricksal"/>

# Add a data connection in PowerApps #
In PowerApps, add a data connection to an existing app, or to an app that you're building from scratch. In this topic you use PowerApps Studio, but you can also use [powerapps.com](https://web.powerapps.com), as the [Manage connections](add-manage-connections.md) topic describes.

Your app's data connection can connect to SharePoint, Salesforce, OneDrive, or [one of many other data sources](connections-list.md).

Your [next step](#next-steps) after this article is to display and manage data from that data source in your app, as in these examples:

- Connect to OneDrive, and manage data in an Excel workbook in your app.
- Connect to Twilio, and send an SMS message from your app.
- Connect to SQL Server, and update a table from your app.

## Prerequisites

[Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.

## Background on data connections

Most PowerApps apps use external information called **Data Sources** that is stored in cloud services. A common example is a table in an Excel file stored in OneDrive for Business. Apps are able to access these data sources by using **Connectors**.

The commonest data sources are tables which you can use to retrieve and store information. You can use connectors to data sources to read and write data in Microsoft Excel workbooks, SharePoint lists, SQL tables, and many other formats, which can be stored in cloud services like OneDrive for Business, DropBox, SQL Server, etc.

There are other kinds of data sources that are not tables, such as email, calendars, twitter, and (coming soon) notifications.

Using the Gallery, Display form, and Edit form controls, it is easy to create an app that reads and writes data from a data source. To get started, read the article Understand data forms.


## Add a connection ##
1. Click or tap **New** on the **File** menu (near the left edge).

	![New option on the File menu](./media/add-data-connection/file-new.png)

2. On the **Blank app** tile, click or tap **Phone layout** .

	![Create an app from scratch](./media/add-data-connection/blank-app.png)

3. Near the lower-right corner, click or tap **Data sources** to open the **Data sources** tab of the right-hand pane.

	![Open data sources tab](./media/add-data-connection/data-sources-tab.png)

	**Note**: If you're updating an existing app and the right-hand pane doesn't show the **Data sources** tab, select any screen by clicking or tapping it in the left navigation bar.

4. In the **Data sources** tab, click or tap **Add data source**.

	![Add data source](./media/add-data-connection/add-data-source.png)

5. To use an existing connection, click or tap it to add it to the app.

	You can use that connection without performing additional steps.

6. To create a connection, follow these steps:

	a. Click or tap **Add connection** to display a list of connectors.

	![Add connection](./media/add-data-connection/add-connection.png)

	b. Scroll through the list of connectors until the type of connection that you want to create appears (for example, **Office 365 Outlook**), and then click or tap it.

	![Choose connection](./media/add-data-connection/choose-connection.png)

	c. Click or tap **Connect** to both create the connection and add it to your app.

	![Connect button](./media/add-data-connection/connect-button.png)

	Some connectors, such as **Microsoft Translator**, require no additional steps, and you can show data from them immediately. Other connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. For example, [SharePoint](connection-sharepoint-online.md) and [SQL Server](connection-azure-sqldatabase.md) require additional information before you can use them.

## Next steps ##
- To show and update data in a source such as Excel, SharePoint, or SQL Server, [add a gallery](add-gallery.md), and [add a form](add-form.md).
- For data in other sources, use connector-specific functions such as those for [Office 365 Outlook](connection-office365-outlook.md), [Twitter](connection-twitter.md), and [Microsoft Translator](connection-microsoft-translator.md).
