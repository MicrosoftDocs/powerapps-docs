---
title: Connect to SQL Server from Power Apps overview
description: Learn how to connect to a SQL server to access and view data from Microsoft Power Apps.
author: lancedMicrosoft
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2024
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# Connect to SQL Server from Power Apps overview

There are different ways to connect to data in SQL Server in your Power Apps app, using Power Fx formulas. You can access data directly or use a view or stored procedures to create, update, or delete data in your app.

## Prerequisites

To access data directly, you can create a *Start with data* app for your SQL Server data. This method lets you get a basic, working app that you can modify with views and stored procedures.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and go to the **Apps** page.
1. Select **New app** > **Start with data**.

   :::image type="content" source="media/sql-connection/new-app-start-with-data.png" alt-text="Screenshot that shows how to create an app by starting with data under the New app menu.":::
1. From the **Start with data** page, choose **Connect external data**.
1. Under **Choose a data set to start** select **From SQL**.

   If you have an existing SQL Server connection, it loads.

   > [!NOTE]
   > If you don't already have a SQL Server connection, you're prompted to create one.
1. Select your SQL connection.
1. Enter your **Server** name and **Database name**, then choose **Connect**. Choose a table from the list of tables that appear.

   :::image type="content" source="media/sql-connection/sql-server-details.png" alt-text="Screenshot that shows the Create an app page where you can choose a SQL Server connection, including a table.":::

   > [!NOTE]
   > Only one connection is shown at a time. To use a different connection, select the **...** overflow menu on your SQL connection, then find a new one or create a new SQL connection.

1. Select **Create app**.

## Access data

Once your app is connected to SQL Server, you can access data: [Access data in SQL Server](sql-connection-access-data.md).

## View results

To view the results of your SQL queries, see: [View results in SQL Server](sql-connection-view-results.md).

## Related information
