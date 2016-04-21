<properties
	pageTitle="Overview of the Azure Blob connection | Microsoft PowerApps"
	description="See the available Azure Blob functions, responses, and examples"
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

#  Azure blob storage

![Azure Blob](./media/connection-azureblob/blobicon.png)

Azure Blob storage is a service for storing large amounts of unstructured data. You can perform various actions such as upload, update, get, and delete blobs in Azure blob storage.

For example, you are working with several developers that create sample projects. Using an app, these developers can upload their sample projects to a Blob storage account. Using this same app, the developers can also update their samples, delete their samples, and more. 

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps web portal][1] or install [PowerApps][2]
- Add the [connection](../add-manage-connections.md)
- Create an app from a [template](../get-started-test-drive.md), from [data](../get-started-create-from-data.md), or from [scratch](../get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-azureblob.md#getfilemetadata) | Retrieves file metadata from Azure Blob Storage using file id |
|[UpdateFile](connection-azureblob.md#updatefile) | Updates a file in Azure Blob Storage |
|[DeleteFile](connection-azureblob.md#deletefile) | Deletes a file from Azure Blob Storage  |
|[GetFileMetadataByPath](connection-azureblob.md#getfilemetadatabypath) | Retrieves file metadata from Azure Blob Storage using path  |
|[GetFileContentByPath](connection-azureblob.md#getfilecontentbypath) | Retrieves file contents from Azure Blob Storage using path |
|[GetFileContent](connection-azureblob.md#getfilecontent) | Retrieves file contents from Azure Blob Storage using id |
|[CreateFile](connection-azureblob.md#createfile) | Uploads a file to Azure Blob Storage |
|[CopyFile](connection-azureblob.md#copyfile) | Copies a file to Azure Blob Storage |
|[ExtractFolderV2](connection-azureblob.md#extractfolderv2) | Extracts an archive file into a folder in Azure Blob Storage (example: .zip) |


## GetFileMetadata
Get File Metadata: Retrieves file metadata from Azure Blob Storage using file id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file|

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

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file to update|
|body|string |Content of the file to update in Azure Blob Storage|


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

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file to delete|

#### Output properties
None. 



## GetFileMetadataByPath
Get File Metadata using path: Retrieves file metadata from Azure Blob Storage using path 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|path|string|Unique path to the file in Azure Blob Storage|

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

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|path|string|Unique path to the file in Azure Blob Storage|

#### Output properties
None.


## GetFileContent
Get file content: Retrieves file contents from Azure Blob Storage using id 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|id|string|Specify the file|

#### Output properties
None.


## CreateFile
Create file: Uploads a file to Azure Blob Storage 

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|folderPath|string|Folder path to upload the file to Azure Blob Storage|
|name|string|Name of the file to create in Azure Blob Storage|
|body|string |Content of the file to upload to Azure Blob Storage|

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

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Url to source file|
|destination|string|Destination file path in Azure Blob Storage, including target filename|
|overwrite|boolean| Optional. Overwrites the destination file if set to 'true'|

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

#### Required input

| Name| Data Type|Description|
| ---|---|---|
|source|string|Path to the archive file|
|destination|string|Path in Azure Blob Storage to extract the archive contents|
|overwrite|boolean|Optional. Overwrites the destination files if set to 'true'|

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

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall
