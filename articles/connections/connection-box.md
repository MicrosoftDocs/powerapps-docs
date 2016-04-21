<properties
	pageTitle="Overview of the Box connection | Microsoft PowerApps"
	description="See the available Box functions, responses, and examples"
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

#  Box

![Box](./media/connection-box/boxicon.png)

Connect to Box to manage your files. You can perform various actions such as upload, update, get, and delete files in Box.

For example, you can create an app with several text boxes that asks the user for information, like maybe a picture and a name. Then, you can take this information and update a file in a Dropbox account. In another example, you can show a list of all the files in a Dropbox folder. Then in your app, let your app users select one of the files. 

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps web portal][1] or install [PowerApps][2]
- Add the [connection](add-manage-connections.md)
- Create an app from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-box.md#getfilemetadata) | Retrieves file metadata from Box using file id |
|[UpdateFile](connection-box.md#updatefile) | Updates a file in Box |
|[DeleteFile](connection-box.md#deletefile) | Deletes a file from Box |
|[GetFileMetadataByPath](connection-box.md#getfilemetadatabypath) | Retrieves file metadata from Box using path |
|[GetFileContentByPath](connection-box.md#getfilecontentbypath) | Retrieves file contents from Box using path |
|[GetFileContent](connection-box.md#getfilecontent) | Retrieves file contents from Box using id |
|[CreateFile](connection-box.md#createfile) | Uploads a file to Box |
|[CopyFile](connection-box.md#copyfile) | Copies a file to Box |
|[OnNewFile](connection-box.md#onnewfile) | Triggers a flow when a new file is created in a Box folder |
|[OnUpdatedFile](connection-box.md#onupdatedfile) | Triggers a flow when a file is modified in a Box folder |
|[ExtractFolderV2](connection-box.md#extractfolderv2) | Extracts an archive file into a folder in Box (example: .zip) |


## GetFileMetadata
Get file metadata using id: Retrieves file metadata from Box using file id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Unique identifier of the file in Box|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string|
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
Update file: Updates a file in Box 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Unique identifier of the file to update in Box|
|body| string|Content of the file to update in Box|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string|
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
Delete file: Deletes a file from Box 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Unique identifier of the file to delete from Box|

#### Output properties
None.


## GetFileMetadataByPath
Get file metadata using path: Retrieves file metadata from Box using path 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|path|string|Unique path to the file in Box|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string|
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
Get file content using path: Retrieves file contents from Box using path 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|path|string|Unique path to the file in Box|

#### Output properties
None.


## GetFileContent
Get file content using id: Retrieves file contents from Box using id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Unique identifier of the file in Box|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Box 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderPath|string|Folder path to upload the file to Box|
|name|string|Name of the file to create in Box|
|body| string|Content of the file to upload to Box|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string|
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
Copy file: Copies a file to Box 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Url to source file|
|destination|string|Destination file path in Box, including target filename|
|overwrite|boolean|Optional. Overwrites the destination file if set to 'true'|

#### Output properties

| Property Name | Data Type | Description |
|---|---|---|
|Id|string|
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
When a file is created: Triggers a flow when a new file is created in a Box folder 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderId|string|Unique identifier of the folder in Box|

#### Output properties
None.


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a Box folder 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderId|string|Unique identifier of the folder in Box|

#### Output properties
None.


## ExtractFolderV2
Extract archive to folder: Extracts an archive file into a folder in Box (example: .zip) 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Path to the archive file|
|destination|string|Path in Box to extract the archive contents|
|overwrite|boolean|Optional. Overwrites the destination files if set to 'true'|

#### Output properties
None.


## Helpful links

See all the [available connections](connections-list.md).
Learn how to [add connections](add-manage-connections.md) to your apps.

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall