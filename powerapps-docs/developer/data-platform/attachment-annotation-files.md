---
title: "Use file data with Attachment and Note records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using file data with Attachment and Note records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/02/2023
ms.reviewer: jdaly
ms.topic: article
author: JimDaly # GitHub ID
ms.subservice: dataverse-developer
ms.author: jdaly # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Use file data with Attachment and Note records

[Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) and [Note (Annotation)](reference/entities/annotation.md) tables contain special string columns that store file data.


These tables existed before file or image columns, so they work differently.

- The binary file data is stored as Base64 encoded string values in string columns: [ActivityMimeAttachment.Body](reference/entities/activitymimeattachment.md#BKMK_Body) and [Annotation.DocumentBody](reference/entities/annotation.md#BKMK_DocumentBody).
- File name data is stored in the `FileName` column.
- Mime type data is stored in the `MimeType` column.

Because these columns are part of the data for the attachment or note record, you should update these three columns together with any other values.

## Using file data

You can directly get and set the values of the `activitymimeattachment.body` and `annotation.documentbody` columns as Base64 encoded strings. This should be fine as long as the files are not too large, for example under 4 MB.

By default the maximum size is 5 MB. You can configure these columns to accept files as large as 128 MB. When you have increased the maximum file size and are working with larger files, you should use messages provided to break the files into smaller chunks when uploading or downloading files.  For information about retrieving or changing the file size limits, see [File size limits](#file-size-limits).

## Attachment files

An attachment is a file that is associated with an [email](reference/entities/email.md) activity, either directly or though an [Email Template (Template)](reference/entities/template.md). Multiple attachments can be associated with the activity or template.

> [!NOTE]
> You can re-use attachment files by setting the `activitymimeattachment.attachmentid` value to refer to another existing attachment rather than by setting the `body`, `filename`, and `mimetype` properties.
> 
> [Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) should not be confused with [activityfileattachment](reference/entities/activityfileattachment.md), which supports files associated with the [Post](reference/entities/post.md) table.
>
> Within the Dataverse schema there is also a public table with the name `Attachment` which is exposed in the Web API as [attachment EntityType](xref:Microsoft.Dynamics.CRM.attachment). This table can be queried and it reflects data in the `ActivityMimeAttachment` table. But it doesn't support create, retrieve, update, or delete operations. This table doesn't appear within the [PowerApps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) designer.

### Upload Attachment files

Use the `InitializeAttachmentBlocksUpload`, `UploadBlock`, and `CommitAttachmentBlocksUpload` messages to upload large files for attachments.

> [!IMPORTANT]
> These messages can only be used to create a new attachment. It you try to update an existing attachment with these messages you will get an error that the record already exists.

#### [SDK for .NET](#tab/sdk)

The following static `UploadAttachment` method shows how to create a new attachment with a file using the <xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>, <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>, and <xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest> classes to return a <xref:Microsoft.Dynamics.CRM.CommitAttachmentBlocksUploadResponse> with `ActivityMimeAttachmentId` and `FileSizeInBytes` properties.

```csharp
static CommitAttachmentBlocksUploadResponse UploadAttachment(
   IOrganizationService service,
   Entity attachment,
   FileInfo fileInfo,
   string fileMimeType = null)
{
   if (attachment.LogicalName != "activitymimeattachment")
   {
         throw new ArgumentException(
            "The attachment parameter must be an activitymimeattachment entity.",
            nameof(attachment));
   }

   // body value in activitymimeattachment not needed. Remove if found.
   if (attachment.Contains("body"))
   {
         attachment.Attributes.Remove("body");
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
   // Don't overwrite mimetype value if it exists
   if (!attachment.Contains("mimetype"))
   {
         attachment["mimetype"] = fileMimeType;
   }

   // Initialize the upload
   InitializeAttachmentBlocksUploadRequest initializeRequest = new()
   {
         Target = attachment
   };

   var initializeResponse =
         (InitializeAttachmentBlocksUploadResponse)service.Execute(initializeRequest);

   string fileContinuationToken = initializeResponse.FileContinuationToken;

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

         string blockId = Convert.ToBase64String(Encoding.UTF8.GetBytes(Guid.NewGuid().ToString()));

         blockIds.Add(blockId);

         // Prepare the request
         UploadBlockRequest uploadBlockRequest = new()
         {
            BlockData = buffer,
            BlockId = blockId,
            FileContinuationToken = fileContinuationToken,
         };

         // Send the request
         service.Execute(uploadBlockRequest);
   }

   // Commit the upload
   CommitAttachmentBlocksUploadRequest commitRequest = new()
   {
         BlockList = blockIds.ToArray(),
         FileContinuationToken = fileContinuationToken,
         Target = attachment
   };
   
      return  (CommitAttachmentBlocksUploadResponse)service.Execute(commitRequest);

}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

[!INCLUDE [cc-trygetcontenttype-note](includes/cc-trygetcontenttype-note.md)]

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to create a new attachment record that sets the `body`, `filename`, and `mimetype` columns for a PDF file named `25mb.pdf`. The attachment is associated to an email.

**Request**

The first request uses the [InitializeAttachmentBlocksUpload Action](xref:Microsoft.Dynamics.CRM.InitializeAttachmentBlocksUpload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeAttachmentBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 315

{
  "Target": {
    "objectid_email@odata.bind": "emails(<activityid>)",
    "objecttypecode": "email",
    "subject": "Sample attached 25mb.pdf",
    "filename": "25mb.pdf",
    "mimetype": "application/pdf",
    "@odata.type": "Microsoft.Dynamics.CRM.activitymimeattachment"
  }
}
```

**Response**

The response is a [InitializeAttachmentBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeAttachmentBlocksUploadResponse) providing the `FileContinuationToken` value to use with subsequent requests.

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeAttachmentBlocksUploadResponse",
  "FileContinuationToken": "<Removed for brevity>"
}
```

You must then break up the file into blocks of 4 MB or less and send each block using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock) with the following properties:


|Property|Description:  |
|---------|---------|
|`BlockId`|A unique Base64 encoded string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size.<br />For a given file, the length of the `BlockId` value must be the same size for each block.|
|`BlockData`|A Base64 encoded string containing the `byte[]` less than 4 MB in size representing the portion of the file being sent.|
|`FileContinuationToken`|The value of the `InitializeAttachmentBlocksUploadResponse.FileContinuationToken`|


[!INCLUDE [cc-generate-blockid-tip](includes/cc-generate-blockid-tip.md)]

**Request**

```http
POST [Organization Uri]/api/data/v9.2/UploadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 5593372

{
  "BlockId": "YTIyNzMzNGUtYThmYy00ZGEwLWExMjctYjMwMDY4ZThhMmMz",
  "BlockData": "<Removed for brevity>",
  "FileContinuationToken": "<Removed for brevity>"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

After all the parts of the file have been sent using multiple requests using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock), use the [CommitAttachmentBlocksUpload Action](xref:Microsoft.Dynamics.CRM.CommitAttachmentBlocksUpload) to complete the upload using these properties:

|Property|Description:  |
|---------|---------|
|`Target`|The attachment record with values set for `filename` and `mimetype`.|
|`BlockList`|An array of strings representing the `BlockId` values in the previous `UploadBlock` operations. The order of these strings represents the order the server will use to combine the blocks into the original file.|
|`FileContinuationToken`|The value of the `InitializeAttachmentBlocksUploadResponse.FileContinuationToken`|

**Request**

In this example the `BlockList` values represent seven previous requests using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock).

