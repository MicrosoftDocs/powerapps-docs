---
title: "Image web resources (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using image web resources to make images available for use" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Image web resources

Use image web resources to make images available for use in model-driven apps.  

There are 5 types of image web resources: 
* PNG Format
* JPG Format
* GIF Format
* ICO Format
* Vector Format (SVG)

> [!NOTE]
> Vector Format (SVG) web resources were added with the model-driven apps.

  
<a name="BKMK_Capabilities"></a>   

## Capabilities of image web resources  
With image web resources you can add images where you need them. Common uses include the following:  
  
- Custom table icons  
- Icons for custom ribbon controls and `SiteMap` subareas  
- Decorative graphics for forms and webpage web resources.  
- Background images that are used by CSS web resources.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

Use Vector Format (SVG) web resources for any icon presented in the application. Vector images are defined as Scalable Vector Graphics (SVG) an XML-based vector image format. The advantage of vector images over other image web resources is that they scale. You can define one vector image and re-use it rather than provide multiple sizes of images. You will use these in with a new <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IconVectorName> property to define the icon for a custom table instead of the `IconLargeName`, `IconMediumName`, or `IconSmallName` properties.

> [!NOTE]
> Vector Format (SVG) web resources are treated like the [Script (JScript)](./script-jscript-web-resources.md) web resources, and carry the same security risks as Script (JScript) web resources because SVG files allow JScript embedding.
  
<a name="BKMK_Limitations"></a>   

## Limitations of image web resources  
Like all web resources, image web resources use the security context. Only licensed users who have the necessary privileges can access them.  
 
  
<a name="BKMK_ReferenceFromWebPageWebResource"></a>   
## Reference an image web resource from a webpage web resource  
 All web resources can use relative URLs to reference each other. In the following example, for the webpage (HTML) web resource new_/content/contentpage.htm to reference the image web resource new_/Images/image1.png, add the following HTML code to new_/content/contentpage.htm:  
  
```html  
<img src="../Images/image1.png" />  
```  
  

## Reference an image web resource from a form  
  
#### Add an image to a form  
  
1. Navigate to the form editor for a table.  
  
2. Select where you want to add the image in the form.  
  
3. On the **Insert tab**, select **Web Resource**.  
  
4. On the **General** tab, select the web resource image that you want to add.  
  
5. Specify a name for the web resource. You can also specify a label and alternative text.  
  
6. On the **Formatting** tab, you can define:  
  
    - The number of columns the images should use.  
  
    - The number of rows the images should use, or if it should automatically expand to use available space.  
  
    -  The size of the image using the following options:  
  
        - **Stretch to fit**  
  
        - **Stretch to fit (maintain aspect ratio)**  
  
        - **Original**  
  
        - **Specific**  
  
    -   If you select “Specific,” you can enter the desired height and width in pixels.  
  
7.  Select **OK**.  
  
8.  You must save your changes and publish the form before users can see the image in the form.  
  
<a name="BKMK_ReferenceWithWebResourcedirective"></a> 
  
## Reference an image web resource from a ribbon element or from the Site Map subarea  

Use the `$webresource:` directive to specify a web resource image to use as an icon in the ribbon or in the application navigation using Site Map. The following sample shows how to specify icons for a button in the ribbon.  
  
```xml  
<Button Id="MyISV.opportunity.form.actions.FlyoutAnchor.Button.1" Image16by16="$webresource:new_/icons/oneIcon16.png" Image32by32="$webresource:new_/icons/oneIcon32.png"/>  
```  
  
> [!NOTE]
> Using the `$webresource:` directive adds a solution dependency that prevents the referenced image web resources from being deleted as long as they are used by another solution component.  
  
### See also  
 [Web resources](web-resources.md)   
 [Using Web Page (HTML) web resources](webpage-html-web-resources.md)   
 [Using Style Sheet (CSS) web resources](css-web-resources.md)   
 [Using Script (JScript) web resources](script-jscript-web-resources.md)   
 [Using Data (XML) web resources](data-xml-web-resources.md)     
 [Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]