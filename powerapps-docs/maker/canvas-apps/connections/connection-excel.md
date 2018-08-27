---
title: Overview of the Excel connection | Microsoft Docs
description: Display and update data in Excel by storing the workbook in a cloud-storage account and then connecting to the data from your app.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/02/2016
ms.author: lanced
ms.reviewer: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Connect to Excel from PowerApps
![Excel](./media/connection-excel/excelicon.png)

Excel is *kind of* a connection. To display Excel data in your app:

1. [Format the Excel data as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).
2. Store the Excel file in a cloud-storage account, such as Box, Dropbox, Google Drive, OneDrive, and OneDrive for Business.
3. [Connect to the cloud-storage account](../add-manage-connections.md), and then add the Excel table as a data source.
4. Display this information in your app by [generating an app automatically](../get-started-create-from-data.md) or by adding and configuring, for example, a **Gallery** control.

> [!NOTE]
> When you connect to your Excel table from PowerApps, it will create a column called **\_PowerAppsId_**, with a unique ID for each row of your Excel table.

[Overview of the cloud-storage connection](cloud-storage-blob-connections.md) shows you how to add the connection, add an Excel table as a data source, and use the Excel data in your app.

For information about how to connect to other types of data, see the [list of connections for PowerApps](../connections-list.md).

### Known limitations
For information about how to share Excel data within your organization, [review these limitations](cloud-storage-blob-connections.md#sharing-excel-tables).

