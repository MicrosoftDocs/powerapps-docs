---
title: "Use IFRAME and web resource controls on a form (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "IFRAME and web resource controls embed content from another location in pages by using an HTML IFRAME element.  " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/15/2021
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
# Use IFRAME and web resource controls on a form

IFRAME and web resource controls embed content from another location in pages by using an HTML IFRAME element.  

> [!NOTE]
>  The designs you choose for the form are also used for the Dynamics 365 for Outlook reading pane and forms used by Dynamics 365 tablets. Web resources and IFRAMEs aren’t displayed using the Dynamics 365 for Outlook reading pane, however, they are supported in Dynamics 365 for tablets. If your IFRAME depends on access to the `Xrm` object of the page or any form event handlers, you should configure the IFRAME so that it's not visible by default.  

 You can use an IFRAME to display the contents from another website in a form, for example, in an ASP.NET page. Displaying a form within an IFrame embedded in another form is not supported.  

 You can use one of the following web resources to display the contents of web resources in a form:  

- [Web Page (HTML) web resources](webpage-html-web-resources.md)  

- [Image (JPG, PNG, GIF, ICO) web resources](image-web-resources.md)  


 The following sections describe your options if you want these controls to show more than static content.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="BKMK_IframeSecurity"></a>   

## Select whether to restrict cross-frame scripting  

 Use the **Restrict cross-frame scripting, where supported** option when you don’t fully trust the content displayed in an IFRAME. When this option is selected, the IFRAME has the parameters set that are listed in the following table.  