```http
POST [Organization Uri]/api/data/v9.2/CommitAttachmentBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1612

{
  "Target": {
    "objectid_email@odata.bind": "emails(b1b7e09f-58a3-ed11-aad1-000d3a9933c9)",
    "objecttypecode": "email",
    "subject": "Sample attached 25mb.pdf",
    "filename": "25mb.pdf",
    "mimetype": "application/pdf",
    "@odata.type": "Microsoft.Dynamics.CRM.activitymimeattachment"
  },
  "BlockList": [
    "YTIyNzMzNGUtYThmYy00ZGEwLWExMjctYjMwMDY4ZThhMmMz",
    "NzFkYTcwZWMtYjBmMC00YWI1LTkyODYtZjc5NmJkMGUyZjBm",
    "ODRmZTU0NDktNWU5Ni00MWM3LWIyOTYtNDRmMjhhNzRkMzIz",
    "NmRiZDcxZTktZGIxNi00ZTM0LWJjNzEtOTM3Y2YwMjQwMTY2",
    "NWRhYTFkYzEtM2Y0MC00OGI5LTlkYzQtNDBiNTVjZjY4ZDQ1",
    "NThjMTk1M2ItMjFiZS00YTQ1LWFkMDMtMDFjNjFmOTM5OTdm",
    "NWFmYzJlYWMtODgwMi00YmY4LTkxNGMtNDgzY2UxN2ZmMGE0"
  ],
  "FileContinuationToken": "<Removed for brevity>"
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CommitAttachmentBlocksUploadResponse",
  "FileSizeInBytes": 25870370,
  "ActivityMimeAttachmentId": "<ID of attachment created>"
}
```

