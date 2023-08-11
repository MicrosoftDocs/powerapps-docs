---
title: "Use file column data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about uploading, downloading, and deleting data in file columns." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/24/2023
ms.reviewer: jdaly
ms.topic: article
author: NHelgren # GitHub ID
ms.subservice: dataverse-developer
ms.author: nhelgren # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - trin-msft
---
# Use file column data

File columns are different from the other system columns that can store binary data because you can't directly set the values in a create or update operation, or retrieve the file data with the record. You must use the methods described in this article to create, retrieve, update, or delete binary data for file columns.

There are several different ways to work with file column data using Web API. All methods are supported equally. Choose the method that works best for you. Because binary files may be large, it's frequently necessary to split the file into multiple chunks (or blocks) that can be sent or received sequentially or in parallel to improve performance.

## File name column

Each file column has a supporting read-only string column that contains the name of the file. The schema name for this column has the same name as the file column, but has `_Name` appended to it. So if the schema name is `sample_FileColumn`, the supporting string column will be `sample_FileColumn_Name`. The logical name for the supporting column will be `sample_filecolumn_name`.

> [!NOTE]
> The file name column does not appear in the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) designer.

## Relationship to FileAttachment table

When a file column is created for a table, a new one-to-many relationship is created between the table and the `FileAttachment` table. The name of the relationship is `{table logical name}_FileAttachments`. For example, if the file column is part of the account table, the relationship name will be `account_FileAttachments`.

