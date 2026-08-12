---
title: "JavaScript Web Resources for Model-Driven Apps"
description: "Learn about using JavaScript web resources to create a library of JavaScript functions that can be accessed from anywhere."
author: anushikhas96
ms.author: anushisharma
ms.date: 08/10/2026
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# JavaScript web resources for model-driven apps

Use JavaScript web resources to create a library of JavaScript functions that you can access from anywhere.  
  
<a name="BKMK_capabilities"></a>

## Capabilities of JavaScript web resources

By using JavaScript web resources, you can more efficiently manage code used in form scripts, webpage (HTML) web resources, or ribbon commands by linking them to a shared library of JavaScript functions.  
  
<a name="BKMK_limitations"></a>

## Limitations of JavaScript web resources

 Like all web resources, JavaScript web resources use the model-driven apps security context. Only licensed users who have the necessary privileges can access them.  
  
> [!NOTE]
>  References included in code between web resources aren't tracked as solution dependencies.  
  
<a name="BKMK_Using"></a>

## Use JavaScript libraries

For information about developing and testing JavaScript libraries as well as how to associate them with ribbon commands and form events, see [Client scripting using JavaScript](client-scripting.md).  
  
<a name="BKMK_Referencing"></a>

## Reference a script web resource from a webpage web resource

All web resources can use relative URLs to reference each other. In the following example, for the webpage web resource `new_/content/contentpage.htm` to reference the JavaScript web resource `new_/scripts/myScript.js`, add the following HTML code to the head element of `new_/content/contentpage.htm`.  
  
```html  
<script type="text/jscript" src="../scripts/myScript.js"></script>  
```  
  
 To reference a JavaScript file from a different publisher, include the customization prefix for that publisher in the path. For example, to reference the `MyIsv_/scripts/customscripts.js` file from the `new_/content/contentpage.htm` page, set the `src` attribute to `../../MyIsv_/scripts/customscripts.js`.  
  
### See also

[Client scripting using JavaScript](client-scripting.md)<br />
[Web resources](web-resources.md)<br />
[Using Web Page (HTML) web resources](webpage-html-web-resources.md)<br />
[Using Style Sheet (CSS) web resources](css-web-resources.md)<br />
[Using Data (XML) web resources](data-xml-web-resources.md)<br />
[Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)<br />
[Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)<br />
[Streamline web resource development using Fiddler AutoResponder](streamline-javascript-development-fiddler-autoresponder.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
