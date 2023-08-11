---
title: "File columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to create, retrieve, update and delete file columns using code." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/02/2023
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
# File columns

Use file columns to store file data up to a specified maximum size. A custom or customizable table can have zero or more file columns. This article is about working with column definitions in code. To use data stored in these columns, see [Use file column data](file-column-data.md).

## Create file columns

The recommended way to create file columns is to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and define your columns using the designer. More information: [File columns](../../maker/data-platform/types-of-fields.md#file-columns).

> [!NOTE]
> A key consideration when creating file columns is the **Maximum file size** stored in the `MaxSizeInKB` property. The default setting for this is `32768`, or 32 MB. The maximum value is `10485760` KB (10 GB). While the API can handle files up to 10 GB in size, Power Apps client controls currently only support files up to 128 MB. Exceeding the 128 MB value when using these controls will result in errors uploading or downloading files.
>
> The `MaxSizeInKB` value cannot be changed in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the designer after you create the file column.
> You can use the API to update the `MaxSizeInKB` property. More information: [Update a column using Web API](webapi/create-update-column-definitions-using-web-api.md#update-a-column) and [Update a column using SDK](org-service/metadata-attributemetadata.md#update-a-column)

You can also create file columns using the Dataverse SDK for .NET or using the Web API. The following examples show how:

#### [SDK for .NET](#tab/sdk)

Use the [FileAttributeMetadata Class](xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata) with the [CreateAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest) to create a file column.


```csharp
public static void CreateFileColumn(
   IOrganizationService service, 
   string entityLogicalName, 
   string fileColumnSchemaName) 
{

    FileAttributeMetadata fileColumn = new()
    {
        SchemaName = fileColumnSchemaName,
        DisplayName = new Label("Sample File Column", 1033),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(
                AttributeRequiredLevel.None),
        Description = new Label("Sample File Column for FileOperation samples", 1033),
        MaxSizeInKB = 30 * 1024 // 30 MB

    };

    CreateAttributeRequest createfileColumnRequest = new() {
        EntityName = entityLogicalName,
        Attribute = fileColumn                   
    };

    service.Execute(createfileColumnRequest);

}
```

Use the [FileAttributeMetadata.MaxSizeInKB](xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata.MaxSizeInKB) property to set the maximum size.

More information:

- [What is the Organization service](org-service/overview.md)
- [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*)

#### [Web API](#tab/webapi)

POST a [FileAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.FileAttributeMetadata) to the `Attributes` collection for the table.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8

{
  "@odata.type": "Microsoft.Dynamics.CRM.FileAttributeMetadata",
  "AttributeTypeName": {
    "Value": "FileType"
  },
  "SchemaName": "sample_FileColumn",
  "MaxSizeInKB": 30720,
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample File Column for FileOperation samples",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample File Column",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  }
}
```

Use the `FileAttributeMetadata.MaxSizeInKB` property to set the maximum size.

**Response:**

```http
HTTP/1.1 204 NoContent
Location: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(9554c5f9-8c51-ed11-bba1-000d3a9933c9)
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(9554c5f9-8c51-ed11-bba1-000d3a9933c9)
```

More information:

- [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)
- [Web API Metadata Operations Sample (C#)](webapi/samples/webapiservice-metadata-operations.md)

---

## Blocked file types

You can control which types of files aren't allowed to be saved in file columns based on the file extension and mime type.

More information:

- [Block files by extension](files-images-overview.md#block-files-by-extension)
- [Block or allow certain mime types](files-images-overview.md#block-or-allow-certain-mime-types)

## Restrictions with Customer Managed Keys (CMK)

> [!IMPORTANT]
> Some restrictions apply when using the File and full-sized Image data-types in Dataverse. If Customer Managed Keys (CMK) is enabled on the tenant, IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of CMK in order to make use of these data-types.<p/>
> All CMK organizations as of version: 9.2.21052.00103 can support the use of the Dataverse File and Image data-types. Files within CMK organizations are
> limited to a maximum size of 128MB per file. All files and images within CMK organizations will be stored in the Dataverse relational storage, instead of Dataverse File Blob storage.
> Other limitations:
>  - User Delegation SAS Downloads are not supported
>  - Chunking uploads and downloads are limited to a single chunk


<!-- File columns are supported in Power Pages only in the [notes](../../maker/portals/configure-notes.md) (annotation) table. -->

### See Also

[Use file column data](file-column-data.md)<br />
[Image columns](image-attributes.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
