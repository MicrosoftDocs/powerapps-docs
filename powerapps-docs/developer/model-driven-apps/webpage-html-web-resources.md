---
title: "Webpage (HTML) Web Resources (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic covers how to implement HTML web resources and its capabilities and limitations" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
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
# Webpage (HTML) web resources

Use webpage (HTML) web resources to create user interface elements for client extensions.

<a name="BKMK_Capabilities"></a>

## Capabilities of HTML web resources

Because an HTML web resource is just streamed to the user's browser, it can include any content that is rendered on the user's browser.  

<a name="BKMK_Limitations"></a>

## Limitations of HTML web resources  

- An HTML web resource can’t contain any code that must be executed on the server. ASP.NET pages can’t be uploaded as HTML web resources.

- HTML web resources can only accept a limited number of query string parameters. [Pass parameters to HTML web resources](webpage-html-web-resources.md#BKMK_PassingParametersToWebResources)  

- HTML web resources embedded as controls in a form be reloaded by the form runtime for performance reasons. For example, the form runtime may destroy and re-initialize the control during tab navigations. 

<a name="BKMK_UsingTextEditor"></a>

## Use the text editor for HTML web resources

 The text editor provided in the web resource form is intended for use with very simple HTML editing. For more sophisticated HTML documents, you should edit the code in an external editor and use the **Browse** button to upload the contents of your file.

 For example, a more complex HTML page that requires script to render the contents of the page will begin like the following sample.

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

 After the document is opened in the text editor and saved, the HTML will be changed to this.  

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

Because of the capability for the HTML in web resources to be changed by using the text editor, it’s recommended that you use managed properties to set complex HTML web resources as not customizable for managed solutions. When viewing web resources in the solutions window, open the **Managed Properties** dialog box to set the **Customizable** property to `false`.  

<a name="BKMK_ReferencingOtherWebResources"></a>

## Reference other web resources from an HTML web resource

 You can create a set of related files outside of Model Driven Apps that use any of the web resource file types. If you’re careful to always use relative paths and import each web resource with a consistent naming convention that reflects the folder structure of your website, you’ll find that the HTML web resource will maintain links to related CSS, XML, JScript, image, and Silverlight files that have been imported as web resources.  

 For example, if you create a web application project that uses the following [folder]/file structure:  

-   page.htm

-   [Styles]

    -   style.css
  
-   [Scripts] 
  
    -   script.js
  
 When you import these files as web resources, you can name where your solution publisher customization prefix is “new” in the following manner:  
  
-   `new_/page.htm`  
  
-   `new_/Styles/style.css`  
  
-   `new_/Scripts/script.js`  
  
 When you follow this pattern, your `new_/page.htm` HTML web resource can reference the other files the most common way using relative paths as shown in the following example.  

```html
<script src="Scripts/script.js" type="text/javascript"></script>
<link href="Styles/style.css" rel="stylesheet" type="text/css" />
```

 The solution publisher customization prefix becomes a virtual root folder for all the web resources in your solution. If you change your customization prefix, the relative paths within your HTML web resources won’t be changed.  
  
> [!NOTE]
>  - An HTML web resource added to a form can’t use global objects defined by the JavaScript library loaded in the form. An HTML web resource may interact with the `Xrm.Page` or `Xrm.Utility` objects within the form by using `parent.Xrm.Page` or `parent.Xrm.Utility`, but global objects defined by form scripts won’t be accessible using the parent. You should load any libraries that an HTML web resource needs within the HTML web resource so they’re not dependent on scripts loaded in the form.  
> - References included in code between web resources aren’t tracked as solution dependencies.  

 Because web resources are also downloaded for users of Dynamics 365 for Microsoft Office Outlook with Offline Access, users will have access to web resource content while they’re working offline.  

<a name="BKMK_PassingParametersToWebResources"></a>

## Pass parameters to HTML web resources

 An HTML web resource can accept only the parameters in the following table.

|Parameter|Name|Description|
|---------------|----------|-----------------|
|typename|Table Name|The name of the table.|
|type|Table Type Code|An integer that uniquely identifies the table in a specific organization.|
|id|Object GUID|The GUID that represents a record.|
|orgname|Organization Name|The unique name of the organization.|
|userlcid|User Language Code|The language code identifier being used by the current user.|
|orglcid|Organization Language Code|The language code identifier that represents the base language for the organization.|
|data|Optional Data Parameter|An optional value that may be passed.|
|formid|Form Id|The GUID that represents a form ID.|
|entrypoint|Entry Point|A string value. This parameter is intended to be passed as an optional value to web resources opened as custom help content for a table. When enabled, the custom help URL will include a value of either “form” or “hierarchychart”.|
|pagemode||For internal use only.|
|security||For internal use only.|
|tabSet||For internal use only.|

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

 If multiple values are passed in the data parameter, they will be automatically encoded. Logic must also be included to decode the multiple parameters using script in your HTML web resource. The [Sample: Passing multiple values to a web resource through the data parameter](sample-pass-multiple-values-web-resource-through-data-parameter.md) topic demonstrates one approach to address passing multiple parameter values.  

### See also

 [Web resources](web-resources.md)   
 [Create accessible web resources](create-accessible-web-resources.md)   
 [Using Style Sheet (CSS) web resources](css-web-resources.md)   
 [Using Script (JScript) web resources](script-jscript-web-resources.md)   
 [Using Data (XML) web resources](data-xml-web-resources.md)   
 [Using Image (JPG, PNG, GIF) web resources](image-web-resources.md)   
 [Using Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
