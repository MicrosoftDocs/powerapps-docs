<properties	pageTitle="Add a data connection in an app | Microsoft PowerApps"
	description="Add a data connection in an existing app or a blank app"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="archnair"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/23/2016"
   ms.author="archanan"/>

# Add a data connection in an app #
In PowerApps, add a connection in an existing app or an app that you're building from scratch. Connect to SharePoint, Salesforce, OneDrive, or [another data source](connections-list.md), and then display and manage data in that source from your app, as in these examples:

- Connect to OneDrive, and manage data in an Excel workbook in your app.
- Connect to Twilio, and send an SMS message from your app.
- Connect to SQL Azure, and update a table from your app.

You can add a connection in PowerApps, as this topic describes, or on [powerapps.com](https://web.powerapps.com), as [Manage connections](add-manage-connections.md) describes.

**Prerequisites**

- [Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.

## Add a connection ##
1. Click or tap **New** on the **File** menu (near the left edge).

1. Under **Create an app**, click or tap **Phone layout** on the **Blank app** tile.

	![Create an app from scratch](./media/add-data-connection/blank-app.png)

1. In the right-hand pane, click or tap **Add data source**.

	If you're updating an existing app and the right-hand pane doesn't show the **Data sources** tab, select any screen by clicking or tapping it in the left navigation bar.

	![Add data source](./media/add-data-connection/add-data-source.png)

1. To use an existing connection, click or tap it to add it to the app.

	You can use that connection without performing additional steps.

1. To create a connection, click or tap **Add connection** to display a list of connectors, click or tap the type of connection that you want to create, and then click or tap **Connect**.  

	Some connectors, such as **Microsoft Translator**, require no additional steps, and you can show data from them immediately. Other connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. For example, [SharePoint Online](connector-sharepoint-online.md) and [SQL Server](connection-azure-sqldatabase.md) require additional information before you can use them.

## Next steps ##
- To show and update data in a source such as Excel, SharePoint Online, SQL Server, or Dynamics CRM, [add a form](add-form.md).
- For data in other sources, use connector-specific functions such as those for [Office 365 Outlook](connection-office365-outlook.md), [Twitter](connection-twitter.md), and [Microsoft Translator](connection-microsoft-translator.md).
