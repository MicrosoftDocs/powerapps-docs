---
title: "Data (XML) Web resources (model-driven apps)"
description: "Learn about using data (XML) Web resources to save and access data."
author: anushikhas96
ms.author: anushisharma
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

# Data (XML) Web resources

Use Data (XML) Web resources to save and access data.  
  
## Capabilities of XML Web resources

Use XML Web resources to cache data that you want to use in your solution.  
  
### Limitations of XML Web resources

Use XML Web resources to cache configuration settings or metadata for your solutions.  

An XML Web resource doesn't represent a robust solution for data multiple users frequently update. When one user is updating an XML Web resource, another user (or automated process) could update the Web resource. Data added by the second user is lost when the first user saves their changes.

All XML files must use the .xml file name extension. Files that use XML data but don't use the .xml file name extension can't be uploaded as Web resources unless the file name extension is changed.  
  
### See also

[Web resources](web-resources.md)   
[Using Web Page (HTML) web resources](webpage-html-web-resources.md)   
[Using Style Sheet (CSS) web resources](css-web-resources.md)   
[Using JavaScript web resources](script-jscript-web-resources.md)   
[Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)   
[Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md) 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
