---
title: "HTML Web Resources for Model-Driven App Extensions"
description: "Learn how to use HTML web resources to build client extensions for model-driven apps, reference related files, pass parameters, and avoid limitations."
author: anushikhas96
ms.author: anushisharma
ms.date: 08/10/2026
ms.reviewer: jdaly
ms.topic: "article"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Webpage (HTML) web resources

Use webpage (HTML) web resources to create user interface elements for client extensions.

<a name="BKMK_Capabilities"></a>

## Capabilities of HTML web resources

Because an HTML web resource streams to the user's browser, it can include any content that the browser renders.  

<a name="BKMK_Limitations"></a>

## Limitations of HTML web resources  

- An HTML web resource can't contain any code that must run on the server. You can't upload ASP.NET pages as HTML web resources.
- HTML web resources can accept only a limited number of query string parameters. [Pass parameters to HTML web resources](webpage-html-web-resources.md#BKMK_PassingParametersToWebResources)  
- The form runtime might reload HTML web resources embedded as controls in a form to improve performance. For example, the form runtime might destroy and reinitialize the control during tab navigation.

<a name="BKMK_UsingTextEditor"></a>

## Use the text editor for HTML web resources

The text editor in the web resource form is designed for simple HTML editing. For more complex HTML documents, edit the code in an external editor and use the **Browse** button to upload your file.

For example, a more complex HTML page that requires script to render the contents of the page begins like the following sample.

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

 For example, a more complex HTML page that requires script to render the contents of the page begins like the previous sample. After you open the document in the text editor and save it, the HTML changes to the following sample:

```html
<HTML><HEAD><TITLE></TITLE>
<META charset=utf-8></HEAD>
<BODY contentEditable=true onload=SDK.ImportWebResources.showData()>
<SCRIPT type=text/javascript src="Script/Script.js"></SCRIPT>
 <LINK rel=stylesheet type=text/css href="CSS/Styles.css">
<DIV id=results></DIV></BODY></HTML>
```

<a name="BKMK_PreventEditing"></a>

## Prevent editing of web resources for managed solutions

Because anyone can change the HTML in web resources by using the text editor, use managed properties to set complex HTML web resources as not customizable for managed solutions. When you view web resources in the solutions window, open the **Managed Properties** dialog box to set the **Customizable** property to `false`.    

<a name="BKMK_ReferencingOtherWebResources"></a>

## Reference other web resources from an HTML web resource

You can create a set of related files outside of model-driven apps that use any of the web resource file types. If you're careful to always use relative paths and import each web resource with a consistent naming convention that reflects the folder structure of your website, the HTML web resource maintains links to related CSS, XML, JScript, and image files that you import as web resources.    

For example, if you create a web application project that uses the following folder and file structure:  

-   `page.htm`
-   `[Styles]`

    -   `style.css`
  
-   `[Scripts]` 
  
    -   `script.js`
  
 When you import these files as web resources, you can name where your solution publisher customization prefix is `new` in the following manner:  
  
-   `new_/page.htm`  
-   `new_/Styles/style.css`  
-   `new_/Scripts/script.js`  
  
 When you follow this pattern, your `new_/page.htm` HTML web resource can reference the other files the most common way by using relative paths as shown in the following example.  

```html
<script src="Scripts/script.js" type="text/javascript"></script>
<link href="Styles/style.css" rel="stylesheet" type="text/css" />
```

The solution publisher customization prefix becomes a virtual root folder for all the web resources in your solution. If you change your customization prefix, the relative paths within your HTML web resources don't change.  
  
> [!NOTE]
>  - An HTML web resource added to a form can't use global objects defined by the JavaScript library loaded in the form. An HTML web resource can interact with the `Xrm.Page` or `Xrm.Utility` objects within the form by using `parent.Xrm.Page` or `parent.Xrm.Utility`, but global objects defined by form scripts aren't accessible by using the parent. You should load any libraries that an HTML web resource needs within the HTML web resource so they're not dependent on scripts loaded in the form.  
> - References included in code between web resources aren't tracked as solution dependencies.  

Client applications that support working offline can download web resources.

<a name="BKMK_PassingParametersToWebResources"></a>

## Pass parameters to HTML web resources

 An HTML web resource can accept only the parameters in the following table.

|Parameter|Name|Description|
|---------------|----------|-----------------|
|`typename`|Table Name|The name of the table.|
|`type`|Table Type Code|An integer that uniquely identifies the table in a specific organization.|
|`id`|Object GUID|The GUID that represents a record.|
|`orgname`|Organization Name|The unique name of the organization.|
|`userlcid`|User Language Code|The language code identifier being used by the current user.|
|`orglcid`|Organization Language Code|The language code identifier that represents the base language for the organization.|
|`data`|Optional Data Parameter|An optional value that can be passed.|
|`formid`|Form ID|The GUID that represents a form ID.|
|`entrypoint`|Entry Point|A string value. This parameter is intended to be passed as an optional value to web resources opened as custom help content for a table. When enabled, the custom help URL includes a value of either `form` or `hierarchychart`.|
|`pagemode`||For internal use only.|
|`security`||For internal use only.|
|`tabSet`||For internal use only.|

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

If you pass multiple values in the data parameter, they're automatically encoded. You must include logic to decode the multiple parameters by using script in your HTML web resource. The [Sample: Passing multiple values to a web resource through the data parameter](sample-pass-multiple-values-web-resource-through-data-parameter.md) article demonstrates one approach to address passing multiple parameter values.  
 
> [!NOTE]
> All characters included in the query string go through validation to ensure the validity of the parameters passed. If the validation process finds any parameters that aren't valid, the request fails. For example, passing text values enclosed in angular brackets is an invalid parameter type.

### See also

[Web resources](web-resources.md)   
[Create accessible web resources](create-accessible-web-resources.md)   
[Using Style Sheet (CSS) web resources](css-web-resources.md)   
[Using JavaScript web resources](script-jscript-web-resources.md)   
[Using Data (XML) web resources](data-xml-web-resources.md)   
[Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)   
[Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
