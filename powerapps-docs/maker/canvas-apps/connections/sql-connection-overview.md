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

There are different ways to connect to data in SQL Server in your Power Apps app. You can access data using a view and then use stored procedures to create, update, or delete data in your Power Apps app.

The results of your view and stored procedures can be made using formulas.

## Prerequisites

Before accessing data in your app, create an app enabled with SQL Server. You can create an app through either a single-page gallery or a three-screen mobile option.

Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and go to the **Home** page.

### Single-page gallery

To create a single-page gallery app with a responsive layout, choose either:

- **Start with data** > **Connect external data** > **From SQL**.
- **Start with a page design** > **Gallery connected to external data** > **From SQL**.

### Three-screen mobile

1. Select **Start with an app template** > **From SQL**.
1. Select your SQL connection and choose a table. To use a different connection, select the **...** overflow menu to switch your connection or create a new SQL connection.

   > [!NOTE]
   > Only one connection is shown at a time.
1. Select **Create app**.

## Access data

Once your app is connected to SQL Server, you can access data: [Access data in SQL Server](sql-access-data.md).

## View results

To view the results of your SQL queries: [View results in SQL Server](sql-view-results.md).

## Related information
