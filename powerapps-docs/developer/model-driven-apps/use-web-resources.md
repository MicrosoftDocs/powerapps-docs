---
title: Use web resources
description: Learn how developers use web resources within model-driven apps.
suite: powerapps
author: anushikhas96
ms.author: anushisharma
ms.date: 10/28/2024
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Use web resources

There's a virtual folder called `webresources` within each Microsoft Dataverse instance where you can request HTML, JS, CSS, image, and other files by name and access them in your browser. You can upload these files using the application or programmatically add them as [Web resource table](../data-platform/reference/entities/webresource.md) records. The [XrmToolBox web resources manager](https://www.xrmtoolbox.com/plugins/MsCrmTools.WebResourcesManager/) is a community tool which can facilitate working with these records.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

These records can refer to each other using relative path names in their content. This ability to upload files and request them by name provides all the building blocks you need to make web applications using files that are processed within the authenticated session of your browser. Using only client-side code with AJAX techniques, you can create rich applications that can run within a browser window or within an IFrame in a form or dashboard. 

Most commonly, you'll use JavaScript web resources to add event handler functions to forms and commands.

More information:
- [Client scripting with model-driven apps](client-scripting.md)
- [Web resources](web-resources.md)

> [!NOTE]
> The maximum size of web resources is controlled with same setting that limits the size of email attachments. See the **Maximum file size for attachments** setting described in [Manage email settings](/power-platform/admin/settings-email).
>
> This value is set in the [Organization.MaxUploadFileSize](../data-platform/reference/entities/organization.md#BKMK_MaxUploadFileSize) column. [Learn how to read and update environment settings using code](../data-platform/organization-table.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
