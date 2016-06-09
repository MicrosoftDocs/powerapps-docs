<properties
	pageTitle="Overview of the Excel connection | Microsoft PowerApps"
	description="See the available Excel functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="MandiOhlinger"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/08/2016"
   ms.author="mandia"/>

#  Excel

![Excel](./media/connection-excel/excelicon.png)

Connect to a cloud storage account to display Excel table data in your app. 

## What you need to know
Excel is *kind of* a connection. To display Excel data in your app, you must do the following:

1. Store an Excel file in a cloud storage connection, including Box, Dropbox, Google Drive, OneDrive, and OneDrive for Business. 
2. Format the Excel data as a table.
3. In your app, create a connection to the cloud storage account, and then add the Excel table as a data source. 

Then, you can display this information in a gallery control on your app. 

[Overview of the cloud storage connection](cloud-storage-blob-connections.md) shows you how to add the connection, add an Excel table as a data source, and use the Excel data in your app. 

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

## Helpful links

See all the [available connections](../connections-list.md).  
Create an app using [Excel data](../get-started-create-from-data.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