|        Parameter        |        Description      |
|-------------------------|--------------------------|
| `security="restricted"` |    This parameter is supported only by versions of Internet Explorer no earlier than version 6. The security parameter applies the user security setting Restricted Sites to the source file of the IFRAME. (Zone settings are found on the **Security** tab of the **Internet Options** dialog box.) By default, scripting isn’t enabled in the Restricted Sites zone. By changing the security settings of the zone, various negative results can occur, including allowing scripts to run. For more information, see [security](https://msdn.microsoft.com/library/ie/ms534622.aspx).                                                                                                                                                                                                                                                                                                     |
|      `sandbox=""`       | For browsers that support this parameter, the content in the IFRAME is essentially limited to only displaying information. The following restrictions could be applied:<br /><br /> -   Browser plug-ins are disabled.<br />-   Forms and scripts are disabled.<br />-   Links to other browsing contexts are disabled.<br />-   Content is treated as from a different domain even if the domain is the same.<br /><br /> This parameter is defined by W3C and is supported by the following browsers:<br /><br /> - Internet Explorer 10, Internet Explorer 11, and Microsoft Edge <br />- Google Chrome<br />- Apple Safari<br />- Mozilla Firefox<br /><br /> For more information about the sandbox parameter see:<br /><br /> -   [How to safeguard your site with HTML5 sandbox](/previous-versions/msdn10/hh563496(v=msdn.10))<br />-   [WC3 Sandbox parameter](https://dev.w3.org/html5/spec-author-view/the-iframe-element.html)<br />-   [Sandbox](/previous-versions/windows/internet-explorer/ie-developer/dev-guides/hh673561(v=vs.85)) |

<a name="BKMK_EnableIFrameCommunicationAcrossDomains"></a>   

### Enabling IFrame communication across domains  

 There are times when you want to enable communication for an IFRAME that contains content on a different domain. `Window.postMessage` is a browser method that provides this capability for versions of Internet Explorer no earlier than Internet Explorer 8. Google Chrome, Mozilla Firefox, and Apple Safari also support it. For more information about using `postMessage`, see the following blog posts:  

-   [Cross domain calls to the parent form](https://blogs.msdn.com/b/devkeydet/archive/2012/02/14/cross-domain-calls-to-the-parent-crm-2011-form.aspx)  

-   [Cross-Document messaging and RPC](/previous-versions/msdn10/ff800814(v=msdn.10))  

<a name="BKMK_PassContextualInformation"></a>   

## Pass contextual information about the record  

 You can provide contextual information by passing parameters to the URL defined in the control. The page that is displayed in the frame must be able to process parameters passed to it. All the parameters in the following table are passed if the IFRAME or web resource is configured by using the **Pass record object-type code and unique identifier as parameters** option.  

 You can specify whether all the parameters in the following table will be passed.  


| Parameter  |        Name        |                                 Description                                 |
|------------|--------------------|-----------------------------------------------------------------------------|
| `typename` |    Table Name     |                           The name of the table.                           |
|   `type`   |  Table Type Code  | The integer that uniquely identifies the table in a specific organization. |
|    `id`    |    Object GUID     |                      A GUID that represents a record.                       |
| `orgname`  | Organization Name  |                    The unique name of the organization.                     |
| `userlcid` | User Language Code |    The language code identifier that is being used by the current user.     |

 [!INCLUDE[languagecode](../../includes/languagecode.md)]  

> [!NOTE]
>  We suggest that you use the table name instead of the type code because the table type code for custom tables may be different between Microsoft Dataverse organizations.  

### Example  
 The following sample shows the URL without parameters.  

```  
https://myserver/mypage.aspx  
```  

 The following sample shows the URL with parameters.  

```  
https://myserver/mypage.aspx?id=%7bB2232821-A775-DF11-8DD1-00155DBA3809%7d&orglcid=1033&orgname=adventureworkscycle&type=1&typename=account&userlcid=1033  
```  

### Read passed parameters  

 Passed parameters are typically read in the target .aspx page by using the **HttpRequest.QueryString** property. In an HTML page, the parameters can be accessed by using the **window.location.search** property in JavaScript. For more information, see [HttpRequest.QueryString Property](/dotnet/api/system.web.httprequest.querystring) and [search Property](https://msdn2.microsoft.com/library/ms534620.aspx).  

<a name="BKMK_PassFormData"></a>  

## Pass form data  

 Use the [getValue](clientapi/reference/controls/getValue.md) method on the columns that contain the data that you want to pass to the other website, and compose a string of the query string arguments the other page will be able to use. Then use a [Column OnChange event](clientapi/reference/events/attribute-onchange.md), [IFRAME OnReadyStateComplete event](clientapi/reference/events/onreadystatecomplete.md), or [Tab TabStateChange event](clientapi/reference/events/tabstatechange.md) and the [setSrc](clientapi/reference/controls/setSrc.md) method to append your parameters to the `src` property of the IFRAME or web resource.  

 If you’re using the data parameter to pass data to a Silverlight web resource, you can use the [getData](clientapi/reference/controls/getData.md) and [setData](clientapi/reference/controls/setData.md) methods to manipulate the value passed via the data parameter. For webpage (HTML) web resources, use the [setSrc](clientapi/reference/controls/setSrc.md) method to manipulate the `querystring` parameter directly.  

 Avoid using the [OnLoad event](clientapi/reference/events/form-onload.md). IFRAMES and web resources load asynchronously and the frame may not have finished loading before the `Onload` event script finishes. This can cause the `src` property of the IFRAME or web resource you have changed to be overwritten by the default value of the IFRAME or web resource URL property.  

<a name="BKMK_ChangeThePage"></a>   

## Change the URL  

 You may want to change the target of the IFRAME based on such considerations as the data in the form or whether the user is working offline. You can set the target of the IFRAME dynamically.  

> [!NOTE]
>  When you change the target page for the IFRAME, parameters aren’t passed to the new URL automatically. You must append the query string parameters to the URL before you use the `setSrc` method.  

### Example  

 The following sample shows you how to set the `src` property for the IFRAME and any parameters by using the `onChange` event of a choice column.  

```javascript  
//Get the value of a choice column  
var value = Xrm.Page.data.entity.attributes.get("new_pagechooser").getValue();  
var newTarget = "";  
//Set the target based on the value of the choice  
switch (value) {  
    case 100000001:  
        newTarget = "https://myServer/test/pageOne.aspx";  
        break;  
    default:  
        newTarget = "https://myServer/test/pageTwo.aspx";  
        break;  
}  
//Get the default URL for the IFRAME, which includes the   
// query string parameters  
var IFrame = Xrm.Page.ui.controls.get("IFRAME_test");  
var Url = IFrame.getSrc();  
// Capture the parameters  
var params = Url.substr(Url.indexOf("?"));  
//Append the parameters to the new page URL  
newTarget = newTarget + params;  
// Use the setSrc method so that the IFRAME uses the  
// new page with the existing parameters  
IFrame.setSrc(newTarget);  
```  

## See Also  

 [Client scripting using JavaScript](client-scripting.md)   
 



[!INCLUDE[footer-include](../../includes/footer-banner.md)]