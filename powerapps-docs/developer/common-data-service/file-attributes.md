---
title: "File attributes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File attributes that store file data within the application, supporting attributes, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
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

A file attribute is used for storing file data up to a specified maximum size. A custom or customizable entity can have zero or more file attributes plus a notes (annotation) collection with zero to one attachment in each note. The <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> of the file attribute is `EntityFile`.

Web API | .NET API
------- | -------
[FieAttributeMetadata](/dynamics365/customer-engagement/web-api/fileattributemetadata) | <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>

For more information about types of files that are not allowed, see [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting.

> [!IMPORTANT]
> Some restrictions do apply when using the File and enhanced Image data-types of the Common Data Service. If Customer Managed Keys (CMK) is enabled on the tenant, then File, Image, and IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of CMK in order to make use of these data-types.


Solutions that involve excluded datatypes will not install.


Organizaion needs to opt out of the CMK in order to have this functionality.

<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
When a file attribute is added to an entity some additional attributes are created to support it.
  
### MaxSizeInKB attribute

 This value represents the maximum size (in kilobytes) of the file data that the attribute can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
  
<a name="BKMK_RetrievingFiles"></a>

## Retrieve file data
To retrieve file data, use the following APIs.

Web API | .NET API
------- | -------
 none  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest>
GET /api/data/v9.0/\<entity-type(id)\>/\<file-attribute-name\>/$value   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete data file by combining the data blocks in the same sequence as the blocks were received.

### Example: REST download

```http
GET
/api/data/v9.0/accounts(id)/myfileattribute/$value
Headers:
Range: 0-1023

Response:
206 Partial Content
byte[]

Response Headers:
Content-Disposition: attachment; filename="sample.txt"
x-ms-file-name: "sample.txt"
x-ms-file-size: 12345
Location: api/data/v9.0/accounts(id)/myfileattribute?FileContinuationToken
```
Chunking will be decided based on the **Range** header existence in the request. The full file will be downloaded (up to 16 MB) in one request if no **Range** header is included. For chunking, the **Location** response header contains the query-able parameter *FileContinuationToken*. Use the provided location header value in the next GET request to retrieve the next block of data in the sequence.

### Example: .NET C# code for download with chunking

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

## Upload file data  
To upload file data, use the following APIs.

Web API | .NET API
------- | -------
none   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>
PATCH /api/data/v9.0/\<entity-type(id)\>/\<file-attribute-name\>   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
none   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest>

As was previously mentioned under [Retrieve file data](#retrieve-file-data), uploading a data file of 16 MB or less can be accomplished in a single API call while uploading more than 16 MB of data requires the file data to be divided into blocks of 4 MB or less data. After the complete set of data blocks has been uploaded and a commit request has been sent, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in Azure Blob Storage.

### Example: REST upload with chunking (first request)

```http
PATCH /api/data/v9.0/accounts(id)/myfileattribute 

Headers: 
x-ms-transfer-mode: chunked 
x-ms-file-name: [User input from power apps] 

Response: 
200 OK 

Response Headers: 
x-ms-chunk-size: 4096 
Accept-Ranges: bytes 
Location: api/data/v9.0/accounts(id)/myfileattribute?FileContinuationToken 
```

### Example: REST upload with chunking (next request)

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

### Example: .NET C# code for upload with chunking

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

## Delete file data  
To delete file, attachment, or annotation data in Azure Blob Storage, use the following APIs.

Web API | .NET API
------- | -------
DELETE /api/data/v9.0/\<entity-type(id)\>/\<attribute-name\> | <xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest>

### See Also
[Image attributes](image-attributes.md)