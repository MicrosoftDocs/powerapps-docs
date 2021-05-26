---
title: "Image columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about image columns that store image data, supporting columns, retrieving image data, and Uploading image data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Image columns

Certain system tables and all custom tables support entity images. Those tables that do support images can contain both a thumbnail and a full-size primary image. The thumbnail image can be seen in the web application when viewing the form data. There can be multiple image columns in a table but there can be only one primary image. However, you can change the primary image from one image to another by setting [IsPrimaryImage](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata.isprimaryimage?view=dynamics-general-ce-9#Microsoft_Xrm_Sdk_Metadata_ImageAttributeMetadata_IsPrimaryImage) for that column to `true`. Each full-sized image column is limited to 30 MB in size. The <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> of the entity image column is `EntityImage`. More information: [Entity images](/dynamics365/customer-engagement/developer/introduction-entities#entity-images).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Thumbnail images and image metadata are stored in Microsoft Dataverse, which includes the information needed to retrieve the full image. Full images are stored in file storage on the Azure blob to reduce data storage consumption.

Web API (REST) | .NET API (SOAP) 
------- | -------
[ImageAttributeMetadata](/dynamics365/customer-engagement/web-api/imageattributemetadata) | <xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata>
IsPrimaryImage, MaxHeight, MaxWidth | [IsPrimaryImage](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata.isprimaryimage?view=dynamics-general-ce-9#Microsoft_Xrm_Sdk_Metadata_ImageAttributeMetadata_IsPrimaryImage), [MaxHeight](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata.maxheight?view=dynamics-general-ce-9), [MaxWidth](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata.maxwidth?view=dynamics-general-ce-9)

In addition to image columns, custom tables support zero or more file columns that can contain any file data. These file columns can contain a much larger amount of data than image columns. For more information see [File columns](file-attributes.md).

> [!NOTE]
> The ability to store more than one image column in a table, storage of image data in an Azure blob, a maximum image size of 30MB, and file columns are supported in <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.SdkClientVersion> 9.0.45.329 or greater and Web API version 9.1 or greater.


## Supporting columns  

When an image column is added to a table some additional columns are created to support it.  
  
### EntityImage_Timestamp column  

Attribute Type Name:  `BigIntType`  
  
 The value represents when the image was last updated and is used to help make sure that the latest version of the image is downloaded and cached on the client.  
  
### EntityImage_URL column  
 Attribute Type Name: `StringType`  
  
 An absolute URL to display the entity image in a client.  
  
 The URL is composed this way:  
  
```http  
{0}/image/download.aspx?entity={1}&attribute={2}&id={3}&timestamp={4}
```  
  
- 0 : The organization URL  
  
- 1 : The table logical name  
  
- 2 : The column logical name  
  
- 3 : The EntityImageId value.  
  
- 4 : The EntityImage_Timestamp value  
  
  For example:   
  `https://myorg.crm.dynamics.com/image/download.aspx?attribute=entityimage&entity=contact&id={ECB6D3DF-4A04-E311-AFE0-00155D9C3020}&timestamp=635120312218444444`  
  
### EntityImageId  
 Attribute Type Name: `UniqueIdentifierType`  
  
 The unique identifier of the image  

### MaxSizeInKB column

 This value represents the maximum size (in kilobytes) of the image data that the column can contain. Set this value to the smallest useable data size appropriate for your particular application. See the <xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.MaxSizeInKB> property for the allowable size limit and the default value.
 
 > [!NOTE]
 > MaxSizeInKB is set when the Image column is added to a table. This cannot be changed after it is set.

### CanStoreFullImage column

 This value indicates if an image column can store a full image. See the <xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata.CanStoreFullImage> property.

## Retrieve image data  

To download thumbnail image column data, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
GET /api/data/v9.1/\<entity-type(id)\>/\<image-attribute-name\>/$value   | <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest>

 > [!NOTE]
> When you use <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> or <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>, the `EntityImage` is not included when the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>.`AllColumns` property is set to `true`. Because of the potential size of data in this column, to return this column you must explicitly request it.

Image data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. Image data greater that that amount must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all image data has been received. It is your responsibility to join the downloaded data blocks to form the complete image by combining the data blocks in the same sequence as the blocks were received.

 More information on chunking: [File columns](file-attributes.md).

To download the full image column data use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
 none  | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksDownloadRequest>
GET /api/data/v9.1/\<entity-type(id)\>/\<image-attribute-name\>/$value?size=full   | <xref:Microsoft.Crm.Sdk.Messages.DownloadBlockRequest>

Note that in this case the image column download makes use of the file column message requests. 

### Example: REST thumbnail download

**Request**
```http
GET [Organization URI]/api/data/v9.1/accounts(b9ccec62-f266-e911-8196-000d3a6de638)/myentityimage/$value

Headers:
Content-Type: application/octet-stream
```

**Response**
```http
204 No Content

Body:
byte[]
```

### Example: REST full image download (<=16MB)

**Request**
```http
GET [Organization URI]/api/data/v9.1/accounts(C0864F1C-0B71-E911-8196-000D3A6D09B3)/myentityimage/$value?size=full

Headers:
Content-Type: application/octet-stream
```
**Response**
```http
204 No Content

Body:
byte[]

Response Headers:
x-ms-file-name: "sample.png"
x-ms-file-size: 12345
```

In the above example, the query string parameter `size=full` indicates to download the full image. The file name and size will be provided in the response headers.

### Example: REST full image download (>16MB)

**Request**
```http
GET [Organization URI]/api/data/v9.1/accounts(C0864F1C-0B71-E911-8196-000D3A6D09B3)/myentityimage/$value?size=full

Header:
Range: bytes=0-1023/8192
```
**Response**
```http
206 Partial Content

Body:
byte[]

Response Headers:
x-ms-file-name: "sample.png"
x-ms-file-size: 8192
Location: api/data/v9.1/accounts(id)/myentityimage?FileContinuationToken
```
In the above example, the **Range** header indicates the first chunked download of 1024 bytes for an image that is 8192 bytes in total.
  
## Upload image data  
 To update images, set the value of the image column to a byte array that contains the content of the image file. Thumbnail images are cropped and resized to a 144x144 pixel square by the web service to reduce the size of the data before being saved. The reduction in size follows these rules:
  
- Images with at least one side larger than 144 pixels are cropped on center to 144x144.  
  
- Images with both sides smaller than 144 are cropped square to their smallest side.  
  
  The following table shows two examples.  
  
|Before|After|  
|------------|-----------|  
|![Image before resize](media/crm-itpro-cust-imagebeforeresize.png "Image before resize")<br /><br /> 300x428|![image after resize](media/crm-itpro-cust-imageafterresize.jpg "image after resize")<br /><br /> 144x144|  
|![Second image resize example](media/crm-itpro-cust-imagebeforeresizeexample2.png "Second image resize example")<br /><br /> 91x130|![second resize example](media/crm-itpro-cust-imageafterresizeexample2.jpg "second resize example")<br /><br /> 91x91|

Images can be uploaded either in full up to the maximum size configured, or in chunks.

> [!NOTE]
> As of this article's publication date, the restriction of using chunked upload for images greater than 16 MB has been removed.
> The chunking APIs will continue to be available to maintain backwards compatibility with existing solutions.

To upload full image data in single call, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
PUT or PATCH /api/data/v9.1/\<entity-type(id)\>/\<image-attribute-name\>   | <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>

### Example: REST full image upload

**Request**
```http
PUT [Organization URI]/api/data/v9.1/accounts(C0864F1C-0B71-E911-8196-000D3A6D09B3)/myentityimage

Header:
Content-Type: application/octet-stream
x-ms-file-name: sample.png

Body:
byte[]
```
After the upload is completed, a thumbnail image is automatically created by the web service. 

If your code is using the legacy method, image data transfers from the web service endpoints are limited to a maximum of 16 MB data in a single service call. Image data 16MB or greater must be divided into 4 MB or smaller data blocks (chunks) where each block is uploaded in a separate API call until all image data has been received. It is your responsibility to divide the image data into blocks up to 4MB in size and upload them in the correct sequence.

 More information on chunking: [File columns](file-attributes.md).

To use the legacy chunking to upload image data greater than 16MB in size, use the following APIs.

Web API (REST) | .NET API (SOAP)
------- | -------
none   | <xref:Microsoft.Crm.Sdk.Messages.InitializeFileBlocksUploadRequest>
PATCH /api/data/v9.1/\<entity-type(id)\>/\<image-attribute-name\>   | <xref:Microsoft.Crm.Sdk.Messages.UploadBlockRequest>
none   | <xref:Microsoft.Crm.Sdk.Messages.CommitFileBlocksUploadRequest>


### Example: REST upload with chunking (first request)

**Request**
```http
PATCH [Organization URI]/api/data/v9.1/accounts(id)/myentityimage

Headers:
x-ms-transfer-mode: chunked
x-ms-file-name: sample.png
```

**Response**
```http
Response:
200 OK

Response Headers:
x-ms-chunk-size: 4096
Accept-Ranges: bytes 
Location: api/data/v9.1/accounts(id)/myentityimage?FileContinuationToken
```
In the above example, the `x-ms-transfer-mode: chunked` header indicates a chunked upload.
 
### Example: REST upload with chunking (next request)

**Request**
```http
PATCH [Organization URI]/api/data/v9.1/accounts(id)/myentityimage?FileContinuationToken

Headers:
Content-Range: bytes 0-4095/8192
Content-Type: application/octet-stream
x-ms-file-name: sample.png

Body:
byte[]
```

**Response**
```http
204 No Content
```
In the above request, the next block of data is being uploaded. After all image data has been received by the web service, a thumbnail image is automatically created by the web service.

### See also  
[File columns](file-attributes.md)  
[Introduction to tables in Dynamics 365](/dynamics365/customer-engagement/developer/introduction-entities)   
[Introduction to table columns in Dynamics 365](/dynamics365/customer-engagement/developer/introduction-entity-attributes)   
[Sample: Set and retrieve entity images](/dynamics365/customerengagement/on-premises/developer/sample-set-retrieve-entity-images)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
