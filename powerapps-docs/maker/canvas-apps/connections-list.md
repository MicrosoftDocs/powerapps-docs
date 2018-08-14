---
title: Connectors overview | Microsoft Docs
description: Overview of all the available connections you can use to build apps
author: lancedMicrosoft
manager: kvivek

ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/28/2017
ms.author: lanced

---
# Overview of connectors for PowerApps
Data is at the core of most apps, including those you build in PowerApps. Data is stored in a *data source*, and you bring that data into your app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. PowerApps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, Twitter, and more. To get started adding data to an app, see [Add a data connection in PowerApps](add-data-connection.md).

A connector may provide **tables** of data or **actions**. Some connectors only provide tables and some only provide actions and some provide both. Also your connector may be either a standard or custom connector.

## Tables

If your connector provides tables then you can simply first add and select your data source.  Then select the table in the data source you wish to work with. PowerApps handles both the retrieval of table data into your app and the update of data in your data source for you. For example, if you are working with a table in your data source named "Lessons" the Items property in the formula bar will appear as follows in the control where it is used (e.g., a gallery or a form):

 ![Plain data source Items property](./media/connections-list/ItemPropertyPlain.png)

You can easily customize the data that your app retrieves by customing the Items property on the control where your data appears. To continue with the "Lessons" example, if you want to sort or filter the data you can add additional commands in the Items property formula to accomplish it. In the example below, Items property formula specifies a search and sort of data in the data source based on the text input from TextSearchBox1. 

 ![Expanded data source Items property](./media/connections-list/ItemPropertyExpanded.png)

For more information on how to to customize your formula with tables see the following articles:

  [Understand data sources in PowerApps](working-with-data-sources.md),  [Generate an app from Excel data](get-started-create-from-data.md),  [Create an app from scratch](get-started-create-from-blank.md),  [Understand tables and records in PowerApps](working-with-tables.md)

    > [!NOTE]
  > To connect to data in Excel, the workbook must be hosted in a cloud-storage service like OneDrive. For more information, see [Connect to cloud-storage from PowerApps](connections/cloud-storage-blob-connections.md).


## Actions

If your connector provides actions then, as with tables, you must first select your data source. But you do not select a table. You  must manually connect your control to an action. Edit the Items property formula of the control that will show your data. As you author the formula, select an action to get data. For example if you are working with Yammer, simply typing the name of the data source will not retrieve any data.  Selecting a specific action like "GetMessagesInGroup(5033622).messages" will populate your control with data.

![Action data source Items property](./media/connections-list/ItemPropertyAction.png)

Handle custom data updates for action connectors via a "Patch" command where you identify the action to use and the fields you will bind to the action.  

For more information on how to to customize your formula for custom updates, see the following articles:

[Patch()](functions/function-patch.md), [Collect()](functions/function-clear-collect-clearcollect.md), [Update()](functions/function-update-updateif.md)


## Popular connectors

The following table has links to more information about our most popular connectors. For a complete list of connectors, see [All connectors](#all-connectors).

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- |
| ![Common Data Service](./media/connections-list/cdm.png) |[**Common Data Service**](../common-data-service/data-platform-intro.md) |&nbsp; |![Office 365 Outlook](./media/connections-list/office365.png) |[**Office 365 Outlook**](connections/connection-office365-outlook.md) |
| ![SharePoint](./media/connections-list/sharepoint.png) |[**SharePoint**](connections/connection-sharepoint-online.md) |&nbsp; |![Excel](./media/connections-list/excel.png) |[**Excel**](connections/connection-excel.md) |
| ![SQL Server](./media/connections-list/sql.png) |[**SQL Server**](connections/connection-azure-sqldatabase.md) |&nbsp; |![OneDrive for Business](./media/connections-list/onedrive.png) |[**OneDrive for Business**](connections/cloud-storage-blob-connections.md) |
| ![Dynamics 365](./media/connections-list/dynamics-365.png) |[**Dynamics 365**](connections/connection-dynamics-crmonline.md) |&nbsp; |![OneDrive](./media/connections-list/onedrive.png) |[**OneDrive**](connections/cloud-storage-blob-connections.md) |
| ![Office 365 Users](./media/connections-list/office365.png) |[**Office 365 Users**](connections/connection-office365-users.md) |&nbsp; |![Dropbox](./media/connections-list/dropbox.png) |[**Dropbox**](connections/cloud-storage-blob-connections.md) |



## Standard and Custom
PowerApps connectors are either *standard* like the ones listed above or *custom connectors*. If you're connecting to a data source that PowerApps supports with a standard connector, use that connector. If you need to connect to another source, like a service that you've built, see [Register and use custom connectors](../canvas-apps/register-custom-api.md).

Standard connectors behave differently depending on the type of data source they connect to and how data is returned by that data source:

## All connectors
See the [Microsoft Connector Reference](https://docs.microsoft.com/connectors/) for a list of all our connectors. Premium connectors require PowerApps Plan 1 or Plan 2. For more information, see [PowerApps Plans](https://powerapps.microsoft.com/pricing/).


If you have questions about a specific connector, please use the [PowerApps Forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1). If you have an idea for a new connector or suggestions for improvement, use [PowerApps Ideas](https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas).
