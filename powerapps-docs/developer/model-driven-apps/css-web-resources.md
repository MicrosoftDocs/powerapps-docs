---
title: "CSS web resources (model-driven apps)"
description: "Use cascading style sheet (CSS) web resources to create style sheets for use in webpage web resources. "
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

# CSS web resources

Use cascading style sheet (CSS) web resources to create style sheets for use in webpage web resources.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]
  
## Capabilities of CSS web resources 

With CSS web resources, you can manage the appearance of webpage web resources by linking them to a shared library of CSS styles.  
  
### Limitations of CSS web resources  

 Like all web resources, CSS web resources are only available in the security context. Only licensed users who have the necessary privileges can access them.
  
## Referencing a style sheet web resource from a webpage web resource  

 All web resources can use relative URLs to reference each other. In the following example, for the webpage web resource `sample_/content/contentpage.htm` to reference the style sheet web resource `sample_/styles/styles.css`, add the following example to the head element of sample_/content/contentpage.htm:  
  
```html  
<link rel="stylesheet" type="text/css" href="../styles/styles.css" />  
```  
  
 To reference a style sheet from a different publisher, the path must include that solution publisher customization prefix. For example, for the `sample_/content/contentpage.htm` page to reference the `MyIsv_/styles/styles.css` page, the href parameter value should be `../../MyIsv_/styles/styles.css`.  
  
> [!NOTE]
>  References included in code between web resources aren't tracked as solution dependencies.  
  
### See also  

 [Web resources](web-resources.md)   
 [Using Web Page (HTML) web resources](webpage-html-web-resources.md)   
 [Using JavaScript web resources](script-jscript-web-resources.md)   
 [Using Data (XML) web resources](data-xml-web-resources.md)   
 [Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)   
 [Using Silverlight (XAP) web resources](/dynamics365/customer-engagement/developer/silverlight-xap-web-resources)  
 [Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)   
 [WebResource table](../data-platform/reference/entities/webresource.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