---


### Download Attachment files

You can download an attachment file in a single operation using the Web API, or you can download the attachment file in chunks using the SDK or Web API.

#### Download Attachment files in a single operation using Web API

Using the Web API, you can download an attachment file in a single operation:

**Request**

```http
GET [Organization Uri]/api/data/v9.2/activitymimeattachments(<activitymimeattachmentid>)/body/$value HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Content-Type: text/plain

<Base64 string content removed for brevity>
```

> [!NOTE]
> Unlike retrieving file columns, this method does not provide information about file size, file name, or mime type. More information: [Download a file in a single request using Web API](file-column-data.md#download-a-file-in-a-single-request-using-web-api) and [Retrieve the raw value of a property](webapi/retrieve-entity-using-web-api.md#retrieve-the-raw-value-of-a-property)

#### Download Attachment files in chunks

To retrieve the file in in chunks, you must use the following, with either the SDK or Web API:

|Message|Description|
|---------|---------|
|`InitializeAttachmentBlocksDownload`|Use this message to indicate the note record that you want to download a file from. It returns the file size in bytes and a *file continuation token* that you can use to download the file in blocks using the `DownloadBlock` message.|
|`DownloadBlock`|Request the size of the block, the offset value and the file continuation token.|

Once you've downloaded all the blocks, you must join them to create the entire downloaded file.

#### [SDK for .NET](#tab/sdk)

The following static `DownloadAttachment` method shows how to download an attachment using the SDK with the [InitializeAttachmentBlocksDownloadRequest](xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksDownloadRequest) and [DownloadBlockRequest](xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest) classes. This function returns the `byte[]` data and the name of the file.

```csharp
static (byte[] bytes, string fileName) DownloadAttachment(
   IOrganizationService service,
   EntityReference target)
{
   if (target.LogicalName != "activitymimeattachment")
   {
         throw new ArgumentException(
            "The target parameter must refer to an activitymimeattachment record.",
            nameof(target));
   }

   InitializeAttachmentBlocksDownloadRequest initializeRequest = new()
   {
         Target = target
   };

   var response =
         (InitializeAttachmentBlocksDownloadResponse)service.Execute(initializeRequest);

   string fileContinuationToken = response.FileContinuationToken;
   int fileSizeInBytes = response.FileSizeInBytes;
   string fileName = response.FileName;

   List<byte> fileBytes = new(fileSizeInBytes);

   long offset = 0;
   long blockSizeDownload = 4 * 1024 * 1024; // 4 MB

   // File size may be smaller than defined block size
   if (fileSizeInBytes < blockSizeDownload)
   {
         blockSizeDownload = fileSizeInBytes;
   }

   while (fileSizeInBytes > 0)
   {
         // Prepare the request
         DownloadBlockRequest downLoadBlockRequest = new()
         {
            BlockLength = blockSizeDownload,
            FileContinuationToken = fileContinuationToken,
            Offset = offset
         };

         // Send the request
         var downloadBlockResponse =
                  (DownloadBlockResponse)service.Execute(downLoadBlockRequest);

         // Add the block returned to the list
         fileBytes.AddRange(downloadBlockResponse.Data);

         // Subtract the amount downloaded,
         // which may make fileSizeInBytes < 0 and indicate
         // no further blocks to download
         fileSizeInBytes -= (int)blockSizeDownload;
         // Increment the offset to start at the beginning of the next block.
         offset += blockSizeDownload;
   }

   return (fileBytes.ToArray(), fileName);
}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to download a PDF file named 25mb.pdf from the an attachment with the specified `activitymimeattachmentid` value.

**Request**

This request uses the [InitializeAttachmentBlocksDownload Action](xref:Microsoft.Dynamics.CRM.InitializeAttachmentBlocksDownload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeAttachmentBlocksDownload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 165

{
  "Target": {
    "activitymimeattachmentid": "<activitymimeattachmentid>",
    "@odata.type": "Microsoft.Dynamics.CRM.activitymimeattachment"
  }
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeAttachmentBlocksDownloadResponse",
  "FileName": "25mb.pdf",
  "FileSizeInBytes": 25870370,
  "FileContinuationToken": "<Removed for brevity>"
}
```

The response is a [InitializeAttachmentBlocksDownloadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeAttachmentBlocksDownloadResponse) which provides:

- `FileName`: The name of the file
- `FileSizeInBytes`: The size of the file
- `FileContinuationToken`: The file continuation token to use in subsequent requests

Based on the size of the file and the size of the block you'll download, send more requests using the [DownloadBlock Action](xref:Microsoft.Dynamics.CRM.DownloadBlock) as shown below.

**Request**

```http
POST [Organization Uri]/api/data/v9.2/DownloadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 901

{
  "Offset": 0,
  "BlockLength": 4194304,
  "FileContinuationToken": "<Removed for brevity>"
}
```

[!INCLUDE [cc-offset-blocklength-example](includes/cc-offset-blocklength-example.md)]

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DownloadBlockResponse",
  "Data": "<Removed for brevity>"
}
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

