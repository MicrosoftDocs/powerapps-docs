<properties
	pageTitle="Overview of the SQL Server connection | Microsoft PowerApps"
	description="Step-by-step instructions for how to connect to Azure SQL or an on-premises SQL Server database"
	services=""
	suite="powerapps"
	documentationCenter="" 	
	authors="AFTOwen"
	manager="erikre"
	editor=""
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="06/07/2016"
ms.author="anneta"/>

# SQL Server #

![Azure SQL Database](./media/connection-azure-sqldatabase/sqlicon.png)

Connect from PowerApps to either Azure SQL or an on-premises SQL Server database so that you can display information from it in your app.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]
- An Azure SQL database with its user name and password. You can use these steps at [Create a SQL database tutorial](https://azure.microsoft.com/documentation/articles/sql-database-get-started/) to create a database. When you create the SQL database, we suggest you add the **Sample data**.
- A table with a primary key stored in the SQL database.

## Get the connection string

1. In the [Azure portal](https://portal.azure.com/), select **SQL databases**:  

	![SQL Databases](./media/connection-azure-sqldatabase/sqldatabase.png)
2. Select your SQL database from the list. If you don't have one, go to [Create a SQL database tutorial](https://azure.microsoft.com/documentation/articles/sql-database-get-started/) to create a database.

3. When you select it, the properties open. Select **Show database connection strings**:  

	![SQL database properties](./media/connection-azure-sqldatabase/properties.png)
4. Copy the **ADO.NET (SQL authentication)** connection string:  

	![ADO.NET connection string](./media/connection-azure-sqldatabase/adonetconnectionstring.png)

5. Paste the connection string in a text editor, and then look for the following properties:  

	- User ID={your_username}
	- Password={your_password}

	When the SQL database is created, a user name and password is entered. In your connection string, update the **User ID** and **Password** properties with these user name and password values.

	For example, if your username is `powerapps` and your password is `powerapps1609`, your connection string looks similar to the following:  

	`Server=tcp:powerappssqlserver.database.windows.net,1433;Data Source=powerappssqlserver.database.windows.net;Initial Catalog=powerappssqldb;Persist Security Info=False;User ID=powerapps;Password=powerapps1609;Pooling=False;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;`

Keep this connection string nearby. You need it to create the connection in PowerApps.

## Connect to a SQL database and enter your connection string

1. At [powerapps.com](https://web.powerapps.com), expand **Manage**, and select **Connections**:  

	![Azure SQL Database](./media/connection-azure-sqldatabase/connections.png)
2. Select **New connection**, and select **SQL Azure**.
3. When prompted, paste in the connection string you updated in the previous section, and then select **Add connection**:  

	![Paste connection string](./media/connection-azure-sqldatabase/enterconnectionstring.png)

	The connection is added to the list.  
4. Open your app, and add SQL Azure as a [data source](../add-data-connection.md). Select **default**, and then you should see your tables. The following example uses the Sample data:  

	![Azure SQL Database](./media/connection-azure-sqldatabase/tables.png)
5. Select the check box for one or more tables (for example, **Product**, **Customer**, or both), and then select **Connect**. The tables are now listed as a data source.

<!--NotAvailableYet

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetItems](connection-azure-sqldatabase.md#getitems) | Retrieves rows from a SQL table |
|[PostItem](connection-azure-sqldatabase.md#postitem) | Inserts a new row into a SQL table |
|[GetItem](connection-azure-sqldatabase.md#getitem) | Retrieves a single row from a SQL table |
|[DeleteItem](connection-azure-sqldatabase.md#deleteitem) | Deletes a row from a SQL table |
|[PatchItem](connection-azure-sqldatabase.md#patchitem) | Updates an existing row in a SQL table |
|[GetTables](connection-azure-sqldatabase.md#gettables) | Retrieves tables from a SQL database |


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
|ItemInternalId|string|No | |


### GetTables
Get tables: Retrieves tables from a SQL database

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | Can output the Name and DisplayName properties |

-->

## Helpful links ##
- Learn how to [show data from a data source](../add-gallery.md).
- See all the [available connections](../connections-list.md).  
- Learn how to [create a connection](../add-manage-connections.md) from PowerApps to a data source.  
- [Understand tables and records](../working-with-tables.md) with tabular data sources.
