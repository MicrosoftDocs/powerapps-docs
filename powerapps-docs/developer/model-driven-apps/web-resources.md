---
title: "Web Resources (model-driven apps)"
description: "Web resources are virtual files that are stored in the Microsoft Dataverse database and that you can retrieve by using a unique URL address."
author: anushikhas96
ms.author: anushisharma
ms.date: 02/03/2025
ms.reviewer: jdaly
ms.topic: overview
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Web resources in model-driven apps

Web resources are *virtual files* that are stored in the Microsoft Dataverse database and that you can retrieve by using a unique URL address.  

> [!NOTE]
> IFRAMEing content that is behind an authentication boundary isn't supported through web resources or Power Apps component framework. 
> Some embedded IFRAMEs might work in a browser client if the user directly logs into the external service, but this isn't supported in 
> mobile or tablet applications. The specific scenario of embedding a form within an IFRAME, embedded in another form, 
> isn't supported. We recommend the use of [form as a component](../../maker/model-driven-apps/form-component-control.md) for such scenarios.
> 
> In general, use of [Power Apps component framework](../component-framework/overview.md) and 
> [custom pages](../../maker/model-driven-apps/model-app-page-overview.md) is encouraged to build 
> configurable, reusable, and tighter external integrations. 
> More information: [IFRAME component](../component-framework/sample-controls/iframe-control.md)


<a name="BKMK_CapabilitiesOfWebResources"></a>

## Capabilities of web resources  

Web resources represent files that can be used to extend the Dataverse web application such as html files, JavaScript, 
and CSS, and several image formats. You can use web resources in form customizations, the `SiteMap`, or the application 
ribbon because they can be referenced by using URL syntax.  
  
The URL syntax for web resources allows for relative path references. With your development tools, you can create a 
group of interdependent files on a development server by using file types compatible with web resources. Then, if 
you use a consistent naming convention and relative path references, the website will function after you upload all 
the files into Dataverse.
  
Because web resources are stored in Dataverse and are solution components, they can be easily exported and installed 
to other Dataverse orgs. Web resources are also available to users of Dataverse for Microsoft Office Outlook with 
Offline Access when offline because they're synchronized with the user's data.  
  
 You can use the form editor to add and configure form-enabled web resources into your forms.  
  
 Because web resources are stored as records in the database, they can be managed programmatically by using the 
standard techniques to create, retrieve, and update records. Text-based web resources (JScript, CSS, XML, XSL, RESX, and HTML) 
can be edited and saved in the application.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="BKMK_LimitationsOfWebResources"></a>   

### Limitations of web resources  

There's no type of web resource that supports the capabilities of an ASP.NET(.aspx) page to execute code on the server. 
Web resources are limited to static files or files that are processed in the browser. 
A web resource can contain code that is processed in the browser to execute web service calls to interact with Dataverse data.
  
Web resources are only available by using the Dataverse web application security context. 
Only licensed Dataverse users who have the necessary privileges can access them.  
  
#### Size limitations  

