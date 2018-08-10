---
title: "<Topic Title> (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: a4e98fa7-930d-e320-5384-9f773775639b
author: JimDaly" # GitHub ID
ms.author: jdaly" # MSFT alias of Microsoft employees only
manager: shilpas" # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# CSS web resources

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/css-web-resources -->

Use cascading style sheet (CSS) web resources to create style sheets for use in webpage web resources.  
  
## Capabilities of CSS web resources  
 With CSS web resources, you can manage the appearance of webpage web resources by linking them to a shared library of CSS styles.  
  
### Limitations of CSS web resources  
 Like all web resources, CSS web resources are only available in the Dynamics 365 security context. Only licensed Dynamics 365 users who have the necessary privileges can access them.
  
## Referencing a style sheet web resource from a webpage web resource  
 All web resources can use relative URLs to reference each other. In the following example, for the webpage web resource `sample_/content/contentpage.htm` to reference the style sheet web resource `sample_/styles/styles.css`, add the following example to the head element of sample_/content/contentpage.htm:  
  
```html  
<link rel="stylesheet" type="text/css" href="../styles/styles.css" />  
```  
  
 To reference a style sheet from a different publisher, the path must include that solution publisher customization prefix. For example, for the `sample_/content/contentpage.htm` page to reference the `MyIsv_/styles/styles.css` page, the href parameter value should be `../../MyIsv_/styles/styles.css`.  
  
> [!NOTE]
>  References included in code between web resources aren’t tracked as solution dependencies.  
  
### See also  
 [Web Resources for Dynamics 365](web-resources.md)   
 [Using Web Page (HTML) Web Resources](webpage-html-web-resources.md)   
 [Using Script (JScript) Web Resources](script-jscript-web-resources.md)   
 [Using Data (XML) Web Resources](data-xml-web-resources.md)   
 [Using Image (JPG, PNG, GIF) Web Resources](image-web-resources.md)   
 [Using Silverlight (XAP) Web Resources](/dynamics365/customer-engagement/developer/silverlight-xap-web-resources)  
 [Using Stylesheet (XSL) Web Resources](stylesheet-xsl-web-resources.md)   
 [WebResource Entity](../common-data-service/reference/entities/webresource.md)