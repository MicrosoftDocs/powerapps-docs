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

A file attribute is used for storing binary data up to a specified maximum size. The primary intended use of this field is to store a single image, annotation (note), or attachment. However, storage of other forms of binary data is also possible. A custom or customizable entity can have zero or more file attributes. All file attributes have the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> ‘EntityFile’ and the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> ‘entityfile’.

Web API (type) | SDK API (class)
------- | -------
entityfile | <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>

<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->

> [!NOTE]
> File data is stored in Azure Blob Storage for improved data access performance and increased file size limits. This also applies to new attachment and annotation data. Existing attachments and annotations will continue to be stored in the relational data store. A planned future update may move the attachment and annotation data from relational storage to Azure Blob Storage as part of a background task during an organization upgrade.
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
When a file attribute is added to an entity some additional attributes are created to support it.
  
### MaxSizeInKB attribute

 This value represents the maximum size (in kilobytes) of the binary data that the attribute can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
  
<a name="BKMK_RetrievingFiles"></a>

## Retrieving file data
To retrieve file data, use the following APIs.

Web API | SDK API
------- | -------
 none  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest>
GET /api/data/v9.0/\<entity-type(id)\>/\<file-attribute-name\>/$value   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete data file by combining the data blocks in the same sequence as the blocks were received.

### Example: HTTP request/response for download

```http
GET
/api/data/v9.0/accounts(id)/myfileattribute/$value
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
Chunking will be decided based on the **Range** header existence in the request. The full file will be downloaded (up to 16 MB) in one request if no **Range** header is included. For chunking, the **Location** response header contains the query-able parameter *FileContinuationToken*. Use the provided location header value in the next GET request to retrieve the next block of data in the sequence.

`Location: api/data/v9.0/accounts(id)/myfileattribute?FileContinuationToken`

### Example: .NET code for download with chunking

```csharp
static async Task ChunkedDownloadAsync(
            Uri urlPrefix,
            string customEntitySetName,
            string entityId,
            string entityFileOrAttributeAttributeLogicalName,
            string fileRootPath,
            string downloadFileName,
            string token)
        {
            var url = new Uri(urlPrefix, $"{customEntitySetName}({entityId})/{entityFileOrAttributeAttributeLogicalName}/$value?size=full");
            var increment = 4194304;
            var from = 0;
            var fileSize = 0;
            byte[] downloaded = null;
            do
            {
                using (var request = new HttpRequestMessage(HttpMethod.Get, url))
                {
                    request.Headers.Range = new System.Net.Http.Headers.RangeHeaderValue(from, from + increment - 1);
                    request.Headers.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);
                    using (var response = await Client.SendAsync(request))
                    {
                        if (downloaded == null)
                        {
                            fileSize = int.Parse(response.Headers.GetValues("x-ms-file-size").First());
                            downloaded = new byte[fileSize];
                        }

                        var responseContent = await response.Content.ReadAsByteArrayAsync();
                        responseContent.CopyTo(downloaded, from);
                    }
                }

                from += increment;
            } while (from < fileSize);

            await File.WriteAllBytesAsync(Path.Combine(fileRootPath, downloadFileName), downloaded);
        }
```

<a name="BKMK_UploadingFiles"></a>

## Uploading file data  
To upload file data, use the following APIs.

Web API | SDK API
------- | -------
none   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>
PATCH /api/data/v9.0/\<entity-type(id)\>/\<file-attribute-name\>   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
none   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest>

As was previously mentioned under [Retrieving file data](#retrieving-file-data), uploading a binary data file of 16 MB or less can be accomplished in a single API call while uploading more than 16 MB of data requires the file data to be divided into blocks of 4 MB or less data. After the complete set of data blocks has been uploaded and a commit request has been sent, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in Azure Blob Storage.

### Example: HTTP request/response upload with chunking

```http
PATCH /api/data/v9.0/accounts(id)/myfileattribute 

Headers: 
x-ms-transfer-mode: chunked 
x-ms-file-name: [User input from power apps] 

Response: 
200 OK 

Response Header: 
x-ms-chunk-size: 4096 
Accept-Ranges: bytes 

Location: api/data/v9.0/accounts(id)/myfileattribute?FileContinuationToken 
```
```http
PATCH /api/data/v9.0/accounts(id)/myfileattribute?FileContinuationToken 

Headers: 
Content-Range: bytes 0-4095/8190 
Content-Type: application/octet-stream 
x-ms-file-name: [User input from power apps] 

Body: 
byte[]

Response:  
206 Partial Content 
```

### Example: .NET code for upload with chunking

```csharp
static async Task ChunkedUploadAsync(
            Uri urlPrefix,
            string customEntitySetName,
            string entityId,
            string entityFileOrAttributeAttributeLogicalName,
            string fileRootPath,
            string uploadFileName,
            string accessToken)
        {
            var filePath = Path.Combine(fileRootPath, uploadFileName);
            var fileBytes = await File.ReadAllBytesAsync(filePath);
            var url = new Uri(urlPrefix, $"{customEntitySetName}({entityId})/{entityFileOrAttributeAttributeLogicalName}");

            var chunkSize = 0;
            using (var request = new HttpRequestMessage(HttpMethod.Patch, url))
            {
                request.Headers.Add("x-ms-transfer-mode", "chunked");
                request.Headers.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken);
                request.Headers.Add("x-ms-file-name", uploadFileName);
                using (var response = await Client.SendAsync(request))
                {
                    response.EnsureSuccessStatusCode();
                    url = response.Headers.Location;
                    chunkSize = int.Parse(response.Headers.GetValues("x-ms-chunk-size").First());
                }
            }

            for (var offset = 0; offset < fileBytes.Length; offset += chunkSize)
            {
                var count = (offset + chunkSize) > fileBytes.Length ? fileBytes.Length % chunkSize : chunkSize;
                using (var content = new ByteArrayContent(fileBytes, offset, count))
                using (var request = new HttpRequestMessage(HttpMethod.Patch, url))
                {
                    content.Headers.Add("Content-Type", "application/octet-stream");
                    content.Headers.ContentRange = new System.Net.Http.Headers.ContentRangeHeaderValue(offset, offset + (count - 1), fileBytes.Length);
                    request.Headers.Add("x-ms-file-name", uploadFileName);
                    request.Headers.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken);
                    request.Content = content;
                    using (var response = await Client.SendAsync(request))
                    {
                        response.EnsureSuccessStatusCode();
                    }
                }
            }
        }
```
 
<a name="BKMK_DeletingFiles"></a>

## Deleting file data  
To delete file, attachment, or annotation data in Azure Blob Storage, use the following APIs.

Web API | SDK API
------- | -------
DELETE /api/data/v9.0/\<entity-type(id)\>/\<attribute-name\> | <xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest>

### See Also
[Image attributes](image-attributes.md)