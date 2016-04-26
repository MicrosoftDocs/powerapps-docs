<properties
	pageTitle="Overview of the SFTP connection | Microsoft PowerApps"
	description="See the available SFTP functions, responses, and examples"
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

#  SFTP

![SFTP](./media/connection-sftp/sftpicon.png)

Connect to SFTP API to send and receive files. You can perform various operations such as create, update, get or delete files.

You can display this information using different controls in your app. For example, you can add a gallery control to your app, then display the contents from an SFTP folder in this gallery.

This topic shows the available functions.

[AZURE.INCLUDE [connection-requirements](../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetFileMetadata](connection-sftp.md#getfilemetadata) | Retrieves file metadata from SFTP server using file id |
|[UpdateFile](connection-sftp.md#updatefile) | Updates a file in SFTP server |
|[DeleteFile](connection-sftp.md#deletefile) | Deletes a file from SFTP server |
|[GetFileMetadataByPath](connection-sftp.md#getfilemetadatabypath) | Retrieves file metadata from SFTP server using path |
|[GetFileContentByPath](connection-sftp.md#getfilecontentbypath) | Retrieves file contents from SFTP server using path |
|[GetFileContent](connection-sftp.md#getfilecontent) | Retrieves file contents from SFTP Server using id |
|[CreateFile](connection-sftp.md#createfile) | Uploads a file to SFTP server |
|[CopyFile](connection-sftp.md#copyfile) | Copies a file to SFTP server |
|[OnUpdatedFile](connection-sftp.md#onupdatedfile) | Triggers a flow when a file is added or modified in a SFTP folder |
|[ListFolder](connection-sftp.md#listfolder) | Lists files in a SFTP server folder |
|[ListRootFolder](connection-sftp.md#listrootfolder) | Lists files in the SFTP server root folder |
|[ExtractFolderV2](connection-sftp.md#extractfolderv2) | Extracts an archive file into a folder in FTP server (example: .zip) |


## GetFileMetadata
Get file metadata: Retrieves file metadata from SFTP using file id 

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
Update file: Updates file content using SFTP 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|
|body|string |yes|Content of the file to update in SFTP|

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
Delete file: Deletes a file in SFTP 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None. 


## GetFileMetadataByPath
Get file metadata using path: Retrieves file metadata from SFTP using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path of the file in SFTP|

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
Get file content using path: Retrieves file contents from SFTP using path 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|path|string|yes|Unique path of the file in SFTP|

#### Output properties
None. 


## GetFileContent
Get file content: Retrieves file contents from SFTP using id 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|id|string|yes|Specify the file|

#### Output properties
None. 


## CreateFile
Create file: Uploads a file in SFTP 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderPath|string|yes|Unique path of the folder in SFTP|
|name|string|yes|Name of the file|
|body| string |yes|Content of the file to create in SFTP|

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
Copy file: Copies a file to SFTP 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|source|string|yes|Path to the source file|
|destination|string|yes|Path to the destination file, including file name|
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
When a file is added or modified: Triggers a flow when a file is added or modified in SFTP folder 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|folderId|string|yes|Specify a folder|

#### Output properties
None. 


## ListFolder
List files in folder: Lists files contained in SFTP folder 

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
List files in root folder: List the files in the root folder of SFTP 

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
Extract folder: Extracts an archive file into a folder using SFTP (example: .zip) 

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