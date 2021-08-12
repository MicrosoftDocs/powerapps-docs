---
title: "File columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File columns that store file data within the application, supporting columns, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# File columns

A file column is used for storing file data up to a specified maximum size. A custom or customizable table can have zero or more file columns plus a notes (annotation) collection with zero to one attachment in each note. The <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> of the file column is `EntityFile`.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Web API (REST) | .NET API (SOAP)
------- | -------
[FileAttributeMetadata](/dynamics365/customer-engagement/web-api/fileattributemetadata) | <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>

For information about types of files that are not allowed, see [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting.

> [!IMPORTANT]
> Some restrictions do apply when using the File and enhanced Image data-types of the Microsoft Dataverse. If Customer Managed Keys (CMK) is enabled on the tenant, IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of CMK in order to make use of these data-types.<p/>
> All CMK organizations as of version: 9.2.21052.00103 can support the use of the Dataverse File and Image data-types. Files within CMK organizations are
> limited to a maximum size of 128MB per file. All files and images within CMK organizations will be stored in the Dataverse relational storage, instead of Dataverse File Blob
> storage.
> Other limitations:
>  - User Delegation SAS Downloads are not supported
>  - Chunking uploads and downloads are limited to a single chunk
>  
>  File columns are supported in <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.SdkClientVersion> 9.0.45.329 or greater and Web API version 9.1 or greater.


<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->
  
## Supporting columns  
When a file column is added to a table some additional columns are created to support it.
  
### MaxValue column

 This value represents the maximum size (in kilobytes) of the file data that the column can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
 
 > [!NOTE]
 > MaxValue is set when the File column is added to a table. This cannot be changed after it is set.
  
## Retrieve file data
To retrieve file column data use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
 none  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest>
GET /api/data/v9.1/\<entity-type(id)\>/\<file-attribute-name\>/$value   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete data file by combining the data blocks in the same sequence as the blocks were received.

Messages such as <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> cannot be used to download file column data.

### Example: REST download with chunking

**Request**
```http
GET [Organization URI]/api/data/v9.1/accounts(id)/myfileattribute/$value
Headers:
Range: bytes=0-1023/8192
```

**Response**
```http
206 Partial Content

Body:
byte[]

Response Headers:
Content-Disposition: attachment; filename="sample.txt"
x-ms-file-name: "sample.txt"
x-ms-file-size: 8192
Location: api/data/v9.1/accounts(id)/myfileattribute?FileContinuationToken
```

Chunking will be decided based on the `Range` header existence in the request. The Range header value format is: startByte-endByte/total bytes. The full file will be downloaded (up to 16 MB) in one request if no `Range` header is included. For chunking, the `Location` response header contains the query-able parameter `FileContinuationToken`. Use the provided location header value in the next GET request to retrieve the next block of data in the sequence.

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
To upload file column data, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
none   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>
PATCH /api/data/v9.1/\<entity-type(id)\>/\<file-attribute-name\>   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
none   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest>

Files can be uploaded either in full up to the maximum size configured, or in chunks.

> [!NOTE]
> As of this article's publication date, the restriction of using chunked upload for files greater than 16 MB has been removed.
> The chunking APIs will continue to be available to maintain backwards compatibility with existing solutions.

### Example: .NET C# code for full file upload

```csharp
static async Task FullFileUploadAsync(
            Uri urlPrefix,
            string customEntitySetName,
            string entityId,
            string entityFileOrAttributeAttributeLogicalName,
            string fileRootPath,
            string uploadFileName,
            string accessToken)
        {
            var filePath = Path.Combine(fileRootPath, uploadFileName);
            var fileStream = File.OpenRead(filePath);
            var url = new Uri(urlPrefix, $"{customEntitySetName}({entityId})/{entityFileOrAttributeAttributeLogicalName}");

            using (var request = new HttpRequestMessage(new HttpMethod("PATCH"), url))
            {
                request.Headers.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken);
                                request.Content = new StreamContent(fileStream);
                request.Content.Headers.Add("Content-Type", "application/octet-stream");
                request.Content.Headers.Add("x-ms-file-name", uploadFileName);
                                
                using (var response = await Client.SendAsync(request))
                {
                    response.EnsureSuccessStatusCode();
                }
            }
        }
```

The following is the legacy method of uploading a data file of 16 MB or more by dividing file data blocks of 4 MB or less. After the complete set of data blocks has been uploaded and a commit request has been sent, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in Azure Blob Storage.

Messages such as <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> cannot be used to upload file column data.

### Example: REST upload with chunking (first request)

**Request**
```http
PATCH [Organization URI]/api/data/v9.1/accounts(id)/myfileattribute 

Headers: 
x-ms-transfer-mode: chunked 
x-ms-file-name: sample.png
```

**Request** (alternate form)

This form of the request uses a query string parameter and supports non-ASCII language file names. If the file name is specified in both the header and as a query string parameter, the header value has precedence.

```http
PATCH [Organization URI]/api/data/v9.1/accounts(id)/myfileattribute?x-ms-file-name=测试.txt

Headers: 
x-ms-transfer-mode: chunked
```

**Response**
```http
200 OK 

Response Headers: 
x-ms-chunk-size: 4096 
Accept-Ranges: bytes 
Location: api/data/v9.1/accounts(id)/myfileattribute?FileContinuationToken 
```

### Example: REST upload with chunking (next request)
**Request**
```http
PATCH [Organization URI]/api/data/v9.1/accounts(id)/myfileattribute?FileContinuationToken 

Headers: 
Content-Range: bytes 0-4095/8192 
Content-Type: application/octet-stream
x-ms-file-name: sample.png

Body:
byte[]
```

**Response**
```http
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
To delete the file column data from storage, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
DELETE /api/data/v9.1/\<entity-type(id)\>/\<attribute-name\> | <xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest>

### See Also
[Image columns](image-attributes.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
