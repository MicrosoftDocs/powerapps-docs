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

A "File" attribute is used for storing binary data up to a specified maximum size in kilobytes. A custom or customizable entity can have zero or more file attributes. All file attributes have the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> ‘EntityFile’ and the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> ‘entityfile’.

| Web API | SDK API |
| | <xref: Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.FileAttributeMetadata> |

<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->

> [!NOTE]
> New file and attachment data is stored in Microsoft Azure blob storage for improved data access performance and increased data size limits. Existing attachments will continue to be stored in the relational data store. A planned future update may move the attachment data in relational storage to blob storage as part of a background task during an organization upgrade.
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
When a file attribute is added to an entity some additional attributes are created to support it.
  
### MaxSizeInKB attribute

 The value represents the maximum size (in kilobytes) of the binary data that the attribute can contain. Set this to the smallest useable value appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
  
<a name="BKMK_RetrievingFiles"></a>
## Retrieving file data
To retrieve binary file data, use the following APIs.

Web API | SDK API

<!-- Research: Web API may transfer the complete file in one call -->
File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount are divided into 4 MB or smaller data blocks where each block is received in a separate API call until all file data has been received. It is your responsibility to join the data blocks into the final complete binary data file using the same sequence as the data blocks were received.

<a name="BKMK_UploadingFiles"></a>   
## Uploading file data  
To upload binary file data, use the following APIs.

Web API | SDK API

As was previously mentioned under [Retrieving file data](#retrieving-file-data), uploading a binary data file of 16 MB or less can be accomplished in a single API call while uploading more than 16 MB of data requires the file data to be divided into blocks of 4 MB or less encrypted data. Once the complete set of data blocks has been uploaded, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in blob storage.
  
### See also  
