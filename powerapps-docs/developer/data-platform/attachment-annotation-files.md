---
title: "Use file data with Attachment and Note records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using file data with Attachment and Note records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/02/2023
ms.reviewer: jdaly
ms.topic: article
author: DanaMartens # GitHub ID
ms.subservice: dataverse-developer
ms.author: dmartens # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Use file data with Attachment and Note records

[Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) and [Note (Annotation)](reference/entities/annotation.md) tables contain special string columns that store file data.

- An attachment is a file that is associated with an [email](reference/entities/email.md) activity, either directly or though an [Email Template (Template)](reference/entities/template.md). Multiple attachments can be associated with the activity or template.
- A note is a record associated with a table row that contains text and may have a single file attached. Only those tables which have [EntityMetadata.HasNotes](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.HasNotes) may have notes associated with them.

These tables existed before file or image columns, so they work differently.

- The binary file data is stored as Base64 encoded string values in string columns: [ActivityMimeAttachment.Body](reference/entities/activitymimeattachment.md#BKMK_Body) and [Annotation.DocumentBody](reference/entities/annotation.md#BKMK_DocumentBody) .
- File name data is stored in the `FileName` column.
- Mime type data is stored in the `MimeType` column.

Because these columns are part of the data for the record, you should update these three columns together with any other values for the attachment or note.

## Using file data

You can directly get and set the values of the `activitymimeattachment.body` and `annotation.documentbody` columns as Base64 encoded strings. This should be fine as long as the files are not too large, for example under 4 MB.

However, when you have increased the maximum file size and are working with larger files, you should use messages provided to break the files into smaller chunks when uploading or downloading files. More information: [File size limits](#file-size-limits)

## Upload Attachment files

Use the `InitializeAttachmentBlocksUpload`, `UploadBlock`, and `CommitAttachmentBlocksUpload` messages to upload files for attachments.

> [!NOTE]
> These messages can only be used to create a new attachment. It you try to update an existing attachment with these messages you will get an error that the record already exists.

# [SDK for .NET](#tab/sdk)

You can use a static method like the following `UploadAttachment` to create a new attachment with a file using the <xref:Microsoft.Crm.Sdk.Messages.InitializeAttachmentBlocksUploadRequest>, <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>, and <xref:Microsoft.Crm.Sdk.Messages.CommitAttachmentBlocksUploadRequest> classes and it will return a <xref:Microsoft.Dynamics.CRM.CommitAttachmentBlocksUploadResponse>

This method uses the <xref:Microsoft.AspNetCore.StaticFiles.IContentTypeProvider.TryGetContentType%2A?displayProperty=nameWithType> to attempt to set the `activitymimeattachment.mimetype` column if it isn't already set. This is optional. By default the value will be set to `application/octet-stream`.

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

# [Web API](#tab/webapi)

**Request**

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
    "objectid_email@odata.bind": "emails(b1b7e09f-58a3-ed11-aad1-000d3a9933c9)",
    "objecttypecode": "email",
    "subject": "Sample attached 25mb.pdf",
    "filename": "25mb.pdf",
    "mimetype": "application/pdf",
    "@odata.type": "Microsoft.Dynamics.CRM.activitymimeattachment"
  }
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeAttachmentBlocksUploadResponse",
  "FileContinuationToken": "<Removed for brevity>"
}
```

Use the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock) to upload each of the file chunks.

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

---

## Upload Annotation files

Use the `InitializeAnnotationBlocksUpload`, `UploadBlock`, and `CommitAnnotationBlocksUpload` messages to upload files for notes.

> [!NOTE]
> The annotation you pass as the `Target` parameter for these messages must have an `annotationid` value. Typically, you should allow the system to specify the value of a unique identifier for a record. If you follow this pattern, you can only use this message to update existing annotations. To work around this, you can create a `Guid` value to set as the `annotationid` value when you want to create a new note.
<!-- Need to test this -->

## Download Attachment files
## Download Annotation files

## File size limits

The [Organization.MaxUploadFileSize](reference/entities/organization.md#BKMK_MaxUploadFileSize) column specifies the maximum allowed size of an a file (in bytes) for an attachment and note, as well as other kinds of data, such as web resource files used for model-driven apps.

The default size is 5 MB (5242880 bytes) and the maximum value is 125 MB (131072000 bytes) and can be set in the email settings for the environment. More information: [Manage email settings](/power-platform/admin/settings-email)

If you try to upload a file that is too large, you'll get the following error:

> Name: `unManagedidsattachmentinvalidfilesize`<br />
> Code: `0x80044a02`<br />
> Number: `-2147202558`<br />
> Message: `Attachment file size is too big.`

> [!NOTE]
> The maximum upload file size limit applies to the size of the file in Base64 encoding. A Base64 encoding produces a string that is larger than the original `byte[]` file data..

### Retrieve max upload file size

Use the following to retrieve the maximum upload file size.

# [SDK for .NET](#tab/sdk)

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

# [Web API](#tab/webapi)

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

---

### Update max upload file size

Use the following to set the maximum upload file size.

# [SDK for .NET](#tab/sdk)

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

# [Web API](#tab/webapi)

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
OData-EntityId: [Organization Uri]/api/data/v9.2/organizations(883278f5-07af-45eb-a0bc-3fea67caa544)
```

---


## Template
# [SDK for .NET](#tab/sdk)

Content for SDK...

# [Web API](#tab/webapi)

Content for Web API...

---
