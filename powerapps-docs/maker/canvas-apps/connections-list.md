---
title: Connectors overview for canvas apps | Microsoft Docs
description: Overview of all the available connections you can use to build canvas apps
author: lancedMicrosoft
manager: kvivek

ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/28/2017
ms.author: lanced

---
# Overview of canvas-app connectors for PowerApps
Data is at the core of most apps, including those you build in PowerApps. Data is stored in a *data source*, and you bring that data into your canvas app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. PowerApps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, Twitter, and more. To get started adding data to a canvas app, see [Add a data connection in PowerApps](add-data-connection.md).

The following table has links to more information about our most popular connectors. For a complete list of connectors, see [All connectors](#all-connectors).

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- |
| ![Common Data Service](./media/connections-list/cdm.png) |[**Common Data Service**](../common-data-service/data-platform-intro.md) |&nbsp; |![Office 365 Outlook](./media/connections-list/office365.png) |[**Office 365 Outlook**](connections/connection-office365-outlook.md) |
| ![SharePoint](./media/connections-list/sharepoint.png) |[**SharePoint**](connections/connection-sharepoint-online.md) |&nbsp; |![Excel](./media/connections-list/excel.png) |[**Excel**](connections/connection-excel.md) |
| ![SQL Server](./media/connections-list/sql.png) |[**SQL Server**](connections/connection-azure-sqldatabase.md) |&nbsp; |![OneDrive for Business](./media/connections-list/onedrive.png) |[**OneDrive for Business**](connections/cloud-storage-blob-connections.md) |
| ![Dynamics 365](./media/connections-list/dynamics-365.png) |[**Dynamics 365**](connections/connection-dynamics-crmonline.md) |&nbsp; |![OneDrive](./media/connections-list/onedrive.png) |[**OneDrive**](connections/cloud-storage-blob-connections.md) |
| ![Office 365 Users](./media/connections-list/office365.png) |[**Office 365 Users**](connections/connection-office365-users.md) |&nbsp; |![Dropbox](./media/connections-list/dropbox.png) |[**Dropbox**](connections/cloud-storage-blob-connections.md) |

## Types of connectors
PowerApps has two types of connectors: *standard connectors* like the ones listed above, and *custom connectors*. If you're connecting to a data source that PowerApps supports with a standard connector, use that connector. If you need to connect to another source, like a service that you've built, see [Register and use custom connectors](../canvas-apps/register-custom-api.md).

Standard connectors behave differently depending on the type of data source they connect to and how data is returned by that data source:

* Some connectors work with tabular data sources, such as SharePoint, SQL Server, and Excel. When working with these data sources, data is returned to PowerApps as a table. PowerApps uses its own functions, such as [Patch()](functions/function-patch.md), [Collect()](functions/function-clear-collect-clearcollect.md), [Update()](functions/function-update-updateif.md), and so on to interact with the data. Tabular data is also easy to use in forms and galleries, where a field in a table is displayed as a field in a gallery or form. For more information, see the following articles:

    [Understand data sources in PowerApps](working-with-data-sources.md)

    [Generate an app from Excel data](get-started-create-from-data.md)

    [Create an app from scratch](get-started-create-from-blank.md)

    > [!NOTE]
  > To connect to data in Excel, the workbook must be hosted in a cloud-storage service like OneDrive. For more information, see [Connect to cloud-storage from PowerApps](connections/cloud-storage-blob-connections.md).

* Other connectors work with function-based data sources, such as Twitter, Facebook, and Office 365 Outlook. When working with these data sources, data is returned to PowerApps based on calling specific functions in the underlying service. For example, with the Twitter connector you call `Twitter.MyFollowers()` to return a list of your followers. You can still use this data in a form or gallery, but it requires a little more work than tabular data. For more information, see [Connect to Twitter from PowerApps](connections/connection-twitter.md).

## All connectors
See the [Microsoft Connector Reference](https://docs.microsoft.com/connectors/) for a list of all our connectors. Premium connectors require PowerApps Plan 1 or Plan 2. For more information, see [PowerApps Plans](https://powerapps.microsoft.com/pricing/).


If you have questions about a specific connector, please use the [PowerApps Forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1). If you have an idea for a new connector or suggestions for improvement, use [PowerApps Ideas](https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas).
