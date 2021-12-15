---
title: "Stylesheet (XSL) web resources  (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using Stylesheet (XSL) Web resources to transform XML data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: mda-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Stylesheet (XSL) web resources

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/stylesheet-xsl-web-resources -->


Use Stylesheet (XSL) Web resources to transform XML data.  
  
## Capabilities of XSL Web resources  

 Use XSL Web resources to transform XML data used by your solution.  
  
 The following Web resources work together to render a page that displays a table using the data in the XML Web resource. The source files for these Web resources are part of the Import Web Resources sample under the **filestoimport** folder. Download the sample of [Import files as web resources](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ImportWebResources).  
  
 **HTML Web resource:** sample_/ImportWebResources/Content/ShowData.htm  
 ```html  
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
<html>  
<head>  
 <title></title>  
 <script src="Script/Script.js" type="text/javascript"></script>  
 <link href="CSS/Styles.css" rel="stylesheet" type="text/css" />  
</head>  
<body onload="SDK.ImportWebResources.showData()">  
 <div id="results" />  
</body>  
</html>  
```  
  
 **XSL Web resource:** sample_/ImportWebResources/XSL/Transform.xslt  
 ```xml  
<?xml version="1.0" encoding="utf-8"?>  
<xsl:stylesheet version="1.0"  
                xmlns:xsl="https://www.w3.org/1999/XSL/Transform"  
                xmlns:msxsl="urn:schemas-microsoft-com:xslt"  
                exclude-result-prefixes="msxsl"  
>  
 <xsl:output method="xml"  
             indent="yes"/>  
  
 <xsl:template match="@* | node()">  
  <xsl:copy>  
   <xsl:apply-templates select="@* | node()"/>  
  </xsl:copy>  
 </xsl:template>  
  
 <xsl:template match="people">  
  <xsl:element name="table">  
   <xsl:element name="thead">  
    <xsl:element name="tr">  
     <xsl:element name="th">  
      <xsl:text>First Name</xsl:text>  
     </xsl:element>  
     <xsl:element name="th">  
      <xsl:text>Last Name</xsl:text>  
     </xsl:element>  
    </xsl:element>  
   </xsl:element>  
   <xsl:element name="tbody">  
    <xsl:apply-templates />  
   </xsl:element>  
  </xsl:element>  
  
 </xsl:template>  
  
 <xsl:template match="person">  
  <xsl:element name="tr">  
   <xsl:element name="td">  
    <xsl:value-of select="@firstName"/>  
   </xsl:element>  
   <xsl:element name="td">  
    <xsl:value-of select="@lastName"/>  
   </xsl:element>  
  </xsl:element>  
  
 </xsl:template>  
  
</xsl:stylesheet>  
  
```  
  
 **XML Web resource:** sample_/ImportWebResources/Data/Data.xml  
 ```xml  
<?xml version="1.0" encoding="utf-8" ?>  
<people>  
 <person firstName="Apurva"  
         lastName="Dalia" />  
 <person firstName="Ofer"  
         lastName="Daliot" />  
 <person firstName="Jim"  
         lastName="Daly" />  
 <person firstName="Ryan"  
         lastName="Danner" />  
 <person firstName="Mike"  
         lastName="Danseglio" />  
 <person firstName="Alex"  
         lastName="Darrow" />  
</people>  
```  
  
 **Script Web resource:** sample_/ImportWebResources/Script/Script.js  
 ```javascript  
//If the SDK namespace object is not defined, create it.  
if (typeof (SDK) == "undefined")  
{ SDK = {}; }  
// Create Namespace container for functions in this library;  
SDK.ImportWebResources = {  
 dataFile: "Data/Data.xml",  
 transformFile: "XSL/Transform.xslt",  
 showData: function () {  
  
  //Create an XML document from the Data.xml file  
  var dataXml = new ActiveXObject("Msxml2.DOMDocument.6.0");  
  dataXml.async = false;  
  dataXml.load(this.dataFile);  
  
  //Create an XML document from the Transform.xslt file  
  var transformXSLT = new ActiveXObject("Msxml2.DOMDocument.6.0");  
  transformXSLT.async = false;  
  transformXSLT.load(this.transformFile);  
  
  // Set the innerHTML of the results area to the output of the transformation.  
  var resultsArea = document.getElementById("results");  
  resultsArea.innerHTML = dataXml.transformNode(transformXSLT);  
 }  
  
}  
```  
  
 **CSS Web resource:** sample_/ImportWebResources/CSS/Styles.css  
 ```css
body  
{  
    font-family: Calibri;  
}  
table  
{  
    border: 1px solid gray;  
    border-collapse: collapse;  
}  
th  
{  
    text-align: left;  
    border: 1px solid gray;  
}  
td  
{  
    border: 1px solid gray;  
}  
```  
  
### See also  
 [Web Resources](web-resources.md)   
 [Using Web Page (HTML) Web Resources](webpage-html-web-resources.md)   
 [Using Style Sheet (CSS) Web Resources](css-web-resources.md)   
 [Using Script (JScript) Web Resources](script-jscript-web-resources.md)   
 [Using Data (XML) Web Resources](data-xml-web-resources.md)   
 [Using Image (JPG, PNG, GIF) Web Resources](image-web-resources.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]