## Annotation files

A note is a record associated with a table row that contains text and may have a single file attached. Only those tables defined with [EntityMetadata.HasNotes](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.HasNotes) set to true may have notes associated with them.


### Upload Annotation files

Use the `InitializeAnnotationBlocksUpload`, `UploadBlock`, and `CommitAnnotationBlocksUpload` messages to upload files for notes.

> [!NOTE]
> The annotation you pass as the `Target` parameter for these messages must have an `annotationid` value. This is how you can update existing annotation records.
>
> To create a new annotation with these messages you must generate a new `Guid` value to set as the `annotationid` value rather than let Dataverse generate the value. Normally, it is best to let Dataverse generate the unique identifier values when creating new records, but that is not possible with these messages.

#### [SDK for .NET](#tab/sdk)

The following static `UploadNote` method shows how to create or update a note with a file using the <xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksUploadRequest>, <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>, and <xref:Microsoft.Crm.Sdk.Messages.CommitAnnotationBlocksUploadRequest> classes and it will return a <xref:Microsoft.Dynamics.CRM.CommitAnnotationBlocksUploadResponse> with `AnnotationId` and `FileSizeInBytes` properties.

```csharp
static CommitAnnotationBlocksUploadResponse UploadNote(
   IOrganizationService service,
   Entity annotation,
   FileInfo fileInfo,
   string? fileMimeType = null)
{

   if (annotation.LogicalName != "annotation")
   {
         throw new ArgumentException(
            message: "The annotation parameter must be an annotation entity",
            paramName: nameof(annotation));
   }
   if (!annotation.Attributes.Contains("annotationid") || annotation.Id != Guid.Empty)
   {
         throw new ArgumentException(
            message: "The annotation parameter must include a valid annotationid value.",
            paramName: nameof(annotation));
   }

   // documentbody value in annotation not needed. Remove if found.
   if (annotation.Contains("documentbody"))
   {
         annotation.Attributes.Remove("documentbody");
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
   // Don't override what might be included in the annotation.
   if (!annotation.Contains("mimetype")) {
         annotation["mimetype"] = fileMimeType;
   }
   
   // Initialize the upload
   InitializeAnnotationBlocksUploadRequest initializeRequest = new()
   {
         Target = annotation
   };

   var initializeResponse =
         (InitializeAnnotationBlocksUploadResponse)service.Execute(initializeRequest);

   string fileContinuationToken = initializeResponse.FileContinuationToken;

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
         // Generates base64 string blockId values based on a Guid value so they are always the same length.
         string blockId = Convert.ToBase64String(Encoding.UTF8.GetBytes(Guid.NewGuid().ToString()));

         blockIds.Add(blockId);

         // Prepare the request
         UploadBlockRequest uploadBlockRequest = new()
         {
            BlockData = buffer,
            BlockId = blockId,
            FileContinuationToken = fileContinuationToken,
         };

         // Send the request
         service.Execute(uploadBlockRequest);
   }

   // Commit the upload
   CommitAnnotationBlocksUploadRequest commitRequest = new()
   {
         BlockList = blockIds.ToArray(),
         FileContinuationToken = fileContinuationToken,
         Target = annotation
   };

      return  (CommitAnnotationBlocksUploadResponse)service.Execute(commitRequest);
}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

[!INCLUDE [cc-trygetcontenttype-note](includes/cc-trygetcontenttype-note.md)]

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to create a new annotation record that setting the `documentbody` to a PDF file named `25mb.pdf`. The annotation is associated to an account record.

**Request**

The first request uses the [InitializeAnnotationBlocksUpload Action](xref:Microsoft.Dynamics.CRM.InitializeAnnotationBlocksUpload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeAnnotationBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 294

{
  "Target": {
    "annotationid": "<annotationid>",
    "subject": "large PDF file",
    "filename": "25mb.pdf",
    "notetext": "Please see new attached pdf file.",
    "mimetype": "application/pdf",
    "@odata.type": "Microsoft.Dynamics.CRM.annotation"
  }
}
```

