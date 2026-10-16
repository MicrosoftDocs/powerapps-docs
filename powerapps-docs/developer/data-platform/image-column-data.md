---
title: "Use image column data in Microsoft Dataverse"
description: "Learn how to upload, download, and delete image data in Microsoft Dataverse image columns with code examples and API guidance." 
ms.date: 10/14/2026
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.subservice: dataverse-developer
ai-usage: ai-assisted
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Use image column data in Microsoft Dataverse

You can store image data in Microsoft Dataverse using image columns or file columns. Image columns in Dataverse have special behaviors and limitations designed to support displaying images within applications, and you can use many of the same APIs for file columns with image columns.

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

Just like file columns, you can specify the maximum size of data stored in an image column by using the `MaxSizeInKb` property. However, the maximum allowed size is 30 MB.

If you try to upload a file that's too large, you get the following error message:

> Name: `ProcessImageFailure`<br />
> Code: `0x80072553`<br />
> Number: `-2147015341`<br />
> Message: `Error occured when processing image. Reason: File size is too big. MaxSize: 0 MB, Uploaded filesize: 0 MB.`

To check the maximum file size, use the following examples:

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

- [Query table definitions using the Web API > Retrieve attributes](webapi/query-metadata-web-api.md#retrieve-attributes)
- [ImageAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.ImageAttributeMetadata)

---

## Image file types

Image columns store the following binary image types:

|File Format|MIME type|File extensions|
|---------|---------|---------|
|Graphics Interchange Format|`image/gif`|`.gif`|
|Joint Photographic Expert Group image|`image/jpeg`|`.jpg`, `.jpeg`|
|Bitmap file|`image/bmp`|`.bmp`|
|Portable Network Graphics|`image/png`|`.png`|

If you try to save a file that isn't one of these types, you get the following error message:

> Name: `ProcessImageFailure`<br />
> Code: `0x80072553`<br />
> Number: `-2147015341`<br />
> Message: `Error occured when processing image. Reason: Update image properties failed for objectid: <id of record>, logicalName: <logical name of table>, attribute: <logical name of image column`

## Full-size and thumbnail-sized images

When you set an image column value, Dataverse automatically generates a thumbnail-sized image that's suitable for use as an icon in an application.

If you configure the image column to store a full-sized image, you can save and download a file up to the configured `MaxSizeInKb` separately from the thumbnail-sized image. The [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) controls whether an image column stores a full-sized image.

### Detect which image columns support full-sized images

Use the `RetrieveMetadataChanges` message to query schema definitions and retrieve all image columns. Then inspect the [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) to identify the columns that support full-sized images. For more information, see [Query schema definitions](query-schema-definitions.md).

> [!NOTE]
> The `RetrieveMetadataChanges` message doesn't support filtering on the `ImageAttributeMetadata.CanStoreFullImage` property. Filter on `AttributeMetadata.AttributeTypeName` to return all image columns, and then test the `CanStoreFullImage` property in the results.

# [SDK for .NET](#tab/sdk)

The static `PrintFullSizedImageColumns` method uses the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> class to write the logical names of tables and image columns that can store full-sized images.

```csharp
static void PrintFullSizedImageColumns(IOrganizationService service)
{
    EntityQueryExpression query = new()
    {
        Properties = new MetadataPropertiesExpression("LogicalName", "Attributes"),
        AttributeQuery = new AttributeQueryExpression
        {
            Properties = new MetadataPropertiesExpression(
                "LogicalName",
                "CanStoreFullImage"),
            Criteria = new MetadataFilterExpression(LogicalOperator.And)
            {
                Conditions =
                {
                    new MetadataConditionExpression(
                        propertyName: "AttributeTypeName",
                        conditionOperator: MetadataConditionOperator.Equals,
                        value: AttributeTypeDisplayName.ImageType)
                }
            }
        }
    };

    RetrieveMetadataChangesRequest request = new()
    {
        Query = query
    };

    RetrieveMetadataChangesResponse response =
        (RetrieveMetadataChangesResponse)service.Execute(request);

    foreach (EntityMetadata table in response.EntityMetadata)
    {
        foreach (ImageAttributeMetadata imageColumn in table.Attributes)
        {
            if (imageColumn.CanStoreFullImage == true)
            {
                Console.WriteLine($"{table.LogicalName}.{imageColumn.LogicalName}");
            }
        }
    }
}
```

**Output**

```
account.sample_sampleimage
```

# [Web API](#tab/webapi)

The [RetrieveMetadataChanges function](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) accepts an encoded JSON `Query` parameter. The following JSON defines a query that returns the logical names of tables and all image columns. The query also returns the `CanStoreFullImage` property for each image column.

```json
{
  "Properties": {
    "AllProperties": false,
    "PropertyNames": ["LogicalName", "Attributes"]
  },
  "AttributeQuery": {
    "Properties": {
      "AllProperties": false,
      "PropertyNames": ["LogicalName", "CanStoreFullImage"]
    },
    "Criteria": {
      "FilterOperator": "And",
      "Conditions": [
        {
          "ConditionOperator": "Equals",
          "PropertyName": "AttributeTypeName",
          "Value": {
            "Type": "Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName",
            "Value": "ImageType"
          }
        }
      ]
    }
  }
}
```

**Request:**

```http
GET [Organization URI]/api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1=%7B%22Properties%22%3A%7B%22AllProperties%22%3Afalse%2C%22PropertyNames%22%3A%5B%22LogicalName%22%2C%22Attributes%22%5D%7D%2C%22AttributeQuery%22%3A%7B%22Properties%22%3A%7B%22AllProperties%22%3Afalse%2C%22PropertyNames%22%3A%5B%22LogicalName%22%2C%22CanStoreFullImage%22%5D%7D%2C%22Criteria%22%3A%7B%22FilterOperator%22%3A%22And%22%2C%22Conditions%22%3A%5B%7B%22ConditionOperator%22%3A%22Equals%22%2C%22PropertyName%22%3A%22AttributeTypeName%22%2C%22Value%22%3A%7B%22Type%22%3A%22Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName%22%2C%22Value%22%3A%22ImageType%22%7D%7D%5D%7D%7D%7D HTTP/1.1
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
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse",
  "ServerVersionStamp": "123456789",
  "DeletedMetadata": {
    "Count": 0,
    "IsReadOnly": false,
    "Keys": [],
    "Values": []
  },
  "EntityMetadata": [
    {
      "LogicalName": "account",
      "MetadataId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
      "HasChanged": null,
      "Attributes": [
        {
          "@odata.type": "#Microsoft.Dynamics.CRM.ImageAttributeMetadata",
          "LogicalName": "sample_sampleimage",
          "CanStoreFullImage": true,
          "MetadataId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
          "HasChanged": null
           <null properties removed for brevity>
        },
        {
          "@odata.type": "#Microsoft.Dynamics.CRM.ImageAttributeMetadata",
          "LogicalName": "entityimage",
          "CanStoreFullImage": false,
          "MetadataId": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",
          "HasChanged": null
          <null properties removed for brevity>
        }
      ]
    }
  ]
}
```

> [!NOTE]
> The response includes all image columns. To create a list of columns that support full-sized images, loop through the `Attributes` collections in `EntityMetadata` and select the attributes where `CanStoreFullImage` is `true`.
> 
> The `RetrieveMetadataChangesResponse` returns all properties. Null properties are removed from the example above for brevity.

---

### Resize rules for thumbnail-sized images

To generate a thumbnail-sized image, Dataverse crops and resizes the image to a square shape according to the following rules:
  
- If at least one side of the image is larger than 144 pixels, Dataverse crops the image on center to 144x144 pixels.  
- If both sides of the image are smaller than 144 pixels, Dataverse crops the image square to the smallest side.  
  
The following table shows two examples.  
  
|Before|After|  
|------------|-----------|  
|:::image type="content" source="media/crm-itpro-cust-imagebeforeresize.png" alt-text="Image before resize":::<br /><br /> 300x428|:::image type="content" source="media/crm-itpro-cust-imageafterresize.jpg" alt-text="image after resize":::<br /><br /> 144x144|  
|:::image type="content" source="media/crm-itpro-cust-imagebeforeresizeexample2.png" alt-text="smaller image resize before":::<br /><br /> 91x130|:::image type="content" source="media/crm-itpro-cust-imageafterresizeexample2.jpg" alt-text="smaller image resize after":::<br /><br /> 91x91|

## Primary images

Each table can have multiple image columns, but you can only define one image column as the *primary image*. You can only set the primary image by using a create operation. For more information, see [Set only primary images for create operation](#set-only-primary-images-for-create-operation).

The [ImageAttributeMetadata.IsPrimaryImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.IsPrimaryImage) controls which image column represents the primary image for the table.

The [EntityMetadata.PrimaryImageAttribute property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.PrimaryImageAttribute) returns the logical name of the image column that is the current primary image for the table.

You can also query the [Entity Image Configuration (EntityImageConfig) table](reference/entities/entityimageconfig.md) to determine which image columns represent the current primary image by using the `parententitylogicalname` and `primaryimageattribute` column values.

# [SDK for .NET](#tab/sdk)

The static `PrintPrimaryImageColumns` method in the following example writes the table and image column names for all primary image columns.

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

More information: [Build queries with QueryExpression](org-service/queryexpression/overview.md)

# [Web API](#tab/webapi)

The following request returns the table and image column names for all primary image columns.

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

More information: [Query data using the Web API](webapi/query/overview.md)

---

## Download URL

Each image column has the following companion columns, but none of them appear within the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) designer.

|Column |Type|Naming convention |Description |
|---------|---------|---------|---------|
|Image ID|Unique identifier|`<image column name>Id`|A unique identifier for the image.|
|Time Stamp|BigInt|`<image column name>_Timestamp`|Represents when the image was last updated. This value helps make sure the latest version of the image is downloaded rather than the client using a cached version that was retrieved before.|
|URL|string|`<image column name>_URL`|A relative URL to download a thumbnail-sized version of the image|

The image ID and time stamp column values don't have any use cases except that they're used to within the URL string column value.

When the column for a record contains data, the download URL is a relative URL that uses the following format:

`/Image/download.aspx?Entity=<entity logical name>&Attribute=<image column logical name>&Id=<image id value>&Timestamp=<time stamp value>`

You can append this value to the organization URI to construct a URL that you can use to download the thumbnail-sized image file. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885`

### URL to download full-sized image

If the image column is configured to store full-sized images, you can append `&Full=true` to the URL and the link downloads the full-sized image. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885&Full=true`

If the column isn't configured to store full-sized images, the request returns no data.

## Use image data with records

When you work with records, how you handle image data depends on whether you're using the SDK or Web API.

# [SDK for .NET](#tab/sdk)

The following static `RetrieveAndUpdateImageColumn` method retrieves a `byte[]` image value from a column, saves it locally, and uploads a new image.

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
> If you set the [ColumnSet.AllColumns property](xref:Microsoft.Xrm.Sdk.Query.ColumnSet.AllColumns) to true, the query doesn't include image columns. For performance reasons, you must explicitly specify that you want to retrieve image data.

More information:

- [Retrieve a table row using the SDK for .NET](org-service/entity-operations-retrieve.md)
- [Update and delete table rows using the SDK for .NET](org-service/entity-operations-update-delete.md)


# [Web API](#tab/webapi)

By using Web API, you work with property values as base 64 encoded string values that represent the `byte[]` data.

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

Some libraries you use to serialize and deserialize JSON, such as [JSON.NET](https://www.newtonsoft.com/json), automatically convert these encoded string values to `byte[]`. You might not even notice that the transport protocol is using base 64 strings.

For more information about base 64 encoded strings, see:
 - [Base64 - MDN Web Docs Glossary](https://developer.mozilla.org/docs/Glossary/Base64)
 - [Base64 to Image Converter](https://codebeautify.org/base64-to-image-converter)
 - [Image to Base64 Converter](https://codebeautify.org/image-to-base64-converter)

More information:
- [Retrieve a table row using the Web API](webapi/retrieve-entity-using-web-api.md)
- [Update and delete table rows using the Web API](webapi/update-delete-entities-using-web-api.md)

---

### Set only primary images for create operation

When you create a record, set only the value of the current primary image column. If you try to set the value of any other image column, you get this error message:

> Name: `CannotUploadNonPrimaryImageAttributeOnCreate`   
> Code: `0x80090487`   
> Number: `-2146892665`   
> Message: `Non-primary image attribute <image column logical name> of entity <table logical name> is not allowed to upload during Create operation.`

For more information, see [Primary Images](#primary-images).

### Retrieve only thumbnail images

The image data you access through record properties is always the thumbnail-sized images. To access full-sized images, you must download them. For more information, see [Download images](#download-images).


## Upload images

To upload images, use the same APIs you use to upload files. For more information, see [Upload Files](file-column-data.md#upload-files).

## Download images

To download images, use the same APIs you use to download files. Be aware of the following differences.

### Using Dataverse messages

If you use the `InitializeFileBlocksDownload` and `DownloadBlock` messages, you always download the full-sized image if the image column supports it. You can't download the thumbnail-sized image by using this method. For more information, see [Use Dataverse messages to download a file](file-column-data.md#use-dataverse-messages-to-download-a-file).

If the image column doesn't support full-sized images, or if the [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) is false when you upload the image, the following error is returned:

> Name: `ObjectDoesNotExist`<br />
> Code: `0x80040217`<br />
> Number: `-2147220969`<br />
> Message: `No FileAttachment records found for imagedescriptorId: <guid> for image attribute: <image column logical name> of <entity logical name> record with id <guid>.`

### Using Web API

When you download images by using the Web API without using the Dataverse messages, you download the thumbnail-sized image by default. To download the full-sized image, append this parameter to the URL: `?size=full`.

If the image column doesn't support full-sized images, or if the [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) is false when you upload the image, the response returns `204 No Content`.

For more information, see [Download Files](file-column-data.md#download-files).

## Delete images

You can delete images by setting the image column value for the record to null as you would for any other property.

# [SDK for .NET](#tab/sdk)

Set the value of the image attribute to null and update the entity. For more information, see [Basic update](org-service/entity-operations-update-delete.md#basic-update).

# [Web API](#tab/webapi)

You can delete an image column value by using Web API in three different ways.

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

For more information, see [Basic update](webapi/update-delete-entities-using-web-api.md#basic-update).

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

For more information, see [Update a single property value](webapi/update-delete-entities-using-web-api.md#update-a-single-property-value).


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
[Work with image column definitions using code](image-attributes.md)<br />
[Sample: Image Operations using Dataverse SDK for .NET](org-service/samples/set-retrieve-entity-images.md)<br />
[Sample: Image Operations using Dataverse Web API](webapi/samples/image-operations.md)<br />
[Use file column data](file-column-data.md)
