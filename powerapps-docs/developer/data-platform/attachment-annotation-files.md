---
title: "Use file data with Attachment and Annotation records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using file data with Attachment and Annotation records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/02/2023
ms.reviewer: jdaly
ms.topic: article
author: DanaMartens # GitHub ID
ms.subservice: dataverse-developer
ms.author: dmartens # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Use file data with Attachment and Annotation records

[Attachment (ActivityMimeAttachment)](reference/entities/activitymimeattachment.md) and [Note (Annotation)](reference/entities/annotation.md) tables contain special string columns that store file data.

- An Attachment is a file that is associated with an activity, usually an email activity.
- A Note is a record associated with a table row that contains text and may have a single file attached.

These tables existed before file or image columns, so they work differently.

- The binary file data is stored in a String column: [ActivityMimeAttachment.Body](reference/entities/activitymimeattachment.md#BKMK_Body) and [Annotation.DocumentBody](reference/entities/annotation.md#BKMK_DocumentBody)
- File name data is stored in the `FileName` column.
- Mime type data is stored in the `MimeType` column.

Because these columns are part of the data for the record, you should update all three columns together.

## File size limits

The [Organization.MaxUploadFileSize](reference/entities/organization.md#BKMK_MaxUploadFileSize) specifies the maximum allowed size of an a file for an attachment and annotation, as well as other kinds of data, such as web resource files used for model-driven apps.

The default size is 5 MB () [Manage email settings](/power-platform/admin/settings-email)

