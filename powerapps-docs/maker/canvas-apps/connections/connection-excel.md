---
title: Connect to Excel from Power Apps
description: Display and update data in Excel by storing the workbook in a cloud-storage account and then connecting to the data from your app.
author: lancedMicrosoft

ms.topic: reference
ms.custom: canvas
ms.date: 01/27/2022
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
---
# Connect to Excel from Power Apps

Excel is a connection that becomes a data source when added to Power Apps. To connect to Excel from Power Apps, follow these three steps.

## Step 1 - Format your data as a table in Excel

Ensure that the Excel data you want to use in Power Apps is [formatted as a table in Excel](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).

## Step 2 - Store your Excel file in a cloud location

Store the Excel file in a cloud-storage account, such as Dropbox, Google Drive, OneDrive, and OneDrive for Business. There are two versions of the Excel connector. The newer version of the connector can access more cloud locations.

## Step 3 - Add Excel as a data source for your Power App

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Depending on how you want to create your app, from the home screen, select one of the following options:
   - To create a single-page gallery app with a responsive layout, choose either:
     - **Start with data** > **Connect to external data** > **From Excel**.
     - **Start with page design** > **Gallery connected to external data** > **From Excel**.
   - To create a three screen mobile app, select **Start with an app template** > **From Excel**.
1. Only one connection is shown at a time. To select a different connection, select on the **...** button to switch connection or add a new connection.
1. Enter the file location and select the table.
1. When you're done, select **Create app**.


## Other connectors

For information about how to connect to other types of data, see the [list of connections for Power Apps](../connections-list.md).

## Known limitations

For information about how to share Excel data within your organization, [review these limitations](cloud-storage-blob-connections.md#sharing-excel-tables).

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
