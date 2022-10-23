---
title: "Use file column data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about uploading, downloading, and deleting data in file columns." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 10/23/2022
ms.reviewer: jdaly
ms.topic: article
author: NHelgren # GitHub ID
ms.subservice: dataverse-developer
ms.author: nhelgren # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Use file column data

[File columns](../../maker/data-platform/types-of-fields.md#file-columns) store binary data. File columns may be in any custom or customizable Dataverse table.

File columns are different from the other two system columns that can store binary data ([Note (Annotation) DocumentBody](reference/entities/annotation.md#BKMK_DocumentBody) and [Attachment (ActivityMimeAttachment) Body](reference/entities/activitymimeattachment.md#BKMK_Body)), because you cannot directly set the values in a create or update operation or retrieve the values with the record. You must use the methods described in this topic to set, update, or delete binary data for file columns.

There are several different ways to work with file column data. Because binary files may be large, it is frequently necessary to split the file into multiple chunks, (or blocks) that can be sent or received sequentially or in parallel to improve performance.

## Upload Files

There at three different ways to upload files to a file column:

- Use the Dataverse messages available to both the SDK and Web API
- Upload a file in a single request using Web API
- Upload the file in chunks using Web API

### Use the Dataverse messages to upload a file

Uploading a file this way requires using a set of three messages:


|Message|Description|
|---------|---------|
|`InitializeFileBlocksUpload`|Use this message to indicate the column that you want to upload a file to. It returns a *file continuation token* that you can use to upload the file in blocks using the `UploadBlock` message.|
|`UploadBlock`|Split your file into blocks and generate a *blockid* for each block. Then make multiple requests until all the blocks have been sent together with the file continuation token.|
|`CommitFileBlocksUpload`|After you have sent requests for all the blocks using `UploadBlock`, use this message to commit the upload operation by sending:<br />- The list of generated blockids<br />- The name of the file<br />- The mime type of the file<br />- The file continuation token|

#### [SDK for .NET](#tab/sdk)

You can use the following function to upload a file using the SDK:

```csharp
/// <summary>
/// Uploads a file
/// </summary>
/// <param name="service">The service</param>
/// <param name="entityReference">A reference to the record with the file column</param>
/// <param name="fileAttributeName">The name of the file column</param>
/// <param name="fileInfo">Information about the file to upload.</param>
/// <param name="fileMimeType">The mime type of the file, if known.</param>
/// <returns></returns>
static Guid UploadFile(
         IOrganizationService service,
         EntityReference entityReference,
         string fileAttributeName,
         FileInfo fileInfo,
         string fileMimeType = null)
{

   // Initialize the upload
   InitializeFileBlocksUploadRequest initializeFileBlocksUploadRequest = new()
   {
         Target = entityReference,
         FileAttributeName = fileAttributeName,
         FileName = fileInfo.Name
   };

   var initializeFileBlocksUploadResponse =
         (InitializeFileBlocksUploadResponse)service.Execute(initializeFileBlocksUploadRequest);

   string fileContinuationToken = initializeFileBlocksUploadResponse.FileContinuationToken;

   // Capture blockids while uploading
   List<string> blockIds = new();

   using Stream uploadFileStream = fileInfo.OpenRead();

   int blockSize = 4 * 1024 * 1024; // 4 MB

   byte[] buffer = new byte[blockSize];
   int bytesRead = 0;

   long fileSize = fileInfo.Length;
   // The number of iterations that will be required:
   // int blocksCount = (int)Math.Ceiling(fileSize / (float)blockSize);
   int blockNumber = 0;

   // While there is unread data from the file
   while ((bytesRead = uploadFileStream.Read(buffer, 0, buffer.Length)) > 0)
   {
         // The file or final block may be smaller than 4MB
         if (bytesRead < buffer.Length)
         {
            Array.Resize(ref buffer, bytesRead);
         }

         blockNumber++;

         string blockId = Convert.ToBase64String(Encoding.UTF8.GetBytes(blockNumber.ToString().PadLeft(16, '0')));

         blockIds.Add(blockId);

         // Copy the next block of data to send.
         var blockData = new byte[buffer.Length];
         buffer.CopyTo(blockData, 0);

         // Prepare the request
         UploadBlockRequest uploadBlockRequest = new()
         {
            BlockData = blockData,
            BlockId = blockId,
            FileContinuationToken = fileContinuationToken,
         };

         // Send the request
         service.Execute(uploadBlockRequest);
   }

   // Try to get the mimetype if not provided.
   if (string.IsNullOrEmpty(fileMimeType))
   {
         var provider = new FileExtensionContentTypeProvider();

         if (!provider.TryGetContentType(fileInfo.Name, out fileMimeType))
         {
            fileMimeType = "application/octet-stream";
         }
   }

   // Commit the upload
   CommitFileBlocksUploadRequest commitFileBlocksUploadRequest = new()
   {
         BlockList = blockIds.ToArray(),
         FileContinuationToken = fileContinuationToken,
         FileName = fileInfo.Name,
         MimeType = fileMimeType
   };

   var commitFileBlocksUploadResponse =
         (CommitFileBlocksUploadResponse)service.Execute(commitFileBlocksUploadRequest);

   return commitFileBlocksUploadResponse.FileId;

}
```

This function includes some logic to try and get the mime type of the file using the [FileExtensionContentTypeProvider.TryGetContentType(String, String) Method](xref:Microsoft.AspNetCore.StaticFiles.FileExtensionContentTypeProvider.TryGetContentType%2A) if it is not provided. If not found it will set the mime type to `application/octet-stream`.

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to set a file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `2578e950-8e51-ed11-bba1-000d3a9933c9`.

**Request**

This request uses the [InitializeFileBlocksUpload Action](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksUpload).

```http
POST [Organization Uri]/api/data/v9.2/[InitializeFileBlocksUpload](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksUpload) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 207

{
  "Target": {
    "accountid": "2578e950-8e51-ed11-bba1-000d3a9933c9",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "FileName": "25mb.pdf",
  "FileAttributeName": "sample_filecolumn"
}
```

**Response**

The response is a [InitializeFileBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksUploadResponse)

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeFileBlocksUploadResponse",
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

The file must then be broken into blocks of 4MB or less and sent using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock) with the following properties:


|Property|Description:  |
|---------|---------|
|`BlockId`|A string value that is unique within the set of blocks.|
|`BlockData`|A byte[] less than 4MB in size representing the portion of the file being sent.|
|`FileContinuationToken`|The value of the `InitializeFileBlocksUploadResponse.FileContinuationToken`|


**Request**

```http
POST [Organization Uri]/api/data/v9.2/UploadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 5593368

{
  "BlockId": "MDAwMDAwMDAwMDAwMDAwMQ==",
  "BlockData": "<byte[] data removed for brevity>",
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

After all the parts of the file have been sent using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock), use the [CommitFileBlocksUpload Action](xref:Microsoft.Dynamics.CRM.CommitFileBlocksUpload) to complete the upload using these properties:

|Property|Description:  |
|---------|---------|
|`FileName`|The name of the file.|
|`MimeType`|The mime type of the file.|
|`BlockList`|An array of strings representing the `BlockId` values in the previous `UploadBlock` operations. The order of these strings represents the order the server will use to combine the blocks into the original file.|
|`FileContinuationToken`|The value of the `InitializeFileBlocksUploadResponse.FileContinuationToken`|


**Request**

```http
POST [Organization Uri]/api/data/v9.2/CommitFileBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1213

{
  "FileName": "25mb.pdf",
  "MimeType": "application/pdf",
  "BlockList": [
    "MDAwMDAwMDAwMDAwMDAwMQ==",
    "MDAwMDAwMDAwMDAwMDAwMg==",
    "MDAwMDAwMDAwMDAwMDAwMw==",
    "MDAwMDAwMDAwMDAwMDAwNA==",
    "MDAwMDAwMDAwMDAwMDAwNQ==",
    "MDAwMDAwMDAwMDAwMDAwNg==",
    "MDAwMDAwMDAwMDAwMDAwNw=="
  ],
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

**Response**

The [CommitFileBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.CommitFileBlocksUploadResponse) returns the `FileId` value you can use to delete the file using the [DeleteFile Action](xref:Microsoft.Dynamics.CRM.DeleteFile) and the `FileSizeInBytes`.

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CommitFileBlocksUploadResponse",
  "FileId": "3878e950-8e51-ed11-bba1-000d3a9933c9",
  "FileSizeInBytes": 25870370
}
```

---


### Upload a file in a single request using Web API

### Upload the file in chunks using Web API

## Download Files

## Delete Files

There at two different ways to upload files to a file column:

- Use the Dataverse `DeleteFile` message available to both the SDK and Web API
- Send a DELETE request using Web API to the file column of the record.

### Use the DeleteFile message

### Send DELETE request to the file column



### See Also

[File columns](../../maker/data-platform/types-of-fields.md#file-columns)<br />
[Annotation (note) table](annotation-note-entity.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]