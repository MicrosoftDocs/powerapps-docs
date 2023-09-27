---
title: "Use image column data (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about uploading, downloading, and deleting data in image columns." 
ms.date: 02/04/2023
ms.reviewer: jdaly
ms.topic: article
author: NHelgren # GitHub ID
ms.subservice: dataverse-developer
ms.author: nhelgren # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Use image column data

You can store image data in Dataverse using image columns or file columns. You can use many of the APIs for file columns with image columns.
Image columns have some special behaviors and limitations to support displaying images within applications.

The following table introduces some of the differences between image and file columns.


||Image  |File  |
|---------|---------|---------|
|**File Size**|Limited to 30 MB.|Up to 10 GB. While the API can handle files up to 10 GB in size, Power Apps client controls currently only support files up to 128 MB. Exceeding the 128 MB value when using these controls will result in errors uploading or downloading files.|
|**File Types**|Only [Image file types](#image-file-types)|All file types allowed by the [Organization.BlockedAttachments value](reference/entities/organization.md#BKMK_BlockedAttachments). More information: [Block certain types of files](files-images-overview.md#block-certain-types-of-files) |
|**Set with Update**|You can set image column data with other record data using update.|You can only upload files individually to file column properties.|
|**Delete with Update**|You can delete image column data by setting the attribute or property to `null` and then update the record. More information: [Delete images](#delete-images)|You can only delete file column data using the `DeleteFile` message or sending a `DELETE` request to the specific column using Web API. More information: [Delete Files](file-column-data.md#delete-files)|
|**Set with Create**|When the image column is the *primary image*, you can set image data with other record data using create. More information: [Primary Images](#primary-images)|You can only upload files individually to file column properties after the record was created.|
|**Return with Retrieve**|You can retrieve thumb-nail sized images with other record data using retrieve.|The value returned is the file ID. More information: [Behavior when retrieving](file-column-data.md#behavior-when-retrieving)|
|**Download URL**|Each image column has a string column that contains a relative URL you can include in an application that allows downloading the image file. More information: [Download URL](#download-url)|There's no string column with a download URL, but you can compose a URL to download the file directly from the Web API. More information: [Download a file in a single request using Web API](file-column-data.md#download-a-file-in-a-single-request-using-web-api)|

## Maximum image size

Just like file columns, you can specify the maximum size of data stored in an image column using the `MaxSizeInKb` property. However the maximum allowed size is 30 MB.

If you try to upload a file that is too large, you'll get the following error:

> Name: `ProcessImageFailure`<br />
> Code: `0x80072553`<br />
> Number: `-2147015341`<br />
> Message: `Error occured when processing image. Reason: File size is too big. MaxSize: 0 MB, Uploaded filesize: 0 MB.`

You can use the following examples to check the maximum file size:

#### [SDK for .NET](#tab/sdk)

The following static `GetImageColumnMaxSizeInKb` method returns the `MaxSizeInKB` value for an [ImageAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata) column.

```csharp
/// <summary>
/// Retrieves the MaxSizeInKb property of an image column.
/// </summary>
/// <param name="service">IOrganizationService</param>
/// <param name="entityLogicalName">The logical name of the table that has the column</param>
/// <param name="imageColumnLogicalName">The logical name of the image column.</param>
/// <returns></returns>
/// <exception cref="Exception"></exception>
public static int GetImageColumnMaxSizeInKb(
   IOrganizationService service, 
   string entityLogicalName, 
   string imageColumnLogicalName) 
{

   RetrieveAttributeRequest retrieveAttributeRequest = new() { 
         EntityLogicalName = entityLogicalName,
         LogicalName = imageColumnLogicalName
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

   if (retrieveAttributeResponse.AttributeMetadata is ImageAttributeMetadata imageColumn)
   {
         return imageColumn.MaxSizeInKB.Value;
   }
   else
   {
         throw new Exception($"{entityLogicalName}.{imageColumnLogicalName} is not a image column.");
   }
}
```

More information:

- [RetrieveAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest)
- [ImageAttributeMetadata.MaxSizeInKB](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.MaxSizeInKB)

#### [Web API](#tab/webapi)

The following request returns the `MaxSizeInKB` value for an [ImageAttributeMetadata](xref:Microsoft.Dynamics.CRM.ImageAttributeMetadata) column with the logical name `sample_imagecolumn` in the `account` table.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='sample_imagecolumn')/Microsoft.Dynamics.CRM.ImageAttributeMetadata?$select=MaxSizeInKB HTTP/1.1
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
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.ImageAttributeMetadata(MaxSizeInKB)/$entity",
  "MaxSizeInKB": 102400,
  "MetadataId": "f315e7f1-6355-ed11-bba3-000d3a9933c9"
}
```

More information:

- [Query table definitions using the Web API > Retrieving attributes](webapi/query-metadata-web-api.md#retrieving-attributes)
- [ImageAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.ImageAttributeMetadata)

---

## Image file types

Image columns store the following binary image types:

|File Format|MIME type|File extension(s)|
|---------|---------|---------|
|Graphics Interchange Format|`image/gif`|`.gif`|
|Joint Photographic Expert Group image|`image/jpeg`|`.jpg`, `.jpeg`|
|Tagged Image File Format|`image/tiff`|`.tif`, `.tiff`|
|Bitmap file|`image/bmp`|`.bmp`|
|Portable Network Graphics|`image/png`|`.png`|

If you try to save a file that isn't one of these types, you'll get the following error:

> Name: `ProcessImageFailure`<br />
> Code: `0x80072553`<br />
> Number: `-2147015341`<br />
> Message: `Error occured when processing image. Reason: Update image properties failed for objectid: <id of record>, logicalName: <logical name of table>, attribute: <logical name of image column`

## Full-size and thumbnail-sized images

When an image column value is set, Dataverse will automatically generate a thumbnail-sized image that is suitable for use as an icon in an application.

If the image column is configured to store a full-sized image, a file up to the configured `MaxSizeInKb` can be saved and downloaded separately from the thumbnail-sized image. The [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) controls whether an image column will store a full-sized image.

### Detect which image columns support full-sized images

You can query the [Image Attribute Configuration (AttributeImageConfig)  table](reference/entities/attributeimageconfig.md) to retrieve a list of image columns that support full-sized images using the `parententitylogicalname`, `attributelogicalname`, and `canstorefullimage` column values.

# [SDK for .NET](#tab/sdk)

The static `PrintFullSizedImageColumns` method will write the names of the table and image columns that can store full-sized images.

```csharp
static void PrintFullSizedImageColumns(IOrganizationService service)
{
    QueryExpression query = new QueryExpression("attributeimageconfig")
    {
        ColumnSet = new ColumnSet("parententitylogicalname", "attributelogicalname"),
        Criteria = new FilterExpression(LogicalOperator.And)
        {
            Conditions =
            {
                new ConditionExpression(
                    attributeName: "canstorefullimage",
                    conditionOperator: ConditionOperator.Equal,
                    value: true)
            }
        }
    };

    EntityCollection response = service.RetrieveMultiple(query);
    foreach (Entity record in response.Entities)
    {
        Console.WriteLine($"{record["parententitylogicalname"]}.{record["attributelogicalname"]}");
    }
}
```

**Output**

```
account.sample_sampleimage
```

# [Web API](#tab/webapi)

This request will return the names of the table and image columns that can store full-sized images.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/attributeimageconfigs?$select=parententitylogicalname,attributelogicalname&$filter=canstorefullimage eq true HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Cache-Control: no-cache
Allow: OPTIONS,GET,HEAD,POST
Content-Type: application/json; odata.metadata=minimal; odata.streaming=true
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#attributeimageconfigs(parententitylogicalname,attributelogicalname)",
  "value": [
    {
      "@odata.etag": "W/\"76501240\"",
      "parententitylogicalname": "account",
      "attributelogicalname": "sample_sampleimage",
      "attributeimageconfigid": "b8c1750f-c24f-ea11-a813-000d3a5391c8"
    }
  ]
}
```

---

You can also query schema definitions to return columns where [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) is true. More information: [Query schema definitions](query-schema-definitions.md)

### Resize rules for thumbnail-sized images

To generate a thumbnail-sized image, Dataverse will crop and resize the image to a square shape according to the following rules:
  
- Images with at least one side larger than 144 pixels are cropped on center to 144x144.  
- Images with both sides smaller than 144 are cropped square to their smallest side.  
  
The following table shows two examples.  
  
|Before|After|  
|------------|-----------|  
|:::image type="content" source="media/crm-itpro-cust-imagebeforeresize.png" alt-text="Image before resize":::<br /><br /> 300x428|:::image type="content" source="media/crm-itpro-cust-imageafterresize.jpg" alt-text="image after resize":::<br /><br /> 144x144|  
|:::image type="content" source="media/crm-itpro-cust-imagebeforeresizeexample2.png" alt-text="smaller image resize before":::<br /><br /> 91x130|:::image type="content" source="media/crm-itpro-cust-imageafterresizeexample2.jpg" alt-text="smaller image resize after":::<br /><br /> 91x91|

## Primary Images

Each table can have multiple image columns, but only one image column can be defined as the *primary image*. Only the primary image can be set with a create operation. More information: [Only primary images can be set for create](#only-primary-images-can-be-set-for-create)

The [ImageAttributeMetadata.IsPrimaryImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.IsPrimaryImage) controls which image column represents the primary image for the table.

The [EntityMetadata.PrimaryImageAttribute property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.PrimaryImageAttribute) returns the logical name of the image column that is the current primary image for the table.

You can also query the [Entity Image Configuration (EntityImageConfig)  table](reference/entities/entityimageconfig.md) to determine which image columns represent the current primary image using the `parententitylogicalname` and `primaryimageattribute` column values.

# [SDK for .NET](#tab/sdk)

The static `PrintPrimaryImageColumns` method below will write the table and image column names of all primary image columns.

```csharp
static void PrintPrimaryImageColumns(IOrganizationService service)
{
    QueryExpression query = new QueryExpression("entityimageconfig")
    {
        ColumnSet = new ColumnSet("parententitylogicalname", "primaryimageattribute"),
    };

    EntityCollection response = service.RetrieveMultiple(query);
    foreach (Entity record in response.Entities)
    {
        Console.WriteLine($"{record["parententitylogicalname"]}.{record["primaryimageattribute"]}");
    }
}
```

**Output**

```
account.sample_sampleimage
```

More information: [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)

# [Web API](#tab/webapi)

The request below will return the table and image column names of all primary image columns.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/entityimageconfigs?$select=parententitylogicalname,primaryimageattribute HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Cache-Control: no-cache
Allow: OPTIONS,GET,HEAD,POST
Content-Type: application/json; odata.metadata=minimal; odata.streaming=true
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#entityimageconfigs(parententitylogicalname,primaryimageattribute)",
  "value": [
    {
      "@odata.etag": "W/\"76501240\"",
      "parententitylogicalname": "account",
      "primaryimageattribute": "sample_sampleimage",
      "entityimageconfigid": "b8c1750f-c24f-ea11-a813-000d3a5391c8"
    }
  ]
}
```

More information: [Query data using the Web API](webapi/query-data-web-api.md)

---

## Download URL

Each image column has the following companion columns, but none of them appear within the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) designer.

|Column |Type|Naming convention |Description |
|---------|---------|---------|---------|
|Image ID|Unique identifier|`<image column name>Id`|A unique identifier for the image.|
|Time Stamp|BigInt|`<image column name>_Timestamp`|Represents when the image was last updated. This value helps make sure the latest version of the image is downloaded rather than the client using a cached version that was retrieved before.|
|URL|string|`<image column name>_URL`|A relative URL to download a thumbnail-sized version of the image|

The image ID and time stamp column values don't have any use cases except that they're used to within the URL string column value.

When the column for a record contains data, the download URL will be a relative URL using the following format:

`/Image/download.aspx?Entity=<entity logical name>&Attribute=<image column logical name>&Id=<image id value>&Timestamp=<time stamp value>`

You can append this value to the organization URI to construct a URL that can be used to download the thumbnail-sized image file. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885`

### URL to download full-sized image

If the image column is configured to store full-sized images, you can append `&Full=true` to the URL and the link will download the full-sized image. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885&Full=true`

If the column isn't configured to store full-sized images, no data will be returned.

## Use image data with records

When you're working with records, how you work with image data depends on whether you're using the SDK or Web API.

# [SDK for .NET](#tab/sdk)

The following static `RetrieveAndUpdateImageColumn` method retrieves a `byte[]` image value from a column, saves it locally and uploads a new image.

```csharp
static void RetrieveAndUpdateImageColumn(
    IOrganizationService service,
    Guid accountid,
    string imageColumnLogicalName) 
{

    // Retrieve account with image
    Entity account = service.Retrieve(
        entityName: "account",
        id: accountid, 
        columnSet: new ColumnSet(imageColumnLogicalName));

    // Save the image retrieved
    File.WriteAllBytes(
        path: "original_image.png",
        bytes: account.GetAttributeValue<byte[]>(imageColumnLogicalName));


    // Instantiate a new entity for update with new image
    Entity accountForUpdate = new("account") { 
        Attributes = {
            { "accountid", accountid },
            { imageColumnLogicalName , File.ReadAllBytes("new_image.png")}
        }
    };

    // Update the account
    service.Update(accountForUpdate);               
}
```

> [!NOTE]
> Image columns are not included if you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true. For performance reasons you must explicitly specify that you want to retrieve image data.

More information:

- [Retrieve a table row using the SDK for .NET](org-service/entity-operations-retrieve.md)
- [Update and delete table rows using the SDK for .NET](org-service/entity-operations-update-delete.md)


# [Web API](#tab/webapi)

With Web API, the property values are base 64 encoded string values representing the `byte[]` data.

This request returns an image column named `sample_imagecolumn` with an account record:

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(<accountid>)?$select=sample_imagecolumn HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"76796548"
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(sample_imagecolumn)/$entity",
  "@odata.etag": "W/\"76796548\"",
  "sample_imagecolumn": "<base 64 encoded string truncated for brevity>",
  "accountid": "<accountid>"
}
```

This request updates the `sample_imagecolumn` image column with an updated image:

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/accounts(<accountid>) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 5220

{
  "sample_imagecolumn": "<base 64 encoded string truncated for brevity>"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(<accountid>)
```

Some libraries you may use to serialize and deserialize JSON, such as [JSON.NET](https://www.newtonsoft.com/json), will automatically convert these encoded string values to `byte[]` so you might not even notice that the transport protocol is using base 64 strings.

For more information, about base 64 encoded strings see:
 - [Base64 - MDN Web Docs Glossary](https://developer.mozilla.org/docs/Glossary/Base64)
 - [Base64 to Image Converter](https://codebeautify.org/base64-to-image-converter)
 - [Image to Base64 Converter](https://codebeautify.org/image-to-base64-converter)

More information:
- [Retrieve a table row using the Web API](webapi/retrieve-entity-using-web-api.md)
- [Update and delete table rows using the Web API](webapi/update-delete-entities-using-web-api.md)

---

### Only primary images can be set for create

When you create a record, you can only set the value of the current primary image column. If you try to set the value of any other image column, you'll get this error:

> Name: `CannotUploadNonPrimaryImageAttributeOnCreate`<br />
> Code: `0x80090487`<br />
> Number: `-2146892665`<br />
> Message: `Non-primary image attribute <image column logical name> of entity <table logical name> is not allowed to upload during Create operation.`

More information: [Primary Images](#primary-images)

### Only thumbnail images can be retrieved

The image data you access via record properties will always be the thumbnail-sized images. To access full-sized images, you must download them. More information: [Download images](#download-images)


## Upload images

Use the same APIs you use to upload files to upload images individually. More information: [Upload Files](file-column-data.md#upload-files)

## Download images

Use the same APIs you use to download files to download images, but be aware of the following differences.

### Using Dataverse messages

If you use the `InitializeFileBlocksDownload` and `DownloadBlock` messages, the full-sized image will always be downloaded if the image column supports them. You can't download the thumbnail-sized image using this method. More information: [Use Dataverse messages to download a file](file-column-data.md#use-dataverse-messages-to-download-a-file)

If the image column doesn't support full-sized images, or if the [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) was false when the image was uploaded, the following error is returned:

> Name: `ObjectDoesNotExist`<br />
> Code: `0x80040217`<br />
> Number: `-2147220969`<br />
> Message: `No FileAttachment records found for imagedescriptorId: <guid> for image attribute: <image column logical name> of <entity logical name> record with id <guid>.`

### Using Web API

When you download images using the Web API without using the Dataverse messages, the thumbnail-sized image will be downloaded by default. To download the full-sized image, you must append this parameter to the URL: `?size=full`.

If the image column doesn't support full-sized images, or if the [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) was false when the image was uploaded, the response will return `204 No Content`.

More information: [Download Files](file-column-data.md#download-files)

## Delete images

You can delete images by setting the image column value for the record to null as you would for any other property.

# [SDK for .NET](#tab/sdk)

Simply set the value of the image attribute to null and update the entity. More information: [Basic update](org-service/entity-operations-update-delete.md#basic-update)

# [Web API](#tab/webapi)

There are three different ways to delete an image column value using Web API.

### Use PATCH and set the image column value to null

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/accounts(<accountid>) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 90

{
  "accountid": "<accountid>",
  "sample_imagecolumn": null
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(<accountid>)
```

More information: [Basic update](webapi/update-delete-entities-using-web-api.md#basic-update)

### Use PUT and set the image column value to null

**Request:**

```http
PUT [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_imagecolumn HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 15

{"value": null}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

More information: [Update a single property value](webapi/update-delete-entities-using-web-api.md#update-a-single-property-value)


### Use DELETE with the resource URL referencing the image column

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/accounts(<accountid>)/sample_imagecolumn HTTP/1.1
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

---

### See also

[Files and images overview](files-images-overview.md)<br />
[Image columns](image-attributes.md)<br />
[Sample: Image Operations using Dataverse SDK for .NET](org-service/samples/set-retrieve-entity-images.md)<br />
[Sample: Image Operations using Dataverse Web API](webapi/samples/image-operations.md)<br />
[Use file column data](file-column-data.md)
