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
   ms.date="04/21/2016"
   ms.author="mandia"/>

#  Excel

![Excel](./media/connection-excel/excelicon.png)

Excel connector


You can display this information in a text box on your app. You can display one function, multiple functions, or even combine different functions. For example, you can create an expression that combines the User Name and Phone Number, and then display this information in your app.

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps portal][1] or install [PowerApps][2]
- Add the [connection](../add-manage-connections.md)
- Create an app from a [template](../get-started-test-drive.md), from [data](../get-started-create-from-data.md), or from [scratch](../get-started-create-from-blank.md)

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



## GetTables
Get tables: Retrieves table names from an Excel file 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|value|array|You can output the table name (a string value) and the table display name (a string value). e.g. { "value" : [ { "Name": "Table1", "DisplayName": "Table 1"}, { "Name": "Table2", "DisplayName": "Table 2"} ] }  |


## GetItems
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



## PostItem
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



## GetItem
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



## DeleteItem
Delete row: Deletes a row from an Excel table 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Excel file name|
|table|string|yes|Excel table name|
|id|string|yes|Unique identifier of the row to delete|

#### Output properties
None.



## PatchItem
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



## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall