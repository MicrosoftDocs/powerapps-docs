<properties
	pageTitle="Overview of the Dropbox connection | Microsoft PowerApps"
	description="See the available Dropbox functions, responses, and examples"
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
ms.date="04/26/2016"
ms.author="anneta"/>

#  Dropbox

![Dropbox](./media/connection-dropbox/dropboxicon.png)

Upload, update, get, and delete files and other data in Dropbox. For example, list all the files in a Dropbox folder so that users can select one, or create an app that prompts users to provide contact information and adds that data to a file in Dropbox. 

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body|string |yes|Content of the file to update in Dropbox|

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None.


## GetFileMetadataByPath
Get file metadata using path: Retrieves file metadata from Dropbox using path

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in Dropbox|

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in Dropbox|

#### Output properties
None.


## GetFileContent
Get file content using id: Retrieves file contents from Dropbox using id

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Dropbox

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to Dropbox|
|name|string|yes|Name of the file to create in Dropbox|
|body|string |yes|Content of the file to upload to Dropbox|

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in Dropbox, including target filename|
|overwrite|boolean|no| Overwrites the destination file if set to 'true'|

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None.


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a Dropbox folder

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None.


## ListFolder
List files and folders in folder: Lists files and folders in a Dropbox folder

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|id|string|yes|Specify the folder|

#### Output properties

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

#### Input properties
None.

#### Output properties

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

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path in Dropbox to extract the archive contents|
|overwrite|boolean|no| Overwrites the destination files if set to 'true'|

#### Output properties

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
