---
title: "Use JavaScript (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic helps you explore various opportunities that Model-driven Apps provides to use JavaScript. You can use JavaScript to perform actions in form scripts, command bar (ribbon) commands, and web resources." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
---
# Use JavaScript with model-driven apps

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/use-javascript -->

Model-driven Apps provide many opportunities to use JavaScript. All JavaScript used in Model-driven Apps is added by creaating JavaScript web resources. This topic has information for developers who use JavaScript and includes links to relevant topics in the CDS for Apps Web Services and other sources.  
  
<a name="BKMK_AreasToUseJavaScript"></a>   

## Areas where you can use JavaScript in Dynamics 365 
 
 You can use JavaScript to perform actions in form scripts, command bar (ribbon) commands, and web resources.  
  
<a name="bkmk_FormScripts"></a>   

### Form scripts  

 The most common use of JavaScript in Model-driven Apps is to add functions as event handlers for entity form events. For more information, see [Client scripting using JavaScript](clientapi/client-scripting.md).  
  
<a name="bkmk_commandBar"></a>   

### Command bar (ribbon) commands  

 When you customize the Model-driven Apps command bar, you can configure commands for controls that you add. These commands contain rules that control whether the control is enabled and what action is performed when the control is used. For more information, see [Customize commands and the ribbon](customize-commands-ribbon.md).  
  
<a name="bkmk_webResources"></a>   

### Web resources  

Model-driven Apps provides an organization-owned entity that stores a binary representation of a file that can be accessed by using a URL. This file is called a web resource. There are several types of web resources. A web resource that represents a JavaScript library is called a JavaScript web resource. You can use a webpage (HTML) web resource to provide a user interface with JavaScript libraries included just as you would for files on a web server. Because these files are part of Model-driven Apps, users who access them are already authenticated. Therefore, you can use Model-driven Apps web services without having to write code to authenticate the user. For more information, see [Web Resources](web-resources.md) and [Get started with the Common Data Service for Apps Web API (client-side JavaScript)](../common-data-service/webapi/get-started-web-api-client-side-javascript.md).  
  
<a name="BKMK_UsingjQuery"></a>   

## Use of jQuery  

 **Use jQuery with HTML web resources**  
 We recommend that you use jQuery together with HTML web resources to provide user interfaces because it is an excellent cross-browser library.  
  
 With HTML web resources, you control the libraries that are present and there is no restriction against manipulating the DOM. Feel free to use jQuery within your HTML Web resources.  
  
 
  
<a name="BKMK_WriteJavaScriptForMutlipleBrowsers"></a>
   
