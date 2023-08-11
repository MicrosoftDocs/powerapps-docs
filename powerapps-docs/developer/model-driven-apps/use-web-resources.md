---
title: Use web resources | Microsoft Docs
description: Learn how developers use web resources within model-driven apps.
suite: powerapps
author: sriharibs-msft
ms.author: srihas

ms.date: 04/01/2022
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

There is a virtual folder called `webresources` within each Microsoft Dataverse instance where you can request HTML, JS, CSS, image, and other files by name and access them in your browser. You can upload these files using the application or programatically add them as [Web resource table](../data-platform/reference/entities/webresource.md) records. The [XrmToolBox web resources manager](https://www.xrmtoolbox.com/plugins/MsCrmTools.WebResourcesManager/) is a community tool which can facilitate working with these records.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

These records can refer to each other using relative path names in their content. This ability to upload files and request them by name provides all the building blocks you need to make web applications using files that are processed within the authenticated session of your browser. Using only client-side code with AJAX techniques, you can create rich applications that can run within a browser window or within an IFrame in a form or dashboard. 

Most commonly, you will use JavaScript web resources to add event handler functions to forms and commands.

More information:
- [Client scripting with model-driven apps](client-scripting.md)
- [Web resources](web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
