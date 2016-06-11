<properties
	pageTitle="Overview of the Azure Blob connection | Microsoft PowerApps"
	description="See the available Azure Blob functions, responses, and examples"
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

#  Azure blob storage

![Azure Blob](./media/connection-azure-blob/blobicon.png)

Azure Blob storage is a service for storing large amounts of unstructured data. You can perform various actions such as upload, update, get, and delete blobs in Azure blob storage.

For example, you are working with several developers that create sample projects. Using an app, these developers can upload their sample projects to a Blob storage account. Using this same app, the developers can also update their samples, delete their samples, and more.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-azure-blob.md#getfilemetadata) | Retrieves file metadata from Azure Blob Storage using file id |
|[UpdateFile](connection-azure-blob.md#updatefile) | Updates a file in Azure Blob Storage |
|[DeleteFile](connection-azure-blob.md#deletefile) | Deletes a file from Azure Blob Storage  |
|[GetFileMetadataByPath](connection-azure-blob.md#getfilemetadatabypath) | Retrieves file metadata from Azure Blob Storage using path  |
|[GetFileContentByPath](connection-azure-blob.md#getfilecontentbypath) | Retrieves file contents from Azure Blob Storage using path |
|[GetFileContent](connection-azure-blob.md#getfilecontent) | Retrieves file contents from Azure Blob Storage using id |
|[CreateFile](connection-azure-blob.md#createfile) | Uploads a file to Azure Blob Storage |
|[CopyFile](connection-azure-blob.md#copyfile) | Copies a file to Azure Blob Storage |
|[ExtractFolderV2](connection-azure-blob.md#extractfolderv2) | Extracts an archive file into a folder in Azure Blob Storage (example: .zip) |


## GetFileMetadata
Get File Metadata: Retrieves file metadata from Azure Blob Storage using file id

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |


## UpdateFile
Update file: Updates a file in Azure Blob Storage

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body|string |yes|Content of the file to update in Azure Blob Storage|


#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |



## DeleteFile
Delete file: Deletes a file from Azure Blob Storage

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None.



## GetFileMetadataByPath
Get File Metadata using path: Retrieves file metadata from Azure Blob Storage using path

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in Azure Blob Storage|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |


## GetFileContentByPath
Get file content using path: Retrieves file contents from Azure Blob Storage using path

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in Azure Blob Storage|

#### Output properties
None.


## GetFileContent
Get file content: Retrieves file contents from Azure Blob Storage using id

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Azure Blob Storage

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to Azure Blob Storage|
|name|string|yes|Name of the file to create in Azure Blob Storage|
|body|string |yes|Content of the file to upload to Azure Blob Storage|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |


## CopyFile
Copy file: Copies a file to Azure Blob Storage

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in Azure Blob Storage, including target filename|
|overwrite|boolean| no| Overwrites the destination file if set to 'true'|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |


## ExtractFolderV2
Extract archive to folder: Extracts an archive file into a folder in Azure Blob Storage (example: .zip)

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path in Azure Blob Storage to extract the archive contents|
|overwrite|boolean|no| Overwrites the destination files if set to 'true'|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Id | string |
| Name | string |
| DisplayName | string |
| Path | string |
| LastModified | string |  
| Size | integer |
| MediaType | string |
| IsFolder | boolean |
| ETag | string |
| FileLocator | string |



## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
