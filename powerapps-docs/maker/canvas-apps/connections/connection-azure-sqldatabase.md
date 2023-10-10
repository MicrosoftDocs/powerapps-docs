---
title: Connect to SQL Server from Power Apps
description: Step-by-step instructions for how to connect to Azure SQL or an on-premises SQL Server database
author: lancedMicrosoft

ms.topic: reference
ms.custom: canvas
ms.date: 04/28/2021
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




## Next steps
* Learn how to [show data from a data source](../add-gallery.md).
* Learn how to [view details and create or update records](../add-form.md).
* See other types of [data sources](../connections-list.md) to which you can connect.  
* [Understand tables and records](../working-with-tables.md) with tabular data sources.

<!--NotAvailableYet
## View the available functions ##
This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetItems](connection-azure-sqldatabase.md#getitems) | Retrieves rows from a SQL table |
|[PostItem](connection-azure-sqldatabase.md#postitem) | Inserts a new row into a SQL table |
|[GetItem](connection-azure-sqldatabase.md#getitem) | Retrieves a single row from a SQL table |
|[DeleteItem](connection-azure-sqldatabase.md#deleteitem) | Deletes a row from a SQL table |
|[PatchItem](connection-azure-sqldatabase.md#patchitem) | Updates an existing row in a SQL table |
|[GetTables](connection-azure-sqldatabase.md#gettables) | Retrieves tables from a SQL database |

### GetItems
Get rows: Retrieves rows from a SQL table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Name of SQL table|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

### PostItem
Insert row: Inserts a new row into a SQL table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Name of SQL table|
|item| |yes|Row to insert into the specified table in SQL|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


### GetItem
Get row: Retrieves a single row from a SQL table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Name of SQL table|
|id|string|yes|Unique identifier of the row to retrieve|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No | |


### DeleteItem
Delete row: Deletes a row from a SQL table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Name of SQL table|
|id|string|yes|Unique identifier of the row to delete|

#### Output properties
None.

### PatchItem
Update row: Updates an existing row in a SQL table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Name of SQL table|
|id|string|yes|Unique identifier of the row to update|
|item| |yes|Row with updated values|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No | &nbsp; |


### GetTables
Get tables: Retrieves tables from a SQL database

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | Can output the Name and DisplayName properties |

### ExecuteProcedure
Execute stored procedure: Executes a stored procedure in SQL

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|procedure|string|yes|Procedure name|
|parameters| |yes|Input parameters|

#### Output properties
Result of the stored procedure execution.

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|OutputParameters|object|No | Output parameter values |
|ReturnCode|integer|No | Return code of a procedure |
|ResultSets|object|No | Result sets|

-->


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
