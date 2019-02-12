---
title: Connectors overview for canvas apps | Microsoft Docs
description: Overview of all the available connections that you can use to build canvas apps
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 08/28/2017
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Overview of canvas-app connectors for PowerApps
Data is at the core of most apps, including those you build in PowerApps. Data is stored in a *data source*, and you bring that data into your app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. PowerApps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, and Twitter. To get started adding data to a canvas app, see [Add a data connection in PowerApps](add-data-connection.md).

A connector may provide **tables** of data or **actions**. Some connectors provide only tables, some provide only actions, and some provide both. Also your connector may be either a standard or custom connector.

## Tables

If your connector provides tables, you add your data source and then select the table in the data source that you want to manage. PowerApps both retrieves table data into your app and updates data in your data source for you. For example, you can add a data source that contains a table named **Lessons** and then set the **Items** property of a control, such as a gallery or a form, to this value in the formula bar:

 ![Plain data source Items property](./media/connections-list/ItemPropertyPlain.png)

You can specify the data that your app retrieves by customing the **Items** property of the control that shows your data. Continuing the previous example, you can sort or filter the data in the **Lessons** table by using that name as an argument for the **Search** and **SortByColumn** functions. In this graphic, the formula to which the **Items** property is set specifies that the data is sorted and filtered based on the text in **TextSearchBox1**. 

 ![Expanded data source Items property](./media/connections-list/ItemPropertyExpanded.png)

For more information about how to to customize your formula with tables, see these topics:

  [Understand data sources in PowerApps](working-with-data-sources.md)<br> 
  [Generate an app from Excel data](get-started-create-from-data.md)<br> 
  [Create an app from scratch](get-started-create-from-blank.md)<br>
  [Understand tables and records in PowerApps](working-with-tables.md)

  > [!NOTE]
  > To connect to data in an Excel workbook, it must be hosted in a cloud-storage service such as OneDrive. For more information, see [Connect to cloud-storage from PowerApps](connections/cloud-storage-blob-connections.md).

## Actions

If your connector provides actions, you must still select your data source as you did before. Instead of selecting a table as the next step, however, you manually connect a control to an action by editing the **Items** property of the control that will show your data. The formula to which you set the **Items** property specifies the action that retrieves data. For example, the app won't retrieve any data if you connect to Yammer and then set the **Items** property to the name of the data source. To populate a control with data, specify an action such as **GetMessagesInGroup(5033622).messages**.

![Action data source Items property](./media/connections-list/ItemPropertyAction.png)

If you need to handle custom data updates for action connectors, build a formula that includes the **Patch** function. In the formula, identify the action and the fields that you'll bind to the action.  

For more information about how to to customize your formula for custom updates, see these topics:

[Patch](functions/function-patch.md)<br>[Collect](functions/function-clear-collect-clearcollect.md)<br>[Update](functions/function-update-updateif.md)

## Popular connectors

This table has links to more information about our most popular connectors. For a complete list of connectors, see [All connectors](https://docs.microsoft.com/connectors/).

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- |
| ![Common Data Service](./media/connections-list/cdm.png) |[**Common Data Service**](../common-data-service/data-platform-intro.md) |&nbsp; |![Office 365 Outlook](./media/connections-list/office365.png) |[**Office 365 Outlook**](connections/connection-office365-outlook.md) |
| ![SharePoint](./media/connections-list/sharepoint.png) |[**SharePoint**](connections/connection-sharepoint-online.md) |&nbsp; |![Excel](./media/connections-list/excel.png) |[**Excel**](connections/connection-excel.md) |
| ![SQL Server](./media/connections-list/sql.png) |[**SQL Server**](connections/connection-azure-sqldatabase.md) |&nbsp; |![OneDrive for Business](./media/connections-list/onedrive.png) |[**OneDrive for Business**](connections/cloud-storage-blob-connections.md) |
| ![Dynamics 365](./media/connections-list/dynamics-365.png) |[**Dynamics 365**](connections/connection-dynamics-crmonline.md) |&nbsp; |![OneDrive](./media/connections-list/onedrive.png) |[**OneDrive**](connections/cloud-storage-blob-connections.md) |
| ![Office 365 Users](./media/connections-list/office365.png) |[**Office 365 Users**](connections/connection-office365-users.md) |&nbsp; |![Dropbox](./media/connections-list/dropbox.png) |[**Dropbox**](connections/cloud-storage-blob-connections.md) |

## Standard and custom connectors
PowerApps provides *standard* connectors for many commonly used data sources, such as those listed above. If PowerApps has a standard connector for the type of data source that you want to use, you should use that connector. If you want to connect to other types of data sources, such as a service that you've built, see [Register and use custom connectors](../canvas-apps/register-custom-api.md).

## All standard connectors
See the [Microsoft Connector Reference](https://docs.microsoft.com/connectors/) for a list of all the standard connectors. Premium connectors require PowerApps Plan 1 or Plan 2. For more information, see [PowerApps Plans](https://powerapps.microsoft.com/pricing/).

You can ask questions about a specific connector in the [PowerApps forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1), and you can suggest connectors to add or other improvements to make in [PowerApps Ideas](https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas).