You can use this relationship to return more data about the file column and any other file columns for the table. More information: [Retrieve additional information about files for a record](#retrieve-additional-information-about-files-for-a-record).

## Behavior when retrieving

When you retrieve a record and include a file column, the value returned will be a unique identifier for the file. You can use this value to delete the file using the `DeleteFile` message. There's no other use for this ID other than to check whether the column has a value. More information: [Use the DeleteFile message](#use-the-deletefile-message).

The following examples show what you can expect when retrieving data from file columns as you would with other columns.

These examples retrieve the  `name`, `sample_filecolumn`, and `sample_filecolumn_name` columns for an account record:

#### [SDK for .NET](#tab/sdk)

```csharp
static void RetrieveAccountRecordWithFileColumns(
    IOrganizationService service,
    Guid accountid) 
{

   Entity account = service.Retrieve(
         "account", 
         accountid, 
         new ColumnSet("name", "sample_filecolumn", "sample_filecolumn_name"));

   Console.WriteLine($"name: {account["name"]}");
   Console.WriteLine($"sample_filecolumn: {account["sample_filecolumn"]}");
   Console.WriteLine($"sample_filecolumn_name: {account["sample_filecolumn_name"]}");
}
```

**Output**:

```
name: Contoso Ltd.
sample_filecolumn: <file id>
sample_filecolumn_name: 25mb.pdf
```

> [!NOTE]
> You must explicitly request the column to return the file id. If you use [ColumnSet.AllColumns](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true in your query the file column will not be returned. If you used `new ColumnSet(true)` in the function above, the result would be a <xref:System.Collections.Generic.KeyNotFoundException?displayProperty=fullName>.

More information:

- [What is the Organization service](org-service/overview.md)
- [IOrganizationService.Retrieve Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A)

#### [Web API](#tab/webapi)

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(<accountid>)?$select=name,sample_filecolumn,sample_filecolumn_name HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,sample_filecolumn,sample_filecolumn_name)/$entity",
    "@odata.etag": "W/\"75119522\"",
    "name": "Contoso Ltd.",
    "sample_filecolumn": "<file id>",
    "sample_filecolumn_name": "25mb.pdf",
    "accountid": "<accountid>"
}
```

More information: [Retrieve a table row using the Web API](webapi/retrieve-entity-using-web-api.md)

---

### Retrieve additional information about files for a record

You can use the relationship between the file column table and the `FileAttachment` table to return information about all file columns associated to that table row.

#### [SDK for .NET](#tab/sdk)

The `RetrieveAccountRecordWithFileData` static method shows how to return information about all the file columns that contain data related to the `account` record with the matching `accountid` value.

```csharp
static void RetrieveAccountRecordWithFileData(
    IOrganizationService service, 
    Guid accountid)
{
    // Create query for related records
    var relationshipQueryCollection = new RelationshipQueryCollection {
        {
            new Relationship("account_FileAttachments"),
            new QueryExpression("fileattachment"){
                ColumnSet = new ColumnSet(
                                "createdon",
                                "mimetype",
                                "filesizeinbytes",
                                "filename",
                                "regardingfieldname",
                                "fileattachmentid")
            }
        }
    };

    // Include the related query with the Retrieve Request
    RetrieveRequest request = new RetrieveRequest
    {
        ColumnSet = new ColumnSet("accountid"),
        RelatedEntitiesQuery = relationshipQueryCollection,
        Target = new EntityReference("account", accountid)
    };

    // Send the request
    RetrieveResponse response = (RetrieveResponse)service.Execute(request);

    //Display related FileAttachment data for the account record
    response.Entity.RelatedEntities[new Relationship("account_FileAttachments")]
        .Entities.ToList().ForEach(e =>
        {
            Console.WriteLine($"createdon: {e.FormattedValues["createdon"]}");
            Console.WriteLine($"mimetype: {e["mimetype"]}");
            Console.WriteLine($"filesizeinbytes: {e.FormattedValues["filesizeinbytes"]}");
            Console.WriteLine($"filename: {e["filename"]}");
            Console.WriteLine($"regardingfieldname: {e["regardingfieldname"]}");
            Console.WriteLine($"fileattachmentid: {e["fileattachmentid"]}");
        });
}
```

**Output**:

In this case, there's a single file column in the account table named `sample_filecolumn`, and this is the data about the file stored in that column.

```
createdon: 10/22/2022 2:01 PM
mimetype: application/pdf
filesizeinbytes: 25,870,370
filename: 25mb.pdf
regardingfieldname: sample_filecolumn
fileattachmentid: 63a6afb7-4c52-ed11-bba1-000d3a9933c9
```

More information:

- [What is the Organization service](org-service/overview.md)
- [Retrieve with related rows](org-service/entity-operations-retrieve.md#retrieve-with-related-rows)

#### [Web API](#tab/webapi)

The request below will return information about all the file columns that contain data related to the `account` record specified using `accountid`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(<accountid>)?$filter=sample_filecolumn ne null&$expand=account_FileAttachments($select=createdon,mimetype,filesizeinbytes,filename,regardingfieldname)&$select=accountid HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

In this case, there's a single file column in the account table named `sample_filecolumn`, and this is the data about the file stored in that column.

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(accountid,account_FileAttachments(createdon,mimetype,filesizeinbytes,filename,regardingfieldname))/$entity",
  "@odata.etag": "W/\"75119522\"",
  "accountid": "<accountid>",
  "account_FileAttachments": [
    {
      "@odata.etag": "W/\"75119363\"",
      "createdon": "2022-10-22T21:01:45Z",
      "mimetype": "application/pdf",
      "filesizeinbytes": 25870370,
      "filename": "25mb.pdf",
      "regardingfieldname": "sample_filecolumn",
      "fileattachmentid": "<file id>"
    }
  ]
}
```

