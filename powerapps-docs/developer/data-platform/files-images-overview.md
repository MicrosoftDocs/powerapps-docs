---
title: "Files and images overview (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using file and image data in Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/26/2023
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
# Files and images overview

Dataverse provides several different ways to save binary data representing files in different types of columns. The following table summarizes some of the similarities and differences.


||File|Image|Attachment & Note|
|---------|---------|---------|---------|
|**Attribute Type**|File|Image|String|
|**Create new columns?**|Yes. See [File columns](file-attributes.md)|Yes, See [Image columns](image-attributes.md)|No, only `activitymimeattachment.body` and `annotation.documentbody` columns.|
|**File Size limits**|Configurable by column `MaxSizeInKB` setting<br />Up to 10 GB, but client controls limited to 128 MB|Configurable by column `MaxSizeInKB` setting<br />Up to 30 MB.|Configurable by [Organization.MaxUploadFileSize](reference/entities/organization.md#BKMK_MaxUploadFileSize) setting up to 128 MB. See [File size limits](attachment-annotation-files.md#file-size-limits)|
|**Upload Messages**|`InitializeFileBlocksUpload`<br >`UploadBlock`<br />`CommitFileBlocksUpload`|`InitializeFileBlocksUpload`<br >`UploadBlock`<br />`CommitFileBlocksUpload`|`InitializeAttachmentBlocksUpload`<br >`UploadBlock`<br />`CommitAttachmentBlocksUpload`<br />OR<br />`InitializeAnnotationBlocksUpload`<br >`UploadBlock`<br />`CommitAnnotationBlocksUpload`|
|**Download Messages**|`InitializeFileBlocksDownload`<br >`DownloadBlock`|`InitializeFileBlocksDownload`<br >`DownloadBlock`|`InitializeAttachmentBlocksDownload`<br >`DownloadBlock`<br />OR<br />`InitializeAnnotationBlocksDownload`<br >`DownloadBlock`|
|**Retrieve Behavior**|Can't retrieve file with record. Returns `fileid` value instead.|Can retrieve thumbnail-sized images with records.|Can retrieve file with records.|
|**Set with Create**|No|Only Primary image column|Yes|
|**Set with Update**|No, you must set the column value.|Yes|Yes|
|**Delete File data**|Set column value to null or use `DeleteFile` message.|Set column value to null.|Set column value to null.|
|**File types supported**|Any file not blocked by [Organization.BlockedAttachments](reference/entities/organization.md#BKMK_BlockedAttachments). See [Block certain types of files](#block-certain-types-of-files)|Only `gif`, `jpeg`, `tiff`, `bmp`, & `png` files.|Any file not blocked by [Organization.BlockedAttachments](reference/entities/organization.md#BKMK_BlockedAttachments). See [Block certain types of files](#block-certain-types-of-files)|
|**Special Behaviors**||Column always creates and saves thumbnail-sized images. Full-sized images are saved only when the column is configured to do so. Special syntax required to download full-sized image files.<br /><br />Each column has a companion string column that contains a relative URL to download the image.||
|**More information**|[Use file column data](file-column-data.md)|[Use image column data](image-column-data.md)|[Use file data with Attachment and Note records](attachment-annotation-files.md)|
|**Sample Code**|[SDK for .NET](org-service/samples/file-operations.md)<br />[Web API](webapi/samples/file-operations.md)|[SDK for .NET](org-service/samples/set-retrieve-entity-images.md)<br />[Web API](webapi/samples/image-operations.md)|[SDK for .NET](org-service/samples/attachment-annotation-files.md)<br />[Web API](webapi/samples/attachment-annotation-file-operations.md)|

## Block certain types of files

You can block the types of files that can be uploaded by the extension or MIME type.

### Block files by extension

You can specify which types of files can't be saved in file columns, attachments and notes. Use the [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting to control the file types to be blocked.

You can also query and modify this data programmatically. It's stored in the [Organization.BlockedAttachments](reference/entities/organization.md#BKMK_BlockedAttachments) column. There's only one row in the organization table. You can use the SDK or Web API to query this data:


#### [SDK for .NET](#tab/sdk)

This static `RetrieveBlockedAttachments` method:

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

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/organizations?$select=blockedattachments HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

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

When anyone tries to upload a file using one of the blocked types, the following error occurs:

> Name: `AttachmentBlocked`<br />
> Code: `0x80043e09`<br />
> Number: `-2147205623`<br />
> Message: `The attachment is either not a valid type or is too large. It cannot be uploaded or downloaded.`

### Block or allow certain MIME types

You can block or allow upload of files based on MIME types. More Information: [Mime Type Validation](/power-platform/admin/settings-privacy-security#mime-type-validation).

You can also query and modify this data programmatically. It's stored in the [Organization.BlockedMimeTypes](reference/entities/organization.md#BKMK_BlockedMimeTypes) and [Organization.AllowedMimeTypes](reference/entities/organization.md#BKMK_AllowedMimeTypes) columns. There's only one row in the organization table. You can use the SDK or Web API to query this data:

#### [SDK for .NET](#tab/sdk)

```csharp
public static (string, string) RetrieveMimeTypes(IOrganizationService service)
{
    var query = new QueryExpression("organization")
    {
        ColumnSet = new ColumnSet("blockedmimetypes", "allowedmimetypes"),
        TopCount = 1
    };
    EntityCollection results = service.RetrieveMultiple(query);
    Entity organization = results.Entities.FirstOrDefault();
    return (
        organization.Contains("blockedmimetypes") ? (string)organization["blockedmimetypes"] : string.Empty,
        organization.Contains("allowedmimetypes") ? (string)organization["allowedmimetypes"] : string.Empty);
}
```

#### [Web API](#tab/webapi)

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/organizations?$select=blockedmimetypes,allowedmimetypes HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#organizations(blockedmimetypes,allowedmimetypes)",
    "value": [
        {
            "@odata.etag": "W/\"4719801\"",
            "blockedmimetypes": "image/svg+xml",
            "allowedmimetypes": null,
            "organizationid": "8daa44aa-e2f8-ed11-a66e-00224820c64b"
        }
    ]
}
```

If `allowedmimetypes` is set, `blockedmimetypes` is ignored. Only the MIME types specified in `allowedmimetypes` are allowed.

If `blockedmimetypes` isn't empty and `allowedmimetypes` is empty, the following error occurs when someone tries to upload a MIME type that is in blocked MIME types:

> Name: `MimeTypeBlocked`<br />
> Code: `0x80072522`<br />
> Message: `Operation not allowed as mime type image/svg+xml is blocked.`

If `allowedmimetypes` isn't empty, the following error occurs when someone tries to upload a MIME type that isn't in `allowedmimetypes`:

> Name: `MimeTypeNotInAllowedList`<br />
> Code: `0x80072521`<br />
> Message: `Operation not allowed as mime type image/svg+xml is not in the allow list.`

### See also

[Use file column data](file-column-data.md)<br />
[Use image column data](image-column-data.md)<br />
[Use file data with Attachment and Note records](attachment-annotation-files.md)

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]
