<properties
	pageTitle="Overview of the OneDrive for Business connection | Microsoft PowerApps"
	description="See the available OneDrive for Business functions, responses, and examples"
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
   ms.date="04/28/2016"
   ms.author="mandia"/>

#  OneDrive for Business

![OneDrive](./media/connection-onedrive-for-business/onedriveforbusinessicon.png)

Connect to OneDrive for Business to manage your files. You can perform various actions such as upload, update, get, and delete on files.

You can manage your OneDrive for Business account within your app. For example, you can list all the items in a OneDrive folder in your app, and display this list in a Gallery control. 

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-onedrive-for-business.md#getfilemetadata) | Retrieves metadata of a file in OneDrive for Business using id  |
|[UpdateFile](connection-onedrive-for-business.md#updatefile) | Updates a file in OneDrive for Business  |
|[DeleteFile](connection-onedrive-for-business.md#deletefile) | Deletes a file from OneDrive for Business  |
|[GetFileMetadataByPath](connection-onedrive-for-business.md#getfilemetadatabypath) | Retrieves metadata of a file in OneDrive for Business using path  |
|[GetFileContentByPath](connection-onedrive-for-business.md#getfilecontentbypath) | Retrieves contents of a file in OneDrive for Business using path  |
|[GetFileContent](connection-onedrive-for-business.md#getfilecontent) |  Retrieves contents of a file in OneDrive for Business using id  |
|[CreateFile](connection-onedrive-for-business.md#createfile) | Uploads a file to OneDrive for Business   |
|[CopyFile](connection-onedrive-for-business.md#copyfile) | Copies a file to OneDrive for Business   |
|[OnNewFile](connection-onedrive-for-business.md#onnewfile) | Triggers a flow when a new file is created in a OneDrive for Business folder   |
|[OnUpdatedFile](connection-onedrive-for-business.md#onupdatedfile) | Triggers a flow when a file is modified in a OneDrive for Business folder  |
|[ListFolder](connection-onedrive-for-business.md#listfolder) |  Lists files in a OneDrive for Business folder  |
|[ListRootFolder](connection-onedrive-for-business.md#listrootfolder) | Lists files in the OneDrive for Business root folder   |
|[ExtractFolderV2](connection-onedrive-for-business.md#extractfolderv2) | Extracts a folder to OneDrive for Business   |



## GetFileMetadata
Get file metadata using id: Retrieves metadata of a file in OneDrive for Business using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## UpdateFile
Update file: Updates a file in OneDrive for Business 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body| |yes|Content of the file to update in OneDrive for Business|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## DeleteFile
Delete file: Deletes a file from OneDrive for Business 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None. 


## GetFileMetadataByPath
Get file metadata using path: Retrieves metadata of a file in OneDrive for Business using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in OneDrive for Business|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## GetFileContentByPath
Get file content using path: Retrieves contents of a file in OneDrive for Business using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in OneDrive for Business|

#### Output properties
None. 


## GetFileContent
Get file content using id: Retrieves contents of a file in OneDrive for Business using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None. 


## CreateFile
Create file: Uploads a file to OneDrive for Business 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to OneDrive for Business|
|name|string|yes|Name of the file to create in OneDrive for Business|
|body| |yes|Content of the file to upload to OneDrive for Business|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## CopyFile
Copy file: Copies a file to OneDrive for Business 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in OneDrive for Business, including target filename|
|overwrite|boolean|no|Overwrites the destination file if set to 'true'|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## OnNewFile
When a file is created: Triggers a flow when a new file is created in a OneDrive for Business folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a OneDrive for Business folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## ListFolder
List files in folder: Lists files in a OneDrive for Business folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the folder|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## ListRootFolder
List root folder: Lists files in the OneDrive for Business root folder 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## ExtractFolderV2
Extract folder: Extracts a folder to OneDrive for Business 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path in OneDrive for Business to extract the archive contents|
|overwrite|boolean|no|Overwrites the destination files if set to 'true'|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |
 

## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