More information: [Retrieve with related rows](org-service/entity-operations-retrieve.md#retrieve-with-related-rows)

---

## Upload Files

There at three different ways to upload files to a file column:

- Use Dataverse messages available to both the SDK and Web API
- Upload a file in a single request using Web API
- Upload the file in chunks using Web API

> [!NOTE]
> - You should verify whether the column maximum file size is large enough to accept the file you are uploading. More information: [Check maximum file size](#check-maximum-file-size).
> - You can also use these APIs to upload image column data. More information: [Use image column data](image-column-data.md)

### Use Dataverse messages to upload a file

You can use Dataverse messages using the SDK for .NET or Web API. Uploading a file this way requires using a set of three messages:

|Message|Description|
|---------|---------|
|`InitializeFileBlocksUpload`|Use this message to indicate the column that you want to upload a file to. It returns a *file continuation token* that you can use to upload the file in blocks using the `UploadBlock` message and with `CommitFileBlocksUpload`.|
|`UploadBlock`|Split your file into blocks and generate a *blockid* for each block. Then make multiple requests until all the blocks have been sent together with the file continuation token.|
|`CommitFileBlocksUpload`|After you have sent requests for all the blocks using `UploadBlock`, use this message to commit the upload operation by sending:<br />- The list of generated blockids<br />- The name of the file<br />- The [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the file<br />- The file continuation token|

#### [SDK for .NET](#tab/sdk)

You can use a function like the following to upload a file or image using the [InitializeFileBlocksUploadRequest](xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest), [UploadBlockRequest](xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest), and [CommitFileBlocksUploadRequest](xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest) classes.

```csharp
/// <summary>
/// Uploads a file or image column value
/// </summary>
/// <param name="service">The service</param>
/// <param name="entityReference">A reference to the record with the file or image column</param>
/// <param name="fileAttributeName">The name of the file or image column</param>
/// <param name="fileInfo">Information about the file or image to upload.</param>
/// <param name="fileMimeType">The mime type of the file or image, if known.</param>
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

More information:

- [Use the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

[!INCLUDE [cc-trygetcontenttype-note](includes/cc-trygetcontenttype-note.md)]

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to set a PDF file named `25mb.pdf` to the file column named `sample_filecolumn` on the `account` table for a record with the specified `accountid`.

**Request:**

The first request uses the [InitializeFileBlocksUpload Action](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksUpload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeFileBlocksUpload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 207

{
  "Target": {
    "accountid": "<accountid>",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "FileName": "25mb.pdf",
  "FileAttributeName": "sample_filecolumn"
}
```

**Response:**

The response is a [InitializeFileBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksUploadResponse) providing the `FileContinuationToken` value to use with subsequent requests.

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeFileBlocksUploadResponse",
  "FileContinuationToken": "<Removed for brevity>"
}
```

You must then break up the file into blocks of 4 MB or less and send each block using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock) with the following properties:


|Property|Description:  |
|---------|---------|
|`BlockId`|A valid Base64 string value that identifies the block. Prior to encoding, the string must be less than or equal to 64 bytes in size.<br />For a given file, the length of the `BlockId` value must be the same size for each block.|
|`BlockData`|A Base64 encoded string containing the byte[] less than 4 MB in size representing the portion of the file being sent.|
|`FileContinuationToken`|The value of the `InitializeFileBlocksUploadResponse.FileContinuationToken`|

[!INCLUDE [cc-generate-blockid-tip](includes/cc-generate-blockid-tip.md)]

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/UploadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 5593368

{
  "BlockId": "OThjODg5NjgtNzM2Zi00YmI1LTgyNzktNmU2NzgwMTRiMzFk",
  "BlockData": "<Base64 encoded string of byte[] data removed for brevity>",
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

After all the parts of the file have been sent using multiple requests using the [UploadBlock Action](xref:Microsoft.Dynamics.CRM.UploadBlock), use the [CommitFileBlocksUpload Action](xref:Microsoft.Dynamics.CRM.CommitFileBlocksUpload) to complete the upload using these properties:

|Property|Description:  |
|---------|---------|
|`FileName`|The name of the file.|
|`MimeType`|The [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the file.|
|`BlockList`|An array of strings representing the `BlockId` values in the previous `UploadBlock` operations. The order of these strings represents the order the server will use to combine the blocks into the original file.|
|`FileContinuationToken`|The value of the `InitializeFileBlocksUploadResponse.FileContinuationToken`|


**Request:**

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
    "OThjODg5NjgtNzM2Zi00YmI1LTgyNzktNmU2NzgwMTRiMzFk",
    "ZWUxNzcxZjgtNjEwOC00NDk1LWI2NzMtODFkNDM3YjMyNTFm",
    "YWMwYzhjMzEtY2U0My00NjUwLThlZmEtNjg3NDM5ZTA1MGJi",
    "ZGM3NWQ2NjUtNTViMy00ODQ2LWE5NmQtNDE3ZGUyYTIxYjhi",
    "NzE2OWYyZGEtZGQ1Ni00YWMwLWJiNWUtNjIyNDlkYzRiNmEy",
    "ZmU2ZDMzNjQtMzg2My00ZGZlLWIwYjItMDc4NTY2MDE1MzY1",
    "NWY1ZDAyMWUtNTJiNi00YjA5LTg4ZWItYzg3OTdhMDYxMTRl"
  ],
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

**Response:**

The [CommitFileBlocksUploadResponse ComplexType](xref:Microsoft.Dynamics.CRM.CommitFileBlocksUploadResponse) returns the `FileSizeInBytes` and the `FileId` value you can use to delete the file using the [DeleteFile Action](xref:Microsoft.Dynamics.CRM.DeleteFile).

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CommitFileBlocksUploadResponse",
  "FileId": "3878e950-8e51-ed11-bba1-000d3a9933c9",
  "FileSizeInBytes": 25870370
}
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

### Upload a file in a single request using Web API

If the size of the file is less than 128 MB, you can upload the file in a single request using the Web API.

The following example uploads a text file named `4094kb.txt` to the file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/octet-stream
x-ms-file-name: 4094kb.txt
Content-Length: 4191273

< binary content removed for brevity>
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

### Upload the file in chunks using Web API

To upload your file in chunks using the Web API, use the following set of requests.

The following example uploads a PDF file named `25mb.pdf` to the file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

The first request must include this header:`x-ms-transfer-mode: chunked`

Set the file name using the `x-ms-file-name` query parameter.


```http
PATCH [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn?x-ms-file-name=25mb.pdf HTTP/1.1
x-ms-transfer-mode: chunked
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

> [!NOTE]
> The file name can also be included as a `x-ms-file-name` request header, but this will not support file names outside the ASCII character set. If the header is used, it will take precedence over the `x-ms-file-name` query parameter.

**Response:**

```http
HTTP/1.1 200 OK
Accept-Ranges: bytes
Location: [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn?sessiontoken=<sessiontoken value removed for brevity>
OData-Version: 4.0
x-ms-chunk-size: 4194304
Access-Control-Expose-Headers: x-ms-chunk-size
```

The response [Location](https://developer.mozilla.org/docs/Web/HTTP/Headers/Location) header includes a URL to use in subsequent requests. It includes a `sessiontoken` query parameter that indicates that all the requests sent using it are part of the same operation.

The response includes the following headers.

|Header|Description|
|---------|---------|
|`x-ms-chunk-size`|Provides a recommended chunk size in bytes.|
|[Accept-Ranges](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Ranges)|Indicates the server supports partial requests from the client for file downloads. The value `bytes` indicates that the range value in subsequent requests should be in bytes.|
|[Access-Control-Expose-Headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)|Indicates that the `x-ms-chunk-size` header value should be made available to scripts running in the browser, in response to a cross-origin request.|

**Request:**

Subsequent requests should use the value of the `Location` header returned by the first request so that the `sessiontoken` value is included.

Each request must contain that portion of the file in the body and the following headers:

|Header|Description|
|---------|---------|
|`x-ms-file-name`|The name of the file.|
|[Content-Type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type)| Set to `application/octet-stream`|
|[Content-Range](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Range)|Using this format: <br />`<unit> <range-start>-<range-end>/<size>`<br />The value of the first request: `bytes 0-4194303/25870370` indicates that the measurement is using bytes. This request includes the first `4194303` bytes of a file that is `25870370` bytes (almost 25 MB) in size.<br />Each subsequent request will see this value increase until the entire file has been sent:<br />`bytes 4194304-8388607/25870370`<br />`bytes 8388608-12582911/25870370`<br />`bytes 12582912-16777215/25870370`<br />`bytes 16777216-20971519/25870370`<br />`bytes 20971520-25165823/25870370`<br />`bytes 25165824-25870369/25870370`<br />|
|[Content-Length](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Length)|Indicates the size of the message. In the example above, this value for the last request will be `704546` rather than `4194304`.|

```http
PATCH [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn?sessiontoken=<sessiontoken value removed for brevity> HTTP/1.1
x-ms-file-name: 25mb.pdf
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/octet-stream
Content-Range: bytes 0-4194303/25870370
Content-Length: 4194304

< byte[] content removed for brevity>
```

For each request that contains partial content, the response will be [206 PartialContent](https://developer.mozilla.org/docs/Web/HTTP/Status/206).

**Response:**

```http
HTTP/1.1 206 PartialContent
OData-Version: 4.0
```

For the final request that includes the last chunk of the file, the response will be [204 NoContent](https://developer.mozilla.org/docs/Web/HTTP/Status/204).

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

### Check maximum file size

Before you upload a file, you can check whether the size of the file exceeds the configured **Maximum file size** stored in the `MaxSizeInKB` property.

If you try to upload a file that is too large, you'll get the following error:

> Name: `unManagedidsattachmentinvalidfilesize`<br />
> Code: `0x80044a02`<br />
> Number: `-2147202558`<br />
> Message: `Attachment file size is too big.`

You can use the following examples to check the maximum file size:

#### [SDK for .NET](#tab/sdk)

The static `GetFileColumnMaxSizeInKb` method returns the `MaxSizeInKB` value for a file column.

```csharp
/// <summary>
/// Retrieves the MaxSizeInKb property of a file column.
/// </summary>
/// <param name="service">IOrganizationService</param>
/// <param name="entityLogicalName">The logical name of the table that has the column</param>
/// <param name="fileColumnLogicalName">The logical name of the file column.</param>
/// <returns></returns>
/// <exception cref="Exception"></exception>
public static int GetFileColumnMaxSizeInKb(
    IOrganizationService service, 
    string entityLogicalName, 
    string fileColumnLogicalName) 
{

   RetrieveAttributeRequest retrieveAttributeRequest = new() { 
         EntityLogicalName = entityLogicalName,
         LogicalName = fileColumnLogicalName
   };

   RetrieveAttributeResponse retrieveAttributeResponse;
   try
   {
         retrieveAttributeResponse = (RetrieveAttributeResponse)service.Execute(retrieveAttributeRequest);
   }
   catch (Exception)
   {
         throw;
   }

   if (retrieveAttributeResponse.AttributeMetadata is FileAttributeMetadata fileColumn)
   {
         return fileColumn.MaxSizeInKB.Value;
   }
   else
   {
         throw new Exception($"{entityLogicalName}.{fileColumnLogicalName} is not a file column.");
   }
}
```

More information:

- [RetrieveAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest)
- [FileAttributeMetadata.MaxSizeInKB](xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB)

#### [Web API](#tab/webapi)

The following request returns the `MaxSizeInKB` value for a file column with the logical name `sample_filecolumn` in the `account` table.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='sample_filecolumn')/Microsoft.Dynamics.CRM.FileAttributeMetadata?$select=MaxSizeInKB HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.FileAttributeMetadata(MaxSizeInKB)/$entity",
  "MaxSizeInKB": 102400,
  "MetadataId": "f315e7f1-6355-ed11-bba3-000d3a9933c9"
}
```

More information:

- [Query table definitions using the Web API > Retrieving attributes](webapi/query-metadata-web-api.md#retrieving-attributes)
- [FileAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.FileAttributeMetadata)

---

## Download Files

There at three different methods to download files from a file column:

- Use Dataverse messages available to both the SDK and Web API
- Download a file in a single request using Web API
- Download the file in chunks using Web API

> [!NOTE]
> These methods can also be used to download image columns, but there are some differences. More information: [Download images](image-column-data.md#download-images)
> 
> For on-premises environments or when an environment uses Customer Managed Keys, the file is not in file storage. When a file is not in file storage, downloading in multiple chunks is not supported. The [InitializeFileBlocksDownloadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksDownloadResponse) and [InitializeFileBlocksDownloadResponse Class](xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadResponse) have an `IsChunkingSupported`property that indicates if the file can be downloaded in multiple chunks or not. If chunking is not supported, then set `BlockLength` to the file size.
> 
> Trying to download partial chunk when IsChunkingSupported is set to false will result in this error:<br />
> 
> Name: `UploadingAndDownloadingInMultipleChunksNotSupported`<br />
> Code: `0x80090017`<br />
> Message: `Downloading in multiple chunks is not supported for the files stored in the database.`

### Use Dataverse messages to download a file

You can use Dataverse messages using the SDK for .NET or Web API. Downloading a file this way requires using a pair of messages:

|Message|Description|
|---------|---------|
|`InitializeFileBlocksDownload`|Use this message to indicate the column that you want to download a file from. It returns the file size in bytes and a *file continuation token* that you can use to download the file in blocks using the `DownloadBlock` message.|
|`DownloadBlock`|Request the size of the block, the offset value and the file continuation token.|

Once you've downloaded all the blocks, you must join them to create the entire downloaded file.

#### [SDK for .NET](#tab/sdk)

You can use a function like the following to download a file or image using the SDK using the [InitializeFileBlocksDownloadRequest](xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest) and [DownloadBlockRequest](xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest) classes.

```csharp
/// <summary>
/// Downloads a file or image
/// </summary>
/// <param name="service">The service</param>
/// <param name="entityReference">A reference to the record with the file or image column</param>
/// <param name="attributeName">The name of the file or image column</param>
/// <returns></returns>
private static byte[] DownloadFile(
            IOrganizationService service,
            EntityReference entityReference,
            string attributeName)
{
   InitializeFileBlocksDownloadRequest initializeFileBlocksDownloadRequest = new()
   {
         Target = entityReference,
         FileAttributeName = attributeName
   };

   var initializeFileBlocksDownloadResponse =
         (InitializeFileBlocksDownloadResponse)service.Execute(initializeFileBlocksDownloadRequest);

   string fileContinuationToken = initializeFileBlocksDownloadResponse.FileContinuationToken;
   long fileSizeInBytes = initializeFileBlocksDownloadResponse.FileSizeInBytes;

   List<byte> fileBytes = new((int)fileSizeInBytes);

   long offset = 0;
   // If chunking is not supported, chunk size will be full size of the file.
   long blockSizeDownload = !initializeFileBlocksDownloadResponse.IsChunkingSupported ? fileSizeInBytes :  4 * 1024 * 1024;

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

   return fileBytes.ToArray();
}
```

More information:

- [What is the Organization service](org-service/overview.md)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

#### [Web API](#tab/webapi)

The following series of requests and responses show the interaction when using the Web API to download a PDF file named `25mb.pdf` from the file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

This request uses the [InitializeFileBlocksDownload Action](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksDownload).

```http
POST [Organization Uri]/api/data/v9.2/InitializeFileBlocksDownload HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 180

{
  "Target": {
    "accountid": "<accountid>",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "FileAttributeName": "sample_filecolumn"
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InitializeFileBlocksDownloadResponse",
  "FileSizeInBytes": 25870370,
  "FileName": "25mb.pdf",
  "FileContinuationToken": "<file continuation token value removed for brevity>",
  "IsChunkingSupported": true
}
```

The response is a [InitializeFileBlocksDownloadResponse ComplexType](xref:Microsoft.Dynamics.CRM.InitializeFileBlocksDownloadResponse) which provides:

- `FileSizeInBytes`: The size of the file
- `FileName`: The name of the file
- `FileContinuationToken`: The file continuation token to use in subsequent requests
- `IsChunkingSupported`: Flag to indicate if downloading in chunks is supported or not

Based on the size of the file and the size of the block you'll download, send more requests using the [DownloadBlock Action](xref:Microsoft.Dynamics.CRM.DownloadBlock) as shown below.

> [!NOTE]
> The example below is for cases when `IsChunkingSupported` is set to true. If it is false, set `BlockLength` to full file size.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/DownloadBlock HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 921

{
  "Offset": 0,
  "BlockLength": 4194304,
  "FileContinuationToken": "<file continuation token value removed for brevity>"
}
```

[!INCLUDE [cc-offset-blocklength-example](includes/cc-offset-blocklength-example.md)]

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DownloadBlockResponse",
  "Data": "<byte[] data removed for brevity>"
}
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---


### Download a file in a single request using Web API

The following example downloads a text file named `4094kb.txt` from the file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn/$value HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

The response includes the following headers.

|Header|Description|
|---------|---------|
|`x-ms-file-size`|The size of the file in bytes.|
|`x-ms-file-name`|The name of the file.|
|`mimetype`|The [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the file.|
|[Access-Control-Expose-Headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)|Indicates that the `x-ms-file-size`, `x-ms-file-name`, and `mimetype` header values should be made available to scripts running in the browser, in response to a cross-origin request.|

```http
HTTP/1.1 200 OK
x-ms-file-size: 4191273
x-ms-file-name: 4094kb.txt
mimetype: text/plain
Access-Control-Expose-Headers: x-ms-file-size; x-ms-file-name; mimetype

< byte[] content removed for brevity. >
```

### Download the file in chunks using Web API

> [!NOTE]
> The example below is for cases when `IsChunkingSupported` is set to true. If it is false, please use [Download a file in a single request using Web API](#download-a-file-in-a-single-request-using-web-api).

To download your file in chunks using the Web API, use the following set of requests.

The following example downloads a PDF file named `25mb.pdf` to the file column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

Use the [Range](https://developer.mozilla.org/docs/Web/HTTP/Headers/Range) header to specify the number of bytes to return using this format:<br />
`<unit>=<range-start>-<range-end>`<br />
Where the `unit` is bytes and the `range-start` for the first request is `0`.

You won't know how many iterations are required to download the entire file until you get the first response where the `x-ms-file-size` response header tells you the size of the file.

While the `<range-start>` is smaller than total size of the file, for each subsequent request increment the `<range-start>` and `<range-end>` values to request the next chunk of the file.

```http
GET [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn/$value HTTP/1.1
Range: bytes=0-4194303
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

The response includes the following headers:

|Header|Description|
|---------|---------|
|`x-ms-file-size`|The size of the file in bytes.|
|`x-ms-file-name`|The name of the file.|
|`x-ms-chunk-size`|Provides a recommended chunk size in bytes.|
|`mimetype`|The [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the file.|
|[Access-Control-Expose-Headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)|Indicates that the `x-ms-file-size`, `x-ms-file-name`, `x-ms-chunk-size`, and `mimetype` header values should be made available to scripts running in the browser, in response to a cross-origin request.|


```http
HTTP/1.1 206 PartialContent
x-ms-file-size: 25870370
x-ms-file-name: 25mb.pdf
x-ms-chunk-size: 4194304
mimetype: application/pdf
Access-Control-Expose-Headers: x-ms-file-size; x-ms-file-name; x-ms-chunk-size; mimetype
OData-Version: 4.0

< byte[] content removed for brevity. >
```

## Delete Files

There at two different ways to delete files to a file column:

- Use the Dataverse `DeleteFile` message available to both the SDK and Web API
- Send a DELETE request using Web API to the file column of the record.

### Use the DeleteFile message

Using the unique identifier returned from the `CommitFileBlocksUploadResponse.FileId` or retrieved from the column as described in [Behavior when retrieving](#behavior-when-retrieving), you can delete the file using the `DeleteFile` message.

#### [SDK for .NET](#tab/sdk)

You can use a function like the following to delete a file using the unique identifier using the [DeleteFileRequest Class](xref:Microsoft.Crm.Sdk.Messages.DeleteFileRequest).

```csharp
static Guid DeleteFile(IOrganizationService service, Guid fileId)
{
   DeleteFileRequest deleteFileRequest = new()
   {
      FileId = fileId
   };
   service.Execute(deleteFileRequest);
}
```

#### [Web API](#tab/webapi)

Use the following request to delete a file with the ID using the Web API [DeleteFile Action](xref:Microsoft.Dynamics.CRM.DeleteFile).

```http
POST [Organization Uri]/api/data/v9.2/DeleteFile HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 56

{
  "FileId": "3878e950-8e51-ed11-bba1-000d3a9933c9"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

### Send DELETE request to the file column

With the Web API, you can delete a file by sending a `DELETE` request to the location of the file resource. 

The following example deletes file data for a column named `sample_filecolumn` on the `account` table for a record with `accountid` equal to `<accountid>`.

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_filecolumn HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

More information: [Delete a single property value](webapi/update-delete-entities-using-web-api.md#delete-a-single-property-value)


### See Also

[Files and images overview](files-images-overview.md)<br />
[Column data types > File columns](../../maker/data-platform/types-of-fields.md#file-columns)<br />
[File columns](file-attributes.md)<br />
[Sample: File Operations using Dataverse SDK for .NET](org-service/samples/file-operations.md)<br />
[Sample: File Operations using Dataverse Web API](webapi/samples/file-operations.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
