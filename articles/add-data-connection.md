<properties	pageTitle="Add a new data connection | Microsoft PowerApps"
	description="Add a new data connection to an existing app or when building a new blank app"
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
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/13/2016"
   ms.author="archanan"/>

# Add a new data connection #
In this tutorial, you will learn how to add a new data connection to an existing app or when you are building a new app from blank.

**Prerequisites**

- Learn how to build an [app from blank](get-started-create-from-blank.md) in PowerApps
- Account information for the service you want to connect to

## Add datasource to your app  ##
1. In PowerApps, select the **Content** tab in the ribbon.

	![Content tab in the ribbon](./media/add-data-connection/content-tab.png)

1. Select **Data sources**.

	![Data sources](./media/add-data-connection/data-sources.png)

1. The Data sources pane will slide out on the right. Select **Add data source**.

	![Data sources pane](./media/add-data-connection/add-data-source.png)

1. You can select an existing connection OR choose to add a new connection. Let's go through the flow of adding a new connection. Select **Add connection**

	![List of connections](./media/add-data-connection/list-of-connections.png)

1. From the list of available connections, choose the data source you want to connect to, such as **SharePoint Online** and select it.

	![List of APIs](./media/add-data-connection/list-of-api.png)

1. Click **Connect** and provide your credentials for SharePoint Online.

   ![SharePoint Online connect screen](./media/add-data-connection/sharepoint-connect.png)

1. Once the connection is established, select a site from the list of **Recent Sites** OR enter a **New Site**.

	![Select a SharePoint site](./media/add-data-connection/select-sp-site.png)

1. Select the table you want to use in your app using the checkbox. You can also select multiple tables. Select **Connect**.

	![Select the tables in SharePoint](./media/add-data-connection/select-sp-tables.png)

1. The data sources are now added to your app and ready to be consumed.

	![List of datasources addded to the app](./media/add-data-connection/data-sources-list.png)

## Consume the datasource in your app ##

1. For tabular datasources such as SharePoint, SQL, Dynamics CRM or Excel, you will be able to consume the data in the app by binding the imported table to the controls in the app. See how to [show list of items in your app](add-gallery.md) or how to [show, add or edit a record from a table](add-form.md) for more details.

1. For non-tabular datasources such as Twitter, Microsoft Translator, you can consume it in your app by calling functions supported by that service.

	 For example, once you import Microsoft Translator as a datasource in your app (by following steps called out in the previous section), it will show up in the data source pane.

	 ![Twitter datasource](./media/add-data-connection/translator.png)

	 You can add a Text box to your app and bind the "Text" property of the Text box to MicrosoftTranslator.Translate("Hello","fr"). This function will translate the text "Hello" to French and you will see it in the text box.

  ![Function bar for Translator](./media/add-data-connection/translator-func.png)

	![Text box for Translator](./media/add-data-connection/translation-textbox.png)
