<properties
	pageTitle="Overview of the Dropbox connection | Microsoft PowerApps"
	description="See the available Dropbox functions, responses, and examples"
	services=""	
	suite="powerapps"
	documentationCenter="" 	
	authors="MandiOhlinger"	
	manager="erikre"	
	editor="" 
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="04/21/2016"
ms.author="mandia"/>

#  Dropbox

![Dropbox](./media/connection-dropbox/dropboxicon.png)

Connect to Dropbox to manage your files. You can perform various actions such as upload, update, get, and delete files in Dropbox.

For example, you can create an app with several text boxes that asks the user for information, like maybe a picture and a name. Then, you can take this information and update a file in a Dropbox account. In another example, you can show a list of all the files in a Dropbox folder. Then in your app, let your app users select one of the files. 

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps web portal][1] or install [PowerApps][2]
- Add the [connection](../add-manage-connections.md)
- Create an app from a [template](../get-started-test-drive.md), from [data](../get-started-create-from-data.md), or from [scratch](../get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-dropbox.md#getfilemetadata) | Retrieves file metadata from Dropbox using file id  |
|[UpdateFile](connection-dropbox.md#updatefile) | Updates a file in Dropbox |
|[DeleteFile](connection-dropbox.md#deletefile) | Deletes a file from Dropbox |
|[GetFileMetadataByPath](connection-dropbox.md#getfilemetadatabypath) | Retrieves file metadata from Dropbox using path |
|[GetFileContentByPath](connection-dropbox.md#getfilecontentbypath) | Retrieves file contents from Dropbox using path |
|[GetFileContent](connection-dropbox.md#getfilecontent) | Retrieves file contents from Dropbox using id |
|[CreateFile](connection-dropbox.md#createfile) | Uploads a file to Dropbox |
|[CopyFile](connection-dropbox.md#copyfile) | Copies a file to Dropbox |
|[OnNewFile](connection-dropbox.md#onnewfile) | Triggers a flow when a new file is created in a Dropbox folder |
|[OnUpdatedFile](connection-dropbox.md#onupdatedfile) | Triggers a flow when a file is modified in a Dropbox folder |
|[ListFolder](connection-dropbox.md#listfolder) | Lists files and folders in a Dropbox folder |
|[ListRootFolder](connection-dropbox.md#listrootfolder) | Lists files and folders in the Dropbox root folder |
|[ExtractFolderV2](connection-dropbox.md#extractfolderv2) | Extracts an archive file into a folder in Dropbox (example: .zip) |

## GetFileMetadata
Get file metadata using id: Retrieves file metadata from Dropbox using file id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## UpdateFile
Update file: Updates a file in Dropbox 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file to update|
|body|string |Content of the file to update in Dropbox|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## DeleteFile
Delete file: Deletes a file from Dropbox 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file to delete|

#### Output properties
None.


## GetFileMetadataByPath
Get file metadata using path: Retrieves file metadata from Dropbox using path 

#### Required input

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in Dropbox|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## GetFileContentByPath
Get file content using path: Retrieves file contents from Dropbox using path 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|path|string|Unique path to the file in Dropbox|

#### Output properties
None.


## GetFileContent
Get file content using id: Retrieves file contents from Dropbox using id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Dropbox 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderPath|string|Folder path to upload the file to Dropbox|
|name|string|Name of the file to create in Dropbox|
|body|string |Content of the file to upload to Dropbox|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## CopyFile
Copy file: Copies a file to Dropbox 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Url to source file|
|destination|string|Destination file path in Dropbox, including target filename|
|overwrite|boolean|Optional. Overwrites the destination file if set to 'true'|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## OnNewFile
When a file is created: Triggers a flow when a new file is created in a Dropbox folder 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderId|string|Specify a folder|

#### Output properties
None.


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a Dropbox folder 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderId|string|Specify a folder|

#### Output properties
None.


## ListFolder
List files and folders in folder: Lists files and folders in a Dropbox folder 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the folder|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## ListRootFolder
List files and folders in root folder: Lists files and folders in the Dropbox root folder 

#### Required input
None.

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |


## ExtractFolderV2
Extract archive to folder: Extracts an archive file into a folder in Dropbox (example: .zip) 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Path to the archive file|
|destination|string|Path in Dropbox to extract the archive contents|
|overwrite|boolean|Optional. Overwrites the destination files if set to 'true'|

#### Output properties - BlobMetadata

| Property Name | Data Type | Description |
|---|---|---|
|Id|string| |
|Name|string| |
|DisplayName|string| |
|Path|string| |
|LastModified|string| |
|Size|integer| |
|MediaType|string| |
|IsFolder|boolean| |
|ETag|string| |
|FileLocator|string| |



## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall
