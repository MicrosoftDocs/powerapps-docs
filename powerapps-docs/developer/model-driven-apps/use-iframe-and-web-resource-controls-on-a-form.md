---
title: "Use IFRAME and Web Resource Controls in Model-Driven Apps"
description: "Learn how to use IFRAME and web resource controls on model-driven app forms to embed content, pass record context, and change URLs with JavaScript."
author: anushikhas96
ms.author: anushisharma
ms.date: 08/18/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Use IFRAME and web resource controls on a form

Learn how to use IFRAME and web resource controls to embed content in model-driven app forms, pass record context and form data, and change target URLs.  

> [!NOTE]
>  The designs you choose for the form are also used for the Dynamics 365 for Outlook reading pane and forms used by Dynamics 365 tablets. Dynamics 365 for Outlook reading pane doesn't display web resources and IFRAMEs, but Dynamics 365 for tablets supports them. If your IFRAME depends on access to the `Xrm` object of the page or any form event handlers, configure the IFRAME so that it's not visible by default.  

You can use an IFRAME to display the contents from another website in a form, such as an ASP.NET page. 

Use [Power Apps component framework components](../component-framework/custom-controls-overview.md) if you want to use a web resource to show content that users interact with.
 
You can't display a form within an IFrame embedded in another form.  

 Use one of the following web resources to display the contents of web resources in a form:  

- [Web Page (HTML) web resources](webpage-html-web-resources.md)  
- [Image (JPG, PNG, GIF, ICO) web resources](image-web-resources.md)  


 The following sections describe your options if you want these controls to show more than static content.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="BKMK_IframeSecurity"></a>   

## Select whether to restrict cross-frame scripting  

Use the **Restrict cross-frame scripting, where supported** option when you don't fully trust the content displayed in an IFRAME. When you select this option, the [iframe sandbox parameter](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox) is passed with an empty value: `sandbox=""`. This setting applies all restrictions.


<a name="BKMK_EnableIFrameCommunicationAcrossDomains"></a>

### Communicate with a cross-origin IFRAME

Use the standard [Window.postMessage](https://developer.mozilla.org/docs/Web/API/Window/postMessage) method to exchange messages between a model-driven app form and an IFRAME whose content has a different origin. Both the form and the page in the IFRAME must implement the messaging behavior. This method doesn't give the cross-origin page direct access to the form's document object model (DOM), `Xrm` object, form context, or other JavaScript objects.

The website that serves the IFRAME content must allow the model-driven app to embed it. The website can control which origins can embed the page by using the [`Content-Security-Policy: frame-ancestors`](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors) directive. The `X-Frame-Options` response header can also prevent the page from being embedded.


When you send a message, specify the exact expected origin in the `targetOrigin` parameter instead of `*`. When you receive a message, verify the `origin` and, when possible, the `source` properties of the message event. Validate the structure and content of the message data before you use it.

If you select **Restrict cross-frame scripting, where supported**, the resulting IFRAME sandbox restrictions can prevent scripts in the embedded page from running and using `postMessage`.

<a name="BKMK_PassContextualInformation"></a>   

## Pass contextual information about the record  

 You can provide contextual information by passing parameters to the URL defined in the control. The page that displays in the frame must be able to process parameters passed to it. If you configure the IFRAME or web resource by using the **Pass record object-type code and unique identifier as parameters** option, it passes all the parameters in the following table.  

 You can specify whether to pass all the parameters in the following table.  


| Parameter  |        Name        |                                 Description                                 |
|------------|--------------------|-----------------------------------------------------------------------------|
| `typename` |    Table Name     |                           The logical name of the table.                           |
|   `type`   |  Table Type Code  | The integer that uniquely identifies the table in a specific organization. |
|    `id`    |    Object GUID     |                      A GUID that represents a record.                       |
| `orgname`  | Organization Name  |                    The unique name of the organization.                     |
| `userlcid` | User Language Code |    The language code identifier that the current user is using.     |

 [!INCLUDE[languagecode](../../includes/languagecode.md)]  

> [!NOTE]
>  Use the table logical name instead of the type code because the table type code for custom tables is usually different between Microsoft Dataverse organizations.

### Example URLs with contextual record parameters  
 The following sample shows the URL without parameters.    

```  
https://myserver/mypage.aspx  
```  

 The following sample shows the URL with parameters.  

```  
https://myserver/mypage.aspx?id=%7bB2232821-A775-DF11-8DD1-00155DBA3809%7d&orglcid=1033&orgname=adventureworkscycle&type=1&typename=account&userlcid=1033  
```  

### Read passed parameters  

Typically, read passed parameters in the target .aspx page by using the [`HttpRequest.QueryString` property](/dotnet/api/system.web.httprequest.querystring) . In an HTML page, access the parameters by using the [`window.location.search` property](https://developer.mozilla.org/en-US/docs/Web/API/Location/search) in JavaScript.

<a name="BKMK_PassFormData"></a>  

## Pass form data  

Use the [getValue](clientapi/reference/controls/getValue.md) method on the columns that contain the data you want to pass to the other website, and compose a string of the query string arguments the other page can use. Then use a [Column OnChange event](clientapi/reference/events/attribute-onchange.md), [IFRAME OnReadyStateComplete event](clientapi/reference/events/onreadystatecomplete.md), or [Tab TabStateChange event](clientapi/reference/events/tabstatechange.md) and the [setSrc](clientapi/reference/controls/setSrc.md) method to append your parameters to the `src` property of the IFRAME or web resource.  

If you're using the data parameter to pass data to webpage (HTML) web resources, use the [setSrc](clientapi/reference/controls/setSrc.md) method to manipulate the `querystring` parameter directly.  

Avoid using the [OnLoad event](clientapi/reference/events/form-onload.md). IFRAMES and web resources load asynchronously and the frame might not finish loading before the `Onload` event script finishes. This condition can cause the `src` property of the IFRAME or web resource you changed to be overwritten by the default value of the IFRAME or web resource URL property.  

<a name="BKMK_ChangeThePage"></a>   

## Change the URL  

 You might want to change the target of the IFRAME based on such considerations as the data in the form or whether the user is working offline. You can set the target of the IFRAME dynamically.  

> [!NOTE]
>  When you change the target page for the IFRAME, parameters aren't passed to the new URL automatically. You must append the query string parameters to the URL before you use the `setSrc` method.  

### Example to change an IFRAME URL

 The following sample shows how to set the `src` property for the IFRAME and any parameters by using the `onChange` event of a choice column.    

```javascript  
//Get the value of an option set attribute
var formContext = executionContext.getFormContext();
var value = formContext.getAttribute("new_pagechooser").getValue();  
var newTarget = "";  
//Set the target based on the value of the option set  
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
var IFrame = formContext.ui.controls.get("IFRAME_test");  
var Url = IFrame.getSrc();  
// Capture the parameters  
var params = Url.substr(Url.indexOf("?"));  
//Append the parameters to the new page URL  
newTarget = newTarget + params;  
// Use the setSrc method so that the IFRAME uses the  
// new page with the existing parameters  
IFrame.setSrc(newTarget);
```  

## See also  

[Client scripting using JavaScript](client-scripting.md)   
 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
