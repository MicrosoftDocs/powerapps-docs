---
title: "Create File columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to create file columns using code." # 115-145 characters including spaces. This abstract displays in the search result.
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
# File columns

Use file columns to store file data up to a specified maximum size. A custom or customizable table can have zero or more file columns.

## Create file columns

The recommended way to create file columns is to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and define your columns using the designer. More information: [File columns](../../maker/data-platform/types-of-fields.md#file-columns).

> [!NOTE]
> A key consideration when creating file columns is the **Maximum file size** stored in the `MaxSizeInKB` property. The default setting for this is `32768`, or 32 MB. The maximum value is `10485760` KB (10 GB). This value cannot be changed in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the designer after you create the file column.
> You can use the API to update the `MaxSizeInKB` property. More information: [Update a column using Web API](webapi/create-update-entity-definitions-using-web-api.md#update-a-column) and [Update a column using SDK](org-service/metadata-attributemetadata.md#update-a-column)

You can also create file columns using the Dataverse SDK for .NET or using the Web API. The following examples show how:

#### [SDK for .NET](#tab/sdk)

Use the [FileAttributeMetadata Class](xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata) with the [CreateAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest) to create a file column.


```csharp
public static void CreateFileColumn(IOrganizationService service, string entityLogicalName, string fileColumnSchemaName) {

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

**Request**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1393

{
  "@odata.type": "Microsoft.Dynamics.CRM.FileAttributeMetadata",
  "AttributeType": "Virtual",
  "AttributeTypeName": {
    "Value": "FileType"
  },
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
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample File Column for FileOperation samples",
      "LanguageCode": 1033,
      "IsManaged": false
    }
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
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Sample File Column",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "RequiredLevel": {
    "Value": "None",
    "CanBeChanged": false,
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
  },
  "SchemaName": "sample_FileColumn"
}
```

Use the `FileAttributeMetadata.MaxSizeInKB` property to set the maximum size.

**Response**

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

## Block certain types of files

You can control which types of files are not allowed to be saved in file Columns. You can set and change this in the [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting. This setting also applies to files that can be set in the [Annotation (note)](annotation-note-entity.md) and [Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) tables.

You can also query and modify this data programmatically. It is stored in the [Organization.BlockedAttachments](reference/entities/organization.md#BKMK_BlockedAttachments) column. There is only one row in the organization table. You can use the SDK or Web API to query this data:


#### [SDK for .NET](#tab/sdk)

This function:

```csharp
protected static string RetrieveBlockedAttachments(IOrganizationService service) {

   var query = new QueryExpression("organization")
   {
         ColumnSet = new ColumnSet("blockedattachments"),
         TopCount = 1
   };
   EntityCollection results = service.RetrieveMultiple(query);
   return (string)results.Entities.FirstOrDefault()["blockedattachments"];

}
```

Returns a string value like this by default:

`ade;adp;app;asa;ashx;asmx;asp;bas;bat;cdx;cer;chm;class;cmd;com;config;cpl;crt;csh;dll;exe;fxp;hlp;hta;htr;htw;ida;idc;idq;inf;ins;isp;its;jar;js;jse;ksh;lnk;mad;maf;mag;mam;maq;mar;mas;mat;mau;mav;maw;mda;mdb;mde;mdt;mdw;mdz;msc;msh;msh1;msh1xml;msh2;msh2xml;mshxml;msi;msp;mst;ops;pcd;pif;prf;prg;printer;pst;reg;rem;scf;scr;sct;shb;shs;shtm;shtml;soap;stm;tmp;url;vb;vbe;vbs;vsmacros;vss;vst;vsw;ws;wsc;wsf;wsh;svg`

More information: [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)

#### [Web API](#tab/webapi)

Use this request to return only the `blockedattachments` value of the organization record.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/organizations?$select=blockedattachments HTTP/1.1
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
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#organizations(blockedattachments)",
    "value": [
        {
            "@odata.etag": "W/\"75142950\"",
            "blockedattachments": "ade;adp;app;asa;ashx;asmx;asp;bas;bat;cdx;cer;chm;class;cmd;com;config;cpl;crt;csh;dll;exe;fxp;hlp;hta;htr;htw;ida;idc;idq;inf;ins;isp;its;jar;js;jse;ksh;lnk;mad;maf;mag;mam;maq;mar;mas;mat;mau;mav;maw;mda;mdb;mde;mdt;mdw;mdz;msc;msh;msh1;msh1xml;msh2;msh2xml;mshxml;msi;msp;mst;ops;pcd;pif;prf;prg;printer;pst;reg;rem;scf;scr;sct;shb;shs;shtm;shtml;soap;stm;tmp;url;vb;vbe;vbs;vsmacros;vss;vst;vsw;ws;wsc;wsf;wsh;svg",
            "organizationid": "883278f5-07af-45eb-a0bc-3fee67caa544"
        }
    ]
}
```

More information: [Query data using the Web API](webapi/query-data-web-api.md)

---

When anyone tries to upload a file of this type the following error will be thrown:

> Name: `AttachmentBlocked`<br />
> Code: `0x80043e09`<br />
> Number: `-2147205623`<br />
> Message: `The attachment is either not a valid type or is too large. It cannot be uploaded or downloaded.`

## Restrictions with Customer Managed Keys (CMK)

> [!IMPORTANT]
> Some restrictions apply when using the File and enhanced Image data-types in Dataverse. If Customer Managed Keys (CMK) is enabled on the tenant, IoT data-types are not available to the tenant's organizations. Solutions that contain excluded data-types will not install. Customers must opt-out of CMK in order to make use of these data-types.<p/>
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
