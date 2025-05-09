---
title: "Work with file column definitions using code | Microsoft Docs"
description: "Learn about how to create, retrieve, update and delete file column definitions using code."
ms.date: 01/17/2024
ms.reviewer: jdaly
ms.topic: how-to
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Work with file column definitions using code

Use file columns to store file data up to a specified maximum size. File columns are optimized for storing binary data. Dataverse doesn't save this data in the relational data store, which improves performance and reduces the capacity usage. [Learn more about storage capacity](/power-platform/admin/whats-new-storage)

A custom or customizable table can have zero or more file columns. This article is about working with column definitions in code. To use data stored in these columns, see [Use file column data](file-column-data.md).

## Create file columns

The recommended way to create file columns is to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and define your columns using the designer. More information: [File columns](../../maker/data-platform/types-of-fields.md#file-columns).

> [!NOTE]
> A key consideration when creating file columns is the **Maximum file size** stored in the `MaxSizeInKB` property. The default setting for this is `32768`, or 32 MB. The maximum value is `10485760` KB (10 GB). While the API can handle files up to 10 GB in size, the requests must be 'chunked'. The size limit to send a single request is 128 MB. When a client application attempts to send a file larger than 128 MB in a single request, an error will be thrown. [Learn to upload files](file-column-data.md#upload-files).
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

- [What is the SDK for .NET](org-service/overview.md)
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
Location: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(00aa00aa-bb11-cc22-dd33-44ee44ee44ee)
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(00aa00aa-bb11-cc22-dd33-44ee44ee44ee)
```

More information:

- [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)
- [Web API table schema operations sample (C#)](webapi/samples/webapiservice-metadata-operations.md)

---

## Blocked file types

You can control which types of files aren't allowed to be saved in file columns based on the file extension and mime type.

More information:

- [Block files by extension](files-images-overview.md#block-files-by-extension)
- [Block or allow certain mime types](files-images-overview.md#block-or-allow-certain-mime-types)

## Restrictions with self-managed key (BYOK)

> [!IMPORTANT]
> Some restrictions apply when using the File and full-sized Image data-types in Dataverse. If [self-managed key (BYOK)](/power-platform/admin/manage-encryption-key) is enabled on the tenant, IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of BYOK in order to make use of these data-types.
>
> All BYOK organizations as of version: 9.2.21052.00103 can support the use of the Dataverse File and Image data-types. Files within BYOK organizations are
> limited to a maximum size of 128MB per file. All files and images within BYOK organizations will be stored in the Dataverse relational storage, instead of Dataverse File Blob storage.
> Other limitations:
>  - User Delegation SAS Downloads are not supported
>  - Chunking uploads and downloads are limited to a single chunk


<!-- File columns are supported in Power Pages only in the [notes](../../maker/portals/configure-notes.md) (annotation) table. -->

### See Also

[Use file column data](file-column-data.md)<br />
[Work with image column definitions using code](image-attributes.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
