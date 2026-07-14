---
title: "Image web resources (model-driven apps)"
description: "Learn about using image web resources to make images available for use."
author: anushikhas96
ms.author: anushisharma
ms.date: 04/26/2024
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Image web resources

Use image web resources to make images available for use in model-driven apps.  

There are five types of image web resources:

- PNG Format
- JPG Format
- GIF Format
- ICO (Windows icon format) Format
- SVG (Scalable Vector Graphics) format

> [!NOTE]
> Vector Format (SVG) web resources were added with the model-driven apps.


## Capabilities of image web resources

With image web resources, you can add images where you need them. Common uses include:  
  
- Custom table icons.
- Icons for custom ribbon controls and `SiteMap` subareas.
- Decorative graphics for forms and webpage web resources.
- Background images that are used by CSS web resources.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Working with Scalable Vector Graphics (SVG)

Use Vector Format (SVG) web resources for any icon presented in the application. Vector images are defined as Scalable Vector Graphics (SVG), an XML-based vector image format. We recommend using SVG over other image types like PNG and JPG because they have better accessibility, smaller in file size, and can scale with their container.

### Better accessibility

Model-driven apps can control the icon color to avoid contrast issues when SVG's don't contain hex values for colors. Using the [currentColor](https://developer.mozilla.org/docs/Web/CSS/color_value#currentcolor_keyword) can help ensure that the correct theme colors are used.

```html
<path fill="currentColor" d="M16,0c-0,0-0-0.0-0-0.0v-0c0-0,0-0.0,0-0.0s0,0.0,0,0.0v0C00,0.0,00,0,00,0z"/>
```

### Smaller file size

SVG files are typically smaller than raster type images, such as jpg or png.

### Scale with their container

You can reuse a single SVG rather than provide multiple sizes of images. Use SVG web resources in the [EntityMetadata.IconVectorName](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IconVectorName) property to define the icon for a custom table instead of the `IconLargeName`, `IconMediumName`, or `IconSmallName` properties.  

### Best practices

Ensure that a default size is set through the [svg](https://developer.mozilla.org/docs/Web/SVG/Element/svg) element [width](https://developer.mozilla.org/docs/Web/SVG/Attribute/width), [height](https://developer.mozilla.org/docs/Web/SVG/Attribute/height), and [viewBox](https://developer.mozilla.org/docs/Web/SVG/Attribute/viewBox) attributes.

Where possible, remove any hard coded fill colors and don't use embedded style sheets and classes within the SVG. Embedded stylesheets could leak styles if other SVG files are referencing that same class. Use the style attribute to assign values instead. For example:

```html
<path style="fill:#231F20;" d="M16,0c-0,0-0-0.0-0-0.0v-0c0-0,0-0.0,0-0.0s0,0.0,0,0.0v0C00,0.0,00,0,00,0z"/>
```

> [!NOTE]
> Vector Format (SVG) web resources are treated like the [Script (JScript)](./script-jscript-web-resources.md) web resources, and carry the same security risks as JavaScript web resources because SVG files allow JScript embedding.

## Limitations of image web resources

Image web resources use the security context like all web resources. Only licensed users who have the necessary privileges can access them.

## Reference an image web resource from a webpage web resource

All web resources can use relative URLs to reference each other. In the following example, for the webpage (HTML) web resource new_/content/contentpage.htm to reference the image web resource new_/Images/image1.png, add the following HTML code to new_/content/contentpage.htm:  
  
```html  
<img src="../Images/image1.png" />  
```  
  

## Reference an image web resource from a form  
  
### Add an image to a form  
  
1. Navigate to the form editor for a table.
1. Select where you want to add the image in the form.
1. On the **Insert tab**, select **Web Resource**.
1. On the **General** tab, select the web resource image that you want to add.
1. Specify a name for the web resource. You can also specify a label and alternative text.
1. On the **Formatting** tab, you can define:
  
    - The number of columns the images should use.
    - The number of rows the images should use, or if it should automatically expand to use available space.
    - The size of the image using the following options:
  
        - **Stretch to fit**  
        - **Stretch to fit (maintain aspect ratio)**
        - **Original**  
        - **Specific**  
  
    - If you select "Specific," you can enter the desired height and width in pixels.  
  
1. Select **OK**.
1. You must save your changes and publish the form before users can see the image in the form.
  
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
[Using JavaScript web resources](script-jscript-web-resources.md)   
[Using Data (XML) web resources](data-xml-web-resources.md)     
[Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
