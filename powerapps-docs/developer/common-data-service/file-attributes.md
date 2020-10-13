---
title: "File attributes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about File attributes that store file data within the application, supporting attributes, retrieving data, and uploading file data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/09/2020
ms.reviewer: "pehecke"
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

Web API (REST) | .NET API (SOAP)
------- | -------
[FileAttributeMetadata](/dynamics365/customer-engagement/web-api/fileattributemetadata) | <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>

For information about types of files that are not allowed, see [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting.

> [!IMPORTANT]
> Some restrictions do apply when using the File and enhanced Image data-types of the Common Data Service. If Customer Managed Keys (CMK) is enabled on the tenant, then File, Image, and IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of CMK in order to make use of these data-types.<p/>
> File attributes are supported in <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.SdkClientVersion> 9.0.45.329 or greater and Web API version 9.1 or greater.


<!--File data is not passed to plug-ins for performance reasons. You must retrieve the file data in plug-in code using an explicit retrieve call. -->
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
When a file attribute is added to an entity some additional attributes are created to support it.
  
### MaxSizeInKB attribute

 This value represents the maximum size (in kilobytes) of the file data that the attribute can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
 
 > [!NOTE]
 > MaxSizeInKB is set when the File attribute is added to an entity. This cannot be changed after it is set.
  
<a name="BKMK_RetrievingFiles"></a>

## Retrieve file data
To retrieve file attribute data use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
 none  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest>
GET /api/data/v9.1/\<entity-type(id)\>/\<file-attribute-name\>/$value   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

File data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. File data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete data file by combining the data blocks in the same sequence as the blocks were received.

Messages such as <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> cannot be used to download file attribute data.

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
To upload file attribute data, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
none   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>
PATCH /api/data/v9.1/\<entity-type(id)\>/\<file-attribute-name\>   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
none   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest>,<br/><xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest>

As was previously mentioned under [Retrieve file data](#retrieve-file-data), uploading a data file of 16 MB or less can be accomplished in a single API call while uploading more than 16 MB of data requires the file data to be divided into blocks of 4 MB or less data. After the complete set of data blocks has been uploaded and a commit request has been sent, the web service will automatically combine the blocks, in the same sequence as the data blocks were uploaded, into a single data file in Azure Blob Storage.

Messages such as <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> cannot be used to upload file attribute data.

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
To delete the file attribute data from storage, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
DELETE /api/data/v9.1/\<entity-type(id)\>/\<attribute-name\> | <xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest>

### See Also
[Image attributes](image-attributes.md)