**Response**

The response is a [InitializeAnnotationBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeAnnotationBlocksUploadResponse) providing the `FileContinuationToken` value to use with subsequent requests.

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeAnnotationBlocksUploadResponse",
  "FileContinuationToken": "<Removed for brevity>"
}
```

You must then break up the file into blocks of 4 MB or less and send each block using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock) with the following properties:


|Property|Description:  |
|---------|---------|
|`BlockId`|A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size.<br />For a given file, the length of the `BlockId` value must be the same size for each block.|
|`BlockData`|A Base64 encoded string containing the byte[] less than 4 MB in size representing the portion of the file being sent.|
|`FileContinuationToken`|The value of the `InitializeAttachmentBlocksUploadResponse.FileContinuationToken`|


[!INCLUDE [cc-generate-blockid-tip](includes/cc-generate-blockid-tip.md)]

**Request**

```http
POST [Organization Uri]/api/data/v9.2/UploadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 5593352

{
  "BlockId": "Yjc3ZmU5MjgtZjBlNi00NTY5LThkYjMtYmFlZDkzOGE1ODFm",
  "BlockData": "<Removed for brevity>",
  "FileContinuationToken": "<Removed for brevity>"
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

After all the parts of the file have been sent using multiple requests using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock), use the [CommitAnnotationBlocksUpload Action](xref:Microsoft.Dynamics.CRM.CommitAnnotationBlocksUpload) to complete the upload using these properties:

|Property|Description:  |
|---------|---------|
|`Target`|The note record with values set for `filename` and `mimetype`.|
|`BlockList`|An array of strings representing the `BlockId` values in the previous `UploadBlock` operations. The order of these strings represents the order the server will use to combine the blocks into the original file.|
|`FileContinuationToken`|The value of the `InitializeAnnotationBlocksUploadResponse.FileContinuationToken`|

**Request**

```http
POST [Organization Uri]/api/data/v9.2/CommitAnnotationBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1571

{
  "Target": {
    "annotationid": "<annotationid>",
    "subject": "large PDF file",
    "filename": "25mb.pdf",
    "notetext": "Please see new attached pdf file.",
    "mimetype": "application/pdf",
    "@odata.type": "Microsoft.Dynamics.CRM.annotation"
  },
  "BlockList": [
    "Yjc3ZmU5MjgtZjBlNi00NTY5LThkYjMtYmFlZDkzOGE1ODFm",
    "ODg0NDM3NDgtMzkzZi00NjE5LTkzODUtNDA5YmNhOTQzYWNh",
    "Zjk2ZDg2ZjYtZjczNS00MWU1LTkzZjUtOGQ3MzhlODYzZjA0",
    "YzJhZGY3YjctODkyYy00YmEzLWJiM2UtNjI1ODZiY2EwZmM4",
    "NTg5MjY1NWUtN2U1Ni00MTFlLWI0MzktZWIxNTVhNzViZTBl",
    "NTQwYjZjZjctYjkyMy00MzBlLWIzNzAtYjYyYmFlOGE3NTY2",
    "YzhlNTFiNDQtNDA4ZC00NDdlLThjYTgtMGMyNmY5YjRlMTA5"
  ],
  "FileContinuationToken": "<Removed for brevity>"
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CommitAnnotationBlocksUploadResponse",
  "AnnotationId": "<annotationid>",
  "FileSizeInBytes": 25870370
}
```

---


### Download Annotation files

You can download a note file in a single operation using the Web API, or you can download the note file in chunks using the SDK or Web API.

#### Download Annotation files in a single operation using Web API

Using the Web API, you can download an note file in a single operation:

**Request**

```http
GET [Organization Uri]/api/data/v9.2/annotations(<annotationid>)/documentbody/$value HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Content-Type: text/plain

<Base64 string content removed for brevity>
```

> [!NOTE]
> Unlike retrieving file columns, this method does not provide information about file size, file name, or mime type. More information: [Download a file in a single request using Web API](file-column-data.md#download-a-file-in-a-single-request-using-web-api) and [Retrieve the raw value of a property](webapi/retrieve-entity-using-web-api.md#retrieve-the-raw-value-of-a-property)

#### Download Annotation files in chunks

To retrieve the file in in chunks, you must use the following, with either the SDK or Web API:

|Message|Description|
|---------|---------|
|`InitializeAnnotationBlocksDownload`|Use this message to indicate the note record that you want to download a file from. It returns the file size in bytes and a *file continuation token* that you can use to download the file in blocks using the `DownloadBlock` message.|
|`DownloadBlock`|Request the size of the block, the offset value and the file continuation token.|

Once you've downloaded all the blocks, you must join them to create the entire downloaded file.

#### [SDK for .NET](#tab/sdk)

The following static `DownloadNote` method shows how to download an note using the SDK with the [InitializeAnnotationBlocksDownloadRequest](xref:Microsoft.Crm.Sdk.Messages.InitializeAnnotationBlocksDownloadRequest) and [DownloadBlockRequest](xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest) classes. This function returns the `byte[]` data and the name of the file.

```csharp
static (byte[] bytes, string fileName) DownloadNote(
    IOrganizationService service,
    EntityReference target)
{
if (target.LogicalName != "annotation")
{
      throw new ArgumentException("The target parameter must refer to an note record.", nameof(target));
}

InitializeAnnotationBlocksDownloadRequest initializeRequest = new()
{
      Target = target
};

var response =
      (InitializeAnnotationBlocksDownloadResponse)service.Execute(initializeRequest);

string fileContinuationToken = response.FileContinuationToken;
int fileSizeInBytes = response.FileSizeInBytes;
string fileName = response.FileName;

List<byte> fileBytes = new(fileSizeInBytes);

long offset = 0;
long blockSizeDownload = 4 * 1024 * 1024; // 4 MB

// File size may be smaller than defined block size
if (fileSizeInBytes < blockSizeDownload)
{
      blockSizeDownload = fileSizeInBytes;
}

while (fileSizeInBytes > 0)
{
      // Prepare the request
      DownloadBlockRequest downLoadBlockRequest = new()
      {
            BlockLength = blockSizeDownload,
            FileContinuationToken = fileContinuationToken,
            Offset = offset
      };

      // Send the request
      var downloadBlockResponse =
                  (DownloadBlockResponse)service.Execute(downLoadBlockRequest);

      // Add the block returned to the list
      fileBytes.AddRange(downloadBlockResponse.Data);

      // Subtract the amount downloaded,
      // which may make fileSizeInBytes < 0 and indicate
      // no further blocks to download
      fileSizeInBytes -= (int)blockSizeDownload;
      // Increment the offset to start at the beginning of the next block.
      offset += blockSizeDownload;
}

return (fileBytes.ToArray(), fileName);
}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to download a PDF file named 25mb.pdf from the a note with the specified `annotationid` value.

**Request**

This request uses the [InitializeAnnotationBlocksDownload Action](xref:Microsoft.Dynamics.CRM.InitializeAnnotationBlocksDownload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeAnnotationBlocksDownload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 141

{
  "Target": {
    "annotationid": "<annotationid>",
    "@odata.type": "Microsoft.Dynamics.CRM.annotation"
  }
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeAnnotationBlocksDownloadResponse",
  "FileContinuationToken": "<removed for brevity>",
  "FileSizeInBytes": 25870370,
  "FileName": "25mb.pdf"
}
```

The response is a [InitializeAnnotationBlocksDownloadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeAnnotationBlocksDownloadResponse) which provides:

- `FileName`: The name of the file
- `FileSizeInBytes`: The size of the file
- `FileContinuationToken`: The file continuation token to use in subsequent requests

Based on the size of the file and the size of the block you'll download, send more requests using the [DownloadBlock Action](xref:Microsoft.Dynamics.CRM.DownloadBlock) as shown below.

**Request**

```http
POST [Organization Uri]/api/data/v9.2/DownloadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 901

{
  "Offset": 0,
  "BlockLength": 4194304,
  "FileContinuationToken": "<Removed for brevity>"
}
```

[!INCLUDE [cc-offset-blocklength-example](includes/cc-offset-blocklength-example.md)]

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DownloadBlockResponse",
  "Data": "<Removed for brevity>"
}
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