## Write JavaScript for multiple browsers  

 Because you don’t know what browser will be in use, you should make sure that any scripts that you use will work with all supported browsers. Most of the significant differences between Internet Explorer and other browser have to do with HTML and XML DOM manipulation. Because HTML DOM manipulation is not supported, if script logic is only performing supported actions and using the [Client API](clientapi/understand-clientapi-object-model.md), the changes required to support other browsers could be small.  
  
 A cross-browser library like jQuery is a good solution for developing web resources but should not be necessary for form scripts or ribbon commands. More information: [Avoid using jQuery for form scripts](clientapi/client-scripting-best-practices.md#avoid-using-jquery-for-form-scripts)   
 
  
<a name="BKMK_JavaScriptBestPractices"></a>  
 
## JavaScript programming best practices  

 The following sections describe best practices when you use JavaScript with Model-driven Apps.  
  
<a name="bkmk_avoidUnsupportedMethods"></a> 
  
### Avoid using unsupported methods  

 On the Internet, you can find many examples or suggestions that describe using unsupported methods. These may include leveraging undocumented internal function for page controls. These methods may work but because they are not supported you can’t expect that they will continue to work in future versions of Model-driven Apps.  
 
  
<a name="bkmk_useJavaScriptFramework"></a>

### Use a cross-browser JavaScript library for HTML web resource user interfaces  
 A cross-browser JavaScript library, such as [jQuery](http://jquery.com/), provides many advantages when developing HTML web resources that must support multiple browsers. JavaScript libraries like jQuery provide a unified development experience for all browsers supported by Model-driven Apps. These capabilities are appropriate when you are using HTML web resources to provide user interfaces. JavaScript libraries like jQuery provide consistent ways to interact with the Document Object Model (DOM).  
  
<a name="bkmk_nojQuery"></a>
 
### Do not use jQuery for form script or commands
 
 We do not recommend or support using jQuery for any pages within the application. This includes form scripts and ribbon commands. More information: [Use of jQuery](use-javascript.md#BKMK_UsingjQuery).  
  
<a name="bkmk_CDNLimitations"></a>

### Recognize limitations for content delivery network (CDN) libraries

 Content delivery network (CDN) JavaScript libraries provide many advantages for public websites. Because these libraries are hosted on the Internet, you do not need to create web resources that contain the content of the libraries. For Model-driven Apps you should consider the following issues before you use a CDN JavaScript library.  
  
- Users of the Dynamics 365 for Microsoft Office Outlook with Offline Access client have the capability to work with no Internet connection while working offline. If you are depending on an Internet connection for your JavaScript libraries, your code will fail.  
  
- Some organizations will restrict Internet access for employees. Unless they configure the network to allow access to the CDN library sites, your code may fail for those organizations.  
  
  The alternative to using CDN libraries is to create a script (JavaScript) web resource with the contents of the library. Because web resources are organization-owned entities they will be synchronized when a Dynamics 365 for Apps for Outlook with Offline Access user goes offline. Because these web resources now become part of the application they will not be blocked if an organization restricts access to the Internet.  
  
<a name="bkmk_useFeatureDetection"></a>

### Use feature detection when writing functions for multiple browsers

 Even when you use a cross-browser library like jQuery, you need to be very aware of differences between browsers. You can generally detect which browser is being used by querying the `navigator.useragent` property. This is called browser detection. Browser detection is not a good strategy for most cases because it can’t take into account what features newer versions of a browser have. Also, some browsers provide the capability to modify the `navigation.useragent` property so that they appear to be a different browser.  
  
 Feature detection is the recommended approach. By detecting what features are available, you can create code paths for the browsers you support without knowing exactly which browser is being used. For more information about feature detection, see [How to Detect Features Instead of Browsers](https://msdn.microsoft.com/library/hh273397\(VS.85\).aspx).  
  
<a name="bkmk_DoNotAccessDOM"></a>
 
### Do not access the DOM

 JavaScript developers are used to interacting with Document Object Model (DOM) elements in code. You might use the `window.getElementById` method or the jQuery library. You are free to use these techniques in your HTML web resources, but they are not supported to access elements in Model-driven Apps application pages or entity forms. Instead, access to entity form elements are exposed through the [Client API object model](clientapi/understand-clientapi-object-model.md). The Model-driven Apps development team reserves the right to change how pages are composed, including the `ID` values for elements, so using the [Client API object model](clientapi/understand-clientapi-object-model.md) protects your code from changes in how pages are implemented.  
  
<a name="bkmk_DefineUniqueNames"></a>
  
### Define unique names for your JavaScript functions

 When you are the only developer for an HTML page you can easily manage the names of the JavaScript functions you use. In Model-driven Apps, other solutions may add JavaScript functions to the page where your function is used.  
  
 If two JavaScript functions on a page have the same name, the first function defined is overwritten by the second. For this reason, make sure that you define unique names for your JavaScript functions. For more information, see [Client scripting in Customer Engagement using JavaScript](clientapi/client-scripting.md).  
  
<a name="bkmk_useasynchronous"></a>

### Use asynchronous data access methods

 When you access data by using the Model-driven Apps web services, always use an [XMLHttpRequest](https://msdn.microsoft.com/library/ms535874\(VS.85\).aspx) that is configured to execute asynchronously. The reason is that the browser operates on a single thread. If that thread is being used to execute a long-running process synchronously the browser will stop responding.  
  
> [!NOTE]
>  Synchronous XMLHttpRequests are deprecated on the main thread of the browser because of the detrimental effects to the end user’s experience. Some browsers now provide a warning when this is detected. If browsers implement the specification at some time in the future an InvalidAccessError exception will be thrown. More information: [http://www.w3.org/TR/XMLHttpRequest/#synchronous-flag](http://www.w3.org/TR/XMLHttpRequest/) and [https://xhr.spec.whatwg.org/#the-open()-method](https://xhr.spec.whatwg.org/)  
  
  
  
### See also

 [Client scripting using JavaScript](clientapi/client-scripting.md)<br />
 [Customize commands and the ribbon](customize-commands-ribbon.md)
 [Web Resources](web-resources.md)<br />
 [Get started with the Common Data Service for Apps Web API (client-side JavaScript)](../common-data-service/webapi/get-started-web-api-client-side-javascript.md)<br />
 [Understand the Client API Object Model](clientapi/understand-clientapi-object-model.md)<br />
 [Blog: Debugging JavaScript code using browser developer tools](http://go.microsoft.com/fwlink/p/?LinkId=715699)<br />
