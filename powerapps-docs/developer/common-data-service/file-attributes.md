---
title: "File attributes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File attributes that store binary data within the application, supporting attributes, retrieving binary data, and uploading binary data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 09/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# File attributes

A "File" attribute is used for storing binary data up to a specified maximum size. The primary intended use of this field is to store a single image, annotation (note), or attachment. However, storage of other forms of binary data is also possible. A custom or customizable entity can have zero or more file attributes. All file attributes have the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> ‘EntityFile’ and the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> ‘entityfile’.

Web API (type) | SDK API (class)
------- | -------
entityfile | <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>

<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->

> [!NOTE]
> Binary file data is stored in Microsoft Azure blob storage for improved data access performance and increased file size limits. This also applies to new attachment and annotation data. Existing attachments and annotations will continue to be stored in the relational data store. A planned future update may move the attachment and annotation data from relational storage to blob storage as part of a background task during an organization upgrade.
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
When a file attribute is added to an entity some additional attributes are created to support it.
  
### MaxSizeInKB attribute

 The value represents the maximum size (in kilobytes) of the binary data that the attribute can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
  
<a name="BKMK_RetrievingFiles"></a>

## Retrieving file data
To retrieve binary file data, use the following APIs.

Web API | SDK API
------- | -------
 *none*  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest>
GET /api/data/v9.0/\<entity-type(id)\>/\<file-attribute-name\>/$value   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete binary data file by combining the data blocks in the same sequence as the blocks were received.

### Example Web API download with chunking

```http
GET
/api/data/v9.0/accounts(id)/fileattribute/$value
Headers:
Range: 0-1023

Response:
206 Partial Content
byte[]

Response Header:
Content-Disposition: attachment; filename="sample.txt"
x-ms-file-name: "sample.txt"
x-ms-file-size: 12345
```
Chunking will be decided based on the **Range** header existence in the request. The full file will be downloaded (up to 16 MB) in one request if no **Range** header is included. For chunking, the **Location** response header contains the query-able parameter "FileContinuationToken" whose value must be provided as a parameter in subsequent GET requests to retrieve the next block of data in the sequence.


<a name="BKMK_UploadingFiles"></a>

## Uploading file data  
To upload binary file data, use the following APIs.

Web API | SDK API
------- | -------
call1   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>
call2   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
call3   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest>

As was previously mentioned under [Retrieving file data](#retrieving-file-data), uploading a binary data file of 16 MB or less can be accomplished in a single API call while uploading more than 16 MB of data requires the file data to be divided into blocks of 4 MB or less data. After the complete set of data blocks has been uploaded and a commit request has been sent, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in blob storage.

### Web API upload with chunking
 
<a name="BKMK_DeletingFiles"></a>

## Deleting file data  
To delete file, attachment, or annotation data in blob storage, use the following APIs.

Web API | SDK API
------- | -------
DELETE /api/data/v9.0/\<entity-type(id)\>/\<attribute-name\> | <xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest>