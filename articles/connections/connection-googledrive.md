<properties
	pageTitle="Overview of the Google Drive connection | Microsoft PowerApps"
	description="See the available Google Drive functions, responses, and examples"
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
   ms.date="04/26/2016"
   ms.author="mandia"/>

#  Google Drive

![Google Drive](./media/connection-googledrive/googledriveicon.png)

Connect to Google Drive to manage your files. You can perform various actions such as upload, update, get, and delete on files in Google Drive.

You can display this information in a text box on your app. You can display one function, multiple functions, or even combine different functions. For example, you can create an expression that combines the User Name and Phone Number, and then display this information in your app.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-googledrive.md#getfilemetadata) | Retrieves file metadata from Google Drive using id  |
|[UpdateFile](connection-googledrive.md#updatefile) | Updates a file in Google Drive |
|[DeleteFile](connection-googledrive.md#deletefile) | Deletes a file from Google Drive |
|[GetFileMetadataByPath](connection-googledrive.md#getfilemetadatabypath) | Retrieves file metadata from Google Drive using path |
|[GetFileContentByPath](connection-googledrive.md#getfilecontentbypath) | Retrieves file contents from Google Drive using path |
|[GetFileContent](connection-googledrive.md#getfilecontent) | Retrieves file contents from Google Drive using id |
|[CreateFile](connection-googledrive.md#createfile) | Uploads a file to Google Drive |
|[CopyFile](connection-googledrive.md#copyfile) | Copies a file to Google Drive |
|[ListFolder](connection-googledrive.md#listfolder) | Lists files in a Google Drive folder |
|[ListRootFolder](connection-googledrive.md#listrootfolder) | Lists files in the Google Drive root folder |
|[ExtractFolderV2](connection-googledrive.md#extractfolderv2) | Extracts an archive file into a folder in Google Drive (example: .zip) |
|[GetTables](connection-googledrive.md#gettables) | Retrieves sheet names from a Google Sheet file  |
|[GetItems](connection-googledrive.md#getitems) | Retrieves rows from a Google Sheet  |
|[PostItem](connection-googledrive.md#postitem) | Inserts a row into a Google Sheet  |
|[GetItem](connection-googledrive.md#getitem) | Retrieves a single row from a Google Sheet |
|[DeleteItem](connection-googledrive.md#deleteitem) | Deletes a row from a Google Sheet |
|[PatchItem](connection-googledrive.md#patchitem) | Updates a row in a Google Sheet |


## GetFileMetadata
Get file metadata using id: Retrieves file metadata from Google Drive using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |



## UpdateFile
Update file

#### Description
Updates a file in Google Drive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body| string|yes|Content of the file to upload to Google Drive|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## DeleteFile
Delete file: Deletes a file from Google Drive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None.


## GetFileMetadataByPath
Get file metadata using path: Retrieves file metadata from Google Drive using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Path of the file in Google Drive|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## GetFileContentByPath
Get file content using path: Retrieves file content from Google Drive using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Path of the file in Google Drive|

#### Output properties
None.


## GetFileContent
Get file content using id: Retrieves file content from Google Drive using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Unique identifier of the file to retrieve in Google Drive|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Google Drive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to Google Drive|
|name|string|yes|Name of the file to create in Google Drive|
|body|string |yes|Content of the file to upload to Google Drive|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## CopyFile
Copy file: Copies a file on Google Drive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in Google Drive, including target filename|
|overwrite|boolean|no|Overwrites the destination file if set to 'true'|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## ListFolder
List files in folder: List files in a Google Drive folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the folder in Google Drive|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## ListRootFolder
List files in root folder: Lists files in the Google Drive root folder 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## ExtractFolderV2
Extract archive to folder: Extracts an archive file into a folder in Google Drive (example: .zip) 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path in Google Drive to extract the archive contents|
|overwrite|boolean|no|Overwrites the destination files if set to 'true'|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| Uses date-time format |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## GetTables
Get sheets: Retrieves sheet names from a Google Sheet file 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|


#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|value|array| You can output the table name (a string value) and the table display name (a string value). e.g. { "value" : [ { "Name": "Table1", "DisplayName": "Table 1"}, { "Name": "Table2", "DisplayName": "Table 2"} ] } |


## GetItems
Get rows: Retrieves rows from a Google Sheet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|
|table|string|yes|Specify the worksheet|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|


#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|value|Item[]|This property is dynamic and depends on what you're connecting to | 


## PostItem
Insert row: Inserts a row into a Google Sheet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|
|table|string|yes|Specify the worksheet|
|item| |yes|Row to insert into the specified sheet|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|This property is dynamic and depends on what you're connecting to |


## GetItem
Get row: Retrieves a single row from a Google Sheet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|
|table|string|yes|Specify the worksheet|
|id|string|yes|Unique identifier of row to retrieve|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|This property is dynamic and depends on what you're connecting to |


## DeleteItem
Delete Row: Deletes a row from a Google Sheet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|
|table|string|yes|Specify the worksheet|
|id|string|yes|Unique identifier of the row to delete|

#### Output properties
None.


## PatchItem
Update row: Updates a row in a Google Sheet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Specify the file|
|table|string|yes|Specify the worksheet|
|id|string|yes|Unique identifier of the row to update|
|item| |yes|Row with updated values|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|This property is dynamic and depends on what you're connecting to |


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
