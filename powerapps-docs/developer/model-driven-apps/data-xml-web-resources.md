---
title: "Data (XML) Web resources (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about using data (XML) Web resources to save and access data." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 2bf0d49f-8b6d-6d5b-0af5-edf6dd485fed
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Data (XML) Web resources

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/data-xml-web-resources -->

Use Data (XML) Web resources to save and access data.  
  
## Capabilities of XML Web resources  
 Use XML Web resources to cache data that you want to use in your solution.  
  
### Limitations of XML Web resources  
 Use XML Web resources to cache configuration settings or metadata for your solutions.  
  
 An XML Web resource does not represent a robust solution for data that is frequently updated by multiple users. While one user is updating an XML Web resource, another user (or automated process) could update the Web resource and that data would be lost when the first user saves their changes.  
  
 All XML files must use the .xml file name extension. Files that use XML data but do not use the .xml file name extension cannot be uploaded as Web resources unless the file name extension is changed.  
  
### See also  
 [Web Resources](web-resources.md)   
 [Using Web Page (HTML) Web Resources](webpage-html-web-resources.md)   
 [Using Style Sheet (CSS) Web Resources](css-web-resources.md)   
 [Using Script (JScript) Web Resources](script-jscript-web-resources.md)   
 [Using Image (JPG, PNG, GIF) Web Resources](image-web-resources.md)   
 [Using Silverlight (XAP) Web Resources](/dynamics365/customer-engagement/developer/silverlight-xap-web-resources)<br/>   <!-- TODO need to update the relevant link from the powerapps repo-->
 [Using Stylesheet (XSL) Web Resources](/dynamics365/customer-engagement/developer/stylesheet-xsl-web-resources) <!-- TODO need to update the relevant link from the powerapps repo-->