## File size limits

The [Organization.MaxUploadFileSize](reference/entities/organization.md#BKMK_MaxUploadFileSize) column specifies the maximum allowed size of an a file (in bytes) for an attachment and note, as well as other kinds of data, such as web resource files used for model-driven apps.

The default size is 5 MB (5242880 bytes) and the maximum value is 128 MB (131072000 bytes) and can be set in the email settings for the environment. More information: [Manage email settings](/power-platform/admin/settings-email)

If you try to upload a file that is too large, you'll get the following error:

> Name: `unManagedidsattachmentinvalidfilesize`<br />
> Code: `0x80044a02`<br />
> Number: `-2147202558`<br />
> Message: `Attachment file size is too big.`

> [!NOTE]
> The maximum upload file size limit applies to the size of the file in Base64 encoding. A Base64 encoding produces a string that is larger than the original `byte[]` file data..

### Retrieve max upload file size

Use the following ways to retrieve the maximum upload file size.

# [SDK for .NET](#tab/sdk)

Use a static method like the following `GetMaxUploadFileSize` to get the value.

```csharp
public static int GetMaxUploadFileSize(IOrganizationService service) {

   QueryExpression query = new("organization") { 
         ColumnSet = new ColumnSet("maxuploadfilesize")
   };

   EntityCollection organizations = service.RetrieveMultiple(query);

   // There is only one row in organization table
   return (int)organizations.Entities.FirstOrDefault()["maxuploadfilesize"];
}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.RetrieveMultiple Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)
- [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)


# [Web API](#tab/webapi)

Return the single row from the organization table with the `maxuploadfilesize` property.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/organizations?$select=maxuploadfilesize HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#organizations(maxuploadfilesize)",
  "value": [
    {
      "@odata.etag": "W/\"77676290\"",
      "maxuploadfilesize": 5242880,
      "organizationid": "<organizationid>"
    }
  ]
}
```

More information:

[Query data using the Web API](webapi/query-data-web-api.md)

---

### Update max upload file size

Use the following to set the `organization.maxuploadfilesize` value.

# [SDK for .NET](#tab/sdk)

Use a static method like the following `SetMaxUploadFileSize` to set the maximum upload file size.

```csharp
public static void SetMaxUploadFileSize(
    IOrganizationService service, 
    int maxUploadFileSizeInBytes)
{
   if (maxUploadFileSizeInBytes > 131072000 || maxUploadFileSizeInBytes < 1) {
         throw new ArgumentOutOfRangeException(nameof(maxUploadFileSizeInBytes), 
         "The maxUploadFileSizeInBytes parameter must be less than 131072000 bytes and greater than 0 bytes.");
   }

   QueryExpression query = new("organization")
   {
         ColumnSet = new ColumnSet("organizationid")
   };

   EntityCollection organizations = service.RetrieveMultiple(query);

   // There is only one row in organization table
   Entity organization = organizations.Entities.FirstOrDefault();
   organization["maxuploadfilesize"] = maxUploadFileSizeInBytes;

   service.Update(organization);
}
```

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.RetrieveMultiple Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)
- [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)
- [IOrganizationService.Update Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A)

# [Web API](#tab/webapi)

There is only a single row in the organization table. After you retrieve that value, use the `organizationid` returned to update the row. The <xref:Microsoft.Dynamics.CRM.WhoAmIResponse> also includes this value.

**Request**

```http
PATCH [Organization Uri]/api/data/v9.2/organizations(<organizationid>) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 38

{
  "maxuploadfilesize": 131072000
}
```

**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/organizations(<organizationid>)
```

More information: [Basic update](webapi/update-delete-entities-using-web-api.md#basic-update)

---


### See also

[Files and images overview](files-images-overview.md)<br />
[Sample: File operations with Attachments and Notes using the Dataverse SDK for .NET](org-service/samples/attachment-annotation-files.md)<br />
[Sample: Attachment and Annotation file operations using Dataverse Web API](webapi/samples/attachment-annotation-file-operations.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
