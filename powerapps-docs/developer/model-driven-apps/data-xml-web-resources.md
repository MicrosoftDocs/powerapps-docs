---
title: "Data (XML) Web resources (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about using data (XML) Web resources to save and access data." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: article
ms.assetid: 2bf0d49f-8b6d-6d5b-0af5-edf6dd485fed
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Data (XML) Web resources

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/data-xml-web-resources -->

Use Data (XML) Web resources to save and access data.  
  
## Capabilities of XML Web resources  
 Use XML Web resources to cache data that you want to use in your solution.  
  
### Limitations of XML Web resources  
 Use XML Web resources to cache configuration settings or metadata for your solutions.  
  
 An XML Web resource does not represent a robust solution for data that is frequently updated by multiple users. While one user is updating an XML Web resource, another user (or automated process) could update the Web resource and that data would be lost when the first user saves their changes.  
  
 All XML files must use the .xml file name extension. Files that use XML data but do not use the .xml file name extension cannot be uploaded as Web resources unless the file name extension is changed.  
  
### See also  
 [Web resources](web-resources.md)   
 [Using Web Page (HTML) web resources](webpage-html-web-resources.md)   
 [Using Style Sheet (CSS) web resources](css-web-resources.md)   
 [Using Script (JScript) web resources](script-jscript-web-resources.md)   
 [Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)   
 [Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md) 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]