The [Organization.MaxUploadFileSize](../data-platform/reference/entities/organization.md#BKMK_MaxUploadFileSize) property determines maximum size of files that can be uploaded.
This property is set in the Email tab of the System Settings in the Dynamics 365 application. 
This setting limits the size of files that can be attached to email messages, notes, and web resources. 
The default setting is 5 MB. Learn more about [environment settings](../data-platform/organization-table.md) and 
[file size limits](../data-platform/attachment-annotation-files.md#file-size-limits)
  
<a name="BKMK_WebResourceTypes"></a>  
 
## Web resource types  
 
You can use 10 file formats to create web resources. The following table lists each file format, 
the allowed file extensions, and the type value that you use for each.  
  
|File|File extensions|Type|  
|----------|---------------------|----------|  
|Webpage (HTML)|.htm, .html|1|  
|Style Sheet (CSS)|.css|2|  
|Script (JScript)|.js|3|  
|Data (XML)|.xml|4|  
|Image (PNG)|.png|5|  
|Image (JPG)|.jpg|6|  
|Image (GIF)|.gif|7|  
|Silverlight (XAP)|.xap|8|  
|StyleSheet (XSL)|.xsl, .xslt|9|  
|Image (ICO)|.ico|10|  
|Vector format (SVG)|.svg|11|  
|String (RESX)|.resx|12|  
  
<a name="BKMK_ReferencingWebResources"></a>

## Reference web resources

 There are several methods that you can use to reference web resources.
  
> [!NOTE]
> When possible, use the [$webresource directive](#webresource-directive). Only references that use the `$webresource` directive in the site map or 
ribbon commands establish dependencies. Dependencies aren't created when web resources reference each other.
  
<a name="BKMK_WebResourceDirective"></a>

### $webresource directive

You should always use the `$webresource` directive when referencing a web resource from a ribbon control or from 
a `SiteMap` sub area. Use the `$webresource` directive anywhere the XML allows a URL value. The following sample shows how to use it.  
  
```xml  
$webresource:<name of Web Resource>  
```  
  
> [!NOTE]
>  When you use the `$webresource` directive, Dataverse creates or updates solution dependencies.  
  
### Xrm.Navigation.openWebResource

The [Xrm.Navigation.openWebResource](clientapi/reference/Xrm-Navigation/openWebResource.md) function opens an HTML web resource in a 
new window with parameters to pass the name of the web resource, any query string data to be passed in the data parameter, 
and information about height and width of the window.  
  
 The URL generated includes the unique GUID token so that the cached web resource loads.  
  
<a name="BKMK_RelativeUrl"></a>

### Relative URL

When referencing a web resource from areas that don't support using the `$webresource:` directive, use a relative URL.
To enable this, we recommend that you use a consistent naming convention for the web resources that reflect a virtual file structure.
The solution publisher's customization prefix is included as a prefix to the name of the web resource.
This can represent a virtual "root" folder for all web resources added by that publisher.
You can then use the forward slash character (/) to simulate a folder structure that is honored by the web server.
  
From another web resource, you should always use relative URLs to reference each other. 
For example, for the web page web resource `new_/content/contentpage.htm` to reference the 
CSS web resource `new_/Styles/styles.css`, create the link as follows:  
  
```html  
<link rel="stylesheet" type="text/css" href="../styles/styles.css" />  
```  
  
 For the web page web resource `new_/content/contentpage.htm` to open the webpage web resource `isv_/foldername/dialogpage.htm`, 
create the link as follows:  
  
```html  
<a href="../../isv_/foldername/dialogpage.htm">Dialog Page</a>  
```  
  
> [!NOTE]
>  Don't use a relative URL using the `WebResources` folder as the root path for the URL. 
For example, don't use: `/WebResources/<name of web resource>`. When a user belongs to more than one organization on a server, 
this path refers to the users default organization. If the user isn't using their default organization and the 
expected web resource isn't included in the user's default organization, a "File Not Found" error occurs even though the 
web resource does occur in the organization the user is currently working in.  
  
<a name="BKMK_FullUrl"></a>

### Full URL

The following sample shows the style of URL you can use to view web resources.  
  
```  
<Dataverse Environment URL>/WebResources/<name of web resource>  
```  
  
 The application processes this URL and return the file that contains the latest version of the web resource. This URL looks like this:  
  
```  
<Dataverse Environment URL>/%7B<version value>%7D/WebResources/<name of web resource>  
```  
  
The version value is updated when you publish customizations and ensures that the browser uses the latest cached version of the web resource. 
Because of this, use a relative path to a web resource, the [Xrm.Navigation.openWebResource](clientapi/reference/Xrm-Navigation/openWebResource.md) 
function, or the [$webresource Directive](web-resources.md#BKMK_WebResourceDirective) (when possible) because the version value is included. 
For large web resources there can be significant performance implications if you don't use the cached version of the file.  
  
The following sample shows a URL for Dataverse, where `MyOrganization` is the name of your Dataverse Environment, and `new_/test/test.htm` 
is the name of the web resource:  
  
```  
https://MyOrganization.crm.dynamics.com/WebResources/new_/test/test.htm  
```  
  
> [!NOTE]
>  Including the '/' character and a file name extension in the name of the web resource is an optional best practice. 
When you write code to reference a web resource that works for Dataverse, you should use the [getClientUrl](clientapi/reference/Xrm-Utility/getGlobalContext/getClientUrl.md) function.

<a name="BKMK_rendering_differences"></a>

## Layout differences between the legacy web client and Unified Interface

A web resource control configured to use a certain number of rows have different heights in a Unified Client application compared 
to a web client application. This is because there's a difference in the height of a row between Unified Interface and web client. 
If a form is needed in both the web client and Unified Interface, you can use different forms in the Unified Interface app and the 
web client app with the control configured to use the appropriate number of rows in each form.

## Community tools

**WebResources Manager** is a tool that XrmToolbox community developed for Dataverse. 
See the [Developer tools](developer-tools.md) article for community developed tools.

> [!NOTE]
> The community tools are not a product of Dataverse and Microsoft does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 
  
### See also  

 [Create Accessible web resources](create-accessible-web-resources.md)   
 [Web Page (HTML) web resources](webpage-html-web-resources.md)   
 [JavaScript web resources](script-jscript-web-resources.md)   
 [Image web resources](image-web-resources.md)   
 [Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)   
 [Data (XML) web resources](data-xml-web-resources.md)   
 [Style Sheet (CSS) web resources](css-web-resources.md)   
 [Web resource table reference](../data-platform/reference/entities/webresource.md)   
 [Sample: Passing multiple values to a web resource through the data parameter](sample-pass-multiple-values-web-resource-through-data-parameter.md)   
 [Sample: Importing files as web resources](sample-import-files-web-resources.md)   
 [Streamline web resource development using Fiddler Auto-Responder](streamline-javascript-development-fiddler-autoresponder.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
