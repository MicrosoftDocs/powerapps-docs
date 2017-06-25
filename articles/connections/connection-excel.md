<properties
	pageTitle="Overview of the Excel connection | Microsoft PowerApps"
	description="Display and update data in Excel by storing the workbook in a cloud-storage account and then connecting to the data from your app."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="archnair"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/02/2016"
   ms.author="archanan"/>

# Connect to Excel from Microsoft PowerApps #

![Excel](./media/connection-excel/excelicon.png)

Excel is *kind of* a connection. To display Excel data in your app:

1. [Format the Excel data as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).
1. Store the Excel file in a cloud-storage account, such as Box, Dropbox, Google Drive, OneDrive, and OneDrive for Business.
1. [Connect to the cloud-storage account](../add-manage-connections.md), and then add the Excel table as a data source.
1. Display this information in your app by [generating an app automatically](../get-started-create-from-data.md) or by adding and configuring, for example, a **Gallery** control.

Note: Once you connect to your Excel table from PowerApps, PowerApps will create a new column called **\__PowerAppsId__**, with a unique ID for each row of your Excel table.

[Overview of the cloud-storage connection](cloud-storage-blob-connections.md) shows you how to add the connection, add an Excel table as a data source, and use the Excel data in your app.

For information about how to connect to other types of data, see the [list of connections for PowerApps](../connections-list.md).

## Known limitations

There are currently [certain limitations](./connections/cloud-storage-blob-connections.md#Sharing-Excel-Tables) with connectors involving Excel files. These affect apps that you share within your organization.

<!--NotAvailableYet

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetTables](connection-excel.md#gettables) | Retrieves table names from an Excel file  |
|[GetItems](connection-excel.md#getitems) | Retrieves rows from an Excel table |
|[PostItem](connection-excel.md#postitem) | Inserts a new row into an Excel table |
|[GetItem](connection-excel.md#getitem) | Retrieves a single row from an Excel table |
|[DeleteItem](connection-excel.md#deleteitem) | Deletes a row from an Excel table  |
|[PatchItem](connection-excel.md#patchitem) | Updates an existing row in an Excel table |



### GetTables
Get tables: Retrieves table names from an Excel file

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|value|array|You can output the table name (a string value) and the table display name (a string value). e.g. { "value" : [ { "Name": "Table1", "DisplayName": "Table 1"}, { "Name": "Table2", "DisplayName": "Table 2"} ] }  |


### GetItems
Get rows: Retrieves rows from an Excel table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|value|array|This property is dynamic and depends on what you're connecting to |



### PostItem
Insert row: Inserts a new row into an Excel table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|item| |yes|Row to insert into the specified Excel table|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string| This property is dynamic and depends on what you're connecting to|



### GetItem
Get row: Retrieves a single row from an Excel table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|id|string|yes|Unique identifier of row to retrieve|


#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string| This property is dynamic and depends on what you're connecting to|



### DeleteItem
Delete row: Deletes a row from an Excel table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|id|string|yes|Unique identifier of the row to delete|

#### Output properties
None.



### PatchItem
Update row: Updates an existing row in an Excel table

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|id|string|yes|Unique identifier of the row to update|
|item| |yes|Row with updated values|


#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|This property is dynamic and depends on what you're connecting to |

-->
