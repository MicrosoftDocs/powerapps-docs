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

1. The Data sources pane will slide out on the right. Select **Insert your data**.

	![Data sources pane](./media/add-data-connection/data-source-pane.png)

1. Select an existing connection OR choose to add a new connection.

	![List of connections](./media/add-data-connection)

1. To add a new connection, select **Add**.

	![Add button](./media/add-data-connection)

1. From the list of available connections

	![List of available connections](./media/add-data-connection)

1.  Choose the data source you want to connect to, such as **SharePoint Online** and click **Connect**.

	![SharePoint Online connect screen](./media/add-data-connection)

1. Select site from the list of **Recent Sites** OR enter a **New Site**.

	![Select a SharePoint site](./media/add-data-connection)

1. Select the table you want to use in your app using the checkbox. You can also select multiple tables. Select **Connect**.

	![Select the tables in SharePoint that you want to use](./media/add-data-connection)

1. The data sources are now added to your app and ready to be consumed.

	![List of datasources addded to the app](./media/add-data-connection)

## Consume the datasource in your app ##

1. For tabular datasources such as SharePoint, SQL, Dynamics CRM or Excel, you will be able to consume the data in the app by binding the imported table to the controls in the app. See [app from blank](get-started-create-from-blank.md) for more details.

1. For non-tabular datasources such as Twitter, Microsoft Translator, you can consume it in your app by calling functions supported by that service.

	 For example, once you import Microsoft Translator as a datasource in your app (by following steps called out in the previous section), you can bind the "Text" property of the Text box to MicrosoftTranslator.Translate("Hello","fr"). This function will translate the text "Hello" to French and you will see it in the text box.

  ![Function bar for Translator](./media/add-data-connection)

	![Text box for Translator](./media/add-data-connection)
