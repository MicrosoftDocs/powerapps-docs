<properties
	pageTitle="Connectors overview | Microsoft PowerApps"
	description="Overview of all the available connections you can use to build apps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="archnair"
	manager="anneta"
	editor=""
    tags=""/>

<tags
	ms.service="powerapps"
	ms.workload="na"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="article"
	ms.date="08/28/2017"
	ms.author="archanan"/>

# Overview of connectors for PowerApps #
Data is at the core of most apps, including those you build in PowerApps. Data is stored in a *data source*, and you bring that data into your app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. PowerApps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, Twitter, and more. To get started adding data to an app, see [Add a data connection in PowerApps](add-data-connection.md).

The following table has links to more information about our most popular connectors. For a full list of connectors, see the [Microsoft Connector Reference](https://docs.microsoft.com/connectors/).

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|![Common Data Service](./media/connections-list/cdm.png) |[**Common Data Service**](data-platform-intro.md)| &nbsp; |![Office 365 Outlook](./media/connections-list/office365.png) |[**Office 365 Outlook**](./connections/connection-office365-outlook.md)| 
|![SharePoint](./media/connections-list/sharepoint.png) |[**SharePoint**](./connections/connection-sharepoint-online.md)| &nbsp; |![Excel](./media/connections-list/excel.png) |[**Excel**](./connections/connection-excel.md)|
|![SQL Server](./media/connections-list/sql.png) |[**SQL Server**](./connections/connection-azure-sqldatabase.md)| &nbsp; |![OneDrive for Business](./media/connections-list/onedrive.png) |[**OneDrive for Business**](cloud-storage-blob-connections.md)|
|![Dynamics 365](./media/connections-list/dynamics-365.png) |[**Dynamics 365**](./connections/connection-dynamics-crmonline.md)| &nbsp; |![OneDrive](./media/connections-list/onedrive.png) |[**OneDrive**](cloud-storage-blob-connections.md)|
|![Office 365 Users](./media/connections-list/office365.png) |[**Office 365 Users**](./connections/connection-office365-users.md)| &nbsp; |![Dropbox](./media/connections-list/dropbox.png) |[**Dropbox**](cloud-storage-blob-connections.md)|

## Types of connectors
PowerApps has two categories of connectors: standard connectors like the ones listed above, and custom connectors. If you're connecting to a data source that PowerApps supports with a standard connector, use that connector. If you need to connect to another source, like a service that you've built, see [Register and use custom connectors](register-custom-api.md).

Standard connectors behave differently depending on the type of service they connect to and how data is returned by that service. Consider the following three examples:

- Connectors that work with tabular data, such as SharePoint lists, SQL Server tables, and Excel workbooks. PowerApps uses standard in-built functions such as Patch(), Collect(), Update() etc., in order to interact with such tabular data. For more information on working with tabular data, see the following articles:

    [Understand data sources in PowerApps](working-with-data-sources.md)

    [Generate an app from Excel data](get-started-create-from-data.md)

    [Create an app from scratch](get-started-create-from-blank.md) 

- Connectors that call APIs exposed by the underlying service directly. Examples of action connectors are Twitter, Facebook, Office365 Outlook, Office365 Users, Planner etc. PowerApps can directly calls the APIs exposed by the service via the connector. For more information on working with APIs directly, see the following articles:

- [TODO: add link to example here]()

- Blob/Storage connectors are storage connectors, that allow you to connect to Excel files stored on these connectors. Examples of such connectors are OneDrive for Business, Azure Blob, Google Drive, Dropbox etc. For more information on working with cloud storage, see the following articles:
- 
    [Understand data sources in PowerApps](../connections/cloud-storage-blob-connections.md)

    [Generate an app from Excel data](get-started-create-from-data.md)

    [Create an app from scratch](get-started-create-from-blank.md) 



