---
title: "Files and images overview (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using file and image data in Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/02/2023
ms.reviewer: jdaly
ms.topic: article
author: JimDaly # GitHub ID
ms.subservice: dataverse-developer
ms.author: jdaly # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Files and images overview

[Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) should not be confused with [activityfileattachment](reference/entities/activityfileattachment.md), which supports files associated with the [Post](reference/entities/post.md) table.

<!-- Removed the following from file-attributes.md -->
## Block certain types of files

You can control which types of files aren't allowed to be saved in file columns, attachments and notes. You can set and change this in the [System Settings General tab](/power-platform/admin/system-settings-dialog-box-general-tab) under the **Set blocked file extensions for attachments** setting.

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

When anyone tries to upload a file using one of the blocked types the following error will be thrown:

> Name: `AttachmentBlocked`<br />
> Code: `0x80043e09`<br />
> Number: `-2147205623`<br />
> Message: `The attachment is either not a valid type or is too large. It cannot be uploaded or downloaded.`