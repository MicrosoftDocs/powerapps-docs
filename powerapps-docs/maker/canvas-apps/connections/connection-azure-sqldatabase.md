---
title: Connect to SQL Server from Power Apps
description: Step-by-step instructions for how to connect to Azure SQL or an on-premises SQL Server database
author: lancedMicrosoft

ms.topic: reference
ms.custom: canvas
ms.date: 01/05/2024
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---
# Connect to SQL Server from Power Apps

Connect to SQL Server, in either Azure or an on-premises database, so that you can manage your data with create, read, update, and delete operations.

> [!NOTE] 
> Newly created SQL data sources are no longer prefixed with "[dbo]" as they have been in previous versions of Power Apps. See the [common issues and resolutions](/troubleshoot/power-platform/power-apps/common-issues-and-resolutions) page for more information.

## Prerequisites

* [Sign up](../../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.
* Gather the following information for a database that contains at least one table with a primary key:
  
  * the name of the database
  * the name of the server on which the database is hosted
  * a valid user name and password to connect to the database
  * the type of authentication needed to connect to the database
    
    If you don't have this information, ask the administrator of the database that you want to use.
* For an on-premises database, identify a [data gateway](../gateway-management.md) that was shared with you (or create one).

## Generate an app automatically


Depending upon whether you have the [new look](../intro-maker-portal.md?tabs=home-new-look) or [classic look](../intro-maker-portal.md?tabs=home-classic) turned on, select the appropriate tab below to know more.


1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Depending on how you want to create your app, from the home screen, select one of the following options:
   - To create a single-page gallery app with a responsive layout, choose either:
     - **Start with data** > **Connect to external data** > **From SQL**.
     - **Start with a page design** > **Gallery connected to external table** > **From SQL**.
   - To create a three screen mobile app, select **Start with an app template** > **From SQL**.
1. Select your SQL connection and then select a table. Note, that only one connection is shown at a time. To select a different connection, select on the **...** button to switch connection or create a new SQL connection.
1. When you're done, select **Create app**.

## Known issues

### SQL data sources no longer adds a "[dbo]" prefix to the data source name

The "[dbo]" prefix does not serve any practical purpose in Power Apps as datasource names are automatically disambiguated. Existing data sources won't be affected, but any newly added SQL data sources won't include the prefix. If you need to update a large number of formulas in one of your apps, the [Power Apps Source File Pack and Unpack Utility](https://powerapps.microsoft.com/blog/source-code-files-for-canvas-apps/) can be used to do a global search-and-replace.

Starting in version 3.21054, we'll automatically update broken legacy name references to the new data source name after reading the data source.

## Next steps

* Learn how to [show data from a data source](../add-gallery.md).
* Learn how to [view details and create or update records](../add-form.md).
* See other types of [data sources](../connections-list.md) to which you can connect.  
* [Understand tables and records](../working-with-tables.md) with tabular data sources.

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
