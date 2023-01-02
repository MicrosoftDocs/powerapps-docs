---
title: "Use image column data (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about uploading, downloading, and deleting data in image columns." 
ms.date: 01/10/2023
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
# Use image column data

You can store image data in Dataverse using image columns or file columns.
Image columns have some special behaviors and limitations to support displaying images within applications.

The following table introduces some of the differences between image and file columns.


||Image  |File  |
|---------|---------|---------|
|**File Size**|Limited to 30MB.|Up to 10GB.|
|**File Types**|Only [Image file types](#image-file-types)|All file types allowed by the [Organization.BlockedAttachments value](reference/entities/organization.md#BKMK_BlockedAttachments). More information: [Block certain types of files](file-attributes.md#block-certain-types-of-files) |
|**Set with Update**|You can set image column data with other record data using update.|You can only upload files individually to file column properties.|
|**Delete with Update**|You can delete image column data by setting the attribute or property to `null` and then update the record.|You can only delete file column data using the `DeleteFile` message or sending a `DELETE` request to the specific column using Web API. More information: [Delete Files](file-column-data.md#delete-files)|
|**Set with Create**|When the image column is the *primary image*, you can set image columns with other record data using create. More information: [Primary Images](#primary-images)|You can only upload files individually to file column properties after the record was created.|
|**Return with Retrieve**|You can retrieve thumb-nail sized images with other record data using retrieve.|The value returned is the file id.|
|**Download URL**|Each image column has a string column that contains a relative URL you can include in an application that allows downloading the image file. More information: [Download URL](#download-url)|Not available for file columns, but you can compose a URL to download the file directly from the Web API. See [Download a file in a single request using Web API](file-column-data.md#download-a-file-in-a-single-request-using-web-api)|

## Image file types

Image columns store the following binary image types:

|File Format|MIME type|File extension(s)|
|---------|---------|---------|
|Graphics Interchange Format|`image/gif`|`.gif`|
|Joint Photographic Expert Group image|`image/jpeg`|`.jpg`, `.jpeg`|
|Tagged Image File Format|`image/tiff`|`.tif`, `.tiff`|
|Bitmap file|`image/bmp`|`.bmp`|
|Portable Network Graphics|`image/png`|`.png`|

If you try to save a file that is not one of these types, you will get the following error:

> Name: `ProcessImageFailure`<br />
> Code: `0x80072553`<br />
> Number: `-2147015341`<br />
> Message: `Error occured when processing image. Reason: Update image properties failed for objectid: <id of record>, logicalName: <logical name of table>, attribute: <logical name of image column`

## Full-size and thumbnail-sized images

When an image column value is set, Dataverse will automatically generate a thumb-nail sized image that is suitable for use as an icon in an application. For example, in model-driven apps a thumbnail-sized image can be displayed in the application.

If the image column is configured to store a full-sized image, a file up to 30MB in size can be saved and downloaded separately from the thumbnail-sized image. The [ImageAttributeMetadata.CanStoreFullImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage) indicates whether an image column will store a full-sized image.

### Detect which image columns support full-sized images

TODO: 
 - Check Metadata to verify single column
 - use [Image Attribute Configuration (AttributeImageConfig)  table/entity reference](reference/entities/attributeimageconfig.md) to check the system for any image attribute metadata that support full-sized images

### Re-size rules for thumbnail-sized images

When a thumbnail-sized image is generated, it is cropped and re-sized according to the following rules:

TODO

## Primary Images

Each table can have multiple image columns associated with it, but only one image column can be defined as the primary image. The [ImageAttributeMetadata.IsPrimaryImage property](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.IsPrimaryImage) controls which image column represents the primary image for the table. When this is set to true, the value for any other image columns for the table will change to false. The [EntityMetadata.PrimaryImageAttribute property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.PrimaryImageAttribute) returns the logical name of the image column that is the current primary image.

TODO
Detect whether a column is the primary image
 - individually
 - Use [Entity Image Configuration (EntityImageConfig)  table/entity reference](reference/entities/entityimageconfig.md)

## Download URL

When a new file column is created a companion string column will be created for the table that follows the naming convention: `<image column name>_url`. For example, if the image column logical name is `sample_imagecolumn` the download URL column logical name will be `sample_imagecolumn_url`.

When the column for a record contains data, the download URL will be a relative URL using the following format:

`/Image/download.aspx?Entity=<entity logical name>&Attribute=<image column logical name>&Id=<record id>&Timestamp=<time stamp value>`

You can append this value to the organization URI to construct a URL which can be used to download the thumbnail-sized image file. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885`

### URL to download full-sized image

If the image column is configured to store full-sized images, you can append `&Full=true` to the URL and the link will download the full-sized image. For example:

`https://yourorg.crm.dynamics.com/Image/download.aspx?Entity=account&Attribute=sample_imagecolumn&Id=7a4814f9-b0b8-ea11-a812-000d3a122b89&Timestamp=637388308718090885&Full=true`

If the column isn't configured to store full-sized images, no data will be returned.

## Use image data with records

When working with records you can set or access image column values but there are some limitations.

### Only primary images can be set for create

When you create a record, you can only set the value of the current primary image column. If you try to set the value of any other image column you will get this error:

> Name: `CannotUploadNonPrimaryImageAttributeOnCreate`<br />
> Code: `0x80090487`<br />
> Number: `-2146892665`<br />
> Message: `Non-primary image attribute <image column logical name> of entity <table logical name> is not allowed to upload during Create operation.`



### Only thumbnail images can be retrieved

The image data you access via record properties will always be the thumbnail-sized images.

## Upload images

## Download images

## Delete images
