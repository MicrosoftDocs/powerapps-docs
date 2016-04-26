<properties
	pageTitle="Overview of the FTP connection | Microsoft PowerApps"
	description="See the available FTP functions, responses, and examples"
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
ms.date="04/26/2016"
ms.author="mandia"/>

#  FTP

![FTP](./media/connection-ftp/ftpicon.png)

Connect to FTP server to manage your files. You can perform various actions such as upload, update, get, and delete files in FTP server.

You can display this information using different controls in your app. For example, you can add a gallery control to your app, then display the contents from an FTP folder in this gallery.

This topic shows the available functions.

[AZURE.INCLUDE [connection-requirements](../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-ftp.md#getfilemetadata) | Retrieves file metadata from FTP server using file id |
|[UpdateFile](connection-ftp.md#updatefile) | Updates a file in FTP server |
|[DeleteFile](connection-ftp.md#deletefile) | Deletes a file from FTP server |
|[GetFileMetadataByPath](connection-ftp.md#getfilemetadatabypath) | Retrieves file metadata from FTP server using path |
|[GetFileContentByPath](connection-ftp.md#getfilecontentbypath) | Retrieves file contents from FTP server using path |
|[GetFileContent](connection-ftp.md#getfilecontent) | Retrieves file contents from FTP Server using id |
|[CreateFile](connection-ftp.md#createfile) | Uploads a file to FTP server |
|[CopyFile](connection-ftp.md#copyfile) | Copies a file to FTP server |
|[OnUpdatedFile](connection-ftp.md#onupdatedfile) | Triggers a flow when a file is added or modified in a FTP folder |
|[ListFolder](connection-ftp.md#listfolder) | Lists files in a FTP server folder |
|[ListRootFolder](connection-ftp.md#listrootfolder) | Lists files in the FTP server root folder |
|[ExtractFolderV2](connection-ftp.md#extractfolderv2) | Extracts an archive file into a folder in FTP server (example: .zip) |

## GetFileMetadata
Get File Metadata: Retrieves file metadata from FTP server using file id 

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
Update file: Updates a file in FTP server 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to update|
|body| string|yes|Content of the file to update in FTP server|

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
Delete file: Deletes a file from FTP server 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file to delete|

#### Output properties
None. 


## GetFileMetadataByPath
Get File Metadata using path: Retrieves file metadata from FTP server using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in FTP server|

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
Get file content using path: Retrieves file contents from FTP server using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path to the file in FTP server|

#### Output properties
None. 


## GetFileContent
Get file content: Retrieves file contents from FTP Server using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None. 


## CreateFile
Create file: Uploads a file to FTP server 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Folder path to upload the file to FTP server|
|name|string|yes|Name of the file to create in FTP server|
|body| string|yes|Content of the file to upload to FTP server|

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
Copy file: Copies a file to FTP server 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Url to source file|
|destination|string|yes|Destination file path in FTP server, including target filename|
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


## OnUpdatedFile
When a file is added or modified: Triggers a flow when a file is added or modified in a FTP folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## ListFolder
List files in folder: Lists files in a FTP server folder 

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
List files in root folder: Lists files in the FTP server root folder 

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
Extract folder: Extracts an archive file into a folder in FTP server (example: .zip) 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the archive file|
|destination|string|yes|Path to the destination folder|
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
