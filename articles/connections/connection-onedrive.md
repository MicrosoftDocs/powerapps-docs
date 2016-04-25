<properties
	pageTitle="Overview of the OneDrive connection | Microsoft PowerApps"
	description="See the available OneDrive functions, responses, and examples"
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
   ms.date="04/25/2016"
   ms.author="mandia"/>

#  OneDrive

![OneDrive](./media/connection-onedrive/onedriveicon.png)

Connect to OneDrive to manage your files. You can perform various actions such as upload, update, get, and delete on files in OneDrive.

You can manage your OneDrive within your app. For example, you can list all the items in a OneDrive folder in your app, and display this list in a Gallery control. 

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps portal][1] or install [PowerApps][2]
- Add the [connection](add-manage-connections.md)
- Create an app from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-onedrive.md#getfilemetadata) | Retrieves metadata of a file in OneDrive using id  |
|[UpdateFile](connection-onedrive.md#updatefile) | Updates a file in OneDrive  |
|[DeleteFile](connection-onedrive.md#deletefile) | Deletes a file from OneDrive  |
|[GetFileMetadataByPath](connection-onedrive.md#getfilemetadatabypath) | Retrieves metadata of a file in OneDrive using path  |
|[GetFileContentByPath](connection-onedrive.md#fetfilecontentbypath) | Retrieves contents of a file in OneDrive using path  |
|[GetFileContent](connection-onedrive.md#getfilecontent) |  Retrieves contents of a file in OneDrive using id  |
|[CreateFile](connection-onedrive.md#createfile) | Uploads a file to OneDrive   |
|[CopyFile](connection-onedrive.md#copyfile) | Copies a file to OneDrive   |
|[OnNewFile](connection-onedrive.md#onnewfile) | Triggers a flow when a new file is created in a OneDrive folder   |
|[OnUpdatedFile](connection-onedrive.md#onupdatedfile) | Triggers a flow when a file is modified in a OneDrive folder  |
|[ListFolder](connection-onedrive.md#listfolder) |  Lists files in a OneDrive folder  |
|[ListRootFolder](connection-onedrive.md#listrootfolder) | Lists files in the OneDrive root folder   |
|[ExtractFolderV2](connection-onedrive.md#extractfolderv2) | Extracts a folder to OneDrive   |


## GetFileMetadata
Get file metadata using id: Retrieves metadata of a file in OneDrive using id 

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
Update file: Updates a file in OneDrive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body|string |yes|Content of the file to update in OneDrive|

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
Delete file: Deletes a file from OneDrive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None. 


## GetFileMetadataByPath
Get file metadata using path: Retrieves metadata of a file in OneDrive using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in OneDrive|

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
Get file content using path: Retrieves contents of a file in OneDrive using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in OneDrive|

#### Output properties
None. 


## GetFileContent
Get file content using id: Retrieves contents of a file in OneDrive using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None. 


## CreateFile
Create file: Uploads a file to OneDrive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to OneDrive|
|name|string|yes|Name of the file to create in OneDrive|
|body| string|yes|Content of the file to upload to OneDrive|

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
Copy file: Copies a file to OneDrive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in OneDrive, including target filename|
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
When a file is created: Triggers a flow when a new file is created in a OneDrive folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a OneDrive folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## ListFolder
List files in folder: Lists files in a OneDrive folder 

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
List root folder: Lists files in the OneDrive root folder 

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
Extract folder: Extracts a folder to OneDrive 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path in OneDrive to extract the archive contents|
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

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall